import ast
import sys
from contextmanager import ContextManager
import cppfunction as cfunc
import cppvariable as cvar
import scopes
import pyramisexceptions as pyex
from __old__.logger import logger


_iEVENT = 0


class PyAnalyzer(ast.NodeVisitor):
    comparison_map = {
        "Eq": " == ",
        "NotEq": " != ",
        "Lt": " < ",
        "LtE": " <= ",
        "Gt": " > ",
        "GtE": " >= ",
    }

    def __init__(self, cppfile, pylines):
        self.__cppfile = cppfile
        self.__pylines = pylines

    def analyzeAST(self, tree, file_index, contextmanager):

        self.__file_index = file_index
        self._IRContextManager = contextmanager

        self.visit(tree)  # begin tree walk.

    def get_rightmost_leaf(self, node):
        """
        Travels through nested ifs/fors to return last expr in the nest.
        Does not walk into Else Nodes.
        """
        if isinstance(node, ast.Expr):
            return node
        if isinstance(node, ast.If):
            return self.get_rightmost_leaf(node.body[-1])
        if isinstance(node, ast.For):
            return self.get_rightmost_leaf(node.body[-1])

        return node

    def visit_nested_block(self, node):
        if isinstance(node, ast.If):
            self.visit_If(node)
        elif isinstance(node, ast.For):
            self.visit_For(node)

    def visit_FunctionDef(self, node):
        logger.debug(f"Analyze: EVENT {node.name}")
        global _iEVENT  # event index.
        _iEVENT += 1

        start = node.lineno

        # enclosing_scope must always be the Global Scope,
        # hence we reset the enclosing scope on reaching an
        # Event i.e. FunctionDef, append the ref to EVENTScope to
        # GlobalScope event_scopes list, and returns that
        # reference as current_scope.
        start = node.lineno
        end = node.end_lineno
        level = self._IRContextManager.current_scope.level + 1
        current_scope = self._IRContextManager.enter_scope(
            "EVENT",
            level,  # will be reset
            self._IRContextManager.current_scope,  # will be reset
            start,
            end,
        )

        self.generic_visit(node)

        logger.info("Exiting EVENTScope @ (%d-%d)", start, end)
        current_scope.exit_count += 1
        self._IRContextManager.current_scope = current_scope.enclosing_scope

        current = self._IRContextManager.get_current_scope()

        params = [param.arg for param in node.args.args]
        ename = node.name

        event = cfunc.PyramisEvent(
            self._IRContextManager,
            current,  # cf=None for 1st.
            ename,
            "void",
            params,
            _iEVENT,
        )

        event.syntax_check()

        event.type_assign()

        event.semantic_check()

        event.add_params_to_scope()

        # create file entry, set scope event.
        file_ = self.__cppfile[self.__file_index]
        file_.events.append(event)
        current.event = file_.events[-1]

        # else:
        #     logger.debug(f"Failed: {event._header.name}")
        #     self._IRContextManager._failed.append(event) #empty params.
        #     current.event = self._IRContextManager._failed[-1] #subsequent calls will be added to the failed event.

        assert isinstance(self._IRContextManager.get_current_scope(), scopes.EVENTScope)

        self.generic_visit(node)

    def visit_Call(self, node):
        class_name = f"K_{node.func.id}"
        logger.debug(f"Analyze: {class_name}\n")

        start = node.lineno
        level = self._IRContextManager.current_scope.level + 1
        current_scope = self._IRContextManager.enter_scope(
            "CALL", level, self._IRContextManager.current_scope, start, end=start
        )

        assert isinstance(current_scope, scopes.CALLScope)

        param_strings = [arg.value for arg in node.args]

        # Store first instance of typed params in scope.
        current_scope.update_types(
            self._IRContextManager, class_name, param_strings
        )  # big switch case with the type assignment stuff for scope

        # Create a keyword_expr, link to the typed scope.
        fmod = sys.modules["cppfunction"]
        class_handler = getattr(fmod, class_name)
        expr = class_handler(self._IRContextManager, current_scope, param_strings)

        expr.syntax_check()
        expr.type_assign()
        expr.semantic_check()
        current_scope.expr = expr

        # Every non-CALLScope is associated with a single (block) expr.
        # every block expr has a body that represents the statements it encapsulates.
        # expr are stored in the CPPFile (File.events)
        # scope object only contains a reference to its expr, and
        # body is an intrinsic property of an expr.
        # typed body-> codegen in a single loop by traversing the file.events list
        # ASTNodevisitor -> Scope-Tree -> CPPFile
        assert not isinstance(current_scope.enclosing_scope, scopes.CALLScope)
        current_scope.enclosing_scope.expr.body.append(expr)

        # reset current to current.enclosing before moving to
        # next line in lexical order. reset scope before generic_visit is unique
        # to visit_Call as it represents a single-line scope.
        self._IRContextManager.current_scope = current_scope.enclosing_scope

        # Either a single-line K_* scope will be encountered with correct
        # enclosing scope, or a multi-line K_* scope (FOR, IF, ELSE).
        self.generic_visit(node)

    def visit_If(self, node):

        start = node.lineno
        end = self.get_rightmost_leaf(node).lineno  # stops at Else
        self._IRContextManager.enter_scope(descr="IF", start=start, end=end)
        current = self._IRContextManager.get_current_scope()  # IF

        node_type = node.test.__class__

        cstr = ""

        if node_type is ast.Compare:

            lhsname = node.test.left.value

            op = type(node.test.ops[0]).__name__  # str
            optxt = PyAnalyzer.comparison_map[op]

            rhsname = node.test.comparators[0].value

            cstr = f"{cstr}{lhsname}{optxt}{rhsname}"  # will contain MACRO if present

        elif node_type is ast.Constant:
            cstr = f"{node.test.value}"

        params = [cstr]

        expr = cfunc.K_If(self._IRContextManager, current, params)

        expr.type_assign()  # splits _params into clauses, assigns types

        current.k_expr = expr
        expr.add_params_to_scope()

        expr.semantic_check()

        parent = current.get_parent_scope()  # block or event
        assert isinstance(parent, (scopes.BlockScope, scopes.EVENTScope))

        if isinstance(parent, scopes.BlockScope):
            parent.k_expr.body.append(expr)  # store in scope
        else:
            parent.event.calls.append(
                expr
            )  # store in file if event typed, else in _failed

        # check for an If/For in IF body.
        if any(cnode in node.body for cnode in [ast.If, ast.For]):
            for cnode in node.body:
                if isinstance(cnode, (ast.If, ast.For)):
                    self.visit_nested_block(cnode)
                else:
                    logger.debug(f"In If, now accessing {type(cnode)}")
                    self.visit(cnode)
        else:  # no nesting in IF body
            if node.orelse:
                start = node.orelse[0].lineno - 1
                end = node.orelse[-1].lineno
                # IRC.current = some CALL always. empty body is ast syntax error.
                self._IRContextManager.enter_scope(
                    "ELSE", start, end
                )  # prev must be scope_exit.

                current = self._IRContextManager.get_current_scope()
                assert isinstance(current, scopes.ELSEScope)

                # else keyword
                expr = cfunc.K_Else(self._IRContextManager, current)
                current.k_expr = expr

                if isinstance(current, scopes.ELSEScope):
                    current.k_expr.body.append(
                        expr
                    )  # IF is considered parent of else. IF-ELSE will have single if, _calls = {ELSE}, else _calls will be other calls in else.
                else:
                    raise pyex.PyramisSyntaxError("Else without IF")

                if any(enode in node.orelse for enode in [ast.If, ast.For]):
                    # Nesting in Else
                    for enode in node.orelse:
                        if isinstance(enode, (ast.If, ast.For)):
                            self.visit_nested_block(enode)
                        else:
                            self.visit(enode)
            else:
                # Plain If/end of nesting
                for cnode in node.body:
                    self.visit(cnode)

    def visit_For(self, node):
        logger.debug("Analyze: FOR")
        start = node.lineno
        end = self.get_rightmost_leaf(node).lineno  # stops at Else

        self._IRContextManager.enter_scope(descr="FOR", start=start, end=end)
        current = self._IRContextManager.get_current_scope()  # IF

        params = [node.target.id, node.iter.args[0].value, node.iter.args[1].value]

        expr = cfunc.K_Loop(self._IRContextManager, current, params)

        expr.syntax_check()

        expr.type_assign()

        current.k_expr = expr
        expr.add_params_to_scope()

        expr.semantic_check()

        parent = current.get_parent_scope()

        if isinstance(parent, scopes.BlockScope):
            parent.k_expr.body.append(expr)
        else:  # EVENT
            parent.event.calls.append(expr)

        for cnode in node.body:
            # if isinstance(cnode, (ast.If, ast.For)):
            #     self.visit_nested_block(cnode)
            # else:
            logger.debug(f"In For, now accessing {type(cnode)}")
            self.visit(cnode)

    def visit_Break(self, node):
        start = node.lineno
        self._IRContextManager.enter_scope(
            descr="CALL", start=start, end=start, class_="K_BREAK"
        )

        current = self._IRContextManager.get_current_scope()

        expr = cfunc.K_BREAK(self._IRContextManager, current)
        current.k_expr = expr

        parent = current.get_parent_scope()

        if isinstance(parent, scopes.BlockScope):
            parent.k_expr.body.append(expr)  # store in scope
        else:
            expr.semantic_check()

    def visit_Continue(self, node):
        start = node.lineno
        self._IRContextManager.enter_scope(
            descr="CALL", start=start, end=start, class_="K_CONTINUE"
        )

        current = self._IRContextManager.get_current_scope()

        expr = cfunc.K_CONTINUE(self._IRContextManager, current)
        current.k_expr = expr

        parent = current.get_parent_scope()

        if isinstance(parent, scopes.BlockScope):
            parent.k_expr.body.append(expr)  # store in scope
        else:
            expr.semantic_check()

    def visit_Pass(self, node):
        start = node.lineno
        self._IRContextManager.enter_scope(
            descr="CALL", start=start, end=start, class_="K_PASS"
        )

        current = self._IRContextManager.get_current_scope()

        expr = cfunc.K_CONTINUE(self._IRContextManager, current)
        current.k_expr = expr

        parent = current.get_parent_scope()

        if isinstance(parent, scopes.BlockScope):
            parent.k_expr.body.append(expr)  # store in scope
        else:
            expr.semantic_check()
