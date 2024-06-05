class Type:
    def __init__(self, ident, thing=None, indirection=None):
        self.ident = ident # typename
        self.subs = {} # attr:Type
        self.thing = thing  
        self.indirection = indirection # use during translate()

    def contains(self, attr):
        '''
        Returns True if a given nested asn type
        has a particular string as an attribute,
        at any nesting level, else False.
        '''
        if attr in self.subs:
            return True, self.subs[attr]
        
        for sub in self.subs:
            res, type = self.subs[sub].contains(attr)
            if res:
                return res, type
        return False, None
    
    def get_typeof(self, attr):
        '''
        If a type contains attr, return
        its type.
        '''
        _, type = self.contains(attr)
        return type

    def __str__(self):
        _str = f"{self.ident}\n"
        if not self.subs:
            return self.ident
        for s, st in self.subs.items():
            _str += f"\t{s}: {str(st)}"
        return _str
    
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
    "Json::Value"
]

TH_ENUM = "enum"

base_types = [
    {
        "__name__": "SynerPMessageHeader_t",
        "__attributes__": {
            "size": {
                "__id__": "size",
                "__type__": "uint8_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            },
            "cmd": {
                "__id__": "cmd",
                "__type__": "_e_SynerPCommand",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            }
        }
    },
    {
        "__name__": "Username_t",
        "__attributes__": {
            "sz": {
                "__id__": "sz",
                "__type__": "uint8_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            },
            "contents": {
                "__id__": "contents",
                "__type__": "char",
                "__thing__": "ARRAY",
                "__ptr__": 0
            }
        }
    },
    {
        "__name__": "DataBlock_t",
        "__attributes__": {
            "sz": {
                "__id__": "sz",
                "__type__": "uint8_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            },
            "contents": {
                "__id__": "contents",
                "__type__": "char",
                "__thing__": "ARRAY",
                "__ptr__": 0
            }
        }
    },
    {
        "__name__": "SynerPMessage_t",
        "__attributes__": {
            "header": {
                "__id__": "header",
                "__type__": "SynerPMessageHeader_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            },
            "uname": {
                "__id__": "uname",
                "__type__": "Username_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            },
            "data": {
                "__id__": "data",
                "__type__": "DataBlock_t",
                "__thing__": "SIMPLE",
                "__ptr__": 0
            }
        }
    }
]

TH_UNION = "union"
def consolidate_duplicate_types(all_types):
    '''
    1. duplicate types into list.
    2. All unions into a single list.
    '''
    consolidated = {}
    for struct in all_types:
        name = struct["__name__"]
        if name is None:
            # Handle cases where "__name__" is missing
            #print("union maybe")
            struct["__name__"] = TH_UNION 
        if name not in consolidated:
            consolidated[name] = struct
        else:
            # If name already exists, convert value to a list if not already
            if not isinstance(consolidated[name], list):
                consolidated[name] = [consolidated[name]]
            consolidated[name].append(struct)
    return consolidated

# for a single main struct
def reduce_to_type(struct, bases):
    # if struct["__name__"] in gx.type_cache:
    #     return gx.type_cache[struct["__name__"]]
    
    final = Type(struct["__name__"])     
    attributes = struct["__attributes__"]
    for attr in attributes.values():
        #print(attr)
        if attr["__type__"] in C_TYPES:
            # in a ident a.b.c.d, looking for type_of(c) should return name of Python.Type() only (excluding subs)
            # eg: if c in t.subs, return t.sibs[c].type_str
            # remember invariant: Each python.Type() must be stored in the scope. Hence incomplete types are not accessed
            # incividually. 
            final.subs[attr["__id__"]] = Type(attr["__type__"], attr["__thing__"], attr["__ptr__"])
        elif (attr["__type__"] in bases) or ("struct " + attr["__type__"]) in bases:
            try:
                nested_struct = bases[attr["__type__"]] # this can become a python.type(), should be 
            except:
                nested_struct = bases["struct " + attr["__type__"]] # this can become a python.type(), should be 
            
            nested_ = reduce_to_type(nested_struct, base_types) # returns a python.Type with filled in subs
            #gx.type_cache[nested_["__name__"]] = nested_
            final.subs[attr["__id__"]] = nested_
        else:
            # enum type
            print(f"{attr} likely enum")
            final.subs[attr["__type__"]] = Type(attr["__type__"], thing=TH_ENUM)
    
    return final

# call from CREATE MESSAGE 
# need to decode it first.
def type_from_json_arg(arg):
    #assert(isinstance(gx, config.GlobalInfo))
    bases = consolidate_duplicate_types(base_types)

    if "json" in arg or "Json" in arg:
        return Type(arg)

    # first check in user types
    for struct in bases.values():
        assert(isinstance(struct, dict))
        if struct["__name__"] == arg:
            final = reduce_to_type(struct, bases)# base structs will have indirection, thing empty. pain to modify struct parsing to differenciate b/w a BASE and a MEMBER
            return final
    
    print(f"{arg} is not a valid type for this system.")
    
    # something is wrong with my struct parser itself OR
    # (more likely user has given an incorrect type)
    #error.error(f"{arg} is not a valid type for this system.")

my_type = type_from_json_arg("SynerPMessageHeader_t")
print(my_type)
#tp = my_type.get_typeof("uname")
#print(tp)

