from . import python
from . import config
from . import error
from . import utils
import copy

class Scope:
    '''
    
    '''
    MODULE = "Module"
    EVENT = "Event"
    BLOCK = "BLOCK"

    def __init__(self, kind, encloser=None):
        self.kind = kind  # MODULE, EVENT
        self.encloser = encloser
        self.symtab = {}  # name: python.Variable
        self.id = id(self)

def enter_new_scope(mv, scope_kind):
    '''
    Create a new scope object, Update the live-scope maintained in gx,
    set parent of new scope = current scope, return ref to new scope
    ---
    On new scope entry, inherit all variables from symtab of parent.
    '''
    if scope_kind == Scope.MODULE:
        # Entering a new module, i.e. set root scope
        mv.root_scope = Scope(Scope.MODULE) # must never change
        mv.live_scope = mv.root_scope
        mv.indent = 0
        indent = 0

    elif scope_kind == Scope.EVENT:
        # Entering a new event.
        assert(mv.live_scope.kind == Scope.MODULE) # scope exits must be done correctly for If
        new_scope = Scope(Scope.EVENT)
        new_scope.encloser = mv.live_scope
        mv.live_scope = new_scope
        mv.indent+= + 1
    
    elif scope_kind == Scope.BLOCK:
        # Enter new BLOCK scope
        assert(mv.live_scope.kind == Scope.EVENT or mv.live_scope.kind == Scope.BLOCK)
        new_scope = Scope(Scope.BLOCK)
        new_scope.encloser = mv.live_scope
        mv.live_scope = new_scope
        mv.indent += 1
    else:
        error.error("Not a valid Scope kind", warning=True)

    print(f"Created new live scope of kind {mv.live_scope.kind}")

    indent = copy.deepcopy(mv.indent)

    # copy parent variables
    if not (mv.live_scope.kind == Scope.MODULE):
        for var_name, var in mv.live_scope.encloser.symtab.items():
            mv.live_scope.symtab[var_name] = var

    return mv.live_scope, indent

def exit_live_scope(mv):
    '''
    Set the gx live-scope to the parent of the current live scope.
    Should call at the end of every node visit.
    '''
    mv.live_scope = mv.live_scope.encloser
    mv.indent -= 1
    print(f"Exiting scope, new live scope: {mv.live_scope.kind}, indent: {mv.indent}")

def add_var_to_live_scope(mv, var):
    '''
    Relies on the fact that child scope inherits variables of its parent.
    Symtab for an identifier may contain a list of python.Types
    in case the protocol library has multiple structs with the same
    name.
    '''
    # print(f"adding var to scope: {var}: {var.type}")
    if var.name not in mv.live_scope.symtab:
        # first instance of the var in this scope
        # print(f"First instance of {var.name} in this scope, {mv.live_scope.kind}")
        mv.live_scope.symtab[var.name] = var
    elif var.type and (not mv.live_scope.symtab[var.name].type):
        # definitely overwrite type
        # print(f"previously untyped variable is now typed, {var.name}: {var.type.ident}")
        mv.live_scope.symtab[var.name].type = var.type
    else:
        # overwrite type?
        # print(f"WARNING: `{ mv.live_scope.symtab[var.name].name}`: { mv.live_scope.symtab[var.name].type.ident} already exists in the current scope.")
        # print(f"Avoided overwrting with new value {var.name}: {var.type.ident}")
        pass

C_TYPES = [
    "char",
    "signed char",
    "unsigned char",
    "string",
    "short",
    "unsigned short",
    "int",
    "unsigned int",
    "long",
    "unsigned long",
    "long long",
    "unsigned long long",
    "float",
    "double",
    "long double",
    "int8_t",
    "uint8_t",
    "int16_t",
    "uint16_t",
    "int32_t",
    "uint32_t",
    "int64_t",
    "uint64_t",
    "string", 
    "json",
    "Json::Value",
    "void",
    "size_t",
    "std::string"
]


def is_int(arg):
    '''
    true if arg str is an integer.
    '''

# mv needs to call only when appropriate
# eg STORE. dotted attrs must also be stored as is in the scope tree.

def get_variable_from_scope(mv, arg_idx, parent, ident):
    # search the persistent scope structure
    # upto the current event.
    # return variable (typed/untyped) if true, else None
    curr_scope = mv.live_scope
    while(curr_scope.kind != Scope.MODULE):
        if (ident in curr_scope.symtab):
            # print(f"{ident} found in scope {curr_scope} of kind {curr_scope.kind}")
            # may even return a list
            return curr_scope.symtab[ident]
        else:
            # climb parent
            curr_scope = curr_scope.encloser
    return None

# search for an arg in the local scope tree
# return the python.Variable if found.
# ident must be the full dotted name
# parent is the python.Action() that contains this variable
# create the python.Action before get_variable.
def get_variable(mv, arg_idx, ident, parent):
    # print(f"get_variable(): Attempting to get variable for {ident} in action {parent.name}")
    assert(isinstance(parent, python.Action) or isinstance(parent, python.Event))
    if not ident:
        return None
    
    if ident == "true" or ident == "false":
        _type = python.Type("bool")
        return python.Variable(arg_idx, ident, parent, _type)
    elif is_int(ident) or parent.name == "SET_KEY" or parent.name == "GET_KEY":
        _type = python.Type("int")
        return python.Variable(arg_idx, ident, parent, _type)
    elif '"' in ident:
        _type = python.Type("string")
        return python.Variable(arg_idx, ident, parent, _type)
    elif ".size()" in ident:
        _type = python.Type("size_t")
        return python.Variable(arg_idx, ident, parent, _type)
        
    # store the stem i.e. terminal attribute and root i.e base ident
    stem = ident.split(".")[-1]
    root = ident.split(".")[0]
    dotted = (len(ident.split(".")) > 1)
    # print(ident)
    # print(f"Dotted: {dotted}")

    # search for exact (dotted or otherwise) name in scope.
    var = get_variable_from_scope(mv, arg_idx, parent, ident)
    if (var):
        return var # typed or untyped simple/dotted ident.
    else: # exact name not used yet.
        if not dotted:
            # this is the first ever encounter - i.e. 
            # no python.Var() has ever been created in THIS scope.
            # return untyped variable
            # print(f"Created a new untyped python.Variable for {ident}")
            return python.Variable(arg_idx, ident, parent)
        else:
            # if dotted not found, search for type of root
            # print(f"Getting variable of root {root}")
            var = get_variable_from_scope(mv, arg_idx, parent, root)
            if not var:
                # accessing attributes of an unitialised variable.
                error.error("`%s`: Attempt to access unitialised variable `%s`"%(parent.name, root))
            elif (var.type):
                if var.type.ident == "json":
                    # any attribute of a json obj will have type json.
                    # expect another layer of type assign during
                    # code-gen for set/udf asString()
                    final_t = python.Type("json") 
                # print(f"Type of root {root} is {var.type}")
                final_t = var.type.get_typeof(stem)
                # print(f"Type of stem {stem} is {fi    nal_t}")
                return python.Variable(arg_idx, ident, parent, final_t)
            else:
                # invalid attribute access.
                error.error(f"Invalid sub-attribute of {var.name}  was accessed.")
                return None
    
def test_valid_type(gx, arg):
    # check cache
    if arg in gx.user_base_types or arg in gx.pyramis_base_types:
        return True
    
# for a single main struct
# usage_indirection only from parse_udf.
def reduce_to_type(gx, struct, base_types, usage_indirection):
    print("reducing to type: %s"%struct)
    if isinstance(struct, list):
        # struct with multiple definitions
        # pick the one with most attributes
        _finals = []
        for _struct in struct:
            _finals.append(reduce_to_type(gx, _struct, base_types, usage_indirection))
        return _finals

    assert(isinstance(struct, dict))

    if not isinstance(base_types, dict):
        print(type(base_types))
        # handle list with same type name.

    assert(isinstance(base_types, dict))

    if usage_indirection:
        try:
            final = python.Type(struct["__name__"], struct["__thing__"], usage_indirection, struct["__asn_seq__"])  
        except KeyError as k:
            print("keyerrror thing, ind")
            final = python.Type(struct["__name__"], usage_indirection)
    else:
        try:
            final = python.Type(struct["__name__"], struct["__thing__"]) 
        except KeyError as k:
            print("keyerror thing ,no ind")
            final = python.Type(struct["__name__"]) # type becomes simple 

    attributes = struct["__attributes__"] # dict of dict
    for attr_name, attr in attributes.items(): # attr is a dict
        if attr["__type__"] in C_TYPES: # terminal
            # in a ident a.b.c.d, looking for type_of(c) should return name of Python.Type() only (excluding subs)
            # eg: if c in t.subs, return t.sibs[c].type_str
            # remember invariant: Each python.Type() must be stored in the scope. Hence incomplete types are not accessed
            # incividually. 
            final.subs[attr["__id__"]] = python.Type(attr["__type__"], attr["__thing__"], attr["__ptr__"], attr["__asn_seq__"])
        elif (attr["__type__"] in base_types) or ("struct " + attr["__type__"]) in base_types:
            try:
                nested_struct = base_types[attr["__type__"]] # this can become a python.type(), should be 
            except:
                nested_struct = base_types["struct " + attr["__type__"]] # this can become a python.type(), should be 
            
            print(nested_struct)
            
            nested_ = reduce_to_type(gx, nested_struct, base_types, usage_indirection) # returns a python.Type with filled in subs or a list of types.
            if isinstance(nested_, list):
                print(f"Reduce returned list of types, reduce_to_type: {[(nested__.ident, nested__.thing) for nested__ in nested_]}")
                gx.type_cache[nested_[0].ident] = nested_ # both have same ident, dont care
            else:
                assert(isinstance(nested_, python.Type))
                print(f"Got single python.type: {nested_.ident, nested_.thing}")
                print(nested_.subs.values())
                # try:
                #     print(f"Its attributes: {[(attr, attr_t.ident, attr_t.thing) for attr, attr_t in nested_.subs.items()]}")
                # except  AttributeError as a:
                #     # attr has list of types
                #     for attr, attr_t_list in nested_.subs.items():
                #         print(attr_t_list)
                #         print(f"Its attributes: {(attr, attr_t_list.ident, attr_t_list.thing)}")
                gx.type_cache[nested_.ident] = nested_
            final.subs[attr["__id__"]] = nested_
        else:
            # enum type
            thing = attr["__thing__"]
            if thing != utils.TH_ARRAY:
                print(f"attr {attr_name} is being assigned enum thing. old thing: {thing}")
                final.subs[attr_name] = python.Type(attr["__type__"], thing=utils.TH_ENUM)
            else:
                print(f'attr {attr_name} is being retained: {attr["__type__"]}, {thing}, asn seq: {attr["__asn_seq__"]}')
                final.subs[attr_name] = python.Type(attr["__type__"], thing, usage_indirection, attr["__asn_seq__"])

    ## print(struct)
    return final

# call from CREATE MESSAGE, parse udfs
# need to decode it first.
# base_types will be a dict of type_t: {...etc...}
def type_from_type_str(gx, arg, usage_indirection=None):
    assert(isinstance(gx, config.GlobalInfo))
    ## print(f"convert to python.Type: {arg}")
    if not arg:
        return python.Type("EOT") # end of tree
    
    if "json" in arg:
        return python.Type(arg)
    
    if "std::vector" in arg:
        # extract type
        _tp_name = arg.split("<")[-1].replace(">", "")
        return python.Type(_tp_name, utils.TH_ARRAY, usage_indirection)

    if arg in C_TYPES:
        return python.Type(arg, indirection=usage_indirection)

    # first check in user types
    if gx.user_utils.is_dir():
        user_bases = gx.user_base_types
        for struct_name, struct in user_bases.items():
            if (isinstance(struct, list)):
                if arg != struct_name:
                    continue
                else:
                    # if multiple defns for same type, return a list
                    final = reduce_to_type(gx, struct, user_bases, usage_indirection)
                    return final
            assert(isinstance(struct, dict))
            if struct["__name__"] == arg:
                #print(usage_indirection)
                #print(arg)
                final = reduce_to_type(gx, struct, user_bases, usage_indirection)# base structs will have indirection, thing empty. pain to modify struct parsing to differenciate b/w a BASE and a MEMBER
                return final
    
    pyramis_bases = gx.pyramis_base_types
    for struct_name, struct in pyramis_bases.items():
        if (isinstance(struct, list)):
            if arg != struct_name:
                continue
            else:
                # return first one by default if multiple definitions of 
                # same type
                # ideally: store as a list when create_message is called.
                final = reduce_to_type(gx, struct, pyramis_bases, usage_indirection)
                return final
        assert(isinstance(struct, dict))
        if struct["__name__"] == arg:
            final = reduce_to_type(gx, struct, pyramis_bases, usage_indirection)# base structs will have indirection, thing empty. pain to modify struct parsing to differenciate b/w a BASE and a MEMBER
            return final
    
    # likely enum
    return python.Type(arg, thing=utils.TH_ENUM)

    #error.error(f"{arg} is not a valid type for this system.")
    

        
    


