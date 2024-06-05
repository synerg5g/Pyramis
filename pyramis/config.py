import os
import sys
import pathlib
import re
from . import python
from . import utils
from . import infer

UDF_REGEX = r'(?P<return_type>\S+\s*) ([\w_]+)\(([^,]+(?:,\s*[^,]+)*)?\)' # chatgpt

def consolidate_duplicate_types(all_types):
    '''
    1. duplicate types into list.
    2. All unions into a single list.
    3. returns a dict indexed by typename. below is a rep. k-v pair in a base_types dict.
        "SynerPMessageHeader_t" :  {    "__name__": "SynerPMessageHeader_t"                                                                          
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
                                    }

    duplicate type names (with different attributes) are stored in a list at the same key.
    '''
    consolidated = {}
    for struct in all_types: # {__name__: "a"}
        name = struct["__name__"]
        if name is None:
            # Handle cases where "__name__" is missing
            #print("union maybe")
            struct["__name__"] = utils.TH_UNION 
        if name not in consolidated:
            consolidated[name] = struct
        else:
            # If name already exists, convert value to a list if not already
            if not isinstance(consolidated[name], list):
                consolidated[name] = [consolidated[name]]
            consolidated[name].append(struct)
    return consolidated

class GlobalInfo:
    """
    store information such as parsed asn base types,
    interface, udf file paths.
    """
    def __init__(self, magic, args):
        # env
        self._pyramis = magic
        self.nf_name = args.node # should be present in interfaces.json
        self.nf_dsl = None # dsl file in cwd.
        self.py_module_path = None
        self.py_module = None
        self.pyramis_message_types_path = self._pyramis / "_pyramis_message_types.json"
        self.user_message_types_path = self._pyramis / "_user_message_types.json"
        self.udfs_path = None
        self.udfs = {}
        self.pyramis_base_types = None
        self.user_base_types = None

        # codegen
        self.allfuncs = set()
        self.allvars = set()
        self.type_cache = {} # built types.
        self.scope_tree = None

        self.cwd = self.cwd = pathlib.Path.cwd() # directory that pyramis was called from
        self.raw_dir = self.cwd / "__TRANSLATE_RAW__" / self.nf_name
        self.build_dir = self.cwd/ "__BUILD__" / self.nf_name
        self.run_dir = self.cwd / "__RUN__" / self.nf_name
        self.output_dir = None
        self._utility_lib = None
        self.user_utils = None
        self.init_directories(args)
        self.generate_builtins() # update/create asn_base_types

        self.parse_interfaces()
        self.parse_udfs() # 


        self.modules = {} # cache of py modules handled just in case
    
    def init_directories(self, args):
        if args.subcmd == "translate":
            self.output_dir = self.raw_dir
        elif args.subcmd == "build":
            self.output_dir = self.build_dir
        elif args.subcmd == "run":
            self.output_dir = self.run_dir

        assert(isinstance(self.output_dir, pathlib.Path))
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self._utility_lib = self._pyramis / "utility_library"
        assert(self._utility_lib.is_dir())

        # user_utils: A folder in the cwd other than the 
        # gen folders that contains header file/files.
        # furthermore, atleast one of the contained
        # header-files must be used in udf.h
        # --- 
        # How to decide include files in linking, plat, that 
        # are in user_utils? 
        # A: Just include every header file in user_utils
        # :::temporary::: 
        self.user_utils = self.cwd / "utils"
    
    def parse_interfaces(self):
        # find interfaces.json
        _in = self.cwd / "interfaces.json"
        if not _in.is_file():
            print("Error: interfaces.json not defined.")
            sys.exit(1)

        self.interfaces_path = _in

        # store info so that SEND can easily verify validity
        # -- find nf_name in json, error if not
        # -- store my_interfaces, peer_nf, connection details


        # data = json.load(_in)

    def parse_udfs(self):
        '''
        Build python.UserDefined representation for udfs by 
        parsing the udf.h file.
        '''
        # find udf file
        _in = self.cwd / "udf.h"
        if not _in.is_file():
            print("Error: udf.h not defined.")
            sys.exit(1)

        self.udfs_path = _in

        with open(self.udfs_path, "r") as f_in:
            for _, line in enumerate(f_in, start=1):
                # skip comments
                if line.startswith("/") or line.isspace():
                    continue
                # * <*>(*)
                if re.match(UDF_REGEX, line): # XXX Ugly :)
                    line.strip(";")
                    _ret = line.split("(")[0].split()
                    _func = _ret[-1] # name of the func
                    _ret_type = " ".join(e for e in _ret[:-1])

                    _ptr = 0
                    if "*" in _ret_type or "*" in _func:
                        _ptr += (_ret_type.count("*") + _func.count("*"))
                        _ret_type = _ret_type.replace("*", "")
                        _func = _func.replace("*", "")


                    if "&" in _ret_type or "&" in _func:
                        _ret_type = _ret_type.replace("&", "")
                        _func = _func.replace("&", "")
                    
                    # found a specific instance of a generic type'
                    # generic types are the structs in json,
                    # they have fixed child THING and decay to the
                    # same location.
                    # specific instance is assigning a THING to a generic type.
                    ret_type = infer.type_from_arg(self, _ret_type, _ptr)
                    #ret_type = python.Type(_ret_type, indirection=_ptr)
                    
                    udf = python.UserDefined(_func, ret_type)

                    # store arg (types only).
                    # update udf.arg_types
                    _args =  line.split("(")[1].replace(")", "").split(",")  # ["int *x", "amf_t &y",...]
                    _clean = [_a.strip() for _a in _args]

                    for _arg in _clean:
                        _a = _arg.split()
                        _arg_type = " ".join(e for e in _a[:-1])
                        
                        _ptr = 0
                        if "*" in _arg_type or "*" in _a[-1]:
                            _ptr += (_arg_type.count("*") + _a[-1].count("*"))
                            _arg_type = _arg_type.replace("*", "")
                        
                        if "&" in _arg_type or "&" in _a[-1]:
                            _arg_type = _arg_type.replace("&", "")

                        _arg = infer.type_from_arg(self, _arg_type, _ptr)
                        udf.arg_types.append(_arg)
                    
                    # append to gx udf list
                    if udf.name in self.udfs:
                        udf.name = f"__{udf.name}"
                    self.udfs[udf.name]  = udf
        print(f"Parsed {len(self.udfs)} udfs.")
        print(self.udfs)


    def generate_builtins(self):
        # Initialise asn_base_types
        pyramis_parser = utils.Parser(self, self._utility_lib, self.pyramis_message_types_path)
        all_pyramis_types = pyramis_parser.parse_lib()
        self.pyramis_base_types = consolidate_duplicate_types(all_pyramis_types)
        print(len(self.pyramis_base_types))
        # for k, v in self.pyramis_base_types.items():
        #     if isinstance(v, list):
        #         print(k)
        #         print(v)
        
        # get user-defined types
        user_parser = utils.Parser(self, self.user_utils, self.user_message_types_path)
        all_user_types = user_parser.parse_lib()
        self.user_base_types = consolidate_duplicate_types(all_user_types)

        print(f"System has {len(self.pyramis_base_types) + len(self.user_base_types)} valid types.")