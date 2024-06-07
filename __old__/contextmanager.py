import scopes
from messagetypes import messageTypeContext
import pyramisexceptions as pyex
import cppvariable as cvar
import json
import cppfunction as cfunc
from logger import logger


class ContextManager:
    def __init__(self, udfpath, archpath, configpath):

        self._head = scopes.GlobalScope(udfpath, archpath)
        self.current_scope = self._head
        self._asnbasetypes = (
            messageTypeContext  # eventually make this a dict equivalent to cppvartype.
        )
        # self.__messagetypes = "messagetypes.json"
        fd = open(configpath)
        self._configfile = json.load(fd)

        self._failed = (
            []
        )  # If I reach an EVENT but it hasnt been called before. If it was called before, it would be in globalscope and simple rec g_s_f_s works

    def get_head_scope(self):
        return self._head

    def get_map_accesses(self):
        return self._head.get_map_accesses()

    def get_current_scope(self):
        return self._current

    def set_current_scope(self, scope):
        self._current = scope

    def _get_value_at_json_key(self, inter_ident, child_ident, data=None):
        if not data:
            data = self._configfile[inter_ident]

        if isinstance(data, str):
            return "string"
        elif isinstance(data, int):
            return "int"
        elif isinstance(data, bool):
            return "bool"

        if isinstance(data, dict):
            if child_ident in data:
                logger.debug(f"Found in configfile: {child_ident}: {data[child_ident]}")
                # return data[child_ident]
                return self._get_value_at_json_key(
                    inter_ident, child_ident, data[child_ident]
                )
            else:
                for key, val in data.items():
                    if isinstance(val, (int, str)):
                        continue
                    return self._get_value_at_json_key(key, child_ident, val)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    return self._get_value_at_json_key(inter_ident, child_ident, item)

    def get_call_from_persistent_scope(self, ename):
        def find_call_scope(node):
            if isinstance(node, scopes.CALLScope) and isinstance(
                node.k_expr, cfunc.K_CALL
            ):
                if node.k_expr.ename == ename:
                    return node

            if node.children:
                for child in node.children:
                    result = find_call_scope(child)
                    if result:
                        return result

            return None

        # Start the search from the global scope
        global_scope = self._head
        for event_scope in global_scope.children:
            result = find_call_scope(event_scope)
            if result:
                return result

        # If not found
        logger.debug(f"Event {ename} not called before its definition.")
        return None

    def get_symbol(self, symbolname):
        """
        Returns the object i.e. type
        corresponding to the lowest level attribute of the given name
        """
        # first check if entire attr string was stored previously.
        logger.debug(f"Get Symbol: {symbolname}")

        if isinstance(symbolname, int):
            symbol = cvar.CPPVariableType(int, False)
            return symbol

        symbol = self.get_symbol_from_scopes(symbolname)  # dotted symbol

        if not symbol:
            """
            The symbol is brand new. Could be of many types
            Could even be a compound type.
            Returned type is stored as type of the compound idname.
            """
            logger.debug(f"{symbolname} not in Scope-Tree")

            if symbolname[-1] == '"':
                # Asspn: regular string. json nonly via read_config
                # Nothing else allowed.
                symbol = cvar.CPPVariableType(typestr="string", ispointer=False)
                logger.debug(f"Raw type of {symbolname} is {symbol.raw_typestr}")
                return symbol
            else:
                # check if int.
                pass

            if "." in symbolname:
                # look for root_ident.
                root_ident = symbolname.split(".")[0]
                child_ident = symbolname.split(".")[-1]
                root_ident_t = self.get_symbol_from_scopes(root_ident)

                if root_ident_t:
                    assert isinstance(root_ident_t, cvar.CPPVariableType)

                    if (
                        root_ident_t.raw_typestr == "jsonfile_xt"
                    ):  # assigned by read_config.
                        # return type from s
                        inter_ident = symbolname.split(".")[1]
                        ts = self._get_value_at_json_key(
                            inter_ident,
                            child_ident,
                        )
                        symbol = cvar.CPPVariableType(ts, False)
                        logger.debug(
                            f"Type of {symbolname} from config is {symbol.typestr}"
                        )
                        logger.debug(
                            f"Raw Type of {symbolname} from config is {symbol.typestr}"
                        )
                        return symbol
                    else:
                        # check if the mt is from a prev. CREATE_MESSAGE
                        symbol = root_ident_t.findSubType(child_ident)

                    if symbol:
                        pass
                    else:
                        # create a tree for this type
                        root_ident_t.make_tree(self._asnbasetypes)
                        symbol = root_ident_t.findSubType(child_ident)

                        if not symbol:
                            raise pyex.CompilerTypeInferenceError()
                        else:
                            if symbol.typestr == "JSON":
                                # check json
                                pass
                else:
                    # Possibly being used in a loop.
                    raw_root = root_ident.split("[")[0]
                    raw_root_t = self.get_symbol_from_scopes(raw_root)  # dotted symbol
                    if raw_root_t:
                        symbol = raw_root_t.findSubType(child_ident)
                    else:
                        logger.debug(f"{root_ident} not in Scope-Tree yet.")
                        symbol = cvar.CPPVariableType(
                            typestr="NO_TYPE_YET", ispointer=False
                        )
            else:
                symbol = cvar.CPPVariableType(typestr="NO_TYPE_YET", ispointer=False)
        else:
            logger.debug(f"Type of {symbolname} is {symbol.typestr}")
            return symbol

        logger.debug(f"Type of {symbolname} is {symbol}")
        return symbol

    def get_symbol_from_scopes(self, symbolname):
        # logger.debug(f"Current Scope from Type-assign: {self._current}")
        logger.debug(f"Get Symbol: {symbolname}")
        return self._current.get_symbol_from_scope(symbolname)

    def set_symbol_at_head(self, symbolname, symboltype):
        self._head.set_symbol(symbolname, symboltype)

    # -- OLD
    def enter_scope(self, descr, enclosing_scope, level, start, end):
        """
        This method updates the scope-tree to encode scope entry and exit.

        """
        logger.debug(f"Enter new scope creation, {descr}")
        logger.debug(f"New scope required start: {start}, end: {end}")

        # from analyzer pov. enter_scope updates current
        # for subsequent node-visits.
        prev = self._current

        ancestors = prev.get_ancestor_scopes()  # returns self as well.

        # set scope exit status for previous scope
        # while entering new scope.
        if descr == "EVENT":
            prev.exit_count += 1
        else:
            for sc in ancestors[1:]:  # current is the prev scope.
                logger.debug(f"Ancestor scope {sc} start: {sc.start}, end: {sc.end}")
                if (
                    prev.start == sc.end
                ):  # if current function lineno is also the end of some scope. IF end = end of
                    logger.debug(f"EXIT: Previous {prev} is an exit for {sc}")
                    prev.exit_count += 1
        logger.debug(f"Previous Scope {prev} is an exit for {prev.exit_count} scopes")

        # while creating current scope,
        # found that previous scope was an exit scope.
        # implies current and previous are at different levels
        # i.e will have different parents.
        if prev.exit_count:
            # prev and current will not have same parent,
            # but have same common ancestor self.get_LCA(prev).
            # parent of the previous block scope.
            parent = prev.get_first_block_ancestor()
            # logger.debug(f"Parent of current, LCA: {parent}\n")
            assert isinstance(
                parent, (scopes.EVENTScope, scopes.BlockScope, scopes.GlobalScope)
            )  # new event

        # set default
        # current scope being created is in the same indent level
        # i.e. same parent scope as prev.
        # special case: current is the first call in a block
        # parent = parent of the previous scope( whatever that is)
        else:
            if isinstance(prev, (scopes.EVENTScope, scopes.BlockScope)):
                parent = prev
                logger.debug(f"Parent of current, prev: {parent}\n")
            elif isinstance(prev, scopes.CALLScope):
                parent = prev.get_parent_scope()
                logger.debug(f"Parent of current, prev.parent: {parent}\n")

        if descr == "EVENT":
            assert enclosing_scope == self._head
            # logger.debug(f"Desired start: {start}, end: {end}")
            assert isinstance(parent, scopes.GlobalScope)
            scope = scopes.EVENTScope(descr, enclosing_scope, start, end)
            # logger.debug(f"new Eventscope: start={scope.start} end={scope.end}")

        elif descr == "FOR":
            scope = scopes.FORScope(descr, parent, start, end)

        elif descr == "IF":
            scope = scopes.IFScope(descr, parent, start, end)
            # logger.debug(f"IF parent: {scope.get_parent_scope()}")

        elif descr == "ELSE":
            logger.debug(prev)
            assert isinstance(prev, scopes.CALLScope)  # no empty IF before.

            parent = prev.get_parent_scope()
            assert isinstance(descr, parent, scopes.IFScope)

            scope = scopes.ELSEScope(descr, parent, start, end)

        elif descr == "CALL":
            scope = scopes.CALLScope(descr, parent, start, end)
            # logger.debug(f"call parent: {scope.get_parent_scope()}")

        else:
            raise pyex.CompilerScopeNameError()

        logger.debug(
            f"Scope Creation Successful. {scope}. Start: {scope.start}, end:{scope.end}\n"
        )

        parent.children.append(scope)  # new scope.

        # update current scope is always the last scope created.
        self.current_scope = scope
        return self.current_scope

    # -- NEW
    def enter_scope(self, descr, enclosing_scope, level, start, end):
        if descr == "EVENT":
            # reset enclosing_scope
            enclosing_scope = self._head
            level = enclosing_scope.level + 1
            current_scope = scopes.EVENTScope(descr, enclosing_scope, level, start, end)

            # ContextManager maintains a list of lexical-order
            # event scopes as children of the globalScope.
            # any get_symbol() call will traverse enclosing_scope
            # until globalScope symtab is reached.
            enclosing_scope.event_scopes.append(current_scope)

            return current_scope

        elif descr == "CALL":
            current_scope = scopes.CALLScope(descr, enclosing_scope, level, start, end)

    def is_event_in_arch(self, ename, data=None):
        if not data:
            data = self._head._arch

        def search_value(d):
            if isinstance(d, dict):
                for key, value in d.items():
                    if key == "Processing" and ename in value:
                        return True
                    elif isinstance(value, (dict, list)):
                        if search_value(value):
                            return True
            elif isinstance(d, list):
                for item in d:
                    if isinstance(item, (dict, list)):
                        if search_value(item):
                            return True
            return False

        return search_value(data)


def find_parent_key_by_key(self, target, nested_dict=None):
    """
    Helper function to return the parent key where the given key is a value.
    """
    if not nested_dict:
        nested_dict = self._asnbasetypes

    def _get_parent_key(target):
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                if target in value:
                    yield key
                yield from find_parent_key_by_key(value, target)
            elif value[0] == target:
                yield key

    return _get_parent_key(target)
