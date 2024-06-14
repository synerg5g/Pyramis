The Pyramis DSL aims to provide an alternative to text-based specifications for multi-tier networked systems. 

- The Pyramis Compiler is developed to demonstrate that there does exist a path from a Pyramis specification to a correct implementation.
- This reflects on the validity of Pyramis as a specification language.

## ModuleVisitor (graph.py)
Every python.Module has an associated modulevisitor that implements ast walk and creation of python.XXX objects.
A global modulevisitor object tracks current state during the walk.
1. Make a record of all the pyramis events i.e. functiondefs at walk init, along with the formal arguments passed in.
- events as python.Functions, arguments as list of arg strings.
2. subsequent visit_Functiondef builds python.Variable objects for each function param. 

## Typing Invariants:
- All event i.e. python.Function() formals have python type "str" at init.
- If an ast.Constant.value is a udf name, the subsequent args are assigned types from their udf declarations in gx.udfs. (in visit_constant, check if arg[x] is in gx.udfs. If yes, type from udfs)
- If an ast.Constant ka action is CREATE_MESSAGE, assign type from arg.
- std::vector and fixed size C arrays are treated as 
type = value type, thing = ARRAY
--> int **x is treated as an int with indirection level = 2

## Pyramis Compiler Invariants
1. Single python.Variable object, "stored" in scope symtab. All other
objects maintain references to the single instance and can update it at any time. (variables in scope tree may be untyped for certain durations)

2. All variables in scope tree must be typed after first ast walk.

3. Between CALL Action and python.Event(), only one must create new variables.

4. All Python.Variables() must be stored in a class Scope, and each python.Action and python.Event contains a reference to its enclosing scope. (EVENT/IF/ELSE) and therefore the (eventually) typed variables.

5. Each variable has a parent, i.e. the pyramis.Action that contains it. Further, any 
python.variable encountered in an action must be stored in the appropriate scope.

6. CALL action variables must always be typed in visit_Call(). 
On visit_Functiondef, if the variable untyped after get_variable -> CALL occurs in a different event
On visit_Functiondef, if variable typed after get_variable -> CALL occurred before, was recorded. (by the search-in-calls pathway.)
On visit_Call, if action == CALL, if variable untyped after get_variable -> ??
--> Need to link the variables of events to variables of calls somehow
EVENT entry(a, b, c):
    CALL (eventname, a, b) # stored in mv.calls as a python.Action(), formals [] = a,b