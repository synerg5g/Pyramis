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
        self.maps = {} # used to generate contexts.h

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
        # do stuff

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
        for event in self.events:
            event.emit()
            self.generated.append(event.generated)
        
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
        # do stuff


        file = self.gx.output_dir / f"{self.gx.nf_name}_contexts.h"
        self.write_to_file(file)

    def write_to_file(self, filepath):
        '''Called by the generate_* methods at end.'''
        # do stuff


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

        if node:
            self.gx.all_events.add(self) # gx stores a history of refs to events called all_events

        self.generated = [] # emit appends string lines.


    def emit(self):
        # update self.generated.
        for action in self.actions:
            action.emit()


class Action:
    pyramis_actions = utils.PYRAMIS_ACTIONS

    def __init__(self, gx, name, parent=None, mv=None):
        self.gx = gx
        self.name = name
        self.parent = parent
        self.mv = mv
        self.vars = {} # references to python.Var(), stored in the enclosing scope.
        self.generated = ""

    def emit(self):
        '''
        C++ code generation, unique per action.
        '''
        emitters = {
            action: getattr(self, f"emit_{action.lower()}") for action in Action.pyramis_actions
        }
        
        if self.name in emitters:
            return emitters[self.name]
        else:
            error.error(f"Action {self.name} not supported yet.")

    def emit_assert(self):
        pass

class UserDefined:
    def __init__(self, name, ret_type):
        self.name = name
        self.arg_types = [] # list of python types?
        self.ret_type = ret_type

class Variable:
    def __init__(self, arg_idx, name, parent, type=None):
        self.arg_idx = arg_idx
        self.name = name
        self.parent = parent # usually a python.Action
        self.invisible = False # not in C++
        self.formal_arg = False
        self.type = type
        # assign self.type from somewhere.
    
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
            return repr((self.parent, self.name))
        return self.name
    
class Map:
    def __init__(self, map_name):
        self.name = map_name
        self.struct = utils.Struct(name=f"{map_name}_struct") # one per map
    
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
    def __init__(self, ident, thing=None, indirection=None):
        self.ident = ident # typename
        self.subs = {} # attr:Type
        self.thing = thing  
        self.indirection = indirection # use during translate()
    
    def equals(self, other_type):
        assert(isinstance(other_type, Type))
        if self.ident == other_type.ident:
            return True
        # have some equivalent type rules
        
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

    def __str__(self):
        _str = f"{self.ident}\n"
        if not self.subs:
            return self.ident
        for s, st in self.subs.items():
            _str += f"\t{s}: {str(st)}"
        return _str

# primitive C++ types
# only these will have subs empty
int_t = Type("int")
float_t = Type("float")
str_t = Type("str")

# this type creation should be simulated by the 
# asn parser.
t1 = Type("nas_t")
t1.subs["sst"] = int_t
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

# print(t1)
#print(t2)



    