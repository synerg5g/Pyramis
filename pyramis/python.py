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
        self.procedure_key = Variable()
        
        self.live_map = None # set by Event
        self.previous_map = None # set by action
        self.previous_action = None # set by action
        self.mutex = False

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
                decl_defaults = "int length, int sockfd, struct nfvInstanceData *nfvInst"
                call_defaults = "length, sockfd, nfvInst"
            else:
                decl_defaults = "int sockfd, struct nfvInstanceData *nfvInst"
                call_defaults = "sockfd, nfvInst"

            _user = ""
            for v in event.vars:
                _user += v.type_to_str() + " " + v.name + ", "
        
            _event_decl += (_user + decl_defaults) + ")"
            event.decl += _event_decl # assign to event.
            event.call_defaults += call_defaults

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
            event.emit(self) # pass module for access to live_map
            self.generated.extend(event.generated) # contains all event text.
            
            self.generated += "}\n\n" # each event needs a closing bracket.

            # reset
            self.live_map = None
            self.previous_map = None
            self.previous_action = None
            self.mutex = False


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


    def generate_platform_h(self):
        # gen include headers

        # gen timer_types enum

        # gen timer context structs from gx.timer_contexts

        # gen timer_expiry_context VARIANT. (see demos/variant.cpp)

        # gen the rest of platform files from template.
        pass

    def generate_platform_cpp(self):
        pass

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
        self.call_defaults = ""
        self.indent = 0


    def emit(self, module):
        '''
        p_m_ul can only be triggered by the next action.
        '''
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
            
            # if action is map
            if action.name == "STORE" or action.name == "LOOKUP":
                if action.name == "STORE":
                    _map = action.vars[0]
                elif action.name == "LOOKUP":
                    _map = action.vars[1]

                module.live_map = _map

                # EVENT - map sequence
                # map is first action
                if not module.previous_action:
                    pass
                # map, map sequence.
                # map follows map
                elif module.previous_action.name == "STORE" or module.previous_action.name =="LOOKUP":
                    # if current map different from previous map, unlock previous
                    if module.previous_map and (module.live_map.name != module.previous_map.name):
                        # unlock previous map
                        self.generated.append("pthread_mutex_unlock(&" + module.previous_map.name + "_lock);\n")
            else: # if action is non-map
                if not module.previous_action: # non-map action is first, emit
                    print("No previous actin")
                # map, non-map sequence
                elif module.previous_action.name == "STORE" or module.previous_action.name =="LOOKUP":
                    # unlock previous map
                    self.generated.append("pthread_mutex_unlock(&" + module.previous_map.name + "_lock);\n")
                    
            action.emit(module) # do p_m_l for store/lookup, do access

            print(f"{action.name} exits {action.exits} scopes")
            self.generated.append(action.generated + action.indent* "\t" + action.exits * "}" + "\n")

            module.previous_action = action

        #self.generated.append("}")

class Action:
    pyramis_actions = utils.PYRAMIS_ACTIONS

    def __init__(self, gx, name, parent=None, indent=None, mv=None):
        self.gx = gx
        self.name = name
        self.parent = parent
        self.mv = mv
        self.vars = [] # references to python.Var(), stored in the enclosing scope.

        self.indent = indent # update via modulevisitor.
        self.exits = 0 # scope exits
        self.generated = ""

    def emit(self, module):
        '''
        C++ code generation, unique per action.
        '''
        emitters = {
            action.lower(): getattr(self, f"emit_{action.lower()}") for action in Action.pyramis_actions
        }
        print(self.name.lower())
        if self.name.lower() in emitters:
            emitters[self.name.lower()](module)
        else:
            error.error(f"Action {self.name} not supported yet.")
        
        #module.previous_action = self

    def emit_create_message(self, module):
        _type = self.vars[0].type
        _id = self.vars[0].name

        if not self.vars[0].type.sz:
            self.generated += _type.to_str() + " " + _id + " {};"
        else:
            _sz = self.vars[0].type.sz
            self.generated += _type.to_str() + " " + _id + "[" + _sz + "];"
        
    def emit_decode(self, module):
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

    def emit_encode(self, module):
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
        

    def emit_udf(self, module):
        # declare all undeclared args
        for _arg in self.vars[2:]:
            if "MACRO" in _arg.name:
                _arg.name = _arg.name.split("(")[1][:-1]
            if _arg.undecl and _arg.type.thing != utils.TH_ENUM:
                self.generated += _arg.type.to_str() + " " + _arg.name + " {};\n"

        _fn = self.vars[1]
        _ret_id = self.vars[0]
        if _ret_id.undecl:
            self.generated += _ret_id.type.to_str() + " " + _ret_id.name + " = "
        self.generated += _fn + "("

        _args= ""
        for _arg in self.vars[2:]:
            if (len(self.vars[2:]) == 1):
                _args += _arg.name
                self.generated += _args + ");\n"
                return 
            else:
                _args += _arg.name + ", "
                _args = _args[:-2]
                self.generated += _args

        self.generated += ");\n"

    def emit_set(self, module):
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
                if _lhs.in_timer_ctx:
                    self.generated += _lhs.name + " = " + _rhs.name + ";\n"
                else:
                    self.generated += "memcpy(" + _lhs.name + ", " + _rhs.name + ".data(), " + _rhs.name + ".size());\n"
            else:
                self.generated += _lhs.name + " = " + _rhs.name + ";\n"

    def emit_get_key(self, module):
        _id = self.vars[0].name
        _type = self.vars[0].type

        self.generated += _type.to_str() + " " + _id + " = " + "fd_to_key_map[sockfd];\n"
        
    def emit_set_key(self, module):
        _key = self.vars[0].name

        self.generated += "key_to_fd_map" + "[" + _key + "]" + " = sockfd;\n"

    def emit_append(self, module):
        _container = self.vars[0].seq_alias
        _to_add = self.vars[1]
        if _container.type.asn_seq:
            self.generated += "ASN_SEQUENCE_ADD(&" + _container.name + ", &" + _to_add.name + ");\n"
        
    def emit_call(self, module):
        _event = self.vars[0].name 

        self.generated += _event + "("

        _args = ""
        for _arg in self.vars[1:]:
            _id = _arg.name
            _args += _id + ", "

        # add defaults acc to event
        for _ev in module.events.values():
            if _ev.name == _event:
                event = _ev
                break
        if not event:
            # invalid event was called
            error.error("Called invalid event.")

        _defaults = event.call_defaults
        _args += _defaults
        print(_args)

        self.generated += _args + ");\n"
        
    def emit_store(self, module):
        # do stuff
        # ....
        # p_m_l
        assert(module.live_map)

        # when prev action  = none and previous, live map = none
        try:
            if module.previous_action == "STORE" or module.previous_action == "LOOKUP":
                assert(module.previous_map)
                if module.live_map.name != module.previous_map.name:
                    # new lock for current map
                    self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"
                else:
                    pass
            else:
                self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"

        except AttributeError as a:
            # no previous action - first action in event
            # is a store.
            assert(not module.previous_map)
            self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"
        
        _map = module.live_map
        _key = self.vars[1]
        _attr = self.vars[2]
        _attr_val = self.vars[3]

        self.generated += self.indent * "\t" + _map.name + "[" + _key.name + "]." + _attr.name + " = " + _attr_val.name + ";\n" 
        
        module.previous_map = _map

    def emit_lookup(self, module):
        '''
        <ident.type> <ident.name> = <map>[key].<attribute>
        '''
        # when prev action  = none and previous, live map = none
        try:
            if module.previous_action == "STORE" or module.previous_action == "LOOKUP":
                assert(module.previous_map)
                if module.live_map.name != module.previous_map.name:
                    # new lock for current map
                    self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"
                else:
                    pass
            else:
                self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"

        except AttributeError as a:
            # no previous action - first action in event
            # is a store.
            assert(not module.previous_map)
            self.generated += self.indent * "\t" + "pthread_mutex_lock(&" + module.live_map.name + "_lock);\n"
        
        _map = module.live_map

        _id = self.vars[0]
        _map = self.vars[1]
        _key = self.vars[2]
        _attr = self.vars[3]

        if _id.undecl:
            self.generated += self.indent * "\t" + _id.type.to_str() + " " + _id.name + " = "
        else:
            self.generated += self.indent * "\t" + _id.name + " = "
    
        self.generated += _map.name + "[" + _key.name + "]." + _attr.name + ";\n"

        module.previous_map = _map

    def emit_send(self, module):
        _args = ", ".join(self.vars)
        self.generated += "send_data(" + _args + ", nfvInst" +  ");\n"
        
    def emit_loop(self, module):
        self.generated += "for ("
        print(self.vars)
        _itr = self.vars[0]
        _low = self.vars[1]
        _high  = self.vars[2]

        self.generated += _itr.type.to_str() + " " + _itr.name + " = " + _low.name + "; "
        self.generated += _itr.name + " < " + _high.name + "; "
        self.generated += _itr.name + "++) {\n"
    
    def emit_if(self, module):
        '''
        cond
        '''
        print("conds are %s"%[var for var in self.vars])
        print(len(self.vars))
        self.generated += "if ("

        cond = ""
        for _cond in self.vars:
            if (isinstance(_cond, utils.Condition)):
                # lhs op, rhs
                _lhs = _cond.lhs
                _rhs = _cond.rhs
                _op = _cond.op

                if _op and _rhs:
                    if "MACRO" in _rhs.name:
                        _rhs.name = _rhs.name.split("(")[1][:-1]
                    cond += _lhs.name + " " + _op + " " + _rhs.name
                else:
                    cond += _lhs.name
            else:
                # logical op (&&, ||)
                assert(isinstance(_cond, str))
                cond += " " + _cond + " "

        self.generated += cond
        self.generated += ") {\n"

    def emit_else(self, module):
        self.generated += "else { \n"
        pass

    def emit_read_config(self, module):
        pass

    def emit_break(self, module):
        self.generated += "break;\n"

    def emit_continue(self, module):
        self.generated += "continue'\n"

    def emit_pass(self, module):
        self.generated += ";\n"

    def emit_create_timer_context(self, module):
        self.generated += "//timer context bc\n"

    def emit_timer_start(self, module):
        self.generated += "//timer_start bc\n"

    def emit_timer_stop(self, module):
        self.generated += "timer_stop_bc\n"


class UserDefined:
    def __init__(self, name, ret_type):
        self.name = name
        self.arg_types = [] # list of python types?
        self.ret_type = ret_type
        self.is_keygen = False

class Variable:
    '''
    Invariants
    1. self.type == None only if ident hasnt been assigned concrete type yet
    2. self.type == Type.Multiple (str) only if a search for concrete python.Type returns a list of types.
    --> in this case, self.possible_types must be list.
    3. self.type == python.Type() only if a concrete type has been assigned to the ident.
    '''
    def __init__(self, arg_idx=None, name=None, parent=None, type=None, undecl = False):
        self.arg_idx = arg_idx
        self.name = name

        self.parent = parent # usually a python.Action
        self.invisible = False # not in C++
        self.formal_arg = False
        self.seq_alias = None
        self.undecl = undecl
        self.in_timer_ctx = False

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



    