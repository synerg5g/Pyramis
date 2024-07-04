### 📖 Components of a Pyramis Specification 
In the Pyramis workflow, three files are essential towards specifying your multitier system.

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

### 📌 Pyramis Syntax

The fundamental Pyramis abstraction is the `EVENT`. The Pyramis `EVENT` encapsulates processing actions that must occur on receipt of a message or on timer-expiry. 

```Python

# Define the event __event_name and specify its formal arguments __args.
EVENT(__event_name, [__args]*)
```
Each relevant `EVENT` must be defined in the processing file as a series of <ins><strong>Action</strong></ins>s.

- **Actions** are keywords that are used to specify various kinds of user-level message processing actions. They can be categorised into the following:

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

Pyramis provides five keywords: `CREATE_MESSAGE`, `SET`, `APPEND`, `ENCODE`, `DECODE`

```Python
# Create a message of type __type and assign it to identifier __ident
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
# ELSE, if specified, follows the usual logical semantics.
IF(__condition[op __condition]*)... [ELSE]

# Initialise a loop counter identifier __counter to value __start, loop until its value is __end
LOOP(__counter, __start, __end)

# Early exit/entry from/to a loop iteration.
BREAK
CONTINUE
```

#### Networking Actions

To specify fundamental networking operations

Pyramis provides three keywords: `GET_KEY`, `SET_KEY`, `SEND`

```Python
# Returns the procedure key of the ongoing procedure instance and
# store the value in __ident.
# procedure key is always mapped to the sending file descriptor
GET_KEY(__ident)

# Create a mapping between the sending file descriptor and the
# procedure key __key
SET_KEY(__key)

# Send the message in buffer __message_buffer via own interface __sending_interface to
# peer __peer_nf_name at its interface __receiving_interface.
#
# __callback, if specified, registers the event to be called on receipt of
# response to sending the message in __message_buffer from the peer.
# If not specified, implies that __message was a response to a previous request
#
# SEND must always follow an ENCODE
SEND(__message_buffer, __sending_interface, __peer_nf_name, __receiving_interface, [__callback])
```

#### Timer Actions
Pyramis allows a user to procedurally create, start and stop timers with arbitrary callbacks.
Timer callbacks are specified as regular `EVENT`s in the processing file.

Before starting a timer, the user must create a specific timer context that is linked to the callback associated with the newly created timer type.
- One callback event per timer type (specified in `interfaces.json`)
- One `procedure-key` per module.
- 
  
Thus a single procedure instance can have at most |timer_types| active timers (corresponding to the case where timers are created for each timer type.)

```Python
# Create a timer context struct containing attributes and values expected to be
# used by the timer callback event.
# 
# One timer context struct per __timer_type
CREATE_TIMER_CONTEXT(__id, __timer_type)

# Start a timer  of type __timer_type, for __timeout seconds which on expiry
# triggers the callback __callback
TIMER_START(__timer_type, __timeout, __expiry_context, __callback)

TIMER_STOP(__timer_type)
```

#### Special Actions

Pyramis provides three keywords: `UDF`, `CALL`, `MACRO` that perform specialised tasks.

```Python
# Call the custom C++ function udf_name, with the appropriate expected arguments __args
# Often __udf_name will refer to a function that is dependent on the L-7
# protocol libraries
UDF(__udf_name, [__args]*)

# Call `EVENT` __event_name, passing in the appropriate arguments __args.
CALL(__event_name, [__args]*)

# Specify the usage of a named constant __macro_name
# Often __macro_name will be exposed by the L-7 protocol libraries.
MACRO(__macro_name)
```
