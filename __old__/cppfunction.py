from abc import ABC, abstractmethod
import cppvariable as cvar
import pyramisexceptions as pyex
import Utils.parserhelpers as parsers
import pyramismap as pymap
import cpptypeinference as ctypes
import cppfile as cfile
import scopes
from logger import logger


class FunctionHeader:
    """
    Represents the header-line details of a Funciton only.
    Stores a return type and params list.
    """

    def __init__(self, fname, returntype="void", parameters=[]):
        self.name = fname

        self.returntype = cvar.CPPVariableType(
            typestr=returntype, ispointer=False  # void by default
        )

        self.parameters = parameters  # a list of param strs

        self.raw_code = ""

    def generate_raw_code(self):
        pass


class PyramisEvent:
    """ """

    def __init__(self, IRContextManager, scope, fname, returntype, _params, index):

        self._header = FunctionHeader(fname, returntype, _params)

        self._IRContextManager = IRContextManager
        self._index = index

        self._scope = scope

        self.parameters = []

        self.body = []

        self.converted_cpp_code = ""

    def syntax_check(self):
        pass

    def type_assign(self):
        """
        Functiondef will only get parameter types by
        searching for current event in the symbol table.
        Assume: A call will always be given the correct params.
        If Call not done before event, we store it in failed events.
        We are hoping that the EVENT was CALLED sometime after its first Definition
        At the end of first walk, global scope symtab will have recorded every CALL.
        _failed will have stored entire events that werent called before their defition.
        Ideally, every
        A CALL that doest have a definition and an EVENT that is never called.

        1. If event in failed is not found in calls : Delete that event or raise EventNotCalledError()
        2. If event in failed is found In calls .(calls has 1 instance of that event) : event parmstrs take types from call, updates its parameters
        3. Finally, new entries are added to cppfile.events.
        4. Events are sorted by index.
        5. Events are printed, code is generated."""
        ename = self._header.name
        paramstrs = self._header.parameters

        # give each event an index.

        if self._index == 1:  # first event in file
            defaultbuffer = cvar.CPPVariable(
                name=paramstrs[0], typestr="char", ispointer=True
            )
            self.parameters.append(defaultbuffer)
        else:
            callscope = self._IRContextManager.get_call_from_persistent_scope(ename)

            if not callscope:
                self._scope.is_event_failed = True
                for _p in paramstrs:
                    # NO_TYPE_YET for all params.
                    ptype = self._IRContextManager.get_symbol(_p)
                    param = cvar.CPPVariable(_p, ptype.typestr, ptype.ispointer)

                    self.parameters.append(param)
                for param in self.parameters:
                    assert param.type.raw_typestr == "NO_TYPE_YET"
            else:
                call = callscope.k_expr
                logger.debug(
                    f"Event {self._header.name} found call {call.ename} in persistent tree search."
                )

                typed_call_params = (
                    call.parameters
                )  # CALL typeassign will have ignored ename.

                for param in typed_call_params:
                    logger.debug(f"Call param {param.name} type {param.type.typestr}")
                    logger.debug(
                        f"Call param {param.name} raw type {param.type.raw_typestr}"
                    )

                for param, typed in zip(paramstrs, typed_call_params):  # ignore ename
                    typed_param = cvar.CPPVariable(
                        name=param,
                        typestr=typed.type.raw_typestr,
                        ispointer=typed.type.ispointer,
                    )
                    self.parameters.append(typed_param)

                assert len(self.parameters) == len(
                    typed_call_params
                )  # rhs ignores the callname param.

                for param in self.parameters:
                    logger.debug(
                        f"Assigned Event param {param.name} type {param.type.typestr}"
                    )
                    logger.debug(
                        f"Assigned Event param {param.name} raw type {param.type.raw_typestr}"
                    )

                # if len(call.parameters[1:]) != len(self.parameters):
                #     logger.debug(f"Call params: {call.parameters[1:]}")
                #     logger.debug(f"Event params: {self.parameters}")
                #     raise pyex.PyramisIncompatibleCallSignatureError()

        defaults = []
        if self._index == 1:  # a hack
            defaults.extend(
                [
                    cvar.CPPVariable(name="len", typestr="int"),
                    cvar.CPPVariable(name="fd", typestr="int"),
                    cvar.CPPVariable(
                        name="client_ip", typestr="struct sockaddr_in", ispointer=True
                    ),
                    cvar.CPPVariable(
                        name="nfvInst", typestr="struct nfvInstanceData", ispointer=True
                    ),
                ]
            )
        elif self._IRContextManager.is_event_in_arch(ename):
            defaults.extend(
                [
                    cvar.CPPVariable(name="len", typestr="int"),
                    cvar.CPPVariable(name="fd", typestr="int"),
                    cvar.CPPVariable(
                        name="client_ip", typestr="struct sockaddr_in", ispointer=True
                    ),
                    cvar.CPPVariable(
                        name="nfvInst", typestr="struct nfvInstanceData", ispointer=True
                    ),
                ]
            )
        else:
            defaults.extend(
                [
                    cvar.CPPVariable(name="fd", typestr="int"),
                    cvar.CPPVariable(
                        name="client_ip", typestr="struct sockaddr_in", ispointer=True
                    ),
                    cvar.CPPVariable(
                        name="nfvInst", typestr="struct nfvInstanceData", ispointer=True
                    ),
                ]
            )

        # storing typed parameters in event header.
        self.parameters.extend(defaults)
        self._header.parameters = self.parameters
        # presently, pyramis params wont be given to the event.
        # only defaults will be added.

    # def type_validate(self):
    #     if not self.parameters:
    #         return False
    #     else:
    #         return True

    def add_params_to_scope(self):
        for param in self.parameters:
            self._scope.set_symbol(param.name, param.type)

    def semantic_check(self):
        # update the scope symbols
        pass

    def generate_event_text(self):
        """
        Will go through its header, and then its calls,
        call generate_raw_code, and store the objects
        test as a formatted string in converted_cpp_code.
        Called by pytranslator
        """
        eheader = self._header
        logger.debug(f"{eheader.name}")

        # calls generate_raw_code().
        # Contains indents acc to current pyt. flow.
        # alter: seperate raw_code_gen from indent + file write.


class PyramisKeywordFunctionExpr(ABC):
    """
    Base for all IR Pyramis Keywords. Always created after scope.
    """

    def __init__(self, IRContextManager, scope, _params=[]):
        self._IRContextManager = IRContextManager
        self.scope_exit = 0
        self._scope = scope
        self._params = _params  # list of strings from DSL
        self.parameters = []  # list of CPPVariables, generated from _param.

        self.raw_code = ""  # tab indented code, no braces.

        # self.indent = context.previousindent # only new scope KW changes previous indent.

    def add_params_to_scope(self):
        t_scope = self._scope.get_first_block_ancestor()
        logger.debug(f"Adding to scope: {t_scope}")

        for param in self.parameters:
            logger.debug(param)
            t_scope.set_symbol(param.name, param.type)

        logger.debug(
            f"Symbols:{[(param.name, param.type.typestr) for param in self.parameters]}\n"
        )
        logger.debug(f"Updated symtab: {t_scope._symtab}")

        logger.debug(
            f"Symbols:{[(sym, param_t.typestr) for sym, param_t in t_scope._symtab.items()]}\n"
        )

    @abstractmethod
    def type_assign(self):
        """
        Given keyword object with param strings,
        give types to the parameters.
        Populates params list of Expr

        We only pass name.split[.][0] and name.split[.][-1]. Any struct
        will be saved in context with its child Type tree. Only IF. exists in attrname.
        - If traverse() doesnt find the type of sub, the attribute is
        invalid.
        """
        pass

    @abstractmethod
    def syntax_check(self):
        """
        1. Checks Signatures of every Expression.
        """
        pass

    @abstractmethod
    def semantic_check(self):
        """
        Enforce scoping rules, semantic type checking.
        Updatescope.symbols
        """
        pass

    @abstractmethod
    def generate_raw_code(self):
        """
        Code is just a cpp string, without regard for
        cpp syntactic sugar.
        All calls to be printed with indent = event.indent + 1
        """
        # headers and footers
        header = ""
        footer = ""

        # if function has endLines, print a } for each


"""
----------------------------------------------------------
Below are all the keywords defined in the Pyramis Language.
To extend the DSL,
define a new class and implement the abstract methods.
----------------------------------------------------------

----------------------------------
PYTHON Keywords, created by visit_
----------------------------------
"""


class K_If(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

        # self.blockindent = context.previousindent + 1 # block indent
        self.body = []
        self.clauses = []

    def syntax_check(self):
        pass

    def type_assign(self):  # assign types to clause-string list
        param = self._params[0]
        # logger.debug(param)

        clausestrs = parsers.make_clauses(
            param
        )  # [[#a1#, #>#, #b1#], '&&', [a2==b2']]..etc.
        # logger.debug(clausestrs)
        # assign types i.e. store as variables in params
        for clause in clausestrs:
            # check scopes for the clause
            for i, cc in enumerate(clause):
                # logger.debug(cc)
                cctype = self._IRContextManager.get_symbol(cc)
                if cctype:
                    ccx = cvar.CPPVariable(
                        name=cc, typestr=cctype.typestr, ispointer=cctype.ispointer
                    )
                    logger.debug(f"{ccx.name} children: {ccx.type.childTypes}")
                    clause[i] = ccx
                else:
                    raise pyex.CompilerTypeInferenceError()
            self.clauses.append(clause)  # typef claause
        logger.debug(f"IF Clauses: {self.clauses}")

    def semantic_check(self):
        # ensure types are consistent
        pass

    def generate_raw_code(self):
        clauses = self.clauses

        for clause in clauses:  # updates self.clauselist
            if len(clause) == 3:  # IF
                _lhs, _, _rhs = clause
            elif len(clause) == 1:
                _lhs = clause[0]
            else:
                logger.debug(clauses)
                raise ValueError("Invalid clause format")

            logger.debug(
                f"type i.e. child for {_lhs.name} is {_lhs.type.type}, infer: {_lhs.type.inferstatus}"
            )

            if "json" in _lhs.type.typestr or "Json" in _lhs.type.typestr:
                _lhs.name = parsers.parse_json_attr(_lhs.name.strip())

                if _lhs.type.typestr == "string":
                    _lhs.name = f"{_lhs.name}.get<string>()"

            elif _lhs.type.typestr in ("HttpRequest", "HttpResponse"):
                _lhs.name = parsers.parse_http_attr(_lhs.name.strip())

            else:
                logger.debug("Th clause is not JSON or HTTP")

            pkey = list(
                self._IRContextManager.find_parent_key_by_key("PrintableString_t")
            )

            if _rhs:
                logger.debug(f"clause init rhs: {_rhs.name}")
                if "MACRO" in _rhs.name:
                    _rhs.name = (
                        _rhs.name.replace("MACRO", "").replace("(", "").replace(")", "")
                    )
                if "UDF" in _rhs.name:
                    _rhs.name = (
                        _rhs.name.replace("UDF", "").replace("(", "").replace(")", "()")
                    )

                if (
                    "json" in _rhs.ptype.typestr or "Json" in _rhs.ptype.typestr
                ):  # ptype needs a fix. typetree.findType(). True or false if an attr of some type exists
                    _rhs.name = parsers.parse_json_attr(_rhs.name.strip())

                    if (
                        "string" not in _lhs.type.typestr
                        and _lhs.type.typestr not in pkey
                    ):
                        _rhs.name = f"{_rhs.name}.asInt()"
                    else:
                        _rhs.name = f"{_rhs.name}.asString().c_str()"

                elif _rhs.ptype.type in ("HttpRequest", "HttpResponse"):
                    _rhs.name = self.parse_http_attr(_rhs.name.strip())

                if (
                    "*" in _lhs.type.typestr
                    and "*" not in _rhs.type.typestr
                    # and _rhs.type.type != "std::string"
                ):
                    _rhs.name = f"&{_rhs.name}"

                logger.debug(f"clause final rhs: {_rhs.name}")

            # Add clauses to raw_code.

            # generate code for exprs in IF body. ELSE should be in body.
            for expr in self.body:
                expr.generate_raw_code()


class K_Loop(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)
        self.body = []

    def syntax_check(self):
        pass

    def type_assign(self):
        for _p in self._params:
            ptype = self._IRContextManager.get_symbol(_p)
            param = cvar.CPPVariable(_p, ptype.raw_typestr, ptype.ispointer)
            self.parameters.append(param)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        # LOOP -> for syntax

        for expr in self.body:
            expr.generate_raw_code()


class K_BREAK(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        assert not self._params

    def type_assign(self):
        pass

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        pass


class K_CONTINUE(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params=None):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        assert not self._params

    def type_assign(self):
        pass

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        pass


class K_PASS(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params=None):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        assert not self._params

    def type_assign(self):
        pass

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        pass


class K_Else(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)
        self.body = []

    def syntax_check(self):
        assert not self._params

    def type_assign(self):
        pass

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        # do ELSE syntax.
        for expr in self.body:
            expr.generate_raw_code()


class K_APPEND(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        """
        Context.currentscope does not contain these params yet.
        """
        # param = cvar.CPPVariable(name = self._params[0],
        #                          typestr = self._params[1])

        # # add to keyword params
        # self.parameters.append(param)

        # check value to be appended is defined, else error.
        if not self._IRContextManager.get_symbol_from_scopes(self._params[0]):
            raise pyex.PyramisNameError()

    def semantic_check(self):
        # is container a valid container type?
        pass

    def generate_raw_code(self):
        container = self.parameters[0]
        value = self.parameters[1]

        if "<std::vector>" in container.type.type:
            self.raw_code = f"\n\t{container.name}.push_back({value.name});\n"

        else:  # check if type contains protocolie_s. If yes, .. else, ...
            test = list(self._IRContextManager.find_parent_key_by_key("protocolIEs"))
            logger.debug(f"ASN_SEQ: {test}")
            if container.type.type in test:
                self.raw_code = f"\n\tASN_SEQUENCE_ADD(&{container.name}.protocolIEs.list, &{value.name});\n"
            else:
                self.raw_code = (
                    f"\n\tASN_SEQUENCE_ADD(&{container.name}.list, &{value.name});\n"
                )


class K_CALL(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)
        self.ename = self._params[0]

    def syntax_check(self):
        pass

    def type_assign(self):
        """
        We expect every CALL to have parameters that are declared
        before being used.
        """
        for p in self._params[1:]:  # skip event name
            ptype = self._IRContextManager.get_symbol(p)
            symbol = cvar.CPPVariable(p, ptype.raw_typestr, ptype.ispointer)
            self.parameters.append(symbol)

    def semantic_check(self):
        """
        `CALL` signatures must match the signature of the first `CALL` in the program.
        If an inconsistency is detected, raise an error.
        """
        pass

    def generate_raw_code(self):
        pass


class K_CREATE_MESSAGE(PyramisKeywordFunctionExpr):
    """
    CREATE MESSAGE or array of MESSAGE only.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        """
        Normal compiler would catch these during parsing
        because of the grammar.
        We need to use this workaround.
        """
        # is number of args = 3 or 2? if no syntax error
        if len(self._params) > 3:
            raise pyex.PyramisSyntaxError()

    def type_assign(self):
        try:
            mid, mtype, msz = self._params
            param = cvar.CPPVariable(name=mid, typestr=mtype, sz=msz)
        except:
            mid, mtype = self._params
            param = cvar.CPPVariable(name=mid, typestr=mtype)

        # if not ctypes.check_type_in_dictionary(param.name, context.messagetypes)
        #     raise pyex.PyramisTypeError()
        logger.debug(f"Create Message of Type: {param.type.typestr}")

        if not param.type.make_tree(self._IRContextManager._asnbasetypes):
            raise pyex.PyramisTypeError()

        logger.debug(f"Typetree: {param.type.childTypes}")

        self.parameters.append(param)

    def semantic_check(self):
        # shadowing warning
        _symbolname = self._params[0]
        if self._IRContextManager.get_symbol_from_scopes(_symbolname):
            logger.debug(f"Warning: Shadowing var in CREATE_MESSAGE: {_symbolname}")

    def generate_raw_code(self):
        msglocalid = self.parameters[0].name
        msgtype = self.parameters[0].type.type
        typesz = self.parameters[0].type.sz

        if typesz:
            text = f"\n\n\t{msgtype} {msglocalid}[{typesz}] = {{}};"
        else:
            text = f"\n\n\t{msgtype} {msglocalid} = {{}};"

        if msgtype == "HttpRequest":
            httpftr = f'\n\t{msglocalid}.options.insert({{"Host", "127.0.0.1"}}); \
                        \n\t{msglocalid}.options.insert({{"User-Agent","cpprestsdk/2.10.15"}}); \
                        \n\t{msglocalid}.options.insert({{"Connection","Keep-Alive"}});\n'
            text = f"{text}{httpftr}"

        self.raw_code = f"{text}"


class K_DECODE(PyramisKeywordFunctionExpr):
    """
    Boilerplate code to signify a decoder is being called.
    Decoder is a UDF that must be defined in udf.cpp
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        # find the UDF
        uname = self._params[0]
        udf = self._IRContextManager.get_symbol_from_scopes(uname)

        if not udf:  # If UDF name is incorrect
            raise pyex.PyramisNameError()

        assert type(udf) == FunctionHeader

        uparameters = [u for u in udf.parameters]

        # assign udf types to params
        for uparameter, param in zip(uparameters, self._params[1:]):
            parameter = cvar.CPPVariable(
                name=param,
                typestr=uparameter.type.raw_typestr,
                ispointer=uparameter.type.ispointer,
            )

            self.parameters.append(parameter)

    def semantic_check(self):
        """
        `params[0]` i.e. the UDF must be defined before tree-walk.
        Via Globalscope check.
        - Apparently checked above.
        """
        pass

    def generate_raw_code(self):
        decoderfunction = self.name
        messagebody = self.parameters[0]
        message = self.parameters[1]

        text = f"\n\t{messagebody.type.typestr} {messagebody.name};\n\t{decoderfunction}({messagebody.name}, {message.name}, len);\n"
        self.raw_code = f"{text}"


class K_ENCODE(PyramisKeywordFunctionExpr):
    """
    Boilerplate code to signify a ENCODER is being called.
    Encoder is a UDF that must be defined in udf.cpp.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        if len(self._params) != 4:
            raise pyex.PyramisSyntaxError()

    def type_assign(self):
        uname = self._params[0]

        udf = self._IRContextManager.get_symbol_from_scopes(uname)

        if not udf:  # If UDF name is incorrect
            raise pyex.PyramisNameError()

        assert type(udf) == FunctionHeader

        uparameters = [u for u in udf.parameters]

        for pid, p in enumerate(self._params):
            if pid == 1:
                # assign udf type
                param = cvar.CPPVariable(
                    name=p,
                    typestr=uparameters[0].type.raw_typestr,
                    ispointer=uparameters[0].type.ispointer,
                )
                self.parameters.append(param)

            elif pid == 2:
                # message to be encoded must have a type before encode
                # else InstantiationError()
                ptype = self._IRContextManager.get_symbol_from_scopes(p)
                if not ptype:
                    raise pyex.PyramisInstantiationError()

                param = cvar.CPPVariable(p, ptype.typestr, ptype.ispointer)

                self.parameters.append(param)

    def semantic_check(self):
        """
        `params[2]` i.e. the message not be empty. Raise warning.
        Note: Add a hasattr field to CPPVariable, update from `SET`.
        """
        pass

    def generate_raw_code(self):
        enfname = self.parameters[0].name
        buf = self.parameters[1]

        param_strings = [f"{param.name}" for param in self.parameters[1:]]
        pstr = ", ".join(param_strings)

        l1 = f"{buf.name} = new char[BUF_SIZE];"
        l2 = f"\n\t{enfname}({pstr});"

        text = f"\n\t{l1}{l2}\n"
        self.raw_code = f"{text}"


class K_GET_KEY(PyramisKeywordFunctionExpr):
    """
    Assumes existence of default maps.
    Gets a value stored at key in a fixed map.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        # "FdToKeyMap" stores keys of type int.
        # store int type only, add to scope.
        # if shadow, ignore. Shadow detected by set_symbol
        dmap = self._IRContextManager.get_head_scope().defaultmaps["FdToKeyMap"]

        key_id = cvar.CPPVariable(
            self._params[0], dmap.keytype.typestr, dmap.keytype.ispointer
        )

        self.parameters.append(key_id)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        mapname = "fdToKeyMap"
        localid = self.parameters[0].name
        localidtype = self.parameters[0].type.type
        func_header_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock);"

        text = f"\n\t{localidtype} {localid} = {mapname}[fd]; \
        \n\tpthread_mutex_unlock(&{mapname}Lock);"

        self.raw_code = f"{func_header_txt}{text}"


class K_LOOKUP(PyramisKeywordFunctionExpr):
    """
    Add to IRContext.map_access_history
    For compund types, only need to look in scope.symbols, traverse()
    Expect any compound type being accessed to have its
    type tree created previously.
    If name.split(.)[-1] not found, its an invalid attribute.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        """
        LOOKUP(localstorageid, Mapname, keyname, attributename)
        """
        for pname in self._params:
            ptype = self._IRContextManager.get_symbol(pname)
            # logger.debug(ptype)
            assert isinstance(ptype, cvar.CPPVariableType)
            param = cvar.CPPVariable(
                name=pname, typestr=ptype.typestr, ispointer=ptype.ispointer
            )

            self.parameters.append(param)

        ident, name, key, attr = self.parameters
        logger.debug(f"LOOKUP ident type: {ident.type.typestr}")  # curious.
        pmapHeader = pymap.PyramisMapAccessHeader(
            line_no=self._scope.start,
            mapname=name,
            class_="LOOKUP",
            mapkey=key,
            mapattr=attr,
        )

        self._IRContextManager.get_map_accesses().append(pmapHeader)

    def semantic_check(self):
        # ident must be of type(attr)
        mapname = self.parameters[1].name
        ident = self.parameters[0]
        attr = self.parameters[2]

        # Check the current mapaccesshistory each time.
        # assume stores only occur in Last Event.
        # STORE semantic check checks for untyped lookups
        # assigns types to a pmapHeader[Lookups].
        # Updates its params

        # Assign types in generate_map_header.
        # Let some NOTPE params persist till then

        # if attr.type == "NOTYPE": # notype even if store comes later.
        #     attr.type = cvar.CPPVariableType(typestr="string",
        #                                      ispointer=False)

        if ident.type.typestr == "NOTYPE":  # need to formalise type predictions.
            # assign type(attr)
            ident.type = attr.type

        # update context
        for param in self.parameters:
            assert isinstance(param, cvar.CPPVariable)
            self._scope.set_symbol(param.name, param.type)

    def generate_raw_code(self):
        # Called after first AST walk.
        # Will all MAP operations be typed after end of first walk?
        # use maps
        mapref = cfile.CPPFile.maps
        mapname = self.parameters[1].name

        keyname = self.parameters[2].name
        attrname = self.parameters[3].name

        localstorageid = self.parameters[0].name

        # return map attribute (name, type, isptr) from map post generate_map_defs()
        localidobj = next(
            (x for x in mapref[mapname].attributes if x.name == attrname), None
        )

        # if parent_func == None: # ???
        #     func_header_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock)"
        prevc = self._scope.get_parent_scope().children[-2]
        prevm = self._IRContextManager.get_map_accesses()[
            -1
        ]  # store mapaccesses as a stack.

        if prevc.class_ not in [
            "K_STORE",
            "K_LOOKUP",
        ]:  # checks if previous call was a store or lookup (scope.calls.prev())
            func_header_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock);"
            # parent_func.last_map_accessed = mapname # store info in scope.
        else:
            if mapname == prevm.name:
                pass
            else:
                f1_txt = f"\n\tpthread_mutex_unlock(&{prevm.name}Lock);"
                f2_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock);"
                func_header_txt = f"{f1_txt}{f2_txt}"

        if not localidobj:  # attr not a common attr.
            text = "/*\n<MAP ELIMINATED. STORED but not LOOKED UP>\n\n*/"
        else:
            if keyname == "NULL":
                text = f'\n\t{localidobj.type.typestr} {localstorageid} = {mapname}["structEntry"].{attrname};'
            else:
                text = f"\n\t{localidobj.type.typestr} {localstorageid} = {mapname}[{keyname}].{attrname};"

        self.raw_code = f"{func_header_txt}{text}"


class K_STORE(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        """
        STORE(mapname, mapkey, mapattribute, mapvalue)

        1. Every store attr will be typed before storing in the mapref.
        2. codegen, semantic for lookups will only use maps{}. parameters unused.
        At the end of STORE, the Map accessed should will have
        a single attribute(TYPED) and single value(TYPED).
        This info is stored in map_access_history as dict of
        mapname: STORE[pmah1, pmah2], LOOKUP[]
        """
        for pname in self._params:

            ptype = self._IRContextManager.get_symbol(pname)
            assert isinstance(ptype, cvar.CPPVariableType)
            param = cvar.CPPVariable(
                name=pname, typestr=ptype.typestr, ispointer=ptype.ispointer
            )

            self.parameters.append(param)

        name, key, attr, val = self.parameters
        # STORE assigns a type to its attribute.
        if val.type.typestr == "NOTYPE":
            raise pyex.PyramisNameError()

        attr.type = val.type

        # store in a mapheader
        pmapHeader = pymap.PyramisMapAccessHeader(
            line_no=self._scope.start,
            mapname=name,
            class_="LOOKUP",
            mapkey=key,
            mapattr=attr,
        )

        self._IRContextManager.get_map_accesses().append(pmapHeader)

    def semantic_check(self):
        # the value base must be declared before store.
        # get_symbol must always return for value.
        pass

    def generate_raw_code(self):
        mapname = self.parameters[0].name
        mapkey = self.parameters[1].name
        mapattr = self.parameters[2].name
        mapvalue = self.parameters[3].name

        # HACK
        if (
            self.parameters[3].ptype.type == "json"
            or self.parameters[3].ptype.type == "Json::Value"
        ):
            splita = mapvalue.split(".")

            vals = []
            for item in splita:
                parts = item.split("[")
                vals.append(parts[0])  # Add the first part
                vals.extend(
                    part.strip("]") for part in parts[1:]
                )  # Add the remaining parts

            if len(vals) != 1:
                rhs = vals[0]
                for val in vals[1:]:
                    if val._isdigit():
                        rhs = f"{rhs}[{val}]"
                    else:
                        rhs = f'{rhs}["{val}"]'
        else:
            rhs = mapvalue

        # if parent_func == None:
        #     func_header_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock)"
        #     parent_func.last_map_accessed = mapname
        prevc = self._scope.get_parent_scope().children[-2]
        prevm = self._IRContextManager.get_map_accesses()[
            -1
        ]  # store mapaccesses as a stack.

        if prevc.class_ not in ["K_STORE", "K_LOOKUP"]:
            func_header_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock);"
        else:
            if mapname == prevm.name:
                pass
            else:
                f1_txt = f"\n\tpthread_mutex_unlock(&{prevm.name}Lock);"
                f2_txt = f"\n\tpthread_mutex_lock(&{mapname}Lock);"
                func_header_txt = f"{f1_txt}{f2_txt}"

        if mapkey == "NULL":
            text = f'\n\t{mapname}["structEntry"].{mapattr} = {rhs};'
        else:
            text = f"\n\t{mapname}[{mapkey}].{mapattr} = {rhs};"
        # dict access code. [] = etc
        self.converted_cpp_code = f"{func_header_txt}{text}"


class K_READ_CONFIG(PyramisKeywordFunctionExpr):
    """
    param[1] can only be a json file. Enforce in syntax check.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        assert "json" in self._params[1]

    def type_assign(self):
        for pid, p in enumerate(self._params):
            if pid == 0:
                param = cvar.CPPVariable(name=p, typestr="jsonfile_xt", ispointer=False)
            elif pid == 1:
                ptype = self._IRContextManager.get_symbol(p)

                param = cvar.CPPVariable(
                    name=p, typestr=ptype.typestr, ispointer=ptype.ispointer
                )
            self.parameters.append(param)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        filename = self.parameters[1].name
        varname = self.parameters[0].name
        vartype = self.parameters[0].type.type

        text = f'\n\n\tifstream ifs("{filename}"); \
                    \n\tJson::Reader reader;\
                    \n\t{vartype} {varname} = {{}}; \
                    \n\treader.parse(ifs, {varname});\n'
        self.raw_code = f"{text}"


class K_SEND(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def _get_port_protocol(
        self, n1, n1_interface
    ):  # AMF, N2 if callback function not NULL
        arch_data = self._IRContextManager.get_head_scope()._arch
        logger.debug(f"arch_data for {n1} and {n1_interface}")
        if n1 in arch_data and "Interfaces" in arch_data[n1]:
            for iface in arch_data[n1]["Interfaces"]:
                if iface["Name"] == n1_interface:
                    conn = "true" if iface["ConnectionType"] == "SHORT" else "false"
                    return iface["Port"], iface["TransportProtocol"], conn

        return None  # Node or interface not found

    def type_assign(self):
        if self._params[3] == "RAN":
            interface_details = self._get_port_protocol(
                self._params[2], self._params[4]
            )

        else:
            interface_details = self._get_port_protocol(
                self._params[3], self._params[4]
            )

        self._params.extend(interface_details)
        logger.debug(self._params)

        for p in self._params:
            ptype = self._IRContextManager.get_symbol(p)
            param = cvar.CPPVariable(str(p), ptype.typestr, ptype.ispointer)
            self.parameters.append(param)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        # change this up to get correct print.
        params = self.parameters
        m_enc = params[0].name  # 3, 7
        ip = params[1].name  # 1
        node1 = params[2].name
        node2 = params[3].name  # 6
        node1_interface = params[4].name  # maybe n1_interface?
        ipfd_key = params[5].name
        cb_fn = params[6].name  # 9
        port = params[7].name
        protocol = params[8].name
        conn = params[9].name
        # 38214: port  num of interface N2 of node n1
        # false:
        # SCTP: TransportProtocol of interface N2 of node n1
        # fd1: keytoipfd[ipfdkey].second
        # sendData("127.0.0.1", 38412, mess, false, SCTP_PROTOCOL, RAN,strlen(m_enc), fd1, NULL, &ipFdPair.first, nfvInst);
        iptxt = f"pthread_mutex_lock(&keyToFdMapLock);\n\tint fd1 = keyToFdMap[{ipfd_key}];\n\tpair<struct sockaddr_in, int> ipFdPair = keyToIpFdMap[gNId_num];\n\tpthread_mutex_unlock (&keyToFdMapLock);\n"

        text = f"\n\t{iptxt}\n\tsendData({ip}, {port}, {m_enc}, {conn}, {protocol}, {node2}, strlen({m_enc}), fd1, {cb_fn}, &ipfdPair.first, nfvInst);"

        self.raw_code = f"{text}"


class K_SET_KEY(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)

    def syntax_check(self):
        pass

    def type_assign(self):
        dmap = self._IRContextManager.get_head_scope().defaultmaps["KeyToFdMap"]

        ident = cvar.CPPVariable(
            self._params[0], dmap.keytype.typestr, dmap.keytype.ispointer
        )

        self.parameters.append(ident)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        mapname = "KeyToFdMap"
        localid = self.parameters[0].name
        localidtype = self.parameters[0].type.type

        func_header_txt = f"\n\tpthread_mutex_lock(&keyToFdMapLock);"

        text = f"\n\t{mapname}[{localid}] = fd; \
                \n\tstruct sockaddr_in addr = {{}};\
                \n\tmemcpy (&addr, client_ip, sizeof(client_ip)); \
                \n\tkeyToIpFdMap[{localid}] = make_pair(addr, fd); \
                \n\tpthread_mutex_unlock(&keyToFdMapLock); \
        "

        self.raw_code = f"{func_header_txt}{text}"


class K_SET(PyramisKeywordFunctionExpr):
    """
    SETs LHS to the ident at rhs.
    Create a new symbol LHS.
    LHS root must be declared first tho.
    """

    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)
        # self.clauses = []

    def syntax_check(self):
        pass

    def type_assign(self):
        logger.debug(self._params)
        for pid, p in enumerate(self._params):
            if pid == 0:  # lhs
                ptype = self._IRContextManager.get_symbol(p)

                if ptype:
                    param = cvar.CPPVariable(
                        name=p, typestr=ptype.typestr, ispointer=ptype.ispointer
                    )
                else:
                    param = cvar.CPPVariable(
                        name=p, typestr="NO_TYPE_YET", ispointer=False
                    )

            elif pid == 1:  # rhs
                # if '"' in p:
                #     param = cvar.CPPVariable(name=p,
                #                              typestr="string",
                #                              ispointer=False)
                # else:
                ptype = self._IRContextManager.get_symbol(p)

                if not ptype:
                    raise pyex.PyramisNameError()
                else:
                    param = cvar.CPPVariable(
                        name=p, typestr=ptype.typestr, ispointer=ptype.ispointer
                    )
            self.parameters.append(param)

        # if lhs is untyped, assign it the type of rhs.
        lhs = self.parameters[0]
        rhs = self.parameters[1]

        if lhs.type.typestr == "NO_TYPE_YET":
            lhs.type.typestr = rhs.type.typestr
            lhs.type.ispointer = rhs.type.ispointer

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        """
        SET ('nausf_auth_ueAuth.body.supiOrSuci','suciTemp')
        SET has special codegen strings that seem to rely on the
        type of lhs.
        Uses clauses for codegen.
        type(a.b.c.d) = type(d).typestr

        # maybe generate_code updates formatted_name in cppvariable
        if param is functionheader, name()
        """
        lhs, rhs = self.parameters

        pkeytypes = list(
            self._IRContextManager.find_parent_key_by_key("PrintableString_t")
        )
        logger.debug(f"pkeytypes: {pkeytypes}")

        logger.debug(f"{self.__class__} lhs: {lhs.name} and rhs: {rhs.name}")

        if lhs.type.type in pkeytypes:
            text = f"\n\tOCTET_STRING_fromBuf(&{lhs.name}, {rhs.name}, strlen({rhs.name}));"
        else:
            text = f"\n\t{lhs.name} = {rhs.name};"

            if lhs.type.sz:
                text = f"\n\tmemcpy({lhs.name}, {rhs.name}, sizeof({rhs.name}))"

        self.converted_cpp_code = f"{text}"


class K_UDF(PyramisKeywordFunctionExpr):
    def __init__(self, IRContextManager, scope, _params):
        super().__init__(IRContextManager, scope, _params)
        self.udf = None  # updated by type_assign()

    def syntax_check(self):
        pass

    def type_assign(self):
        try:
            udf = self._IRContextManager.get_head_scope().get_symbol_from_scope(
                self._params[1]
            )  # i know where UDFs must be.
            assert isinstance(udf, FunctionHeader)
            self.udf = udf

        except KeyError as k:
            raise pyex.PyramisNameError()

        # Fix return type declaration.
        p0 = self._params[0]
        param0 = cvar.CPPVariable(
            p0, self.udf.returntype.typestr, self.udf.returntype.ispointer
        )
        self.parameters.append(param0)

        for _p, up in zip(self._params[2:], udf.parameters):
            p = self._IRContextManager.get_symbol_from_scopes(_p)

            if p:
                ptype = p
            else:
                ptype = up.type
                logger.debug(f"Type of param {_p} from udf: {ptype.typestr}")
                logger.debug(f"Raw type of param {_p} from udf: {ptype.raw_typestr}")

            param = cvar.CPPVariable(
                name=_p, typestr=ptype.raw_typestr, ispointer=ptype.ispointer
            )

            self.parameters.append(param)

    def semantic_check(self):
        pass

    def generate_raw_code(self):
        self.raw_code = f"\n!!UDF!!\n"
