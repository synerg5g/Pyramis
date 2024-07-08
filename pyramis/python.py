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

def parse_file(name):
    filebuf = importlib.util.decode_source(open(name, 'rb').read())
    
    try:
        return ast.parse(filebuf)
    except SyntaxError as s:
        #print("*ERROR* %s:%d: %s" % (name, s.lineno, s.msg))
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

def get_last_include(file_path):
  try:
    with open(file_path, "r") as file:
      lines = []
      saw_include = False  # Flag to track if we encountered an #include

      for line in file:
        lines.append(line)
        if "#include" in line.strip():  # Check for #include in stripped line
          saw_include = True
        elif saw_include and not line.strip():  # Empty line after potential #include
          break
        saw_include = False  # Reset flag after empty line or non-include line
      return lines
  except IOError as e:
    raise IOError(f"Error opening file {file_path}: {e}") from e

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
        self.locks = []

        self.generated = [] # store converted text from events.

    def write_to_file(self, filepath):
        '''Called by the generate_* methods at end.'''
        # do stuff
        with open(filepath, mode="w") as f_w:
            for thing in self.generated:
                f_w.write(thing)

        # reset module.generated
        self.generated = []
    
    def fixup_udf_h(self):
        '''
        add platform.h to udf file
        '''
        print("fixup")
        _plat = self.gx.output_dir / f"{self.gx.nf_name}_platform.h"
        _udf = self.gx.udfs_path

        _generated = ""
        with open(_udf, "r", encoding="utf-8") as f_udf_r:
            _udf_h_r = f_udf_r.read()
            f_udf_r.seek(0)
            _udf_h_l = f_udf_r.readlines()
            _inc = _udf_h_r.find("#include") # first include
            
            _recompile = False
            for line in _udf_h_l:
                if line.startswith("#include") and "__BUILD__" in line:
                    _recompile = True
                    break

            if _inc == -1: # no includes yet.
                _generated += "#include " + "\"" + str(_plat) + "\"" + _udf_h_r
            else:
                if _recompile: # some header already included
                    _generated = _udf_h_r
                else:
                    _generated = _udf_h_r[:_inc] + "#include " + "\"" + str(_plat) + "\""  + "\n" + _udf_h_r[_inc:]
        self.generated.append(_generated)

        self.write_to_file(_udf)

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

        _inc = ["\"../../udf.h\"", f"\"{self.gx.nf_name}_platform.h\"", f"\"{self.gx.nf_name}_contexts.h\"",
                "<algorithm>"]
        #_inc.append(f"\"{self.gx._pyramis}/pyramis.h\"")
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
            if not event.timer_type:
                if any(action.name == "DECODE" for action in event.actions) or any(action.name == "SEND" for action in event.actions):
                    decl_defaults = "size_t length, int sockfd, struct nfvInstanceData *nfvInst"
                    call_defaults = "length, sockfd, nfvInst"
                else:
                    decl_defaults = "size_t sockfd, struct nfvInstanceData *nfvInst"
                    call_defaults = "sockfd, nfvInst"
                
                # if procedure key never invoked:
                if not self.procedure_key.name:
                    error.error("This NF is not tracking procedure instances.", warning=True)
                else:
                    # if keygen udf not in actions, decl must have procedure_key
                    if not any(action.is_keygen for action in event.actions) and not any(v.name == self.procedure_key.name for v in event.vars):
                            decl_defaults += f", {self.procedure_key.type.to_str()} {self.procedure_key.name}"
                            call_defaults += f", {self.procedure_key.name}"
                            event.key_in_decl = True
            else:
                decl_defaults = "struct nfvInstanceData *nfvInst"
                call_defaults = "nfvInst"

            _user = ""
            for v in event.vars:
                if event.timer_type:
                    assert(len(event.vars) == 1)
                    _user += v.type_to_str() + "& " + v.name + ", "
                else:
                    _user += v.type_to_str() + " " + v.name + ", "
        
            _event_decl += (_user + decl_defaults) + ")"
            event.decl += _event_decl # assign to event.
            event.call_defaults += call_defaults

            self.generated.append(_event_decl + ";\n")
        
        _generic_timer = ""
        _generic_timer += "fdData_t generic_timer_start(int __timeout, struct nfvInstanceData *nfvInst);\n"
        _generic_timer += "void generic_timer_stop(auto timer_itr, struct nfvInstanceData *nfvInst);\n"

        self.generated.append(_generic_timer)
        
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

        # header
        _inc = [f"\"{self.gx.nf_name}_linking.h\""]
        _includes = ""
        for __inc in _inc:
            _includes += "#include " + __inc + "\n"
        _includes += "\n"
        self.generated.append(_includes)

        for event in self.events.values():
            event.emit(self) # pass module for access to live_map
            self.generated.extend(event.generated) # contains all event text.
            
            self.generated += "}\n\n" # each event needs a closing bracket.

            # reset
            self.live_map = None
            self.previous_map = None
            self.previous_action = None
            self.mutex = False
        
        # generate generic_timer_start and stop
        g_start = """
fdData_t generic_timer_start(int timeout, struct nfvInstanceData *nfvInst) {
    int tfd = timerfd_create(CLOCK_REALTIME, 0);
    
    struct itimerspec new_spec = {
        .it_interval = {0,0}, 
        .it_value = {timeout, 0}     
    };

    timerfd_settime(tfd, 0, &new_spec, NULL);

    struct epoll_event ev;
    ev.events = EPOLLIN;
    ev.data.fd = tfd;
    epoll_ctl(nfvInst->epoll_fd, EPOLL_CTL_ADD, tfd, &ev);

    fdData_t timer_fdd = fdData_t(TIMERFD_SOCKET, tfd);

    return timer_fdd;
}

"""
        self.generated.append(g_start)

        g_stop = """
void generic_timer_stop(auto timerfd_it, struct nfvInstanceData *nfvInst) {
    int tfd = timerfd_it->second.fd;
    struct itimerspec stop_timer_spec = {{}, {}};
    timerfd_settime(tfd, 0, &stop_timer_spec, NULL);

    close(tfd);

    nfvInst->fd_map.erase(timerfd_it);
}

"""

        self.generated.append(g_stop)

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
        #print(len(self.gx.maps))
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

            # locks used later.
            self.locks.append(map.name + "_lock")
        
        self.generated.append("#endif")
            
        file = self.gx.output_dir / f"{self.gx.nf_name}_contexts.h"
        self.write_to_file(file)


    def generate_platform_h(self):
        _guard = "#ifndef __" + self.gx.nf_name + "_PLATFORM_H__\n"
        _guard += "#define __" + self.gx.nf_name + "_PLATFORM_H__\n"
        
        self.generated.append(_guard)

        # gen include headers
        # #print(f'\"{self.gx.utility_lib}/common/include/datatypes.h\"')
        _inc = [f'\"{self.gx._utility_lib}/common/include/datatypes.h\"', '<map>', '<set>', 
                '<sys/timerfd.h>', '<sys/epoll.h>', '<unistd.h>', 
                '<string.h>', '<iostream>', '<queue>', '<sys/eventfd.h>', '<variant>']
        _includes = ""
        for __inc in _inc:
            _includes += "#include " + __inc + "\n"
        _includes += "\n"
        self.generated.append(_includes)

        # gen constants
        _const = [
            'MAX_CONNECTIONS 1024',
            'E_MAX_NFV_COMPONENTS 10',
            'MAX_EPOLL_EVENTS E_MAX_NFV_COMPONENTS * MAX_CONNECTIONS',  # Keep the expression
            'MAX_MESSAGE_SIZE 10000',
            'LISTEN_QUEUE_BACKLOG 10',
            'NON_UE_MESSAGE_STREAM 0',
            'UE_MESSAGE_STREAM 1',
            ]

        _consts = ""
        for _c in _const:
            _consts += "#define " + _c + "\n"
        _consts += "\n"
        self.generated.append(_consts)

        # gen node enum
        _nodes = ""
        _nodes += "typedef enum NFNode {\n"
        _nodes += "\t" + self.gx.nf_name + ",\n"
        for nf in self.gx.other_nf_interfaces:
            _nodes += "\t" + nf + ", \n"
        _nodes += "} NODE;"

        self.generated.append(_nodes + "\n\n")

        # gen timer_types enum
        _timer_types = ""
        _timer_types += "enum class _e_TimerType: std::uint8_t {\n"
        for i, _timer_type in enumerate(self.gx.timers.keys()):
            _timer_types += "\t" + _timer_type + " = " + str((i + 1)) + ",\n"
        _timer_types += "};\n\n"
        
        self.generated.append(_timer_types)

        # gen timer context structs from gx.timer_contexts
        # need to add a field for _e_timer_type along with procedure_key for STOP timer find.
        #print([ctx._name for ctx in self.gx.timer_contexts.values()])
        _structs = ""
        for ctx in self.gx.timer_contexts.values():
            _struct = ""
            _struct += "struct " + ctx._name + " {\n"
            _struct += "\tint procedure_key;\n"
            _struct += "\tsize_t length;\n"
            _struct += "\t_e_TimerType timer_type;\n"
            for _a in ctx.attrs:
                _attr = ""
                _attr += "\t" + _a.type.to_str() + " " + _a.name + ";\n"
                _struct += _attr
            _struct += "};\n"
            _structs += _struct + "\n"
        
        self.generated.append(_structs)


        # gen timer_expiry_context VARIANT. (see demos/variant.cpp)
        _variants = ""
        _variants += "typedef std::variant<\n"
        for ctx in self.gx.timer_contexts.values():
            _timer_struct = ctx._name
            _variants += "\t" + _timer_struct + ","
        _variants = _variants[:-1]
        _variants += "\n> timer_expiry_context_t;\n\n"

        self.generated.append(_variants)


        # gen the rest of platform files from template.
        _rest = ""
        _file = self.gx._pyramis / "platform_h.txt"
        with open(_file, "r") as _file_r:
            _rest += _file_r.read()
        _rest += "\n"
        self.generated += _rest
        
        self.generated.append("#endif")

        file = self.gx.output_dir / f"{self.gx.nf_name}_platform.h"
        self.write_to_file(file)

    def generate_platform_cpp(self):
        # generate includes
        # gen include headers
        _inc = [f'\"{self.gx.nf_name}_platform.h\"', f'\"{self.gx._utility_lib}/platform/include/logging.h\"',
                '<vector>', '<pthread.h>', '<errno.h>', '<fcntl.h>', '<sys/socket.h>', '<netinet/sctp.h>',
                '<arpa/inet.h>', '<netinet/in.h>']
        _includes = ""
        for __inc in _inc:
            _includes += "#include " + __inc + "\n"
        _includes += "\n"
        self.generated.append(_includes)

        # declare processing callbacks
        async_callbacks = ""
        for _inf in self.gx.interfaces.values():
            for event in self.events.values():
                #print(event.name, *_inf.processing) # single callback for each interface.
                _cb = _inf.processing[0]
                if event.name == _cb:
                    async_callbacks += event.decl + ";\n"
        self.generated.append(async_callbacks + "\n")

        # decl interface vector
        _ifv = ""
        _ifv += "std::vector<fdData_t> interfaceVector = {"
        for _inf in self.gx.interfaces.values():
            _ifv += _inf.make_ifv() + ", "
        _ifv = _ifv[:-2] # remove last comma
        _ifv += "};\n\n"
        self.generated.append(_ifv)

        # initialise user-locks
        #print(self.locks)
        _locks = ""
        for _lock in self.locks:
            _locks += "pthread_mutex_t " + _lock + " = PTHREAD_MUTEX_INITIALIZER;\n"
        _locks += "\n"
        self.generated.append(_locks)

        # transfer defaults from template.
        _rest = ""
        _file = self.gx._pyramis / "platform_cpp.txt"
        with open(_file, "r") as _file_r:
            _rest += _file_r.read()
        _rest += "\n"
        self.generated.append(_rest)

        _main = ""
        _main += "int main(int argc, const char *argv[]) {\n"

        for _inf in self.gx.interfaces.values():
            _register = ""
            #print(_inf.processing[0], self.events)
            if _inf.processing[0] in [event.name for event in self.events.values()]:
                _register += "\tport_request_handler_map[" + str(_inf.port) + "] = " + _inf.processing[0] + ";\n"
            #else:
                #print("WARNING: ... server entry callback is not defined.")
            _main += _register
        
        self.generated.append(_main)

        _footer = ""
        _file = self.gx._pyramis / "platform_cpp_main_footer.txt"
        with open(_file, "r") as _file_r:
            _footer += _file_r.read()
        _footer += "\n"
        self.generated.append(_footer)


        file = self.gx.output_dir / f"{self.gx.nf_name}_platform.cpp"
        self.write_to_file(file)


    def generate_makefile(self):
        # get the headers
        _setup = """
CC = g++
CFLAGS = -std=c++20 -Wall -Wextra -g
LDFLAGS = -lsctp -lpthread
BUILD_DIR = ./build
DEPS_DIR = $(BUILD_DIR)/.deps
"""
        self.generated.append(_setup)
        # define custom utility_library location
        _util = "UTILITY_LIBRARY = " + str(self.gx._utility_lib) + "\n"

        self.generated.append(_util)
        self.generated.append("LOG_LIB_DIR = $(UTILITY_LIBRARY)/platform/src\n\n")

        _target_name = self.gx.nf_name
        _target = ""
        _target += _target_name + ": "
        _target += f"$(DEPS_DIR)/{_target_name}_linking.o $(DEPS_DIR)/platform.o $(DEPS_DIR)/udf.o $(DEPS_DIR)/logging.o\n"
        _target += f"\t@$(CC) $(CFLAGS) $(DEPS_DIR)/{_target_name}_linking.o $(DEPS_DIR)/platform.o $(DEPS_DIR)/udf.o $(DEPS_DIR)/logging.o -o $(BUILD_DIR)/{_target_name} $(LDFLAGS)\n\n"
        self.generated.append(_target)

        _next = ""
        _next += "$(DEPS_DIR)/" + _target_name + "_linking.o: " + _target_name + "_linking.cpp | $(DEPS_DIR)\n"
        _next +=  "\t@$(CC) $(CFLAGS) -c " + _target_name + "_linking.cpp -o $(DEPS_DIR)/" + _target_name + "_linking.o\n\n"
        self.generated.append(_next)

        _after = ""
        _after += f"$(DEPS_DIR)/platform.o: {_target_name}_platform.cpp | $(DEPS_DIR)\n"
        _after += f"\t@$(CC) $(CFLAGS) -c {_target_name}_platform.cpp -o $(DEPS_DIR)/platform.o\n\n"

        _rest = ""
        _mk = self.gx._pyramis / "Makefile.txt"
        with open(_mk, "r") as  f_mk_r:
            _rest += f_mk_r.read()

        self.generated.append(_rest)

        # write_to_file
        file = self.gx.output_dir / "Makefile"
        self.write_to_file(file)

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
        self.key_in_decl = False

        self.timer_type = None # if event is a timer callback.
        self.timer_ctx_var = None # for a timer callback event, timer_ctx_var is fixed.


    def emit(self, module):
        '''
        p_m_ul can only be triggered by the next action.
        '''
        # get function header
        _event_decl = self.decl
        self.generated.append(_event_decl + " {\n")

        # update self.generated.
        for action in self.actions:
            #print(f"Indent: {action.indent}")
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
                    
            action.emit(module, self) # do p_m_l for store/lookup, do access

            #print(f"{action.name} exits {action.exits} scopes")
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
        self.is_keygen = False # for keygen udf.
        self.generated = ""

    def emit(self, module, event):
        '''
        C++ code generation, unique per action.
        '''
        emitters = {
            action.lower(): getattr(self, f"emit_{action.lower()}") for action in Action.pyramis_actions
        }
        #print(self.name.lower())
        if self.name.lower() in emitters:
            emitters[self.name.lower()](module, event)
        else:
            error.error(f"Action {self.name} not supported yet.")
        
        #module.previous_action = self

    def emit_create_message(self, module, event):
        _type = self.vars[0].type
        _id = self.vars[0].name

        if not self.vars[0].type.sz:
            self.generated += _type.to_str() + " " + _id + " {};"
        else:
            _sz = self.vars[0].type.sz
            self.generated += _type.to_str() + " " + _id + "[" + _sz + "];"
        
    def emit_decode(self, module, event):
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

    def emit_encode(self, module, event):
        # decl size and buffer.
        # size_t simple_enc_sz {};
        # std::vector<char> simple_enc(MAX_MESSAGE_SIZE, 0);
        # SynerPMessageEncode(simple, simple_enc, simple_enc_sz); // null added.
        #print([var.name for var in self.vars[1:]])
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
        

    def emit_udf(self, module, event):
        # declare all undeclared args
        _pre = ""
        for _arg in self.vars[2:]:
            if "MACRO" in _arg.name:
                _arg.name = _arg.name.split("(")[1][:-1]
                _arg.macro = True
            elif not _arg.defined and "." not in _arg.name:
                _pre += _arg.type_to_str() + " " + _arg.name + " {};\n"

        _fn = self.vars[1]
        _ret_id = self.vars[0]
        
        _args= ""
        for _arg in self.vars[2:]:
            if (len(self.vars[2:]) == 1):
                self.generated += _pre
                if _ret_id.undecl:
                    self.generated += _ret_id.type.to_str() + " " + _ret_id.name + " = "

                self.generated += _fn + "("
                
                _args += _arg.name
                self.generated += _args + ");\n"
                return
            else:
                _args += _arg.name + ", "
        _args = _args[:-2] # remove comma

        self.generated += _pre

        if _ret_id.undecl:
            self.generated += _ret_id.type.to_str() + " " + _ret_id.name + " = "

        self.generated += _fn + "("

        self.generated += _args + ");\n"

    def emit_set(self, module, event):
        '''
        undecl, decl set according to path taken by
        infer.get_variable()
        '''
        _lhs = self.vars[0]
        _rhs = self.vars[1]

        if "MACRO" in _rhs.name:
            _rhs.name = _rhs.name.split("(")[1][:-1]
        
        if _lhs.in_timer_ctx or _rhs.in_timer_ctx:
            if event.timer_ctx_var:
                _ctx_root = event.timer_ctx_var.name
                ctx_type_t = module.gx.timer_contexts[_lhs.timer_ctx_macro]._name
            elif _lhs.in_timer_ctx:
                _ctx_root = _lhs.name.split(".")[0]
                ctx_type_t = module.gx.timer_contexts[_lhs.timer_ctx_macro]._name
            elif _rhs.in_timer_ctx:
                _ctx_root = _rhs.name.split(".")[0]
                ctx_type_t = module.gx.timer_contexts[_rhs.timer_ctx_macro]._name
            
            if _lhs.in_timer_ctx:
                _ctx_stem = _lhs.name.split(".")[-1]
            elif _rhs.in_timer_ctx:
                _ctx_stem = _rhs.name.split(".")[-1]

        if _lhs.undecl:
            if _lhs.in_timer_ctx: # setting an attribute of ctx.
                # std::get<..>(_root)._stem = _rhs.name
                self.generated += "std::get<" + ctx_type_t + ">(" + _ctx_root + ")." + _ctx_stem + " = " + _rhs.name + ";\n"
            elif _rhs.in_timer_ctx: # getting a value from a ctx, storing in a local ident.
                self.generated += _lhs.type.to_str() + " " + _lhs.name +  " = " + "std::get<" + ctx_type_t + ">(" + _ctx_root + ")." + _ctx_stem + ";\n"
            else:
                if _rhs.type and _rhs.type.thing == utils.TH_ARRAY:
                    self.generated += _rhs.type.to_str() + " " + _lhs.name + "(" + _rhs.name + ");\n"
                else:
                    if _rhs.name in module.gx.timers.keys():
                        self.generated += _lhs.type.to_str() + " " + _lhs.name + " = _e_TimerType::" + _rhs.name + ";\n"
                    else:
                        self.generated += _lhs.type.to_str() + " " + _lhs.name + " = " + _rhs.name + ";\n"
        elif not _lhs.undecl: # dotted always undecl = False
            #print(id(_lhs))
            if _lhs.in_timer_ctx: # setting an attribute of ctx.
                # std::get<..>(_root)._stem = _rhs.name
                self.generated += "std::get<" + ctx_type_t + ">(" + _ctx_root + ")." + _ctx_stem + " = " + _rhs.name + ";\n"
            elif _rhs.in_timer_ctx: # getting a value from a ctx, storing in a local ident.
                self.generated += _lhs.type.to_str() + " " + _lhs.name +  " = " + "std::get<" + ctx_type_t + ">(" + _ctx_root + ")." + _ctx_stem + ";\n"
            else: # set not related to a timer context.
                if _rhs.type.thing == utils.TH_ARRAY: 
                    self.generated += "memcpy(" + _lhs.name + ", " + _rhs.name + ".data(), " + _rhs.name + ".size());\n"
                else:
                    # if its a timer_type, use the enum
                    if _rhs.name in module.gx.timers.keys():
                        self.generated += _lhs.name + " = _e_TimerType::" + _rhs.name + ";\n"
                    else:
                        self.generated += _lhs.name + " = " + _rhs.name + ";\n"

    def emit_get_key(self, module, event):
        _id = self.vars[0].name
        _type = self.vars[0].type

        self.generated += _type.to_str() + " " + _id + " = " + "fd_to_key_map[sockfd];\n"
        
    def emit_set_key(self, module, event):
        _key = self.vars[0].name

        self.generated += "key_to_fd_map" + "[" + _key + "]" + " = sockfd;\n"

    def emit_append(self, module, event):
        _container = self.vars[0].seq_alias
        _to_add = self.vars[1]
        if _container.type.asn_seq:
            self.generated += "ASN_SEQUENCE_ADD(&" + _container.name + ", &" + _to_add.name + ");\n"
        
    def emit_call(self, module, event):
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
        #print(_args)

        self.generated += _args + ");\n"
        
    def emit_store(self, module, event):
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

    def emit_lookup(self, module, event):
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

    def emit_send(self, module, event):
        _callback = self.vars[-1]
        if _callback == "NULL":
            # sending a response. get fd
            # from key_to_fd_map
            # else
            # send via sockfd.
            _key_or_fd = f"key_to_fd_map[{module.procedure_key.name}]"
            _callback = "NULL"
        else:
            _key_or_fd = module.procedure_key.name

        _args = ", ".join(self.vars[:-1])
        _args += ", " + _key_or_fd + ", " + _callback

        _length = ""
        _procedure_key = ""

        action = next((a for a in event.actions if a.name == "ENCODE"), None)
        if event.timer_type:
            ctx_var = event.timer_ctx_var
            ctx_type_t = "timer_expiry_context_" + event.timer_type + "_t"
            _procedure_key += "int procedure_key = std::get<" + ctx_type_t + ">(" + ctx_var.name + ").procedure_key;\n"
            if action: # encode found, new message
                _new_sz = action.vars[-1]
                _length += "size_t length = " + _new_sz.name + ";\n"
            else: # retry
                assert(ctx_var)
                _length += "size_t length = std::get<" + ctx_type_t + ">(" + ctx_var.name + ").length;\n"
        else:
            _procedure_key += "int procedure_key = " + module.procedure_key.name + ";\n"
        
        self.generated += _length

        #print("lookie here")
        # for var in event.vars:
        #     print(var.name)
        
        if not event.key_in_decl:
            self.generated += _procedure_key

        self.generated += "send_data(" + _args + ", nfvInst" +  ");\n"
        
    def emit_loop(self, module, event):
        self.generated += "for ("
        #print(self.vars)
        _itr = self.vars[0]
        _low = self.vars[1]
        _high  = self.vars[2]

        self.generated += _itr.type.to_str() + " " + _itr.name + " = " + _low.name + "; "
        self.generated += _itr.name + " < " + _high.name + "; "
        self.generated += _itr.name + "++) {\n"
    
    def emit_if(self, module, event):
        '''
        cond
        '''
        #print("conds are %s"%[var for var in self.vars])
        #print(len(self.vars))
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

    def emit_else(self, module, event):
        self.generated += "else { \n"
        pass

    def emit_read_config(self, module, event):
        pass

    def emit_break(self, module, event):
        self.generated += "break;\n"

    def emit_continue(self, module, event):
        self.generated += "continue'\n"

    def emit_pass(self, module, event):
        self.generated += ";\n"

    def emit_create_timer_context(self, module, event):
        _type = self.vars[0].type
        _id = self.vars[0].name
        _t_type = self.vars[0].timer_ctx_macro

        self.generated += _type.to_str() + " " + _id + "{};\n" # decl variant

        # get the _name of the timer context struct
        name = module.gx.timer_contexts[_t_type]._name

        self.generated += self.indent * "\t" + "std::get<" + name + ">(" + _id + ")" + ".procedure_key = " + module.procedure_key.name + ";\n"
        # std::get<
        #self.generated += self.indent * "\t" + _id + ".procedure_key" + " = " + module.procedure_key.name + ";\n"

    def emit_timer_start(self, module, event):
        #self.vars[-1] = "&" + self.vars[-1] # callback
        #print(self.vars)
        _timer_type, _timeout, _ctx, _callback = self.vars
        _args = ", ".join(self.vars)

        self.generated += "fdData_t timerfdd = " + "generic_timer_start(" + _timeout + ", nfvInst" + ");\n"
        
        # ctx MUST be of the struct type here. change this.
        self.generated += self.indent * "\t" + "timerfdd.timerCB = " + "&" + _callback + ";\n"
        self.generated += self.indent * "\t" + "timerfdd.ctx = " + _ctx +";\n"
        
        # nfvInst->fd_map[timerfdd.fd] = timerfdd;
        self.generated += self.indent * "\t" + "nfvInst->fd_map[timerfdd.fd] = timerfdd;\n"

    def emit_timer_stop(self, module, event):
        _t_type = self.vars[0]
        if "MACRO" in _t_type.name:
            _t_type.name = _t_type.name.split("(")[1][:-1]

        _ctx_var = event.timer_ctx_var

        if _ctx_var:
            ctx_type_t = module.gx.timer_contexts[event.timer_ctx_var.timer_ctx_macro]._name
        else:
            ctx_type_t = "timer_expiry_context_" +_t_type.name + "_t"

        if _ctx_var: # in callback
            _timer_type = self.indent * "\t"  + "auto __timer_type__ = " + "std::get<" + ctx_type_t + ">(" + _ctx_var.name + ").timer_type;\n"
            _procedure_key = self.indent * "\t" + "auto __procedure_key__ = " + "std::get<" + ctx_type_t + ">(" + _ctx_var.name + ").procedure_key;\n"
        else:
            _timer_type = self.indent * "\t" + "auto __timer_type__ = " + "_e_TimerType::" + _t_type.name + ";\n"
            _procedure_key = self.indent * "\t" + "auto __procedure_key__ = " + module.procedure_key.name + ";\n"
        
        self.generated += _timer_type + _procedure_key

        _find_if = ""
        _find_if += self.indent * "\t" + "const auto it = std::find_if(\n"
        _find_if += self.indent * "\t" + "nfvInst->fd_map.begin(),\n"
        _find_if += self.indent * "\t" + "nfvInst->fd_map.end(),\n"
        _find_if += self.indent * "\t" + "[&__timer_type__, &__procedure_key__]" + "(const auto &fd_map_entry)"
        _find_if += self.indent * "\t" + "{return (std::get<" + ctx_type_t + ">(" + "fd_map_entry.second.ctx).timer_type == __timer_type__\n"
        _find_if += self.indent * "\t" + "&& std::get<" + ctx_type_t + ">(" + "fd_map_entry.second.ctx).procedure_key == __procedure_key__);}\n"
        _find_if += self.indent * "\t" + ");\n\n"

        self.generated += _find_if

        _generic_stop = ""
        _generic_stop += self.indent * "\t" + "if (it != nfvInst->fd_map.end()) {\n"
        _generic_stop += (self.indent + 1) *"\t" + "generic_timer_stop(it, nfvInst);\n"
        _generic_stop += self.indent * "\t" + "}\n"

        self.generated += _generic_stop


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
        self.defined = False

        self.in_timer_ctx = False
        self.timer_ctx_macro = None
        self.macro = False

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
        assert(variable.type) # only refs to typed variables must be added to map. DO NOT MODIFY.
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
        # #print(f"enter {self.ident}")
        # #print(f"{self.ident} has subs {self.subs}")
        # #print(f"{self.ident} is of thing type {self.thing}")
        # for sub in self.subs.values():
        #     #print(sub.ident, sub.thing)
        if not self.subs:
            if self.thing == thing:
                #print("found thing")
                return self
            return []
        for attr_id, sub_type in self.subs.items():
            #print(f"Check attr {attr_id}")
            if isinstance(sub_type, list):
                for _sub in sub_type:
                    if _sub.thing == thing:
                        #print(f"{_sub} has {thing}")
                        path.append(attr_id)
                        return path
                    else:
                        _sub_path = _sub.path_to(thing)
                    if _sub_path:
                        path.append(attr_id)
                        path.extend(sub_path)
                        return path
            else:
                # #print(f"{attr_id} has a unique single type")
                # #print(self.subs[attr_id])
                # #print(sub_type.ident, sub_type.thing)
                # #print(self.thing)
                if self.thing == thing:
                    ##print(f"{sub_type.ident} has {thing}")
                    path.append(attr_id)
                    return path
                if sub_type.thing == thing:
                    ##print(f"{sub_type.ident} has {thing}")
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
            if isinstance(self.subs[sub], list):
                #print(self.subs[sub])
                for _t in self.subs[sub]:
                    res, type = _t._contains(attr)
                    if res:
                        assert(type)
                        return res, type
            else:
                res, type = self.subs[sub]._contains(attr)  
            if res:
                return res, type
        return False, None 
    
    def _pick_type(self):
        '''
        If the base types have multiple definitions for the same
        struct names, this function defines logic to return a single type.
        ??????
        '''
        pass
    
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

    