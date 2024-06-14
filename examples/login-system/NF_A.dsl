# EVENTs are list of Pyramis Actions.
# EVENT is rep via a python.Function object.
# Every Action has an "action". and set of user attributes with Python.Type().
# 
# Sometimes a type cannot be assigned to an identifier before the first visit to its
# enclosing action.
#  --- in this case, store ref to the attribute in untyped attr list stored in the Action.
#  --- Also store refs to all Actions that are yet untyped in the global/scope context.
#  --- while traversing the current scope, keep updating the symbol table.
#  --- At exit from the untyped scope, for each untyped attribute in each untyped EVENT,
#  --- look for the attribute in symtab, and assign a type to the Action if found.
#  --- if not found, raise an incomplete type error to errorlog.
# 
# only UDF, CREATE_MESSAGE, SET_KEY can assign concrete types to attributes.
# other actions (SET) must be checked for consistency with previously assigned types.
# --- SET can also be used to assign type :if the base attr of the lhs (lhs.split(.)[0])
# --- is in the symtab of current or ancestor scopes, and variable on rhs is untyped in
# --- scope, assign the type of rhs. (if char * make ?? <char> or string)
# - See get_variable etc. in infer.py
# 
# per-action processing is definitely needed in visit_Call()
#
# KEY INVARIANT: Single python.Variable object, "stored" in scope symtab. All other
# objects maintain references to the single instance and can update it at any time.
# called from platform file.

EVENT do_echo(message_body):
    ENCODE(SynerPMessageEncode, message_body_enc, message_body, message_body_enc_sz)
    SEND(message_body, <sendingNFInterface>, <peerNFname>, <peerNFInterface>, <callbackname>) # sendingNFInterface to generate protocol

EVENT server_entry(message): 
    DECODE(SynerPMessageDecode, m, message, m_enc_sz)
    SET(userCMD, m.header.cmd) 
    SET(userID, m.uname.contents) # contents is an array -> 

    IF (userCMD == MACRO(ECHO)):
        CALL(do_echo, m) # assert do_echo is not in untyped EVENTs. If it is, assign new type
    ELSE:
        IF(userCMD == MACRO(LOGIN_REQUEST)):
            UDF(procedure_key, generate_procedure_key)
            CALL(do_login, userID, procedure_key)

EVENT do_login(userID, procedure_key):    
    LOOKUP(login_status, user_login_map, userID, login_status) # search for key userID in vector. optional 4th argument if the value at key is a struct.
    IF(login_status):
        # args are timer identifiers.
        # stop timer s.t. name =arg1, associated with
        # userID ... etc. based on the timer context. 
        #TIMER_STOP(T_LOGIN_FORGET, userID) 
        
        CREATE_MESSAGE(simple, SynerPMessage_t)
        SET (simple.header.cmd, MACRO(LOGIN_RESPONSE))
        
        UDF(login_response, generate_login_response, MACRO(USER_EXIST))

        SET(simple.uname.contents, userID)
        SET(simple.uname.sz, userID.size())

        SET(simple.data.contents, login_response)
        SET(simple.data.sz, login_response.size())

        ENCODE(SynerPMessageEncode, simple_enc, simple, simple_enc_sz)
        SEND(simple_m, <sendingNFInterface>, <peerNFname>, <peerNFInterface>, <callbackname>) 

        #TIMER_START(T_LOGIN_FORGET, 5, forget_user)
        SET_KEY(procedure_key) # keytofdmap[proc_key] = sockfd
    ELSE:
        SET_KEY(procedure_key) # keytofdmap[proc_key] = sockfd
        STORE(user_login_map, userID, login_status, true) # Variable(login_status).type = type_of(arg[3])
        
        # ensure that the first arg to timer_start is a/the
        # NF procedure key. try check int, then try check gx.NF_KEY for arg1.
        # generic_timer_start(nfvInst, <timer args>)
        #TIMER_START(procedure_key, T_LOGIN_FORGET, 5, forget_user) # start the T_FORGET timer for user userID for 5 seconds.
        
        CREATE_MESSAGE(simple, SynerPMessage_t)
        SET(simple.header.cmd, MACRO(LOGIN_RESPONSE))
        
        UDF(login_response, generate_login_response, MACRO(USER_NEW))
        
        ENCODE(SynerPMessageEncode, simple_enc, simple, simple_enc_sz)

        SEND(simple_m, <sendingNFInterface>, <peerNFname>, <peerNFInterface>, <callbackname>)

#@@timer
#EVENT forget_user(user_id, timer_id): -> void forget_user(timer_expiry_struct_t timer_ctx, struct nfvInstanceData *nfvInst)
#    STORE(user_login_map, user_id, login_status, false) // get userID type
    
    # Send notification back to client.
#    CREATE_MESSAGE(SynerPMessage_t, simple)

#    SET (simple.header.cmd, MACRO(TIMER_NOTIFICATION))

#    UDF(timer_expiry_response, generate_timer_response, user_id, timer_id, USER_TIMER_EXPIRY) // get timer_id type
#    SET(simple.data.contents, timer_response)
#    SET(simple.data.sz, timer_response.size())

#    GET_KEY(procedure_key) # procedure_inst = fdtokeymap[sockfd]
#    ENCODE(SynerPMessageEncoder, simple_enc, simple, simple_enc_sz)
#    SEND(simple_m, <sendingNFInterface>, <peerNFname>, <peerNFInterface>, <callbackname>)

#    TIMER_STOP(T_LOGIN_FORGET, user_id) 

#@@timer
#EVENT misc_timer2(timer_ctx):
