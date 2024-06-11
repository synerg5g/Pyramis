# FILE: utils.py
# --------------
# Base class that acts implements a
# header file parser API.
# Also contains pre-processing logic.
from . import error
from . import infer
import sys
import os
import glob
from . import python
import re
import pathlib
import copy
from collections import defaultdict
import json

not_found_header_cache = {} 

HEADER_GUARD = "xxx_HEADER_GUARD___"

TH_STRUCT = "struct"
TH_ENUM = "enum"
TH_UNION = "union"
TH_TYPEDEF = "typedef"

TH_ARRAY = "ARRAY"
TH_SIMPLE = "SIMPLE"

def do_struct(mini):
    '''
    Handles simple structs, typdef structs, unions, nested
    struct defintitions, nested unions.
    - Any struct definition encountered, whether simple or
    nested, will have a corresponding object.
    - if typedef <> <string>, need to eventually find the corresp.
    struct object.
    - In do_struct(), create a Struct (old_type, new_type) and store
    it in the struct header.
    - In reduce_to_type, search will find the typedefd Struct object
    with tag_name as a defined struct. Do reduce_to_type(tag_name)
    - typedef can also be used for type renaming accross multiple files.
    '''
    #print(mini_s)
    #print('\n')
    #lines = mini_s.split('\n')
    stack = []
    structs = []

    for line in mini:
        m_struct = re.match(R_STRUCT_OR_TYPEDEF_STRUCT, line)
        m_union = re.match(R_TYPEDEF_UNION, line)
        m_nested_enum = re.match(R_NESTED_ENUM, line)
        m_typedef_enum = re.match(R_TYPEDEF_ENUM, line)
        m_typedef = re.match(R_TYPEDEF, line)
        m_asn_sequence = re.match(R_ASN_SEQUENCE, line)
        if "=" in line or "return" in line:
            continue
        if (m_struct):
            name = line.replace("typedef struct", "").replace("{", "").strip()
            struct = Struct(TH_STRUCT, name)
            stack.append(struct)
        elif m_union:
            struct = Struct(TH_UNION)
            stack.append(struct)
        elif (m_nested_enum or m_typedef_enum):
            line = line.replace(";", "").strip()
            struct = Struct(TH_ENUM)
            stack.append(struct)
        elif (m_typedef):
            old = m_typedef.group(1)
            new = m_typedef.group(3)
            #print(new)            
            struct = Struct(TH_TYPEDEF, new)
            struct.tag_name = old
            #print(struct)
            return [struct] 
        elif "}" in line:
            line = line.replace(";", "").strip()
            try:
                curr = stack.pop()
            except IndexError as e:
                continue
            if stack: # nested
                attr_type_in_parent = curr.tag_name
                if (curr.thing == TH_UNION):
                    # INVARIANT: If a union is present in a struct,
                    # the struct is treated as if it contains each of the 
                    # attributes in the union. (strictly for typechecking,
                    # does not enforce union semantics)
                    attrs_of_parent = curr.attributes
                    for _attr in attrs_of_parent.values():
                        #print(f"...Adding to parent struct, {stack[-1].thing}")
                        #print(_attr)
                        stack[-1].attributes[_attr.id] = _attr
                else:
                    attrs_of_parent = line.replace("}", "").strip().split(",")
                    for attr_id in attrs_of_parent:
                        attr = Attribute(attr_id, attr_type_in_parent)
                        stack[-1].attributes[attr.id] = attr
                if curr:
                    curr.name = curr.tag_name
                    structs.append(curr)
            else: # simple struct
                maybe_name_d = line.split("}")
                maybe_name = [l.strip() for l in maybe_name_d]
                if all([el == '' for el in maybe_name]):
                    assert(curr.tag_name)
                    curr.name = curr.tag_name
                else:
                    curr.name = maybe_name[-1] # new name
                if curr:
                    structs.append(curr)
                return structs
        else: # attr line
            line = line.replace(";", "").strip()
            if stack:
                # create attribute from line
                if (stack[-1].thing == TH_ENUM):
                    attr_id = line.strip(",")
                    attr_type = "int" # default to int
                else:
                    #print(f"...Inside parent, adding attrs to {stack[-1].thing}")
                    
                    if m_asn_sequence:
                        attr_type = m_asn_sequence.group(1) 
                        attr_id = line.split()[-1] + "@@"
                    else:
                        attr_type = ' '.join(line.split()[:-1])
                        attr_id = line.split()[-1]
                    #print(attr_type)
                attr = Attribute(attr_id, attr_type)

                # add attribute to curr struct
                # non-structs will exit with None
                stack[-1].attributes[attr.id] = attr

class Parser:
    '''
    Coordinates the multifile parse.
    asn headers contain typedefs as structs and unions.
    '''
    def __init__(self, gx, utility_lib, outfile):
        self.gx = gx
        self.utility_lib = utility_lib # pyramis utility_lib directory
        self.parsed_parsers = {} # filepath: FileParser
        self.type_cache = {}
        self.reduce_header_cache = defaultdict(list) # attr_type: [list of header filenames] where type not found.
        self._stripped_utility_lib = gx._pyramis / ".deps/stripped"
        self.outfile = outfile

    def parse_lib(self): # create a dict?
        '''
        Create an intermediate dict
        to represent the asn builtin types.
        '''
        for path, _, files in os.walk(self.utility_lib):
            for file in files:
                file_path = os.path.join(path, file)
                if file_path.endswith(".h"):
                    #print(file_path)
                    file_parser = FileParser(self.gx, self._stripped_utility_lib, pathlib.Path(file_path).resolve())
                    file_parser.remove_comments()
                    #print(f"---------------\n{str(file_parser.current_file)}\n--------------------")
                    file_parser.parse_header()
                    self.parsed_parsers[str(file_parser.current_file)] = file_parser # each file will have a key

        # link the included parsers
        # every header-parser now has access to
        # the parsers of its included headers.
        for parser in self.parsed_parsers.values():
            assert(isinstance(parser, FileParser))
            parser.append_includes(self) # append appropriate parsers to the fileparsers include list.
        
        return self.struct_types_to_json()

        # return self.adjust_types()

    def struct_types_to_json(self):
        '''
        Finer parse of struct attribute types, create the _message_types.json file.
        That contains level 1 json objects corresp to each defined type.
        '''
        all_structs = []
        f_message_types = open(self.outfile, mode="w+")
        for parser in self.parsed_parsers.values():
            assert(isinstance(parser, FileParser))
            #parser.struct_to_json(f_message_types)
            #assert(0)
            for struct in parser.structs.values():
                if struct.name not in all_structs:
                    # new struct
                    all_structs.append(struct.to_json())
                else:
                    print(f"Duplicate: {struct}")
        
        with open(self.outfile, mode="w+") as f_message_types_w:
            json.dump(all_structs, f_message_types_w, indent=4)
        
        with open(self.outfile, mode="r") as f_message_types_r:
            # for struct in f_message_types_r:
            #     print(struct)
            data = json.load(f_message_types_r)

        f_message_types.close()
        
        return data

    def adjust_types(self):
        '''
        After a single-level parse of all files, 
        for each struct in a parsed file, reduce_to_type() for each 
        struct in each header file.
        '''
        base_types = {}
        for parser in self.parsed_parsers.values():
            #print(parser.current_file)
            #print(len(parser.structs))
            print(f"xxx--- Building types from {parser.current_file.stem}.h ---xxx")
            for struct in parser.structs.values():
                assert(isinstance(parser, FileParser))
                final = parser.reduce_to_type(struct, self)
                assert(isinstance(final, python.Type))
                print(f"=== *** {final.ident} struct-to-type complete *** ===")
                print(final)
                base_types[final.ident] = final
        return base_types
    
def data_type(s):
    # Attempt to convert to int
    try:
        return int(s)
    except ValueError:
        pass

    try:
        return float(s)
    except ValueError:
        pass

TOKEN_DEFINE = "#define"
TOKEN_STRUCT = "struct"
TOKEN_TYPEDEF_STRUCT = "typedef struct"
TOKEN_RPAR = "}"
TOKEN_INCLUDE = "#include"


R_SINGLE_MULTI_LINE_COMMENT = r'//.*?$|/\*.*?\*/'
R_TYPEDEF_ENUM = r'typedef\s+enum\s+.*\s+{'
R_NESTED_ENUM = r'enum\s*(?:\r?\n\s*)?\{'
R_STRUCT_OR_TYPEDEF_STRUCT = r'(?:typedef\s+)?struct\s+(\w*)\s*\{'
R_TYPEDEF_UNION = r'(?:typedef\s+)?union\s+\S+\s*{?'
R_STRUCT_COMPOUND_ATTRIBUTE = r'struct\s+\S+\s+\S+;' # struct str1 str2;
R_STRUCT_SIMPLE_ATTRIBUTE = r'(?!(?:enum\s+))\S+\s*\S+\s*;'
R_STRUCT_END = r'(\})?\s*([^;]+;)'
R_STRUCT_ARRAY_SIZE = r'\[?[^\[\]]*\]'
R_ASN_SEQUENCE = r'A_SEQUENCE_OF\((.*)\)\s*.*;'

# typedef <arbitrary number of whitespace-sep. strings> string0
# g1: old_type g3: new_type.
R_TYPEDEF = r'typedef\s+((\S+\s+)+)(\S+);'
    
class FileParser:
    '''
    Implements primitive parsing logic for a single file.
    '''
    def __init__(self, gx, path_to_stripped, current_header):
        self.gx = gx # to update asn_base_types
        self._stripped_utility_lib = path_to_stripped
        self.current_file = pathlib.Path(current_header) # full path of header being parsed.

        self.constants = {} # name: value
        self.structs = {}
        self.includes = [] # contains the definitions of nested structs used by structs in this file.
        self.type_cache = {}

        # prep for comment removal.
        stripped = self.current_file.stem + "_stripped___"
        self._stripped_utility_lib.mkdir(parents=True, exist_ok=True)
        self.stripped_file = self._stripped_utility_lib / f"{stripped}.h"

    def parse_header(self):
        '''
        Parse the current file into structs,
        get struct attribute types at the local-file
        level only.
        '''
        f_hdr = open(self.current_file, "r") # actual header

        # store #define values
        self.parse_constants()

        # create struct objects for this header
        self.isolate_structs()

        f_hdr.close()
    
    def remove_comments(self):
        '''
        Remove simple single-line comments.
        '''
        f_hdr = open(self.current_file, "r") # actual header

        code = f_hdr.read()
        stripped = re.sub(R_SINGLE_MULTI_LINE_COMMENT, '', code, flags=re.DOTALL | re.MULTILINE)

        f_hdr_w = open(self.stripped_file, "w+")

        f_hdr_w.write(stripped)

        f_hdr.close()

    def parse_constants(self):
        f_hdr = open(self.stripped_file, "r")
        code = f_hdr.readlines()
        for line in code:
            if line.startswith(TOKEN_DEFINE):
                stuff = line.strip().split()
                name = stuff[1]
                try:
                    val = stuff[2]
                except IndexError as e:
                    val = HEADER_GUARD
                self.constants[name] = data_type(val)
        #print(f"#define : {self.constants}")
        f_hdr.close()

    def isolate_structs(self):
        '''
        Create struct classes for this header.
        IMP: struct.attributes needs to be type: name
        Store struct instances in self.structs.
        mostly correct for asn types.
        IMP: enum values not recorded.
        '''
        # print("-----------------------")
        # print(f"parsing {self.stripped_file}")
        # print("-----------------------")

        f_hdr = open(self.stripped_file, "r")
        code = f_hdr.readlines()
        
        mini = [] # sub_struct
        brackets = 0
        spurious = False

        for line in code:
            line = line.strip()
            if line.startswith('extern "C"'):
                continue
            if not line:
                continue
            
            brackets += line.count("{")
            brackets -= line.count("}")

            # only check for a match in the beginning of the string.
            m_simple_attr = re.match(R_STRUCT_SIMPLE_ATTRIBUTE, line)
            m_compound_attr = re.match(R_STRUCT_COMPOUND_ATTRIBUTE, line)
            m_struct_end = re.match(R_STRUCT_END, line)
            m_nested = re.match(R_STRUCT_OR_TYPEDEF_STRUCT, line)
            m_union = re.match(R_TYPEDEF_UNION, line)
            m_typedef = re.match(R_TYPEDEF, line)
            m_asn_sequence = re.match(R_ASN_SEQUENCE, line)

            if (
                m_simple_attr or 
                m_compound_attr or 
                m_asn_sequence or
                m_nested or 
                m_union or 
                m_struct_end or
                m_typedef
                ):
                spurious = False
                if ")" in line and not m_asn_sequence:
                    continue
                if ((m_simple_attr or m_compound_attr or m_asn_sequence) and brackets == 0 and not m_struct_end):
                    continue
                # if (m_typedef and (brackets == 0)):
                #     # associate a python.Type right here?
                #     print(line)
                #     print(mini)
                #     mini.append(line)
                #     structs = do_struct(mini)
                if (brackets > 0):
                    #print(line)
                    mini.append(line)
                    # the centre portion (if defined already) must now
                    # have a new name
                    # typedef struct cunt CuntDawg -> struct cunt -> CuntDawg.
                    structs = do_struct(mini)
                elif (brackets == 0): # new struct
                    if m_typedef:
                        mini = []
                    mini.append(line)
                    structs = do_struct(mini)
                    try:
                        for _s in structs:
                            #print(_s)
                            if _s.name in self.structs and self.structs[_s.name].thing != TH_TYPEDEF:
                                continue
                            else:
                                self.structs[_s.name] = _s
                    except TypeError as t:
                        continue
                    # reset
                    mini = []
                    brackets = 0
                    spurious = False
            else:
                spurious = True
            
            if spurious:
                continue

        f_hdr.close()
    
    def append_includes(self, controller):
        '''
        Append appropriate parser objects to the  self.includes.
        '''
        #print(self.current_file.name)
        f_hdr = open(self.current_file)
        for line in f_hdr:
            if line.startswith(TOKEN_INCLUDE):
                i_h_i = line.find(TOKEN_INCLUDE) + len(TOKEN_INCLUDE)
                i_h_f = pathlib.Path(line[i_h_i:].strip().replace('"', '')).name
                # o(n) :/
                for key, parser in controller.parsed_parsers.items():
                    if i_h_f == key.split("/")[-1]:
                        #print(parser.current_file)
                        self.includes.append(parser)
        #print(len(self.includes))

    def reduce_to_type(self, struct, controller):
        '''
        return a python.Type tree corresponding to the 
        struct input.
        '''
        assert(isinstance(controller, Parser))

        struct_name = struct.name
        print(f"Reducing to python.Type: \n{struct}")
        if struct_name in controller.type_cache:
            print(f"=== Found {struct_name} in type-cache ===")
            return controller.type_cache[struct_name]
        else:
            final = python.Type(struct_name) # empty subs, # nested struct type name
            for attr in struct.attributes.values(): # each entry in the struct
                # single struct, all primitive attributes
                #print(f"Search for {type(attr.type_str)}")
                if attr.type_str in infer.C_TYPES:
                    print(f"=== {attr.type_str}: {attr.id} is a primitive type ===")
                    final.subs[attr.id] = python.Type(attr.type_str)
                    continue
                # single struct, attr type is a struct in the 
                # same file
                elif (attr.type_str in self.structs) or ("struct " + attr.type_str) in self.structs:
                    print(f"=== Found {attr.type_str} in current file {self.current_file.stem}.h")
                    try:
                        nested_struct = self.structs[attr.type_str] # this can become a python.type(), should be 
                    except:
                        nested_struct = self.structs["struct " + attr.type_str] # this can become a python.type(), should be 
                    nested_ = self.reduce_to_type(nested_struct, controller) # returns a python.Type with filled in subs
                    controller.type_cache[nested_.ident] = nested_
                    final.subs[attr.id] = nested_
                
                # single struct, attr_type is not defined in current file
                # check included files
                elif attr.type_str not in self.structs:
                    print(f"=== {attr.type_str} was not in {self.current_file.stem}.h ===")
                    i_nested = self.find_attr_in_includes(attr.type_str, controller) # check includes
                    # if not i_nested:
                    #     for included in self.includes:
                    #         i_nested = included.find_in_includes(attr.type_str, controller) # check includes of includes
                    if not i_nested:
                        # eg. vector<> , etc.
                        print(f"Likely a collection: {attr.type_str}")
                        i_nested = python.Type(attr.type_str)
                    #     controller.type_cache[attr.type_str] = 
                    #     final.subs[attr.id] = attr
                    # else:
                    controller.reduce_header_cache.clear()
                    controller.type_cache[i_nested.ident] = i_nested
                    final.subs[attr.id] = i_nested
                
            controller.type_cache[final.ident] = final
        
        return final

    def find_attr_in_includes(self, attr_type, controller):
        nested_ = None
        print(f"Included files of {self.current_file.stem}.h are:")
        print([f"{i.current_file.stem}.h" for i in self.includes])

        if (not self.includes) and (attr_type not in self.structs):
            print(f"!!-- Not found (exhaustive): {attr_type} --!!")
            return nested_
                
        # check if type is present in the includes of the current header
        for included in self.includes:
            assert(isinstance(included, FileParser))
            print(f"Searching in {included.current_file.stem}.h")
            try:
                if str(self.current_file) in controller.reduce_header_cache[attr_type]:
                    continue
            except KeyError as k:
                pass
            # for s in included.structs:
            #     print(s)
            # print(included.structs.keys())
            if attr_type in included.structs:
                print(f"=== Found {attr_type} in {included.current_file.stem}.h ===")
                struct_ = included.structs[attr_type]
                assert(isinstance(struct_, Struct))
                nested_ = included.reduce_to_type(struct_, controller)
                return nested_
            else:
                print(f"{attr_type} not found in {included.current_file.stem}.h")
                # add header name to not_found_cache
                print("x---Adding to not_found_header_cache---x")
                controller.reduce_header_cache[attr_type] = str(included.current_file)
                # or check includes of the current parser?
                print("--- Checking recursively ---")
                print(f"Now Searching in included files of {included.current_file.stem}.h")
                found = included.find_attr_in_includes(attr_type, controller)
                if found:
                    return found
                else:
                    continue
                #continue

        # print(f"{attr_type} not found in includes of {self.current_file.stem}.h")
        # if not nested_:
            # search included files of the current file
        # print(f"{attr_type} not found in {included.current_file.stem}.h")
        # print("--- Checking recursively ---")
        # for included in self.includes:
        #     print(f"Now Searching in included files of {included.current_file.stem}.h")
        #     included.find_in_includes(attr_type, controller)

class Attribute:
    def __init__(self, id, type_str):
        self.thing = TH_SIMPLE # array, struct 
        self.id = id # attr id
        self.type_str = type_str # attr_type_str
        self.ptr_indirection = 0 # count of indirection
    
    def __str__(self):
        return f"[{self.type_str}] [{self.id}]\n"

    def to_json(self):
        self.ptr_indirection = self.id.count("*") + self.type_str.count("*")
        if ("[") in self.id:
            self.thing = TH_ARRAY
        if ("@@") in self.id:
            self.id = self.id.replace("@", "")
            self.thing = TH_ARRAY

        self.id = self.id.strip("*")
        self.id = self.id.split(":")[0] if ":" in self.id else self.id.split("[")[0]
        return {"__id__": self.id, "__type__": self.type_str, "__thing__": self.thing, "__ptr__": self.ptr_indirection,}


class Struct:
    def __init__(self, thing, name=None):
        '''
        Represents a parsed struct according to C
        standard.
        '''
        self.thing = thing
        self.name = name # typedef struct <tag_name> {} <alias_name>
        self.tag_name = name
        self.attributes = {} # attr_type_str: attr

        self.vars = {} # for map struct only.

    def __str__(self):
        struct_str = f'{self.name} [{self.thing}]\n'
        if self.thing == TH_TYPEDEF:
            struct_str += f"i.e. {self.tag_name}\n"
        for attr in self.attributes.values():
            struct_str += f'.type_str <{attr.type_str}>\n.id <{attr.id}>\n\n'
        return struct_str

    def to_json(self):
        encoded_attributes = {}
        for attr in self.attributes.values():
            encoded_attributes[attr.id] = attr.to_json()
        return {"__name__": self.name, "__attributes__": encoded_attributes}

PYRAMIS_ACTIONS = [
    #"ASSERT",
    "SET",    # Indicate set message IEs 
    "UDF",    # indicate call to a UDF
    "DECODE", # ""
    "ENCODE", # ""
    "CALL",   # Indicate call to a local function
    "SEND",   # Indicate send a message via a defined interface
    "CREATE_MESSAGE", # Indicate creation of message of asn type.
    "GET_KEY", # Indicate get a value at a key in a map
    "SET_KEY", # Indicate set a value at a key in a map
    "STORE",   # Indicate storing a value in a context
    "LOOKUP",  # Indicate lookup a value in a context
    "LOOP",    # Indicate beginning of a loop construct
    "IF",      # test a condition
    "ELSE",    # branch on condition failure
    #"EXCEPTION",   # XXX not in linking SMF
    "READ_CONFIG", # Indicate parse a json config file.
    #"CREATE_COLLECTION", # XXX not in linking SMF
    #"ADD",         # XXX not in linking SMF
    #"PRINT",       # XXX redundant SMF
    "APPEND",      # add a value/object to a list end.
    "PASS" ,       # XXX dubious
    "BREAK",       # XXX dubious
    "CONTINUE" ,    # XXX dubious
    "TIMER_STOP",
    "TIMER_START"
]

class Preprocessor:
    '''
    buggy for dsl comments
    '''
    def __init__(self, _in, _out):
        self._in = _in
        self._out = _out

    def process(self):
        f_out = open(self._out, "w+")
        with open(self._in, "r") as f_in:
            for lineno, line in enumerate(f_in, start=1):
                if line.isspace():
                    continue
                else:
                    res = self.process_line(line, lineno, tabs=len(line) - len(line.lstrip()))
                f_out.write(f"{res}\n")

        f_out.close()

    def parse_condition(self, condition):
        """
        Function to parse a binary condition expression. Seperates the operator from the operands and adds brackets.

        Parameters
        ----------
        condition : str
                The condition as a single string.

        Output
        ------
        A string of type ('a' op 'b')
        """
        parts = condition.split(" ", 2)
        if len(parts) == 1:
            transformed_string = f"('{parts[0]}')"
        else:
            lhs, operator, rhs = parts
            transformed_string = f"('{lhs}' {operator} '{rhs.strip()}')"

        return transformed_string

    def process_line(self, line, lineno, tabs):
        """
        The main preprocessor function. Generates Python-Syntax string for each DSL line that is read.

        Parameters
        -----------
        line : str
                The current line being read from the Pyramis file.
        tabs : int
                The length of whitespace before the current line. For indentation.

        Output
        ------
        A formatted string that conforms with Python syntax.
        """
        line = line.strip()

        if line[0] == "#":
            return f"{tabs * ' '}{line}"
        
        # if line.startswith("@@timer"):
        #     # third arg is a timer event.

        action_list = line.strip().split(
            "(", 1
        )  # ['EVENT eventname', 'arg1, arg2)'] ['IF', 'arg1 = MACRO(....))'
        action = action_list[0].strip()#
        event_check = action_list[0].strip().split(" ")

        if len(action_list) > 1:
            args = action_list[1].strip()[
                :-1
            ]  # 'arg1, arg2' 'procedureCode == MACRO(ProcedureCode_id_InitialContextSetup)'
            # logger.debug("args: %s", args)
            if "#" in args:
                args = args.split("#")[0]
                # logger.debug("inter args: %s", args)
                if ")" in args:
                    args = args.replace(")", "") # erases both bracks in case of MACRO
            # logger.debug("New args: %s", args)
        else:
            # pass, break, continue etc.
            pass

        if event_check[0] == "EVENT":
            event_name = event_check[1]
            # print(event_name)
            # print(args)
            if args[-1] == ")":
                args = args[:-1]
            return f"{tabs * ' '}def {event_name} ({args}):"


        if action == "LOOP":
            args_list_comma = args.split(",")
            return f"{tabs * ' '}for {args_list_comma[0]} in range(\"{args_list_comma[1].strip()}\", \"{args_list_comma[2].strip()}\"):"

        elif action == "IF":
            if "LIKELY" in args or "UNLIKELY" in args:
                branch_args = args.split("(", 1)
                branch_flag = branch_args[0]
                branch_condition = branch_args[1]
                transformed_string = f"{tabs * ' '}if ('{branch_flag}' and {self.parse_condition(branch_condition[:-1])}):"
            else:
                if args.count(")") > args.count("("):
                    args = args[:-1]
                print(args)
                transformed_string = f"{tabs * ' '}if{self.parse_condition(args)}:"

            return transformed_string

        elif action in ("IF_PRESENT", "IF_NOT_PRESENT"):
            return f"{tabs * ' '}def {action}({args}):"

        elif (action == "ELSE:" or action == "ELSE"):
            return f"{tabs * ' '}else:"
        
        elif action in ("PASS", "CONTINUE", "BREAK"):
            return f"{tabs * ' '}{action.lower()}"
        elif action in PYRAMIS_ACTIONS:
            #print(action)
            args_list_comma = args.split(",")
            if action == "CREATE_COLLECTION":
                comma_formatted_args = ",".join(f"{arg.strip()}" for arg in args_list_comma)
            else:
                comma_formatted_args = ",".join(
                    f"'{arg.strip()}'" for arg in args_list_comma
                )  #'"arg1"', '"arg2"'
            return f"{tabs * ' '}{action} ({comma_formatted_args})"

        else:
            # raise pyex.PyramisKeywordError()
            error.error("`%s` is not a valid Pyramis action, abort.\n" %action, 
                        filename=self._in, lineno=lineno)
            
