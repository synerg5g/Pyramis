# FILE: graph.py
# --------------
# implements a modulevisitor class that
# performs the ast.nodevisit stuff.
# has access to the module and gx. 
# Therefore can update the scope tree.
# NOTE: Can implement multiple AST visitors with entry point in this file.
import os
import sys
import ast
import pathlib
import logging
from . import ast_utils
from . import error
from . import infer
from . import python
from . import utils
from . import log
from . import config

# --- global variable mv
_mv = None

def setmv(mv):
    global _mv
    _mv = mv
    return _mv

def getmv():
    return _mv

def check_redef(gx, node):
    existing_events = getmv().funcs
    print(existing_events)

    for event_name in existing_events:
        name = node.name
        if name in event_name:
            # error.error(
            #     "function/class redefinition is not supported", gx, node, mv=getmv()
            # )
            print("Function redefinition detected.") # todo: error class stores all errors in a logfile without terminating.

def get_arg_nodes(node):
    '''
    Return list of ast.Constant objects that 
    represent Pyramis Action args.
    '''
    args = []

    for arg in node.args:
        args.append(arg)

    return args


class ModuleVisitor(ast_utils.BaseNodeVisitor):
    def __init__(self, module, gx):
        ast_utils.BaseNodeVisitor.__init__(self)
        self.module = module
        self.gx = gx # ref to global translator state
        self.funcs = {} # name: Function
        self.configure_logging()

    def configure_logging(self):
        """
        silent -> WARNING only, (terminal failed type inference)
        
        debug -> DEBUG, (all logs)
        
        default -> INFO (procedure begin/end logs)
        """
        # create "Pyramis" Logger object
        self.log = logging.getLogger(self.__class__.__name__) 

        # create a formatted handler to print logs
        os.makedirs("./__logs/", exist_ok=True)
        log_file = logging.FileHandler(filename="./__logs/mv_log.txt")
        log_file.setFormatter(log.CustomFormatter())
        self.log.addHandler(log_file) 
        
        # log_console = logging.StreamHandler(stream=sys.stdout)
        # log_console.setFormatter(log.CustomFormatter())
        # self.log.addHandler(log_console)

        # set the default log level
        self.log.setLevel(logging.INFO)
    
    def visit(self, node, *args):
        ast_utils.BaseNodeVisitor.visit(self, node, *args)

    # entry point for every node.py walk
    def visit_Module(self, node):
        self.forward_references(node)

        # continue regular ast walk
        for child in node.body:
            self.visit(child, None)

        # can begin a second ast walk from here,
        # if some variables in scope do not have
        # a type yet. Need a way to indicate the 
        # walk number for the other visitor methods.
        # XXX TODO

    #return list of ast nodes of type cl
    def stmt_nodes(self, node, cl):
        result = []
        for child in node.body:
            if isinstance(child, cl):
                result.append(child)
        return result

    def forward_references(self, node):
        """
        - append a list of functiondef nodes to the visitor's .funcnodes field.
        - create Function objects and add string args to their "formals" field.
        """
        getmv().event_nodes = [] # ref to visitor
        
        # gets every ast.node of functiondef i.e. EVENT.
        print(self.stmt_nodes(node, ast.FunctionDef))
        for ast_functiondef_node in self.stmt_nodes(node, ast.FunctionDef):
            check_redef(self.gx, ast_functiondef_node)
            getmv().event_nodes.append(ast_functiondef_node)

            # funcdef.name will give the actual unique name
            # of the pyramis func eg sbiincoming etc.
            # stores the args in "Function.formals" at init.
            getmv().funcs[ast_functiondef_node.name] = python.Event(self.gx, ast_functiondef_node) # maybe add to __untyped_events[n.name] instead
            #print(f"formals: {getmv().funcs[n.name].formals}")

        #print(f"{getmv().funcnodes}")
    
    def visit_FunctionDef(self, node, parent=None):
        if node.name in getmv().funcs:
            func = getmv().funcs[node.name]
        else: 
            print("unexpected")
            func = python.Event(self.gx, node, parent, mv = getmv())
        # go through all the pyramis function variables,
        # create a python.Variable object for each one of them.
        # parent means the containing entity.
        # ----
        # Add python.Variable to scope symtab as soon as it is created. (initially untyped for EVENTS)
        # EVENT and Action objects .attrs must reference the attribute in scope tree.
        # -- .attr is used for codegen.
        # --- as soon as a scope tree variable gets typed, the func ref will also be updated
        # --> ensure persistent scope trees.

        for i, _v in enumerate(func.formals):
            var = infer.get_variable(self.gx, i, func, _v)
        
        #print(func.vars)

        # associate the function object with all nodes
        # in its body. Thus subnodes can modify 
        # state in parent functiondef.
        #print(len(node.body))
        for body_node in node.body:
            self.visit(body_node, func)
            
    def visit_Expr(self, node, func=None):
        #self.bool_test_add(node.value) # node.value = class ast.XXX 
        print(f"aiyo {type(node.value)}")
        self.visit(node.value, func)

    def visit_Call(self, node, func=None):
        '''
        '''
        # func is of type python.Event() 
        # node.func is of type ast.Name, 
        # node.func.id are the pyramis action
        assert isinstance(node.func, ast.Name)
        ident = node.func.id

        # Create action

        # store action formals

        # for i, _v in enumerate(action.formals):
            # obtain v

        
            # laction.vars.append(var)
        if ident == 'CALL':
            # lookup_call in mv.funcs, node.args[0]
            # transfer types
            # remove from untyped
            lfunc = python.lookup_func(node, getmv())
            if lfunc:
                if lfunc.id == node.args[0]:
                    pass

        for arg in get_arg_nodes(node):
            self.visit(arg, func) # func = ast.Call
        
    def visit_For(self, node, func=None):
        self.log.debug(f"In FOR") # all str, maybe some int

    def visit_If(self, node, func=None):
        self.log.debug("In IF") # all str, maybe some int
        for child in node.body:
            self.visit(child, func)
        for child in node.orelse:
            self.visit(child, func)

def parse_module(gx, node=None):
    """create a Module object"""
    assert(isinstance(gx, config.GlobalInfo))
    name = gx.py_module_path.stem # name must be of the python file without .py extension.

    filename = gx.py_module_path

    module = python.Module(gx, filename, node)

    if module.name in gx.modules:  # cached?
        return gx.modules[module.name]
    gx.modules[module.name] = module # AMF.py

    # -- generate AST
    module.ast = python.parse_file(module.filename) 
    
    # write ast to .deps/node.ast
    gx.py_ast_path = gx._pyramis / f".deps/{gx.nf_name}.ast"
    with open(gx.py_ast_path, "w") as f_ast:
        f_ast.write(f"{ast.dump(module.ast, indent = 4)}")  # store AST in a new file.

    # associate ast-vistor with the module
    old_mv = getmv() # None at init
    module.mv = mv = ModuleVisitor(module, gx) # ast has access to gx and actual file
    setmv(mv) # store mv in %rax, set the global _mv to this object.

    #mv.visitor = mv # ?
    mv.visit(module.ast)

    # reset mv to none at end of first walk
    mv = old_mv
    setmv(mv)

    return module # contains state necessary for codegen.
