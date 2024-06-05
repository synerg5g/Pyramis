from . import python
from . import config
from . import error
from . import utils

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

# equivalent to the type cache.
# 
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
    elif is_int(arg):
        _type.ident = "int"
    return _type
    
def test_valid_type(gx, arg):
    # check cache
    if arg in gx.user_base_types or arg in gx.pyramis_base_types:
        return True
    
# for a single main struct
# usage_indirection only from parse_udf.
def reduce_to_type(gx, struct, base_types, usage_indirection):
    assert(isinstance(struct, dict))
    if not isinstance(base_types, dict):
        print(type(base_types))
        # handle list with same type name.
    assert(isinstance(base_types, dict))
    
    if usage_indirection:
        final = python.Type(struct["__name__"], usage_indirection)  
    else:
        if struct["__name__"] in gx.type_cache:
            return gx.type_cache[struct["__name__"]]
        final = python.Type(struct["__name__"])  

    attributes = struct["__attributes__"]
    for attr in attributes.values():
        if attr["__type__"] in C_TYPES:
            # in a ident a.b.c.d, looking for type_of(c) should return name of Python.Type() only (excluding subs)
            # eg: if c in t.subs, return t.sibs[c].type_str
            # remember invariant: Each python.Type() must be stored in the scope. Hence incomplete types are not accessed
            # incividually. 
            final.subs[attr["__id__"]] = python.Type(attr["__type__"], attr["__thing__"], attr["__ptr__"])
        elif (attr["__type__"] in base_types) or ("struct " + attr["__type__"]) in base_types:
            try:
                nested_struct = base_types[attr["__type__"]] # this can become a python.type(), should be 
            except:
                nested_struct = base_types["struct " + attr["__type__"]] # this can become a python.type(), should be 
            
            nested_ = reduce_to_type(gx, nested_struct, base_types, usage_indirection) # returns a python.Type with filled in subs
            gx.type_cache[nested_.ident] = nested_
            final.subs[attr["__id__"]] = nested_
        else:
            # enum type
            #print(f"{attr} likely enum")
            final.subs[attr["__type__"]] = python.Type(attr["__type__"], thing=utils.TH_ENUM)

    #print(struct)
    return final

# call from CREATE MESSAGE, parse udfs
# need to decode it first.
# base_types will be a dict of type_t: {...etc...}
def type_from_arg(gx, arg, usage_indirection=None):
    assert(isinstance(gx, config.GlobalInfo))
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
    user_bases = gx.user_base_types
    for struct_name, struct in user_bases.items():
        if (isinstance(struct, list)):
            if arg != struct_name:
                continue
            else:
                # return first one by default
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
                # return first one by default
                final = reduce_to_type(gx, struct, pyramis_bases.values(), usage_indirection)
                return final
        assert(isinstance(struct, dict))
        if struct["__name__"] == arg:
            final = reduce_to_type(gx, struct, pyramis_bases.values(), usage_indirection)# base structs will have indirection, thing empty. pain to modify struct parsing to differenciate b/w a BASE and a MEMBER
            return final
    
    # something is wrong with my struct parser itself OR
    # (more likely user has given an incorrect type)
    #print(f"[{type(arg)}]")
    # likely enum
    #print(f"{arg} not recognised, default to enum")
    return python.Type(arg, thing=utils.TH_ENUM)

    #error.error(f"{arg} is not a valid type for this system.")
    

        
    


