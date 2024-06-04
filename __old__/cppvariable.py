import cpptypeinference as ctypes

"""
To be more uniform with symbol-table philosophy,
we should rename this file to symbols.py
Next we should define a CallSymbol class, that contains:
- callname
- typed params
- ref to its scope.
Ideally, Call typeAssign should create this callSymbol() that contains cppvar params,
-K_CALL in cppfunction creates callsymbol from self._params. 
add_parms (update_context) will add this call-symbol to the block-anscestr scope. 
- add_param will need to be modified (set_symbol signature) 
- For uniformity, all cppvars must have a ref to their 
Calls will be stored in respective symboltables like other symbols.
Search for a call will be done via a modification to get_symbol, that returns 
the desired call objct via persistenttree search.
the K_EXPR must be seperae entities. Should be updated via param transfer.
K_CALL must only contain ref to a "CAllsymbol". No need to store callsymbol params
seperately.
- This is because call params are only used once to update event params and event scope.
- Subsequent searches for that symbol in current event will return the item in EVENTScope.
"K_CALL contain callscope and ref to callsymbol. PyrmisEvent of a K_CALL contains refs to call params in EVENT Scope."

-----
Presently, we store typed params directly in the cfile as K_Expr object params self.parameters. Scope symbols are refs to these params.
to look for the relevant event, event polls scope tree, and scope-tree returns a ref to CALL
that was stored in Cfile previously. (Existence of a scope with linked k_expr implies existence of call in cfile).
event typeasign transfers call params to event params, and eventscope is updated.
No CALLs stored in symboltables.
"""


class CPPVariableType:
    """
    Only L0 attributes of a symbol will have a type-tree.
    tree wont be constructed if symbol has ".".
    If symbol has ".", its typestr will be type(split[-1]),
    but name will be the entire string.

    """

    def __init__(self, typestr, ispointer, sz=None):
        self.sz = sz
        self.raw_typestr = typestr  # no ptr.

        if ispointer:
            self.typestr = f"{self.raw_typestr}*"
        else:
            self.typestr = self.raw_typestr

        self.ispointer = ispointer

        # dict of attr: CPPVartype.
        self.childTypes = {}

        # @property
        # def raw_typestr(self):
        #     # updates self.typestr based on self.ispointer.

    # Originally called from CREATE_MESSAGE type_assign
    def make_tree(self, context_dict):
        """
        tstr: httprequest -> chld: json -> tstr: JSON
        """
        if ctypes.find_key(
            self.raw_typestr, context_dict
        ):  # check if type is a key, i.e. an attribute
            try:
                attributes = context_dict[self.raw_typestr]
            except KeyError as k:
                # logger.debug(f"Leaf type: {self.typestr}. Make Terminated.")
                return True
            # logger.debug(f"make attributes: {attributes}")

            if isinstance(attributes, tuple):
                self.raw_typestr = attributes[0]
                self.ispointer = attributes[1]
                return True

            for attr, (raw_typestr, ispointer) in attributes.items():
                # logger.debug(f"attr: {attr}, ({raw_typestr, ispointer})")
                child_type = CPPVariableType(raw_typestr, ispointer)
                child_type.make_tree(context_dict)
                self.childTypes[attr] = child_type
            return True
        else:
            if self.typestr in ["char", "int"]:
                return True
            else:
                return False

    # find an attr in local type-tree
    def findSubType(self, attribute):
        """
        Given an attribute of a nested indentifier,
        will traverse the type-tree of the
        root identifier and return its type.
        root_ident.type contains types of child attributes
        as a tree.
        context.get_symbol() will return the root_ident.type always.
        Up to individual type_assign() to call traverse_tree()
        base cond: ONLY if attribute not found, you stop.
        """
        # logger.debug(f"self typestr: {self.typestr}")
        # logger.debug(f"childtypes: {self.childTypes}")

        if attribute == self.raw_typestr:
            return self
        elif attribute in self.childTypes:
            return self.childTypes[attribute]
        else:
            for raw_typestr, child_type in self.childTypes.items():
                # logger.debug(f"Entering raw {raw_typestr}")
                try:
                    # Recursively search for the attribute
                    result = child_type.findSubType(attribute)
                    if result:
                        # logger.debug(f"found {result.typestr}")
                        return result  # If attribute is found, return immediately
                except KeyError:
                    pass
            # logger.debug(f"Attribute '{attribute}' of root '{self.typestr}' not found in type-tree.")
            return None


class CPPVariable:  # Possible rename to Symbol(), SymbolType.
    def __init__(self, name: str, typestr: str, ispointer=False, sz=None):

        if "MACRO" in name:
            name = name.replace("MACRO", "").replace("(", "").replace(")", "")
        elif "UDF" in name:
            name = name.replace("UDF", "").replace("(", "").replace(")", "")

        self.name = name

        self.type = CPPVariableType(typestr, ispointer, sz)  # a tree node

        # self.type = tt.TypeTree(base_type_str, base_type_ispointer, base_type_sz). create subtype tree in __init__.
        # typetree.typestr will always return l0 type. Implement a property in typeTree()

        self.printablename = name  # unless changed externally

    def hassubtype(self, type):
        """
        Returns True if the type-tree of a symbol
        contains an attribute of the desired type.
        Can specify nesting level, default is top layer.
        EG: symbol nausf_auth_ueAuth has typestr HttpReq, which reduces
        to JSON.

        """
        pass
