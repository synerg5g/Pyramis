import cppvariable as cvar


class PyramisMapAccessHeader:
    """
    This class is used to make call-flow agnostic map optimisations.
    """

    def __init__(
        self,
        line_no,
        mapname,
        class_,
        # ALl are typed.
        mapkey=None,
        mapattr=None,
        mapval=None,
    ):

        self.lineno = line_no

        self.name = mapname

        self.class_ = class_  # STORE or LOOKUP

        self._key = mapkey

        self._attr = mapattr

        self._val = mapval


class PyramisMap:
    """
    Class to represent a C++ map created by the Pyramis script.
    This class is used to print final header strings.
    """

    def __init__(
        self,
        mapname,
        mapkeys=None,  # mapvalues=None,
        attributes=None,
        keytype=None,
    ):  # keys are CPPVar objects. mapvalues are any objects

        self.mapname = mapname
        self.keytype = keytype

        self.mapkeys = mapkeys if mapkeys is not None else []  # strings

        self.valuetype = cvar.CPPVariableType(
            typestr=f"{mapname}structure", ispointer=False
        )  # arg1 not reqd

        self.attributes = attributes if attributes is not None else []  # list of cppvar

    def addkeyattrpair(
        self, parent, key, attr
    ):  # only one kv pair added to map per store call.

        # can remove duplicates here itself. Store every key referenced.
        if key.name not in [mapkey.name for mapkey in self.mapkeys]:
            self.mapkeys.append(
                key
            )  # keys list will store all key objects of same type

        if not self.keytype:  # if no keytype assigned to map yet.
            logger.debug(key.name)
            self.keytype = key.type

        if attr.name not in [atr.name for atr in self.attributes]:
            self.attributes.append(attr)  # the valuetype struct is made of attr types.
