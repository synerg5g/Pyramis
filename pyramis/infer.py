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
# def default_var(gx, arg_idx, name, parent, mv=None):
#     '''
#     Transform formals of a python.Function into 
#     python.Variables, store in Function.vars
#     '''
#     if parent:
#         mv = parent.mv

#     var = python.Variable(name, parent)
#     if parent:
#         parent.vars[name] = var
#     gx.allvars.add(var) # global set of variables encountered. Why not store-in-scope?

#     return var

# mv needs to call only when appropriate
# eg STORE. dotted attrs must also be stored as is in the scope tree.

def get_variable_from_scope(gx, arg_idx, parent, ident):
    # search the persistent scope structure
    # upto the current event.
    # return variable (typed/untyped) if true, else None
    pass

# search for an arg in the local scope tree
# return the python.Variable if found.
# ident must be the full dotted name
def get_variable(gx, arg_idx, parent, ident):
    if ident == "true" or ident == "false":
        _type = python.Type("bool")
        return python.Variable(arg_idx, ident, parent, _type)
    elif is_int(ident) or parent == "SET_KEY":
        _type = python.Type("int")
        return python.Variable(arg_idx, ident, parent, _type)
    elif '"' in ident:
        _type = python.Type("string")
        return python.Variable(arg_idx, ident, parent, _type)

    # store the stem i.e. terminal attribute and root i.e base ident
    stem = ident.split(".")[-1]
    root = ident.split(".")[0]
    dotted = (len(ident.split(".")) > 1)

    # search for exact (dotted or otherwise) name in scope.
    var = get_variable_from_scope(gx, arg_idx, parent, ident)
    assert(0)
    if (var):
        return var # typed or untyped simple/dotted ident.
    else: # exact name not used yet.
        # non dotted?
        if not dotted:
            # this is the first ever encounter - i.e. no python.Var() has ever been created
            return None 
        else:
            # if dotted not found, search for type of root
            var = get_variable_from_scope(gx, root)
            # if root of dotted found in scope
            if (var.type):
                final_t = var.type.get_typeof(stem)
                return python.Variable(arg_idx,ident, parent, final_t)
            else:
                # invalid attribute access.
                print(f"Invalid attribute of {var.type.ident} was accessed.")
                assert(0)



    # return variable.

    pass

"""
In every visit_call():
    - create the python.Action
    - store all args_strs in a list.

set_typed = []
set_untyped = []
common pattern:
for i, _v in enumerate(args):
    # if used before, returns python.Variable.
    # if not, need to create a new python.Variable for this ident
    var = get_variable(i, _v, <parent>) # typed/untyped
    if (not var):
        # rare
        var = python.Variable(i, _var, <parent>)
    
    # we have a variable, could be typed or untyped depending on actions before
    # the current one.
    # SET(a, b)
    # If type(a) known and type(b) known:
    # - assert t(a) == t(b), error on mismatch
    # 
    # If type(a) known and type(b) not known:
    # - would be strange, trying to set an ident to a pyramis-invalid value
    #
    # If type(a) unkown:
    # - type(b) must be known and type(a) must be set, strange otherwise.
    # [If either type is known, update the other. If both are known, check
    # type consistency. If neither are known, (eg SET(userid, procedurekey)), 
    # store the untyped variable in the scope.
    if parent.action == SET:
        if (var.type):
            set_typed.append(var)
            if len(set_untyped) == 1:  
                # 0 untyped 1 typed
                # var is 1
                set_untyped[0].type = var.type

        if len(set_types) == 2:
            assert(typed[0].type.equals(typed[1].type))     
        
            
    # if var untyped, either used before or this is first occurence.
    if not var.type:
        # should be able to get a concrete
        # type from somewhere
        switch (parent.action):
            case UDF:
                name = args[1] # whatever the index is
                udf = gx.udfs[name]

                # udfs are always typed
                _type = copy.deepcopy(udf.args[var.get_index()].type)
                var.type = _type

                # add new type to scope
                # if a udf type has indirection 1, it just means
                # that the var.. this is an issue for codegen.
            case SET:
                set_untyped.append(var)
                if set_typed == 1:
                    # 0 typed 1 untyped
                    var.type = set_typed[0].type

                if len(set_untyped) == 2:
                    # both unknown, type assign not 
                    # possible at this stage
                    pass
    # scope, set_typed and untyped contain refs to same obj
    # hence the set modifications will apply to the scope tree itself.         
    infer.add_to_scope(current, var) 
                
        
                
                
                


            
                
"""
# if not get_type(): 
#   set_type()
def set_type_of_ident(gx, arg, arg_t_str):
    '''
    CREATE_MESSAGE(m_name, m_type_str):
    1. m_type = type_from_arg(m_type_str)
    2. m_v = python.Variable(m_name, <parent>, m_type)
    3. infer.add_to_scope(current, m_v)

    CALL(eventx, arg1, arg2):
    1. assert eventx in global events
    2.  for each arg: 
            # lookup scope, hopefully updated by some other action
            # before CALL
            arg_type = infer.get_type_of_ident(arg1) 
            if arg_type:
                arv_v = python.Variable(arg, <parent>, arg_type)
            else:
                print("type of arg not assigned before call, strange.)
                arg_v = python.Variable(arg, <parent>)
            # add to scope
            infer.add_to_scope(current, arg_v)

    3. if eventx in gx.events:
        # the python.Variable will have been created already, 
        # referenced by event
        # get python.function. event args refer to the python.Variable
        # in its scope. As long as a different event block can access a
        # previous python.function, it can access the variable in 
        # a different event scope.
        event = gx.events[eventx]
        for 
        
                


    '''

    
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
            final.subs[attr["__type__"]] = python.Type(attr["__type__"], thing=utils.TH_ENUM)

    #print(struct)
    return final

# call from CREATE MESSAGE, parse udfs
# need to decode it first.
# base_types will be a dict of type_t: {...etc...}
def type_from_type_str(gx, arg, usage_indirection=None):
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
    
    # likely enum
    return python.Type(arg, thing=utils.TH_ENUM)

    #error.error(f"{arg} is not a valid type for this system.")
    

        
    


