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


<details>
<summary> <strong>🛠️ NF architecture under Pyramis</strong></summary>
  
  On successful translation of a Pyramis node specification, two key files are generated: <code>AMF_linking.cpp</code>
  and <code>AMF_platform.cpp</code>. These two files implement the processing-platform split.

  ### Design Requirements
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

  ### Implementation
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
The Pyramis Compiler is developed to demonstrate that Pyramis is a complete and flexible language. The primary goal of the Pyramis compiler is to output multithreaded, C++
code from a Pyramis specification, as a reference implementation. 

- By showing that a path exists from Pyramis specification to a correct implementation, (in our case, via a compiler), we demonstrate the correctness of
Pyramis as a specification language.

The Pyramis Grammar is functionally a subset of the Python Grammar. This allows a major
convenience during compilation to C++, i.e. The compiler does not require a custom lexer or a
parser. Instead, after pre-processing a Pyramis file to generate an equivalent Python file, we can
generate an AST intermediate representation using Python’s `ast.parse()`.

Once the AST is created, the compiler recursively visits each node to further parse identifier
information, create and delete scopes, updating symbol-tables and eventually generating an
intermediate representation suitable for conversion to C++ code.

<details>
<summary> <strong> ⚒ Pyramis Compiler Driver</strong></summary>
</details>


<details>
<summary> <strong> ⚒ Types in Pyramis</strong></summary>
</details>



<details>
<summary> <strong> ⚒ The <code>python.Type</code> API</strong></summary>
</details>



<details>
<summary> <strong> ⚒ Type Assignment and Inference</strong></summary>
</details>











