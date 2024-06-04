from . import python
from . import config

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
]


def is_int(arg):
    '''
    true if arg str is an integer.
    '''

def default_var(gx, name, parent, mv=None):
    '''
    Transform formals of a python.Function into 
    python.Variables, store in Function.vars
    '''
    if parent:
        mv = parent.mv

    var = python.Variable(name, parent)
    if parent:
        parent.vars[name] = var
    gx.allvars.add(var) # global set of variables encountered. Why not store-in-scope?

    return var

# search for an arg in the local scope tree
# return the python.Variable if found.
def lookup_scope(gx, arg):
    pass

# mv needs to call only when appropriate
# eg STORE.
# dotted attrs must also be stored as is in the scope tree.
def type_of_arg(gx, arg):
    # was arg encountered earlier?
    ref = lookup_scope(gx, arg)
    if (ref):
        _type = ref
    else:
        _type = python.Type()
    if arg == "true" or arg == "false":
        _type.ident = "bool"
        return _type
    elif is_int(arg):
        _type.ident = "int"
        return _type
    
def test_valid_type(gx, arg):
    # check cache
    if arg in gx._valid_type_cache:
        return True
    

def type_helper(base_types, arg):
    pass

# call from CREATE MESSAGE 
# need to decode it first.

# def type_from_json_arg(gx, arg):
#     assert(isinstance(gx, config.GlobalInfo))
#     # first check in user types
#     for struct in gx.user_base_types:
#         if struct["__name__"] == arg:
#             final = python.Type(arg) # base structs will have indirection, thing empty. pain to modify struct parsing to differenciate b/w a BASE and a MEMBER
#             attributes = struct["__attributes__"]
#             for attr in attributes:
#                 if attr["__type__"] in C_TYPES:
#                     final.subs[attr["__id__"]] = python.Type(attr["__type__"], attr["__thing__"], attr["__ptr__"])
#                 elif (attr["__type__"] in gx.user_base_types) or ("struct " + attr["__type__"]) in gx.user_base_types:
#                     try:
#                         nested_struct = self.structs[attr.type_str] # this can become a python.type(), should be 
#                     except:
#                         nested_struct = self.structs["struct " + attr.type_str] # this can become a python.type(), should be 
#                     nested_ = self.reduce_to_type(nested_struct, controller) # returns a python.Type with filled in subs
#                     controller.type_cache[nested_.ident] = nested_
#                     final.subs[attr.id] = nested_





    # for struct in gx.pyramis_base_types:

    
    
    # # convert to python.Type()
    # # should be a dict
    # assert(isinstance(attributes, dict))    

