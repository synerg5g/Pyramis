### 📌 Pyramis Syntax
Pyramis defines <ins><strong>action</strong></ins> keywords that are used to specify various kinds of user-level message processing actions. They can be categorised into the following:

#### State-Management Actions

 Pyramis supports the notion of contexts that store application state. Contexts are always persistent
 and are stored in <code>std::map<></code>s as specified by the user. Each Pyramis Map has an associated map struct that is dynamically generated as attributes are accessed.

 Pyramis provides 2 keywords: `STORE` and `LOOKUP`

 ```Python
# Store value __value at the attribute __attribute of the map struct at key __key of map __map_name
STORE(__map_name, __key, __attribute, __value)

# Retrieve the value of the attribute __attribute of the map struct at key __key of map __map_name
# and assign it to identifier __ident
LOOKUP(__ident, __map_name, __key, __attribute)
```

#### Message and Information Element (IE) Actions

Retrieving and manipulating message fields (IEs) is a fundamental operation in all networked systems.

Pyramis provides 5 keywords: `CREATE_MESSAGE`, `SET`, `APPEND`, `ENCODE`, `DECODE`

```Python
# Create a message of type __type and assign it to identifier __ident
# 
# If __size is specified, create a sequence of size __size of messages of type __type,
# and assign it to identifier __ident
CREATE_MESSAGE(__ident, __type, [__size])

# Assign the value of identifier __rhs to identifier __lhs
SET(__lhs, __rhs)

# Append a value __value to identifier __ident that contains or is equivalent to a sequence
APPEND(__ident, __value)

# Serialise message __message into the buffer __to_buffer of size __size using encoder __encoder_name
# --- Encoder must be defined in the UDF File.
ENCODE(__encoder_name, __to_buffer, __message, __size)

# Deserialise message __message into buffer __from_buffer using decoder __decoder_name
# --- Decoder must be defined in the UDF File 
DECODE(__decoder_name, __from_buffer, __message)
```

#### Control-Flow Actions

To provide finer control over the specification of control-flow operations.

Pyramis provides three keywords: `IF`, `ELSE`, `LOOP`

```Python
# Test condition __condition, where __condition is of the form `a` op `b`
# such that `a` and `b` are __conditions and op is a logical operator
#
# ELSE if specified follows the usual logical semantics.
IF(__condition[op __condition]*)... [ELSE]

# Initialise a loop counter identifier __counter to value __start, loop until its value is __end
LOOP(__counter, __start, __end)

<details>
<summary> <strong>Conterol-Flow Actions</strong></summary>
</details>

<details>
<summary> <strong>Special Actions</strong></summary>
</details>

### 📖 Components of a Pyramis Specification
<details>
<summary> <strong>The <code>EVENT</code> Abstraction</strong></summary>
 The Pyramis <code>EVENT</code> encapsulates processing actions that must occur on receipt of a message or on timer-expiry. Each relevant <code>EVENT</code>s must be defined in the processing file.
</details>
 
<details>
<summary> <strong>Interface file</strong></summary>
  The <strong>interface file</strong> is a json file that describes the architecture of your multi-tier system in terms of individual nodes and their <ins>interface descriptions</ins>.
  The interface file has a <a href="https://github.com/armaanchowfin/pyramis/blob/master/examples/login-system/interfaces.json">fixed format </a>, enforced by the compiler.
 
  - The definition of an interface contains several attributes required by Pyramis such as the <ins>port</ins> and the <ins>name of the <code>EVENT</code></ins> that should be invoked on receipt of a message on this interface

  Among other configuration options, it specifies peer nodes and protocols which are used by the compiler to validate the flow of message `SEND`s, and also help in the subsequent generation of the platform file.

</details>

<details>
<summary> <strong>Processing File</strong></summary>
 This file must contain every <code>EVENT</code> definition associated with the current node. 
 
 - In this file, written separately for each node in the system, the developer defines the procedural logic to process incoming messages at the node. 
 - The logic is defined in terms of Pyramis <code>EVENT</code>s that encapsulate <code>Action</code>s.
</details>

<details>
<summary> <strong>User-Defined Functions (UDF) File</strong></summary>
 These refer to a C++ source file udf.cpp and its corresponding header udf.h. 
 
 - The <ins><code>UDF</code> keyword</ins> allows a user to indicate a call to a custom, complex function that cannot be expressed by solely using Pyramis keywords.
 - The <ins><code>UDF</code></ins> is a repository for every <code>UDF</code> used by every node in the system.
</details>


### 📖 Requirements for compilation to executable NF

Pyramis keywords can flexibly represent key aspects of most multi-tier systems. However, to compile to a working implementation, certain constraints have to be imposed on the inputs and outputs.
  
<details>
<summary> <strong>Well-Defined L-7 protocol library</strong></summary>
  Pyramis supports multitier systems using the NGAP and HTTP L-7 protocols out of the box. However, custom application-layer protocol must meet certain requirements: 

- Valid messages for custom protocols must be implemented as complete C/C++ structs. These files may be stored in a `utils` directory in the your root folder.
- HTTP messages must represent and access their payload strings as attributes of nlohmann::json objects. We provide an HTTP library for this purpose.
- All char arrays are interpreted as C++ `std::vector<char>`. Strings, if any, must be null-terminated.
- Header-file library must be fully contained in a `/utils` directory.
</details>

<details>
<summary> <strong>Platform-file + Processing-file architecture</strong></summary>
  Where a platform file triggers kernel networking actions, and the processing file performs user-level message-processing actions

- In the current implementation, a C++ user-level processing file is generated from the Pyramis specification.
- In the current implementation, a multithreaded, asynchronous epoll-based platform.cpp file is generated that declares an entry point into the user-level processing code.
</details>

<details>
<summary> <strong>Notion of procedure key</strong></summary>
  The NF must generate a unique procedure key for each instance of procedure. Procedure may be simple (login request-response) or complex (SMF session-establishment). Complexity arises due to the requirement of demultiplexing messages received at a single interface to the correct message handler. The notion of "key" and its supporting `fd_to_key_map` and `key_to_fd_map` are implementation-specific constructs that enable this message demultiplexing.

- `procedure_key` is used by the NF application to maintain a synchronous message-processing flow despite asynchronous message ingress at an NF
- A single NF independently initiates procedure requests.
  </details>
