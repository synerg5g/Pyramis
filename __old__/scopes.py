import cppvariable as cvar
import Utils.parserhelpers as parsers
from pyramismap import PyramisMap
import pyramisexceptions as pyex
import json
import sys
from logger import logger


"""
These form the nodes of a scope-tree maintained by IRContextManager.
Is there any way to track all the functions that refer to a particular scope?
"""


class Scope:
    def __init__(
        self,
        scope_descr=None,
        enclosing_scope=None,
        scope_level=None,
        scope_start=None,
        scope_end=None,
    ):
        """Constructor

        Initializes the instance variables _symbols, enclosing_scope,
        and _children. If enclosing_scope is not null, it adds the new
        SymbolTable to the enclosing_scope table's list of children.
        """
        # also stores K_CALL objects.
        # update_types will create this
        # K_CALL with typed params.
        self._symtab = {}

        self.expr = None  # ref to associated file event.

        self.scope_descr = scope_descr

        self.enclosing_scope = enclosing_scope
        self.scope_level = scope_level

        self.scope_start = scope_start
        self.scope_end = scope_end

        self.exit_count = 0

        # self.children = [] # Explore scope-tree being a BST instead of the current general tree

        # if enclosing_scope is not None:
        #     enclosing_scope.children.append(self)

    # def __repr__(self):
    #     # print symbols.
    #     logger.debug(f"-*-*-*-*-*-*-{self.scope_descr}Scope-*-*-*-*-*-*-\n")
    #     symbols = [(name, tp) for name, tp in self._symtab.items()]
    #     if not symbols:
    #         return ""
    #     else:
    #         for _, tp in symbols:
    #             if isinstance(tp, cvar.CPPVariableType):
    #                 symbols_ = "\n".join(f"name: {name}, type: {tp.typestr}" for name,tp in symbols)
    #             else:
    #                 symbols_ = "\n".join(f"name: {name}, type: {type(tp)}" for name,tp in symbols)
    #         return symbols_

    @property
    def k_expr(self):
        return self._k_expr

    @k_expr.setter
    def k_expr(self, expr):
        self._k_expr = expr

    def set_symbol(self, symbolname, symboltype):
        if symbolname in self._symtab:
            if isinstance(symboltype, cvar.CPPVariableType):
                # Shadow warning.
                # logger.debug(f"Type of {symbolname} is changed from {self._symtab[symbolname].typestr} to {symboltype.typestr}", file=sys.stderr)
                pass
            elif type(symboltype) != type(self._symtab[symbolname]):
                # invalid name: eg replacing funcheader name with a varname
                raise pyex.PyramisIllegalShadowError()

        self._symtab[symbolname] = symboltype
        # logger.debug(f"Stored: {symbolname}")

    def _get(self, symbolname):
        # logger.debug(self._symtab)
        if symbolname in self._symtab:
            return self._symtab[symbolname]

    def get_symbol_from_scope(
        self, symbolname
    ):  # checks current to global. Does not check asnbasetypes.
        logger.debug(f"Searching : {self}")
        found = self._get(symbolname)
        if found:
            try:
                logger.debug(
                    f"Found {symbolname}:{found.typestr} in scope {self}"
                )  # found in the current table
                logger.debug(f"raw_type: {found.raw_typestr}")
            except:
                logger.debug(f"Found {symbolname}:{type(found)} in scope {self}")
            return found
        elif self.enclosing_scope is not None:  # check the rest of the curr. scope
            return self.enclosing_scope.get_symbol_from_scope(symbolname)
        else:
            return False

    def getenclosing_scope_scope(self):
        return self.enclosing_scope

    def get_ancestor_scopes(self):
        if isinstance(self.enclosing_scope, GlobalScope):
            return [self]  # returns the EVENT scope.

        # Recursive case: If the current scope has a enclosing_scope,
        # recursively call getenclosing_scope_scopes on the enclosing_scope
        if self.enclosing_scope is not None:
            return [self] + self.enclosing_scope.get_ancestor_scopes()
            # return ancestors # returns current scope as well. returns to enclosing_scope_scopes of earlier self.

        # If the current scope is not a GlobalScope and has no enclosing_scope,
        # return an empty list
        return []

    def get_first_block_ancestor(self):
        if isinstance(self, GlobalScope):
            return self
        elif isinstance(self, (BlockScope, EVENTScope)):
            return self
        return self.enclosing_scope.get_first_block_ancestor()


class GlobalScope(Scope):
    def __init__(self, udfpath=None, archpath=None):
        super().__init__(scope_descr="Global", enclosing_scope=None, scope_level=0)

        # List contains ref to event-scopes that
        # themselves refer to event objects in CPPFile.
        # Updated during first AST traversal.
        self.event_scopes = []

        self._udfloader(udfpath)  # updated self.symtab inherited
        self._arch = self._archloader(archpath) if archpath else {}

        self._map_access_history = []  # MAH is a stack of maphdr objects.
        self.defaultmaps = {
            "FdToKeyMap": PyramisMap(
                mapname="FdToKeyMap",
                keytype=cvar.CPPVariableType(typestr="int", ispointer=False),
            ),
            "KeyToFdMap": PyramisMap(
                mapname="KeyToFdMap",
                keytype=cvar.CPPVariableType(typestr="int", ispointer=False),
            ),
        }

    def get_map_accesses(self):
        return self._map_access_history

    def _udfloader(self, udfpath):
        udfsymbols = {}

        with open(udfpath, "r") as udfh:
            for line in udfh:
                if (
                    line.startswith("#")
                    or line.startswith("using")
                    or line.startswith("/")
                    or line.startswith("\n")
                ):
                    continue

                udf = parsers.udfparse(line)
                # assert(isinstance(udf), cppfunction.func)

                if udf.name in udfsymbols:
                    udf.name = f"__{udf.name}"  # Mangle name if mutiple definitions

                self._symtab[udf.name] = udf

    def _archloader(self, archpath):
        with open(archpath, "r") as jf:
            data = json.load(jf)
        return data

    def update_types(self, IRContextManager, class_name, params):
        """
        Assign types to param strings encountered during first
        AST traversal. Stores types in the self._symtab.
        """
        # Set param-types and store in scope.
        if class_name == "K_CREATE_MESSAGE":
            try:
                mid, mtype, msz = params
                param = cvar.CPPVariable(name=mid, typestr=mtype, sz=msz)
            except:
                mid, mtype = params
                param = cvar.CPPVariable(name=mid, typestr=mtype)
            # Make type-tree, store symbol in scope.
            if not param.type.make_tree(IRContextManager._asnbasetypes):
                raise pyex.PyramisTypeError()
            logger.debug(f"Typetree: {param.type.childTypes}")
        else:
            for p in params:
                ptype = IRContextManager.get_symbol(p)
                param = cvar.CPPVariable(p, ptype.raw_typestr, ptype.ispointer)
        self.set_symbol(param.name, param.type)


class EVENTScope(Scope):
    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )
        self.is_event_failed = False


class BlockScope(Scope):
    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )


class IFScope(BlockScope):
    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )
        assert self.scope_descr == "IF"
        # self.expr = None
        # self._calls = {}


class FORScope(BlockScope):
    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )
        # self.scope_descr = "FOR"
        # self.expr = None
        # self._calls = {}


class ELSEScope(BlockScope):
    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )
        # self.scope_descr = "ELSE"
        # self.else_expr = None
        # self._calls = {}


class CALLScope(Scope):
    """
    Contains print-speciic metadata.
    Every keywordExpr will have an associated scope.
    Scope will contain : lineno.
    Type of call being made. Maybe doesnt need the object itself?
    """

    def __init__(
        self, scope_descr, enclosing_scope, scope_level, scope_start, scope_end
    ):
        super().__init__(
            scope_descr, enclosing_scope, scope_level, scope_start, scope_end
        )
