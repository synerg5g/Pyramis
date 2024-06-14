## 🛠️ NF Architecture under Pyramis
On successful translation of a Pyramis node specification, two key files are generated: AMF linking.cpp
and AMF platform.cpp. These files implement the processing-platform split discussed earlier.

AMF platform.cpp performs core networking functions to implement a NF that can act in a multi-
threaded and asynchronous manner, as both a Server and a Client. In the multithreaded view,
multiple nfvInstance threads monitor their local epoll file descriptor, whose watch list contains 
a single listen socket bound to a globally known port. Each NF instance thread is running
its own epoll wait loop. On event detection by epoll wait() at the shared listen socket,
multiple threads may be woken up and there is a race to accept() the incoming connection.
On accept() by a single thread, the newly created data socket is added to a thread-local map
called the active socket map.

Another key criterion is supporting systems that implement multi-node or chained procedures.
Such procedures require imposing a sequential order on asynchronous message receipts and sends.
In systems with short connections, it becomes necessary to record active sockets and sockets
that need to be closed.

To achieve these goals, the platform file maintains the thread-local active socket map of
custom Socket structs. A Socket contains attributes that describe the socket such as its file
descriptor, port number, socket type, peer IP address, and whether the connection is short or
long. Furthermore, each NF instance thread has a single epoll file descriptor that detects events
at active sockets. On detection of an event at any socket, a callback is triggered based on the
type of socket that encountered the event.

For example, on event detection at a data socket, the platform file passes a buffer representing
the event read at the kernel socket to the processing file via the callbacks defined in the platform
file for decoding, IE interpretation, UE context generation, request/response message generation,
and finally triggering a send data() to a peer NF, in whatever manner was described by the
Pyramis specification.

A note on the platform file callbacks

On server initialisation, callbacks that are specified in the interface file are registered with the
sockets bound to the globally known port associated with that interface. During the running
of the server, callback functions bound to the initial port are registered with newly created
sockets as well. These callback functions are specified as EVENTs in the Pyramis specification
and translated to C++ by the compiler.

Therefore, in the two file NF architecture, the callbacks are triggered by the platform file only
on receipt of the incoming message data, but are defined in the processing file.

### Pyramis Compiler
