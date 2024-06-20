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

        self.events = {}
        self.calls = {} # history of CALLed python.Actions
        self.live_event = None

        self.root_scope = infer.Scope(infer.Scope.MODULE) # head
        self.live_scope = None # updated by enter_scope, exit_scope
        self.indent = None
        
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
        
        log_console = logging.StreamHandler(stream=sys.stdout)
        log_console.setFormatter(log.CustomFormatter())
        self.log.addHandler(log_console)

        # set the default log level
        self.log.setLevel(logging.DEBUG)

    # #return list of ast nodes of type cl
    # def stmt_nodes(self, node, cl):
    #     result = []
    #     for child in node.body:
    #         if isinstance(child, cl):
    #             result.append(child)
    #     return result

    # def forward_references(self, node):
    #     """
    #     - append a list of functiondef nodes to the visitor's .funcnodes field.
    #     - create Function objects and add string args to their "formals" field.
    #     """
    #     getmv().event_nodes = [] # ref to visitor
        
    #     # gets every ast.node of functiondef i.e. EVENT.
    #     print(self.stmt_nodes(node, ast.FunctionDef))
    #     for ast_functiondef_node in self.stmt_nodes(node, ast.FunctionDef):
    #         check_redef(self, ast_functiondef_node)
    #         getmv().event_nodes.append(ast_functiondef_node)

    #         # event_name: python.event
    #         getmv().funcs[ast_functiondef_node.name] = python.Event(self.gx, ast_functiondef_node) # maybe add to __untyped_events[n.name] instead
    #         #print(f"formals: {getmv().funcs[n.name].formals}")

    #     #print(f"{getmv().funcnodes}")

    def validate_walk(self):
        for event in self.events.values():
            try:
                print(f"Event {event.name}: vars: {[(var.name, var.type.thing, var.type.ident) for var in event.vars]}")
            except:
                print(f"FAILED: Event vars: {[(var.name) for var in event.vars]}")
                
            for action in event.actions:
                if isinstance(action, python.Action):
                    print(f"Action: {action.name}")
                    print(action.vars)
                else:
                    print(f"Non-action in event.actions: {event} :: {action}")
                    print(type(action))
                for var in action.vars:
                    if isinstance(var, python.Variable):
                        print(f'`{var.name}`: {var.type}')
                    else:
                        print(f"Non-var in action.vars: {action} -> {var}")
                        print(type(var))

        # check if map structs are complete.
        for map in self.gx.maps.values():
            print(f"map {map.name} attributes: {[(key, val.type.thing, val.type.ident) for key, val in map.struct.vars.items()]}")
            print(f"key type: {map.key_type.ident}, {map.key_type.thing}")
    
    def visit(self, node, *args):
        ast_utils.BaseNodeVisitor.visit(self, node, *args)

    # entry point for every node.py walk
    def visit_Module(self, node):
        #self.forward_references(node)

        # enter module scope
        _, indent = infer.enter_new_scope(self, infer.Scope.MODULE)

        # continue regular ast walk
        for child in node.body:
            self.visit(child, None)
        self.log.debug("Module AST walk complete.")

        self.validate_walk()
        print(self.live_scope.kind)

        # can begin a second ast walk from here,
        # XXX TODO
    
    def visit_FunctionDef(self, node, parent=None):
        print(f"Visiting {type(node)} i.e. EVENT {node.name}")
        _, indent = infer.enter_new_scope(self, infer.Scope.EVENT)

        if node.name in getmv().events:
            error.error("Redeclaration of event %s.\n" %node.name)
        else: 
            # print("New EVENT detected.")
            event = python.Event(self.gx, node, parent)
            getmv().events[node.name] = event
        
        self.live_event = event
        # print("Old len: %s" %len(self.live_event.vars))
        for i, _v in enumerate(self.live_event.formals):
            var = infer.get_variable(self, i, _v, self.live_event)
            if not var:
                # search calls - it might be possible that a previous CALL
                # occurred to this EVENT. 
                if event.name in self.calls:
                    call = self.calls[event.name]
                    try:
                        # 
                        var = python.Variable(i, _v, self.live_event, call.vars[i + 1].type)
                    except KeyError as k:
                        # arg mismatch in call, error
                        error.error("Insufficient arguments in previous CALL to event `%s`.\n" %call.name)
                else:
                    # first ever occurence of this EVENT name
                    # just return untyped variables
                    var = python.Variable(i, _v, self.live_event)
            else:
                # create and return untyped variable
                assert(not var.type)
                ## print(f"Impossible: Event variables cannot have been encountered before the event itself.")
            
            event.vars.append(var)
            self.events[event.name] = event # event without actions

            infer.add_var_to_live_scope(self, var)  # scope.symtab[j] = var(j) etc.
        
        # print("New len: %s"%len(self.live_event.vars))
        
        for body_node in node.body:
            self.visit(body_node, node, indent) # parent of all the nodes being visited == ast.Functiondef

        # print(f"Finished visiting sub-nodes of {type(node)} i.e. EVENT {node.name}")
        # exit scope
        self.module.events[node.lineno] = event # event with actions

        infer.exit_live_scope(self)
            
    def visit_Call(self, node, parent=None, _indent=None):
        '''
        '''
        # func is of type python.Event() 
        # node.func is of type ast.Name, 
        # node.func.id are the pyramis action
        assert isinstance(node.func, ast.Name)
        # Create action
        action = python.Action(self.gx, node.func.id, parent, _indent, self)
        print(f"Visiting action {action.name}, parent = {parent}")
        print(f"action indent: {_indent}")

        # print(f"Now visiting args of {node} i.e. action {action}")
        args = get_arg_nodes(node)
        # print(action.name)
        match action.name:
            case "CREATE_MESSAGE":
                if len(args) == 2:
                    # last arg is the var_type
                    _t = args[-1].value
                    _type = infer.type_from_type_str(self.gx, _t) # may return list of types -> in case your library has multiple definitions of the same struct.
                    
                    var = python.Variable(0, args[0].value, action, _type) # here, if _type is a list, store both in this var's possible_types. 
                    
                    # action->var ref
                    action.vars.append(var) # if an ident has two types, 

                    # scope -> var ref
                    infer.add_var_to_live_scope(self, var)

                elif len(args) == 3:
                    # collection
                    pass
            
            case "DECODE":
                '''
                DECODE(decode_fn, *args)
                errors:
                - get_decoder(decoder_name) : 
                '''
                # get the udf
                decoder_name = args[0].value
                decoder = self.gx.get_decoder(decoder_name)
                assert(isinstance(decoder, python.UserDefined))
                action.vars.append(decoder_name)

                # assign types based on arg placement
                for i, _v in enumerate(args[1:]):
                    vt = decoder.arg_types[i]
                    var = infer.get_variable(self, i, _v.value, action)
                    if not var:
                        # create new variables for the new args
                        var = python.Variable(i, _v.value, action, vt)
                    else:
                        var.type = vt
                        
                    var.name = _v.value
                    action.vars.append(var)
                    infer.add_var_to_live_scope(self, var)

            case "ENCODE":
                '''
                ENCODE(encode_fn, *args)
                '''
                encoder_name = args[0].value
                encoder = self.gx.get_encoder(encoder_name)
                assert(isinstance(encoder, python.UserDefined))
                action.vars.append(encoder_name)

                for i, _v in enumerate(args[1:]):
                    vt = encoder.arg_types[i]
                    var = infer.get_variable(self, i, _v.value, action)
                    if not var:
                        # create new variables for the new args
                        var = python.Variable(i, _v.value, action, vt)
                    else:
                        var.type = vt
                    
                    var.name = _v.value
                    print(var.name)
                    action.vars.append(var)
                    infer.add_var_to_live_scope(self, var)

            case "UDF":
                udf_name = args[1].value
                udf = self.gx.get_udf(udf_name)

                ret = args[0].value
                ret_v = infer.get_variable(self, 0, ret, action)
                if not ret_v.type:
                    ret_v.type = udf.ret_type
                action.vars.append(ret_v)

                # print([v.value for v in args[2:]])
                for i, _v in enumerate(args[2:]):
                    # print(i)
                    vt = udf.arg_types[i] # the python.Type() is created by config rather than mv
                    var = infer.get_variable(self, i, _v.value, action)
                    if not var:
                        # create new variables for the new args
                        var = python.Variable(i, _v.value, action, vt)
                    else:
                        var.type = vt

                    var.name = _v.value
                    action.vars.append(var)
                    infer.add_var_to_live_scope(self, var)
            
            case "SET":
                '''
                If SET-ing an identifier that has not been used earlier,
                i.e. get_from_scope = null,
                code-emit must emit it with its declaration.
                '''
                untyped = []
                typed = []
                for i, _v in enumerate(args):
                    # print(f"Getting variable for {_v.value}")
                    var = infer.get_variable(self, i, _v.value, action)

                    if not var:
                        # rare
                        print("setting undeclared var %s"%_v.value)
                        var = python.Variable(i, _v.value, action)
                        var.undecl = True
                    
                    if var.type:
                        typed.append(var)
                        if len(untyped) == 1:
                            untyped[0].type = var.type
                        if len(typed) == 2:
                            assert(typed[0].type.equals(typed[1].type)) 

                    elif not var.type:
                        # print(f"Attempt to copy lhs type to rhs, {_v.value}")
                        untyped.append(var)
                        if len(typed) == 1:
                            var.type = typed[0].type

                        if len(untyped) == 2:
                            # assigning unknown to unknown
                            print([v.name for v in untyped])

                        
                    action.vars.append(var)
                    print(f"var: {var.name}, undecl = {var.undecl}")
                    infer.add_var_to_live_scope(self, var)

            case "GET_KEY": # try get_procedure_key
                '''
                GET_KEY(<key_identifier>)

                Returns the procedure identifier key
                mapped to the sending fd. (i.e. fd that just detected the epollin event)
                i.e. gets <key_identifier> = fdtokeymap[fd]
                '''
                key_name = args[0].value
                var = infer.get_variable(self, 0, key_name, action)
                action.vars.append(var)
                infer.add_var_to_live_scope(self, var)
                
            case "SET_KEY":
                '''
                SET_KEY(<key_identifier>)

                Assigns the current fd to the procedure identifier key
                i.e. sets keytofdmap[<key_identifier>]
                '''
                key_name = args[0].value
                var = infer.get_variable(self, 0, key_name, action)
                action.vars.append(var)
                infer.add_var_to_live_scope(self, var)

            case "APPEND":
                '''
                APPEND(<message_struct>, <some_value>)

                Given a message that contains an array attribute at some
                nesting level, append <some_value> to the end of that array.
                - Constraint: A single struct-level may only have 
                a single array attribute
                '''
                # - find subtype with thing=ARRAY.
                container_var = infer.get_variable(self, 0, args[0].value, action)
                assert(container_var.type) # is this fair? yes.

                # if multiple types
                if container_var.type == python.Type.MULTIPLE:
                    for _type in container_var.possible_types:
                        path = _type.path_to(utils.TH_ARRAY)
                        if path:
                            break
                else:
                    path = container_var.type.path_to(utils.TH_ARRAY)
                    stem = path[-1]
                
                if path:
                    print("found array seq!")
                    new_var_name = container_var.name + "." + ".".join(path)
                    new_var_t = container_var.type.get_typeof(stem)
                    print(new_var_t.ident, new_var_t.thing, new_var_t.asn_seq)
                    new_var = python.Variable(-1, new_var_name, action, new_var_t)
                    container_var.seq_alias = new_var
                    action.vars.append(container_var)
                    print(container_var.seq_alias.name)
                else:
                    # indent does not contain an attribute of container type.
                    error.error("APPEND: %s does not contain attribute of container type"%container_var.name)

                # attr ids encountered
                # path will need to be printed with dots
                # var 1 = dotted path, var 2 = var2

                # check that type rhs equals lhs
                to_add_var = infer.get_variable(self, 1, args[1].value, action)
                action.vars.append(to_add_var)

                print(action.vars[0].seq_alias.name)

                # minor bug in type-checking
                # if not (container_var.type.equals(to_add_var.type)):
                #     # type mismatch error
                #     error.error("APPEND:: Type mismatch: Trying to append `%s` to list of `%s`"%(to_add_var.type.ident, container_var.type.ident))
                infer.add_var_to_live_scope(self, container_var)
            
            case "CALL":
                '''
                CALL(event_name, *args)
                '''
                # check if event_name is defined.
                event_name = args[0].value
                event_name_v = python.Variable(0, event_name, action)
                action.vars.append(event_name_v)

                # for each arg, get_variable() via pure scope lookup
                # - this returns either a typed or untyped python.
                # - unlikely to return None
                for i, _v in enumerate(args[1:]):
                    var = infer.get_variable(self, i, _v.value, action) # scope lookup
                    if not var:
                        # Calling an event and passing arguments that
                        # havent even been initialised yet - error.
                        error.error("Unitialised variable: `%s`"%_v.value)
                    elif not var.type:
                        # i.e. the variable was declared, but no type has been assigned yet.
                        # This could occur if a CALL occurs with event formals, and the formals
                        # arent used anywhere before the CALL.
                        if event_name in self.events:
                            '''
                            EVENT eventname(j, k): 
                                # do stuff that may/may not assign concrete types to j,k

                            EVENT entry(a, b, c):
                                CALL (eventname, a, b) # stored in mv.calls as a python.Action()
                            '''
                            event = self.events[event_name]
                            assert(isinstance(event, python.Event))
                            try:
                                _type = event.vars[i].type
                                if _type:
                                    # belongs to old scope, will have
                                    # formals of other events as ident.
                                    # var is a ref to the variable created 
                                    # by the earlier event.
                                    # 
                                    # If the type exists, i can just create a new variable instance
                                    # for this EVENT without worrying about the need for 
                                    # resolving type in future
                                    var = python.Variable(i, _v.value, action, _type)
                                else:
                                    '''
                                    Can an event remain untyped after it has been parsed?
                                    - Yes, If the EVENT formal args are not used 
                                    - in the EVENT's body
                                    '''
                                    # need to link old scope var with new scope var.
                                    # issue: this would lead to identifier names for this CALL
                                    # to be overwritten by EVENT arg names of the matched EVENT
                                    # - types will be updated simultaneously though.
                                    # Q. Can I create a new variable who's type is a ref to 
                                    # the type of the event arg?
                                    # this hasnt been tested yet.
                                    # its clearlywrong. see _type
                                    var = python.Variable(i, _v, action, event.vars[i].type)
                            except KeyError as k:
                                error.error("Extraneous argument in current CALL to event `%s`: %s.\n" %event.name %_v.value)  
                        else:
                            # CALL an event that has not been defined yet.
                            # in lexical flow.
                            '''
                            args of the CALL may be untyped before calling, eg:
                            EVENT entry(a, b, c):
                                CALL (eventname, a, b) # stored in mv.calls as a python.Action()

                            EVENT eventname(j, k): 
                                # do stuff that uses assigns concrete types to j,k
                                # flow types of j,k to a,b in previous event.
                            '''
                            var = python.Variable(i, _v.value, action)
                    else:
                        # var is typed by actions before call. ideal scenario
                        print(f"`{_v.value}` was typed before CALL: {var.type.ident}")
                    
                    # add to action
                    assert(var)
                    action.vars.append(var)

                    # add to scope
                    infer.add_var_to_live_scope(self, var)

                    # add action to calls
                self.calls[action.name] = action

            case "STORE":
                '''
                - Get the map being accessed from gx.maps
                - set type of map attr variable as type of arg[-1]. This will update the type
                of the ident in scope as well.
                - add_to_map_struct()
                '''
                map_name = args[0].value
                if map_name in self.gx.maps:
                    map = self.gx.maps[map_name]
                else:
                    map = python.Map(map_name)
                
                key = args[1].value
                key_v = infer.get_variable(self, 1, key, action)
                if (key_v.type):
                    if not map.key_type:
                        map.key_type = key_v.type
                
                attr = args[2].value
                attr_v = infer.get_variable(self, 2, attr, action)
                if not attr_v.type:
                    # get type from last arg
                    attr_val = args[3].value
                    attr_val_v = infer.get_variable(self, 3, attr_val, action)
                    assert(attr_val_v.type)
                    attr_v.type = attr_val_v.type

                map.add_to_map_struct(attr_v)

                action.vars.extend([map_name, ])

                infer.add_var_to_live_scope(self, attr_v)
                infer.add_var_to_live_scope(self, key_v)

                # add map to maps
                self.gx.maps[map_name] = map


            case "LOOKUP":
                '''
                LOOKUP(<store_val_at_ident>, <from_map>, <at_key>, <attribute_of_map_struct>)
                - Basically, LOOKUP cannot perform any type assignment. just create default get_variables
                - add to scope.
                - Just create an empty action, with state for future dead code elim.
                '''
                for i, _v in enumerate(args):
                    var = infer.get_variable(self, i, _v.value, action)
                    action.vars.append(var)

            case "SEND":
                '''
                SEND(<message_body_struct>, <sendingNFInterface>, <peerNFname>, <peerNFInterface>, <callbackname>) 
                sendData()
                - If no callback, fd must exist in keytofdmap.
                - If callback present, pass NULL, new socket will be assigned by this NF

                void send_data(std::string peer_ip, int peer_port, std::vector<char>& msg, _e_connectionType conn_type,
                                _e_protocols protocol, NODE peer_node, size_t message_length, int procedure_key_or_original_receiver_fd, 
                                callback, nfvInst)
                '''
                # get peer_ip, peer_port, protocol, own_conn_type from interfaces.json
                # the procedure_key must exist in ancestor scopes of an EVENT that contains a SEND.
                # if args[-1] == NULL : 
                #   # store that variable in .vars, later get val from fd_to_key_map
                #  else:
                #     # only pass the the procedure_key
                # procedure key is defined as the ident passed to the keygen UDF
                message = args[0].value

            case "TIMER_STOP":
                pass

            case "TIMER_START":
                pass

        # add action to live event, 
        # no scope exit required.
        self.live_event.actions.append(action)
    
    def visit_Constant(self, node, parent=None, idx=None):
        map = { } # should contain a set of Pyramis types, accessible by a call to get_type(name). 
        #print(f"Arg: {node.value}\nType: {type(node.value)}")
        self.log.debug(f"do arg {idx} i.e. {node} of {parent}")
        
    def visit_For(self, node, parent=None, _indent=None):
        self.log.debug(f"In LOOP") # all str, maybe some int
        _, indent = infer.enter_new_scope(self, infer.Scope.BLOCK)

        action = python.Action(self.gx, "LOOP", parent, indent, self)

        # it
        itr = infer.get_variable(self, 0, node.target.id, action)
        if not itr.type:
            itr.type = infer.type_from_type_str(self.gx, "int")
        action.vars.append(itr)
        infer.add_var_to_live_scope(self, itr)

        # all loops are range-based
        # var[1] is lower, var[2] is upper.
        for i, _v in enumerate(node.iter.args):
            var = infer.get_variable(self, i, _v.value, action)
            action.vars.append(var)
            infer.add_var_to_live_scope(self, var)

        self.live_event.actions.append(action)

        for child in node.body:
            self.visit(child, node)
        
        infer.exit_live_scope(self)


    def visit_If(self, node, parent=None, _indent=None):
        print(f"Visiting {node}, parent = {parent}")
        _, indent = infer.enter_new_scope(self, infer.Scope.BLOCK)

        action = python.Action(self.gx, "IF", parent, indent, self)
        print(f"IF indent: {indent}")
        # create if utils.Conditions
        # returns a list
        _cond = node.test.value
        print("condition: [%s]"%_cond)

        conditions = utils.make_conditions(_cond)

        for i, cond in enumerate(conditions):
            if isinstance(cond, utils.Condition):
                cond.lhs = infer.get_variable(self, i, cond.lhs, action)
                cond.rhs = infer.get_variable(self, i, cond.rhs, action)
                #cond.type_check()
        
        action.vars.extend(conditions)
        print(len(action.vars))
        
        self.live_event.actions.append(action)

        for child in node.body:
            self.visit(child, node, indent) # parent of all these children will be an ast.IF
        print(f"Finished visiting sub-nodes of {node} i.e. IF Block")

        for child in node.orelse:
            indent -= 1
            # create a basic ELSE ction
            print(f"ELSE ident: {indent}")
            action_ = python.Action(self.gx, "ELSE", action, indent, self)
            self.live_event.actions.append(action_)
            indent += 1
            self.visit(child, node, indent)
        
        infer.exit_live_scope(self)
        
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
