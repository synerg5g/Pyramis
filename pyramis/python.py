# FILE: python.py
# ---------------
# Implement classes to represent Python/Pyramis constructs.
# such as Module, Function, Variable.
import ast
import collections
import importlib.util
import os
import re
import sys
import pathlib
from . import error
from . import utils
import collections

# def find_module(gx, name, basepath):
#     # return full filepath
#     module_name = name
#     module_path = basepath / ".deps"
#     file_path = module_path / f"{module_name}.py"

#     filename = None
#     if file_path.is_file():
#         filename = file_path   

#     if filename is None:
#         raise ModuleNotFoundError("No module named '%s'" % module_name)

#     return filename # Path

def parse_file(name):
    filebuf = importlib.util.decode_source(open(name, 'rb').read())
    
    try:
        return ast.parse(filebuf)
    except SyntaxError as s:
        print("*ERROR* %s:%d: %s" % (name, s.lineno, s.msg))
        sys.exit(1)

def get_arg_name(node, is_tuple_expansion=False):
    if hasattr(node, "arg"):
        assert isinstance(node.arg, str), "non-arg string %s" % type(node.arg)
        return node.arg

    if isinstance(node, ast.Name):
        assert (
            is_tuple_expansion
            and type(node.ctx) == ast.Store
            or type(node.ctx) == ast.Param
        )
        return node.id
    elif isinstance(node, str):
        return node
    else:
        assert False, "Unexpected argument type got %s" % type(node)

def extract_argnames(arg_struct):
    # returns list of arg strings from
    # a functiondef node, stores it in Function.formals
    argnames = [get_arg_name(arg) for arg in arg_struct.args]

    return argnames



class PyObject:
    """Mixin for py objects"""

    def __repr__(self):
        return f"{self.__class__.__name__} {self.ident}"
    
class Module(PyObject):
    """python module class

    name: str               module name
    name_list: [str]        list of names
    ident: str              module name

    filename: Path          module path
    path: Path              module parentdir
    relative_filename: Path module relative_filenmae
    relative_path: Path     relative_filename parentdir

    ast: ast.Module         ast module or None
    node: ast.node          ast Node
    """
    def __init__(self, gx, filename, node):
        self.gx = gx
        self.filename = pathlib.Path(filename) # full path of the module i.e node.py
        self.name = self.filename.name
        self.path = self.filename.parent

        self.ast = None  # to be provided later after analysis
        self.node = node 

        self.events = collections.OrderedDict() # store events by line-no.

        self.generated = [] # store converted text from events.

    def generate_linking_h(self):
        '''
        Contains:
        - linking.cpp event declarations
        - default timer event declarations, in case timers are used
        - include udf.h, platform.h
        - externed map declarations and map mutex locks.
        - header guards
        Store lines in self.generated.
        Create the new <NF>_linking.h file in gx.output_dir
        '''
        _guard = "#ifndef __" + self.gx.nf_name + "_LINKING_H__\n"
        _guard += "#define __" + self.gx.nf_name + "_LINKING_H__\n"
        self.generated.append(_guard)

        _inc = ["\"../../udf.h\"", f"\"{self.gx.nf_name}_platform.h\""]
        _includes = ""
        for __inc in _inc:
            _includes += "#include " + __inc + "\n"
        _includes += "\n"
        self.generated.append(_includes)

        # args: given + defaults
        _event_decl = ""
        for event in self.events.values():
            _name = event.name
            _event_decl = "void " + _name + "("

            if any(action.name == "DECODE" for action in event.actions):
                _defaults = "int length, int sockfd, struct nfvInstanceData *nfvInst"
            else:
                _defaults = "int sockfd, struct nfvInstanceData *nfvInst"

            _user = ""
            for v in event.vars:
                _user += v.type_to_str() + " " + v.name + ", "
        
            _event_decl += (_user + _defaults) + ")"
            event.decl += _event_decl # assign to event.

            self.generated.append(_event_decl + ";\n")
        
        self.generated.append("\n")

        _map_decl = "extern std::map<int, int> fd_to_key_map;\n"
        _map_decl += "extern std::map<int, int> key_to_fd_map;\n\n"
        self.generated.append(_map_decl)

        _map_lock_decl = "extern pthread_mutex_t fd_to_key_map_lock;\n"
        _map_lock_decl += "extern pthread_mutex_t key_to_fd_map_lock;\n"

        _user_locks = ""
        for map in self.gx.maps.values():
            _user_locks += "extern pthread_mutex_t " + map.name + "_lock;\n"
        _map_lock_decl += _user_locks

        self.generated.append(_map_lock_decl)

        self.generated.append("\n#endif")

        file = self.gx.output_dir / f"{self.gx.nf_name}_linking.h"
        self.write_to_file(file)

    def generate_linking_cpp(self):
        '''
        Contains:
        - include linking_h
        - unrolled python.event()s
        Store lines in self.generated.
        Create the new <NF>_linking.cpp file in gx.output_dir
        '''
        for event in self.events.values():
            event.emit()
            self.generated.extend(event.generated) # contains all event text.
            self.generated += "\n\n"


        file = self.gx.output_dir / f"{self.gx.nf_name}_linking.cpp"
        self.write_to_file(file)
        
    def generate_contexts(self):
        '''
        Contains:
        - User level map definitions and map struct definitions.
        i.e. pyramis context.
        - default system includes
        - header guards
        '''
        # preamble
        _desc = """/**
* FILE: contexts.h
* -----------------
* Generated after an analysis of the processing .dsl file.
* Contains declarations and definitions of collections
* referenced in the code.
*/\n"""
        self.generated.append(_desc)

        _guard = "#ifndef __" + self.gx.nf_name + "_CONTEXTS_H__\n"
        _guard += "#define __" + self.gx.nf_name + "_CONTEXTS_H__\n"
        self.generated.append(_guard)

        _inc = ["<vector>", "<map>", "<string>"]
        _includes = ""
        for __inc in _inc:
            _includes += "#include " + __inc + "\n"
        _includes += "\n"
        self.generated.append(_includes)

        # do stuff, fill self.generated.
        print(len(self.gx.maps))
        for map in self.gx.maps.values():
            _map = ""
            _attrs = ""
            for v in map.struct.vars.values():
                _attrs += ("\t" + v.type_to_str() + " " + v.name + ";\n")

            # get map struct definition
            _map += "typedef struct " + map.struct.name + " {\n"
            _map += _attrs

            _map += "} " + map.struct.name + "_t;\n\n"

            assert(map.key_type)

            # declare map with key type and map struct
            _map += "std::map<" + map.key_type.to_str() + ", " + map.struct.name + "_t> " + map.name + " {};\n\n"
            self.generated.append(_map)
        
        self.generated.append("#endif")
            
        file = self.gx.output_dir / f"{self.gx.nf_name}_contexts.h"
        self.write_to_file(file)

    def write_to_file(self, filepath):
        '''Called by the generate_* methods at end.'''
        # do stuff
        with open(filepath, mode="w") as f_w:
            for thing in self.generated:
                f_w.write(thing)

        # reset module.generated
        self.generated = []

class Event:
    def __init__(self, gx, node=None, parent=None):
        self.gx = gx
        self.ast_node = node # own ast node
        if node:
            name = node.name
            self.name = name
            self.formals = extract_argnames(node.args) # list of arg strs.
        self.vars = []
        self.actions = [] # 

        self.generated = [] # emit appends string lines.
        self.decl = "" # declaration/ header
        self.indent = 0


    def emit(self):
        # get function header
        _event_decl = self.decl
        self.generated.append(_event_decl + " {\n")

        # update self.generated.
        for action in self.actions:
            print(f"Indent: {action.indent}")
            try:
                self.generated.append(action.indent * "\t")
            except:
                pass
            action.emit()
            self.generated.append(action.generated + "\n")
        
        self.generated.append("}")

class Action:
    pyramis_actions = utils.PYRAMIS_ACTIONS

    def __init__(self, gx, name, parent=None, indent=None, mv=None):
        self.gx = gx
        self.name = name
        self.parent = parent
        self.mv = mv
        self.vars = [] # references to python.Var(), stored in the enclosing scope.

        self.indent = indent # update via modulevisitor.
        self.generated = ""

    def emit(self):
        '''
        C++ code generation, unique per action.
        '''
        emitters = {
            action.lower(): getattr(self, f"emit_{action.lower()}") for action in Action.pyramis_actions
        }
        print(self.name.lower())
        if self.name.lower() in emitters:
            emitters[self.name.lower()]()
        else:
            error.error(f"Action {self.name} not supported yet.")

    def emit_create_message(self):
        _type = self.vars[0].type
        _id = self.vars[0].name

        if not self.vars[0].type.sz:
            self.generated += _type.to_str() + " " + _id + " {};"
        else:
            _sz = self.vars[0].type.sz
            self.generated += _type.to_str() + " " + _id + "[" + _sz + "];"
        
    def emit_decode(self):
        # arg[1] is the deserialised ident.
        _body_id = self.vars[1].name
        _type = self.vars[1].type
        self.generated += _type.to_str() + " " + _body_id + " {};\n"

        _fn = self.vars[0] # str
        self.generated += (self.indent *"\t" + _fn + "(")

        _args = ""
        for _arg in self.vars[1:]:
            _id = _arg.name
            _args += _id + ", "
        _args += "length"

        self.generated += _args + ");\n"                

    def emit_encode(self):
        # decl size and buffer.
        # size_t simple_enc_sz {};
        # std::vector<char> simple_enc(MAX_MESSAGE_SIZE, 0);
        # SynerPMessageEncode(simple, simple_enc, simple_enc_sz); // null added.
        print([var.name for var in self.vars[1:]])
        _sz = self.vars[-1]
        self.generated += _sz.type.to_str() + " " + _sz.name + " {};\n"

        _buf = self.vars[1]
        self.generated += self.indent* "\t" + _buf.type_to_str() + " " + _buf.name + "(MAX_MESSAGE_SIZE, 0);\n"

        _fn = self.vars[0] # str
        self.generated += (self.indent *"\t" + _fn + "(")

        _args = ""
        for _arg in self.vars[1:]:
            _id = _arg.name
            _args += _id + ", "
        _args = _args[:-2]

        self.generated += _args + ");\n"
        

    def emit_udf(self):
        pass

    def emit_set(self):
        '''
        undecl, decl set according to path taken by
        infer.get_variable()
        '''
        _lhs = self.vars[0]
        _rhs = self.vars[1]

        if "MACRO" in _rhs.name:
            _rhs.name = _rhs.name.split("(")[1][:-1]

        if _lhs.undecl:
            if _rhs.type.thing == utils.TH_ARRAY:
                self.generated += _lhs.type.to_str() + " " + _lhs.name + "(" + _rhs.name + ");\n"
            else:
                self.generated += _rhs.type.to_str() + " " + _lhs.name + " = " + _rhs.name + ";\n"
        elif not _lhs.undecl: # dotted always undecl = False
            if _rhs.type.thing == utils.TH_ARRAY:
                # memcpy
                self.generated += "memcpy(" + _lhs.name + ", " + _rhs.name + ".data(), " + _rhs.name + ".size());\n"
            else:
                self.generated += _lhs.name + " = " + _rhs.name + ";\n"

    def emit_get_key(self):
        _id = self.vars[0].name
        _type = self.vars[0].type

        self.generated += _type.to_str() + " " + _id + " = " + "fd_to_key_map[sockfd];\n"
        
    def emit_set_key(self):
        _key = self.vars[0].name

        self.generated += "key_to_fd_map" + "[" + _key + "]" + " = sockfd;\n"

    def emit_append(self):
        _container = self.vars[0].seq_alias
        _to_add = self.vars[1]
        if _container.type.asn_seq:
            self.generated += "ASN_SEQUENCE_ADD(&" + _container.name + ", &" + _to_add.name + ");\n"
        
    def emit_call(self):
        _event = self.vars[0].name 

        self.generated += _event + "("

        _args = ""
        for _arg in self.vars[1:]:
            _id = _arg.name
            _args += _id + ", "
        _args = _args[:-2]

        self.generated += _args + ");\n"
        

    def emit_store(self):
        pass

    def emit_lookup(self):
        pass

    def emit_send(self):
        pass

    def emit_loop(self):
        pass

    def emit_if(self):
        pass

    def emit_else(self):
        #self.generated += "else: \n"
        pass

    def emit_read_config(self):
        pass

    def emit_break(self):
        self.generated += "break;\n"

    def emit_continue(self):
        self.generated += "continue'\n"

    def emit_pass(self):
        self.generated += ";\n"


class UserDefined:
    def __init__(self, name, ret_type):
        self.name = name
        self.arg_types = [] # list of python types?
        self.ret_type = ret_type

class Variable:
    '''
    Invariants
    1. self.type == None only if ident hasnt been assigned concrete type yet
    2. self.type == Type.Multiple (str) only if a search for concrete python.Type returns a list of types.
    --> in this case, self.possible_types must be list.
    3. self.type == python.Type() only if a concrete type has been assigned to the ident.
    '''
    def __init__(self, arg_idx, name, parent, type=None, undecl = False):
        self.arg_idx = arg_idx
        self.name = name
        self.parent = parent # usually a python.Action
        self.invisible = False # not in C++
        self.formal_arg = False
        self.seq_alias = None
        self.undecl = undecl

        # assign self.type from somewhere.
        if isinstance(type, list):
            self.possible_types = type
            self.type = Type.MULTIPLE
        else:
            self.type = type

    def type_to_str(self):
        if self.type.ident == "char" and self.type.thing == utils.TH_ARRAY:
            if isinstance(self.parent, Event):
                self.type.ident = "std::vector<char>&"
            elif isinstance(self.parent, Action) and self.parent.name == "ENCODE":
                self.type.ident = "std::vector<char>"
            else:
                self.type.ident = "std::string"
        return self.type.ident
    
    def get_index(self):
        return self.arg_idx
    
    def contains(self, attr):
        '''
        "Does this variable contain a particular sub-attribute"
        '''
        _type = self.type
        return _type.contains(attr)    

    def __repr__(self):
        if self.parent:
            return repr((type(self), self.name, self.parent))
        return self.name
    
class Map:
    def __init__(self, map_name):
        self.name = map_name
        self.key_type = None
        self.struct = utils.Struct(name=f"{map_name}_struct", thing=utils.TH_SIMPLE) # one per map
    
    def add_to_map_struct(self, variable):
        # add_to_map only after type_lookup
        assert(variable.type) # only refs to typed variables must be added to map
        self.struct.vars[variable.name] = variable

class Timer:
    '''
    Used like Map, stores the attributes of the timer_ctx struct.
    '''
    def __init__(self, _id, _timeoutsec, _callback):
        self._id = _id
        self._timeoutsec = _timeoutsec
        self._callback = _callback

class Type:
    MULTIPLE = "multi_type" # type assigned but multiple struct defintions.
    def __init__(self, ident, thing=utils.TH_SIMPLE, indirection=None, asn_seq=None):
        self.ident = ident # typename
        self.subs = {} # attr:Type
        self.thing = thing  
        self.indirection = indirection # use during translate()
        self.sz = None
        self.asn_seq = asn_seq

    def to_str(self):
        if self.ident == "char" and self.thing == utils.TH_ARRAY:
            self.ident = "std::string"
        return self.ident
    
    def equals(self, other_type):
        assert(isinstance(other_type, Type))
        if self.ident == other_type.ident:
            return True
        # have some equivalent type rules
        elif ((self.ident == "int" or self.ident == "uint8_t" or self.ident == "size_t") and
            (other_type.ident == "int" or other_type.ident == "uint8_t" or other_type.ident == "size_t")):
            return True
        else:
            return False

    def path_to(self, thing):
        '''
        If a sub attribute is of type with thing thing, return the
        list of attributes encountered in the path to that sub attribute
        '''
        path = []
        # print(f"enter {self.ident}")
        # print(f"{self.ident} has subs {self.subs}")
        # print(f"{self.ident} is of thing type {self.thing}")
        # for sub in self.subs.values():
        #     print(sub.ident, sub.thing)
        if not self.subs:
            if self.thing == thing:
                print("found thing")
                return self
            return []
        for attr_id, sub_type in self.subs.items():
            print(f"Check attr {attr_id}")
            if isinstance(sub_type, list):
                for _sub in sub_type:
                    if _sub.thing == thing:
                        print(f"{_sub} has {thing}")
                        path.append(attr_id)
                        return path
                    else:
                        _sub_path = _sub.path_to(thing)
                    if _sub_path:
                        path.append(attr_id)
                        path.extend(sub_path)
                        return path
            else:
                # print(f"{attr_id} has a unique single type")
                # print(self.subs[attr_id])
                # print(sub_type.ident, sub_type.thing)
                # print(self.thing)
                if self.thing == thing:
                    #print(f"{sub_type.ident} has {thing}")
                    path.append(attr_id)
                    return path
                if sub_type.thing == thing:
                    #print(f"{sub_type.ident} has {thing}")
                    path.append(attr_id)
                    return path
                else:
                    sub_path = sub_type.path_to(thing)
                if sub_path:
                    path.append(attr_id)
                    path.extend(sub_path)
                    return path
        return [] 
    
    def _contains(self, attr):
        '''
        Returns True if a given nested asn type
        has a particular string as an attribute,
        at any nesting level, else False.
        '''
        if attr in self.subs:
            return True, self.subs[attr]
        
        for sub in self.subs:
            res, type = self.subs[sub]._contains(attr)
            if res:
                return res, type
        return False, None 
    
    def get_typeof(self, attr):
        '''
        If a type contains attr, return
        its type.
        '''
        _, type = self._contains(attr)
        return type

    # def __str__(self):
    #     _str = f"{self.ident}\n"
    #     if not self.subs:
    #         return self.ident
    #     for s, st in self.subs.items():
    #         _str += f"\t{s}: {str(st)}"
    #     return _str

def main():
    # primitive C++ types
    # only these will have subs empty
    int_t = Type("int", utils.TH_ARRAY)
    float_t = Type("float")
    str_t = Type("str")

    # this type creation should be simulated by the 
    # asn parser.
    t1 = Type("nas_t")
    t1.subs["sst"] = [int_t, float_t]
    t1.subs["ssd"] = float_t
    t2 = Type("secuheader_t") # type of an attribute of t1
    t1.subs["shdr"] = t2
    t2.subs["cipher"] = float_t
    t2.subs["alg"] = str_t

    # print(t1.contains("shdr"))
    # print(t1.get_typeof("shdr").ident)

    var = Variable("myvar", None, None)
    var.type = t1
    # print(var.contains("shdr"))
    path = t1.path_to(utils.TH_ARRAY)
    print(path)
    # print(t1)
    #print(t2)

if __name__ == "__main__":
    main()



    