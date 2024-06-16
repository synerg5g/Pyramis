# Pyramis Developer Documentation

Pyramis is designed keeping two goals in mind:

<table><tr><th><strong>Abstractions must completely capture all aspects of multi-tier system specifications</strong></th></tr></table>

The 3GPP specifications for 5G are used as a source to extract general-purpose networking
constructs. These inform the choice of Pyramis Syntax. The working assumption is that a
Domain-Specific Language that can specify the procedures listed in the 3GPP specification can
specify a wide range of multi-tier system.

<table><tr><th><strong>Pyramis workflow must be extensibile and reusable for a wide variety of multi-tier systems</strong></th></tr></table>

At present, we have demonstrated support for variation in multitier-systems only at the level of
differences in L-7 protocol. This is enabled by a general purpose header-file parser that generates
a set of base types for the system. The working assumption is that a given set of base types
(along with encoders and decoders) completely specify the L-7 protocol of any multi-tier system

## 🛠️ From Specification to Executable NF

Pyramis keywords can represent key aspects of most multi-tier systems. However, to compile to
a working implementation, certain constraints have to be imposed on the inputs and outputs.

<details>
<summary> <strong>⚒ Well-Defined L-7 protocol library</strong></summary>
    Pyramis supports multitier systems using the NGAP and HTTP L-7 protocols out of the box. However, custom application-layer protocol must meet certain requirements: 

- Valid messages for custom protocols must be implemented as complete C/C++ structs. These files may be stored in a `utils` directory in the your root folder.
- HTTP messages must represent and access their payload strings as attributes of nlohmann::json objects. We provide an HTTP library for this purpose.
- All char arrays are interpreted as C++ `std::vector<char>`. Strings, if any, must be null-terminated.
- Header-file library must be fully contained in a `/utils` directory.
</details>

<details>
<summary> <strong>⚒ Notion of procedure key</strong></summary>
  The NF must generate a unique procedure key for each instance of supported procedure.
  
- Procedure may be simple (login request-response) or complex (SMF session establishment).
- Complexity arises due to the requirement of demultiplexing messages received at a
single interface to the correct message handler.

The notion of key and its supporting `fd_to_key_map` and `key_to_fd_map` are
implementation-specific constructs that enable this message demultiplexing.

- procedure key is used by the NF application to maintain a synchronous message processing flow despite asynchronous message ingress at an NF.
- Your UDF File must always contain a keygen function, defined via `//@@keygen`
</details>

<details>
<summary> <strong>⚒ Platform-file + Processing-file architecture</strong></summary>
  Where a platform file triggers kernel networking actions, and the processing file performs user-level message-processing actions

- In the current implementation, a C++ user-level processing file is generated from the Pyramis specification.
- In the current implementation, a multithreaded, asynchronous epoll-based platform.cpp file is generated that declares an entry point into the user-level processing code.
</details>

## 🛠️ NF architecture under Pyramis</strong></summary>
    
On successful translation of a Pyramis node specification, two key files are generated: <code>AMF_linking.cpp</code>
and <code>AMF_platform.cpp</code>. These two files implement the processing-platform split.
  
<details>
<summary> <strong>⚒ Design</strong></summary>
    
<code>AMF_platform.cpp</code> performs core networking functions to implement a NF that can act in a multi-
threaded and asynchronous manner, as both a Server and a Client. 

In this multithreaded view, on initialisation, 
multiple <code>nfvInstance</code> threads monitor their local epoll file descriptor, whose watch list contains 
a single listen socket bound to a globally known port. Each NF instance thread is running
its own epoll wait loop. On event detection by <code>epoll wait()</code> at the shared listen socket,
multiple threads may be woken up and there is a race to <code>accept()</code> the incoming connection.
On <code>accept()</code> by a single thread, the newly created data socket is added to a thread-local map
called the <code>active_socket_map</code>.

Another key criterion is supporting systems that implement multi-node or chained procedures.
Such procedures require imposing a sequential order on asynchronous message receipts and sends.
In systems with short connections, it becomes necessary to record active sockets and sockets
that need to be closed.
</details>

<details>
<summary> <strong>⚒ Implementation</strong></summary>
  
To achieve these goals, the platform file maintains the thread-local <code>active_socket_map</code> of
custom <code>Socket</code> structs. A <code>Socket</code> contains attributes that describe the socket such as its file
descriptor, port number, socket type, peer IP address, and whether the connection is short or
long. Furthermore, each NF instance thread has a single epoll file descriptor that detects events
at active sockets. On detection of an event at any socket, a callback is triggered based on the
type of <code>Socket</code> that encountered the event.

For example, on event detection at a data <code>Socket</code>, the platform file passes a buffer representing
the event read at the kernel socket to the processing file via the callbacks defined in the platform
file for decoding, IE interpretation, UE context generation, request/response message generation,
and finally triggering a <code>send_data()</code> to a peer NF, in whatever manner was described by the
Pyramis specification.

<ins><strong>A note on the platform file callbacks</strong></ins>

On server initialisation, callbacks that are specified in the interface file are registered with the
sockets bound to the globally known port associated with that interface. During the running
of the server, callback functions bound to the initial port are registered with newly created
sockets as well. These callback functions are specified as EVENTs in the Pyramis specification
and translated to C++ by the compiler.

Therefore, in the two file NF architecture, the callbacks are triggered by the platform file only
on receipt of the incoming message data, but are defined in the processing file.
</details>


## 🛠️ Pyramis-to-C++ Compiler

The Pyramis Grammar is functionally a subset of the Python Grammar. This allows a major
convenience during compilation to C++, i.e. The compiler does not require a custom lexer or a
parser. Instead, after pre-processing a Pyramis file to generate an equivalent Python file, we can
generate an AST intermediate representation using Python’s `ast.parse()`.

Once the AST is created, the compiler recursively visits each node to further parse identifier
information, create and delete scopes, updating symbol-tables and eventually generating an
intermediate representation suitable for conversion to C++ code.

<details>
<summary> <strong> ⚒ Pyramis Compiler Driver</strong></summary>

The compiler driver orchestrates the entire compilation process, right from parsing command-line
options to generating C++ code. Its major functions are listed below.

```
Initialisation
---------------
1. Parse command-line, set global compiler configurations.
2. Parse C++ protocol headers, UDF File and Interface File.
3. Pre-process Pyramis Specification to Python.
4. Create AST, begin AST walk.
```

```
AST Walk
--------
Recursively visit each node
1. Maintain scopes and update symbol tables
2. Infer and assign types to identifier.
3. Incrementally generate an IR of parsed Pyramis EVENTs, python.Actions and
python.Maps.
4. Report semantic errors
```
```
Code Generation
---------------
Generate C++ files from IR
1. Remove redundant Map accesses.
2. Generate timer_expiry_context_t
3. Emit translated EVENT definitions to processing file i.e. linking.cpp.
4. Emit Map definitions to contexts.h.
5. Emit event declarations to linking.h
6. Emit networking code to platform.cpp and platform.h and generate Makefile.
```


</details>


<details>
<summary> <strong> ⚒ Types in Pyramis</strong></summary>
    
Any reasonable networked system implementation defines and is dependent on its L-7 i.e.
application layer protocol. For example, the internet communications occur over the HTTP L-7
protocol, and 3GPP NF-NF communications are required to use either the NGAP or PFCP
protocols.

At its core, an NF protocol is specified by its <ins>state machine, message types, and encoder-decoder
pairs</ins>, all defined and distributed via <ins>protocol libraries</ins>. C++ protocol libraries provide C++
structs and classes in header files to define message types, and define encoders and decoders
for each valid message-type in the protocol. The state-machine of a protocol is 
maintained by the application itself, and is a function of the underlying protocol library.

Likewise, an NF implementation, and its Pyramis specification must necessarily depend on external protocol libraries. Pyramis enables specification of these type constraints
via the `CREATE_MESSAGE`, `ENCODE`, `DECODE` and `UDF` keywords.

From the above discussion, it is clear that a valid Pyramis specification of each node must be
associated with a set of base types that arise from its assumed L-7 protocol.
</details>



<details>
<summary> <strong> ⚒ The <code>python.Type</code> API</strong></summary>

The Pyramis compiler must work extensively with message-types defined in the protocol library
of the NF. Therefore, it implements a recursive python.Type data structure with an associated
internal API to simplify certain operations. python.Type is designed to completely capture the
recursive nature of nested struct definitions.

```C++
// class python . Type represents a recursive C ++ struct .
class Type {
    public :
        ident ,       // top - level name of the type
        thing ,       // array or simple type ?
        indirection , // count of pointer indirection
        subs          // map of attributes of this type to their python.Types

        // Defines rules for equivalent types and returns true
        // if two equivalent types are compared .
        equals ()
        
        // If a sub attribute is of type with thing thing , return the
        // list of attributes encountered in the path to that sub attribute .
        //
        // This is useful if we want to confirm a path to a nested array .
        path_to ()
        
        // If a type contains attr , return
        // its type .
        get_typeof ()

    private :
        // Returns True if a given nested asn type
        // has a particular string as an attribute ,
        // at any nesting level , else False .
        _contains ()
}
```

<ins>**Note on Creating python.Types**</ins>

Recall that python.Types are built to represent recursive C++ message-type structs, defined in
the protocol header files. To give the compiler access to these structs, they are parsed to dicts
during compiler initialisation via a <ins>custom C++ header file parser</ins> in `pyramis/pyramis/utils.py`

The C++ header-file parser performs the crucial function of creating a set of base types for
the NF being implemented. For every header file in the protocol header library, the parser
isolates struct definitions, serializes them into a `.json` file, and finally deserializes the `.json` file to
a nested dictionary. **In essence, the C++ header-file parser takes a set of header files
and extract each `struct/union/enum` definition encountered in the system.**

The work of resolving inter-file struct dependencies, i.e. nested struct definitions takes place
on demand via the `CREATE_MESSAGE` keyword during the AST Walk. This step uses the parsed
structs to generate the appropriate recursive `python.Type` and assigns it to identifier specified.

</details>



<details>
<summary> <strong> ⚒ Type Assignment and Inference</strong></summary>

In the Pyramis Compiler, identifiers are represented as python.Variable objects. Depending on
the progress of the AST Walk, an identifier may be typed or untyped. A identifier is considered
typed if its `python.Variable` has been assigned a concrete `python.Type`.

`CREATE_MESSAGE, ENCODE, DECODE, UDF` are the only Pyramis keywords that are allowed to
directly assign concrete types to an identifier. All other actions must obtain their types indirectly
by an inference procedure. Oftentimes, the compiler is fortunate and encounters typed identifiers
at each action - implying that a concrete type was assigned at some point before the current
action. However, on several occasions identifiers are assigned concrete type after the first usage.

As a uniform solution to this problem, the Pyramis compiler creates and maintains a hierarchy
of Scopes

<ins>Note on Pyramis IR and ModuleVisitor<ins>

The AST Walk is implemented by a custom `ModuleVisitor` subclass of the `ast.NodeVisitor`
class. The `ModuleVisitor` performs a depth-first traversal of the `ast.Node`s in the AST of the
pre-processed Pyramis specification, dynamically dispatch handler functions linked to each
`ast.Node` type. Each handler function performs core functions related to IR creation and type
inference.

The Pyramis IR is designed to enable easy generation of C++ code from the allowed Pyramis
keywords. Keeping these in mind, the fundamental constructs of a Pyramis specification are
defined as `python.Event` for `EVENT`s, `python.Actions` for Pyramis Keywords, and `python.Map`s
for maps accesses. Each of these constructs also depends on their own variables being typed,
hence the IR defines `python.Variable` and a recursive `python.Type`.

With this in mind, a Pyramis processing file can be parsed into a series of python.Events
containing a series of python.Actions. Both of these contain sets of python.Variables
representing the arguments passed to the keyword actions The primary objective of the AST
walk is to generate this complete Pyramis IR.

_A complete Pyramis IR is one in which every variable is typed_. To achieve this target,
more constructs are required such as <ins>Scopes and a mechanism for type inference</ins>. Once the
generated IR is validated, it is used to directly emit C++ code based on certain code-generation
rules.

<details>
<summary> <strong> 📋 Scopes and Type Inference </strong></summary>
    
Pyramis scopes are of three kinds: `MODULE, EVENT and BLOCK`, corresponding to module-level,
`EVENT`-level and `IF/LOOP`-level. The `ModuleVisitor` drives the creation of new scopes, addition of
new `python.Variables` to the corresponding symbol-tables.

In a simplistic interpreter design for a purely statically-typed language, a temporary stack of
scopes starting at every `EVENT` would be sufficient to assign types to identifiers, as each would
have to be declared before usage. For example, in C++ projects, calling a function without first
declaring its typed signature is simply disallowed and leads to a compilation error. Pyramis
`EVENT`s on the other hand, are not provided concrete types in the specification. A subsequent
`CALL` (either from the same `EVENT` or another one) to that `EVENT` would similarly fail unless the typed
signature is generated before. **This behaviour cannot be expected in Pyramis, as assigning
explicit types destroys the purpose of a simple DSL syntax.**

Since EVENT definitions and CALLs are coupled together, there is a requirement for a mechanism
that allows sharing of appropriate variable and their types across EVENTs. The mechanism used
by Pyramis is to maintain a <ins>persistent parent-pointer tree of scopes</ins>. In this setup, we develop a
mechanism for inferring types for identifiers irrespective of the order in which they are assigned
concrete types:

```C++
// The modulevisitor can store references to newly created ( untyped ) EVENT
// variables in its own local scope , and store the python . EVENT
// in a global collection of events with references to its python . Variables .
//
// Similarly , each python . Action i.e. CALL is stored in a global collection of
// calls , with references to its own python . Variable .
//
// See source graph.py for full details .
When a CALL is encountered :
    if event was defined previously
    // type inference across events
    its variables would be referenced by an old scope
    and by the old python . Event stored in the global
    events map .
        if the variable is typed :
            copy the reference to the python . Type to the corresponding
            variable of the CALL that is being processed .
            ... etc
        ..etc
    ..etc

When an EVENT is encountered :
    if event was CALLed earlier :
        assign CALL variable types to the EVENT .
            If the event was typed earlier ,
                // we have succeeded ,
            if not ,
                //untyped variable will be added to scope to be
                // resolved later .
            ..etc
        ..etc
    ..etc
```
    
</details>

</details>











