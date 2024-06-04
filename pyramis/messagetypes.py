messageTypeContext = {
    "": {
        "": ("PFC_MASK_IPV6_LOCAL_ADDRESS_OR_PREFIX_LENGTH_TYPE)", False),
        "=": (
            "if ((this->pfcMask & "
            "PFC_MASK_IPV6_LOCAL_ADDRESS_OR_PREFIX_LENGTH_TYPE)",
            False,
        ),
        "FAILURE": ("return", False),
        'Set")': ('higLog("IPV6 FLAG Already', False),
        "_802_1q_ctag_pcp_dei": ("PCP_DEI_TAG_t", False),
        "_802_1q_ctag_vid": ("VID_TAG_t", False),
        "_802_1q_stag_pcp_dei": ("PCP_DEI_TAG_t", False),
        "_802_1q_stag_vid": ("VID_TAG_t", False),
        "destinationMac": ("uint8_t", True),
        "ethertype": ("uint8_t", True),
        "flowLabelType": ("FlowLabel_t", False),
        "localIpV4AddressType": ("Ipv4AddressType_t", False),
        "localIpV6AddressType": ("Ipv6AddressType_t", False),
        "localPortRange": ("PortRange_t", False),
        "pfcMask": ("uint32_t", False),
        "protocolIdentifier": ("uint8_t", False),
        "remoteIpV4AddressType": ("Ipv4AddressType_t", False),
        "remoteIpV6AddressType": ("Ipv6AddressType_t", False),
        "remotePortRange": ("PortRange_t", False),
        "securityParameterIndex": ("uint32_t", False),
        "singleLocalPort": ("uint16_t", False),
        "singleRemotePort": ("uint16_t", False),
        "sourceMac": ("uint8_t", True),
        "typeOfService_TrafficClass": ("TOS_TC_t", False),
    },
    "1": ("JSON", False),
    "5gAuthData": ("JSON", False),
    "5gQosProfile": ("JSON", False),
    "5gTMSI-number": ("int", False),
    "5gTMSI-start": ("int", False),
    "5qi": ("int", False),
    "ABBA_t": {"contents": ("uint8_t", True), "len": ("uint8_t", False)},
    "AMFConfigurationUpdateAcknowledgeIEs__value_PR_AMF_TNLAssociationSetupList": (
        "AMFConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "AMFConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateAcknowledgeIEs__value_PR_NOTHING": (
        "AMFConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateAcknowledgeIEs__value_PR_TNLAssociationList": (
        "AMFConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateAcknowledgeIEs__value_u": {
        "AMF_TNLAssociationSetupList": ("AMF_TNLAssociationSetupList_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "TNLAssociationList": ("TNLAssociationList_t", False),
    },
    "AMFConfigurationUpdateAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "AMFConfigurationUpdateAcknowledgeIEs__value", False),
    },
    "AMFConfigurationUpdateAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P48_t", False),
    },
    "AMFConfigurationUpdateFailureIEs__value_PR_Cause": (
        "AMFConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateFailureIEs__value_PR_CriticalityDiagnostics": (
        "AMFConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateFailureIEs__value_PR_NOTHING": (
        "AMFConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateFailureIEs__value_PR_TimeToWait": (
        "AMFConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateFailureIEs__value_u": {
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "TimeToWait": ("TimeToWait_t", False),
    },
    "AMFConfigurationUpdateFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "AMFConfigurationUpdateFailureIEs__value", False),
    },
    "AMFConfigurationUpdateFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P49_t", False),
    },
    "AMFConfigurationUpdateIEs__value_PR_AMFName": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_AMF_TNLAssociationToAddList": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_AMF_TNLAssociationToRemoveList": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_AMF_TNLAssociationToUpdateList": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_NOTHING": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_PLMNSupportList": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_RelativeAMFCapacity": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_PR_ServedGUAMIList": (
        "AMFConfigurationUpdateIEs__value_PR",
        False,
    ),
    "AMFConfigurationUpdateIEs__value_u": {
        "AMFName": ("AMFName_t", False),
        "AMF_TNLAssociationToAddList": ("AMF_TNLAssociationToAddList_t", False),
        "AMF_TNLAssociationToRemoveList": ("AMF_TNLAssociationToRemoveList_t", False),
        "AMF_TNLAssociationToUpdateList": ("AMF_TNLAssociationToUpdateList_t", False),
        "PLMNSupportList": ("PLMNSupportList_t", False),
        "RelativeAMFCapacity": ("RelativeAMFCapacity_t", False),
        "ServedGUAMIList": ("ServedGUAMIList_t", False),
    },
    "AMFConfigurationUpdateIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "AMFConfigurationUpdateIEs__value", False),
    },
    "AMFConfigurationUpdate_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P47_t", False),
    },
    "AMFName": ("string", False),
    "AMFName_t": ("PrintableString_t", False),
    "AMFPagingTarget_ExtIEs__value_PR_NOTHING": (
        "AMFPagingTarget_ExtIEs__value_PR",
        False,
    ),
    "AMFPagingTarget_ExtIEs__value_u": {},
    "AMFPagingTarget_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct AMFPagingTarget_ExtIEs__value", False),
    },
    "AMFPagingTarget_PR_NOTHING": ("AMFPagingTarget_PR", False),
    "AMFPagingTarget_PR_choice_Extensions": ("AMFPagingTarget_PR", False),
    "AMFPagingTarget_PR_globalRANNodeID": ("AMFPagingTarget_PR", False),
    "AMFPagingTarget_PR_tAI": ("AMFPagingTarget_PR", False),
    "AMFPagingTarget_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFPagingTarget_u", False),
        "present": ("AMFPagingTarget_PR", False),
    },
    "AMFPagingTarget_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "globalRANNodeID": ("struct GlobalRANNodeID", True),
        "tAI": ("struct TAI", True),
    },
    "AMFPointer_t": ("BIT_STRING_t", False),
    "AMFRegionID_t": ("BIT_STRING_t", False),
    "AMFSetID_t": ("BIT_STRING_t", False),
    "AMFStatusIndicationIEs__value_PR_NOTHING": (
        "AMFStatusIndicationIEs__value_PR",
        False,
    ),
    "AMFStatusIndicationIEs__value_PR_UnavailableGUAMIList": (
        "AMFStatusIndicationIEs__value_PR",
        False,
    ),
    "AMFStatusIndicationIEs__value_u": {
        "UnavailableGUAMIList": ("UnavailableGUAMIList_t", False)
    },
    "AMFStatusIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct AMFStatusIndicationIEs__value", False),
    },
    "AMFStatusIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P50_t", False),
    },
    "AMF_TNLAssociationSetupItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AMF_TNLAssociationSetupItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AMF_TNLAssociationSetupItem_ExtIEs__extensionValue_u": {},
    "AMF_TNLAssociationSetupItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AMF_TNLAssociationSetupItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AMF_TNLAssociationSetupItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_TNLAssociationAddress": ("CPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "AMF_TNLAssociationSetupList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationSetupItem)", False),
    },
    "AMF_TNLAssociationToAddItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AMF_TNLAssociationToAddItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AMF_TNLAssociationToAddItem_ExtIEs__extensionValue_u": {},
    "AMF_TNLAssociationToAddItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AMF_TNLAssociationToAddItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AMF_TNLAssociationToAddItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_TNLAssociationAddress": ("CPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tNLAddressWeightFactor": ("TNLAddressWeightFactor_t", False),
        "tNLAssociationUsage": ("TNLAssociationUsage_t", True),
    },
    "AMF_TNLAssociationToAddList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationToAddItem)", False),
    },
    "AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue_u": {},
    "AMF_TNLAssociationToRemoveItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AMF_TNLAssociationToRemoveItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_TNLAssociationAddress": ("CPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "AMF_TNLAssociationToRemoveList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationToRemoveItem)", False),
    },
    "AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue_u": {},
    "AMF_TNLAssociationToUpdateItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AMF_TNLAssociationToUpdateItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_TNLAssociationAddress": ("CPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tNLAddressWeightFactor": ("TNLAddressWeightFactor_t", True),
        "tNLAssociationUsage": ("TNLAssociationUsage_t", True),
    },
    "AMF_TNLAssociationToUpdateList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationToUpdateItem)", False),
    },
    "AMF_UE_NGAP_ID_t": ("INTEGER_t", False),
    "ANY_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "buf": ("uint8_t", True),
        "size": ("int", False),
    },
    "AUTN_t": {"AUTN": ("uint8_t", True), "len": ("uint8_t", False)},
    "AdditionalQosFlowInformation_more_likely": (
        "e_AdditionalQosFlowInformation",
        False,
    ),
    "AdditionalQosFlowInformation_t": ("long", False),
    "AllocationAndRetentionPriority_ExtIEs__extensionValue_PR_NOTHING": (
        "AllocationAndRetentionPriority_ExtIEs__extensionValue_PR",
        False,
    ),
    "AllocationAndRetentionPriority_ExtIEs__extensionValue_u": {},
    "AllocationAndRetentionPriority_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AllocationAndRetentionPriority_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AllocationAndRetentionPriority_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pre_emptionCapability": ("Pre_emptionCapability_t", False),
        "pre_emptionVulnerability": ("Pre_emptionVulnerability_t", False),
        "priorityLevelARP": ("PriorityLevelARP_t", False),
    },
    "AllowedNSSAI_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "AllowedNSSAI_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "AllowedNSSAI_Item_ExtIEs__extensionValue_u": {},
    "AllowedNSSAI_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "AllowedNSSAI_Item_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AllowedNSSAI_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "AllowedNSSAI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct AllowedNSSAI_Item)", False),
    },
    "AllowedTACs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(TAC_t)", False),
    },
    "AlwaysOnPduSessionIndication_t": {
        "apsi": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "AlwaysOnPduSessionRequested_t": {
        "apsr": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "AmfUeNgapId_t": ("unsigned long", False),
    "AreaOfInterestCellItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AreaOfInterestCellItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AreaOfInterestCellItem_ExtIEs__extensionValue_u": {},
    "AreaOfInterestCellItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AreaOfInterestCellItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AreaOfInterestCellItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nGRAN_CGI": ("NGRAN_CGI_t", False),
    },
    "AreaOfInterestCellList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestCellItem)", False),
    },
    "AreaOfInterestItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AreaOfInterestItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AreaOfInterestItem_ExtIEs__extensionValue_u": {},
    "AreaOfInterestItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AreaOfInterestItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AreaOfInterestItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "areaOfInterest": ("AreaOfInterest_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "locationReportingReferenceID": ("LocationReportingReferenceID_t", False),
    },
    "AreaOfInterestList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct AreaOfInterestItem)", False),
    },
    "AreaOfInterestRANNodeItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AreaOfInterestRANNodeItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AreaOfInterestRANNodeItem_ExtIEs__extensionValue_u": {},
    "AreaOfInterestRANNodeItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AreaOfInterestRANNodeItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AreaOfInterestRANNodeItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "globalRANNodeID": ("GlobalRANNodeID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "AreaOfInterestRANNodeList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestRANNodeItem)", False),
    },
    "AreaOfInterestTAIItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AreaOfInterestTAIItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AreaOfInterestTAIItem_ExtIEs__extensionValue_u": {},
    "AreaOfInterestTAIItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AreaOfInterestTAIItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AreaOfInterestTAIItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "AreaOfInterestTAIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestTAIItem)", False),
    },
    "AreaOfInterest_ExtIEs__extensionValue_PR_NOTHING": (
        "AreaOfInterest_ExtIEs__extensionValue_PR",
        False,
    ),
    "AreaOfInterest_ExtIEs__extensionValue_u": {},
    "AreaOfInterest_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "AreaOfInterest_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AreaOfInterest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "areaOfInterestCellList": ("struct " "AreaOfInterestCellList", True),
        "areaOfInterestRANNodeList": ("struct " "AreaOfInterestRANNodeList", True),
        "areaOfInterestTAIList": ("struct AreaOfInterestTAIList", True),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
    },
    "AssistanceDataForPaging_ExtIEs__extensionValue_PR_NOTHING": (
        "AssistanceDataForPaging_ExtIEs__extensionValue_PR",
        False,
    ),
    "AssistanceDataForPaging_ExtIEs__extensionValue_u": {},
    "AssistanceDataForPaging_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AssistanceDataForPaging_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AssistanceDataForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "assistanceDataForRecommendedCells": (
            "struct " "AssistanceDataForRecommendedCells",
            True,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pagingAttemptInformation": ("struct " "PagingAttemptInformation", True),
    },
    "AssistanceDataForRecommendedCells_ExtIEs__extensionValue_PR_NOTHING": (
        "AssistanceDataForRecommendedCells_ExtIEs__extensionValue_PR",
        False,
    ),
    "AssistanceDataForRecommendedCells_ExtIEs__extensionValue_u": {},
    "AssistanceDataForRecommendedCells_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AssistanceDataForRecommendedCells_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AssistanceDataForRecommendedCells_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "recommendedCellsForPaging": ("RecommendedCellsForPaging_t", False),
    },
    "AssociatedQosFlowItem_ExtIEs__extensionValue_PR_NOTHING": (
        "AssociatedQosFlowItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "AssociatedQosFlowItem_ExtIEs__extensionValue_u": {},
    "AssociatedQosFlowItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "AssociatedQosFlowItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "AssociatedQosFlowItem__qosFlowMappingIndication_dl": (
        "e_AssociatedQosFlowItem__qosFlowMappingIndication",
        False,
    ),
    "AssociatedQosFlowItem__qosFlowMappingIndication_ul": (
        "e_AssociatedQosFlowItem__qosFlowMappingIndication",
        False,
    ),
    "AssociatedQosFlowItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
        "qosFlowMappingIndication": ("long", True),
    },
    "AssociatedQosFlowList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AssociatedQosFlowItem)", False),
    },
    "AuthFailParameter_t": {"AUTS": ("uint8_t", True), "afpLen": ("uint8_t", False)},
    "AuthRespParameter_t": {"RESstar": ("uint8_t", True), "arpLen": ("uint8_t", False)},
    "AuthenticationFailureMsg_t": {
        "_5gmmCause": ("uint8_t", False),
        "authFailParam": ("AuthFailParameter_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "presenceMask": ("uint32_t", False),
    },
    "AuthenticationRejectMsg_t": {"mmHeader": ("_5gmmMsgHeader_t", False)},
    "AuthenticationRequestMsg_t": {
        "abba": ("ABBA_t", False),
        "autn": ("AUTN_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "ngKsi": ("NaskeysetId_t", False),
        "presenceMask": ("uint32_t", False),
        "rand": ("RAND_t", False),
    },
    "AuthenticationResponseMsg_t": {
        "authRespParam": ("AuthRespParameter_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "presenceMask": ("uint32_t", False),
    },
    "AveragingWindow_t": ("long", False),
    "BIT_STRING_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "bits_unused": ("int", False),
        "buf": ("uint8_t", True),
        "size": ("size_t", False),
    },
    "BitRate_t": ("INTEGER_t", False),
    "BroadcastCancelledAreaList_ExtIEs__value_PR_NOTHING": (
        "BroadcastCancelledAreaList_ExtIEs__value_PR",
        False,
    ),
    "BroadcastCancelledAreaList_ExtIEs__value_u": {},
    "BroadcastCancelledAreaList_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "BroadcastCancelledAreaList_ExtIEs__value", False),
    },
    "BroadcastCancelledAreaList_PR_NOTHING": ("BroadcastCancelledAreaList_PR", False),
    "BroadcastCancelledAreaList_PR_cellIDCancelledEUTRA": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_cellIDCancelledNR": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_choice_Extensions": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_emergencyAreaIDCancelledEUTRA": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_emergencyAreaIDCancelledNR": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_tAICancelledEUTRA": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_PR_tAICancelledNR": (
        "BroadcastCancelledAreaList_PR",
        False,
    ),
    "BroadcastCancelledAreaList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("BroadcastCancelledAreaList_u", False),
        "present": ("BroadcastCancelledAreaList_PR", False),
    },
    "BroadcastCancelledAreaList_u": {
        "cellIDCancelledEUTRA": ("struct " "CellIDCancelledEUTRA", True),
        "cellIDCancelledNR": ("struct " "CellIDCancelledNR", True),
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "emergencyAreaIDCancelledEUTRA": (
            "struct " "EmergencyAreaIDCancelledEUTRA",
            True,
        ),
        "emergencyAreaIDCancelledNR": ("struct " "EmergencyAreaIDCancelledNR", True),
        "tAICancelledEUTRA": ("struct " "TAICancelledEUTRA", True),
        "tAICancelledNR": ("struct TAICancelledNR", True),
    },
    "BroadcastCompletedAreaList_ExtIEs__value_PR_NOTHING": (
        "BroadcastCompletedAreaList_ExtIEs__value_PR",
        False,
    ),
    "BroadcastCompletedAreaList_ExtIEs__value_u": {},
    "BroadcastCompletedAreaList_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "BroadcastCompletedAreaList_ExtIEs__value", False),
    },
    "BroadcastCompletedAreaList_PR_NOTHING": ("BroadcastCompletedAreaList_PR", False),
    "BroadcastCompletedAreaList_PR_cellIDBroadcastEUTRA": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_cellIDBroadcastNR": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_choice_Extensions": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_emergencyAreaIDBroadcastEUTRA": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_emergencyAreaIDBroadcastNR": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_tAIBroadcastEUTRA": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_PR_tAIBroadcastNR": (
        "BroadcastCompletedAreaList_PR",
        False,
    ),
    "BroadcastCompletedAreaList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("BroadcastCompletedAreaList_u", False),
        "present": ("BroadcastCompletedAreaList_PR", False),
    },
    "BroadcastCompletedAreaList_u": {
        "cellIDBroadcastEUTRA": ("struct " "CellIDBroadcastEUTRA", True),
        "cellIDBroadcastNR": ("struct " "CellIDBroadcastNR", True),
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "emergencyAreaIDBroadcastEUTRA": (
            "struct " "EmergencyAreaIDBroadcastEUTRA",
            True,
        ),
        "emergencyAreaIDBroadcastNR": ("struct " "EmergencyAreaIDBroadcastNR", True),
        "tAIBroadcastEUTRA": ("struct " "TAIBroadcastEUTRA", True),
        "tAIBroadcastNR": ("struct TAIBroadcastNR", True),
    },
    "BroadcastPLMNItem_ExtIEs__extensionValue_PR_NOTHING": (
        "BroadcastPLMNItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "BroadcastPLMNItem_ExtIEs__extensionValue_u": {},
    "BroadcastPLMNItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "BroadcastPLMNItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "BroadcastPLMNItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
        "tAISliceSupportList": ("SliceSupportList_t", False),
    },
    "BroadcastPLMNList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct BroadcastPLMNItem)", False),
    },
    "COUNTValueForPDCP_SN12_ExtIEs__extensionValue_PR_NOTHING": (
        "COUNTValueForPDCP_SN12_ExtIEs__extensionValue_PR",
        False,
    ),
    "COUNTValueForPDCP_SN12_ExtIEs__extensionValue_u": {},
    "COUNTValueForPDCP_SN12_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "COUNTValueForPDCP_SN12_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "COUNTValueForPDCP_SN12_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "hFN_PDCP_SN12": ("long", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDCP_SN12": ("long", False),
    },
    "COUNTValueForPDCP_SN18_ExtIEs__extensionValue_PR_NOTHING": (
        "COUNTValueForPDCP_SN18_ExtIEs__extensionValue_PR",
        False,
    ),
    "COUNTValueForPDCP_SN18_ExtIEs__extensionValue_u": {},
    "COUNTValueForPDCP_SN18_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "COUNTValueForPDCP_SN18_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "COUNTValueForPDCP_SN18_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "hFN_PDCP_SN18": ("long", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDCP_SN18": ("long", False),
    },
    "CPTransportLayerInformation_ExtIEs__value_PR_NOTHING": (
        "CPTransportLayerInformation_ExtIEs__value_PR",
        False,
    ),
    "CPTransportLayerInformation_ExtIEs__value_u": {},
    "CPTransportLayerInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "CPTransportLayerInformation_ExtIEs__value", False),
    },
    "CPTransportLayerInformation_PR_NOTHING": ("CPTransportLayerInformation_PR", False),
    "CPTransportLayerInformation_PR_choice_Extensions": (
        "CPTransportLayerInformation_PR",
        False,
    ),
    "CPTransportLayerInformation_PR_endpointIPAddress": (
        "CPTransportLayerInformation_PR",
        False,
    ),
    "CPTransportLayerInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CPTransportLayerInformation_u", False),
        "present": ("CPTransportLayerInformation_PR", False),
    },
    "CPTransportLayerInformation_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "endpointIPAddress": ("TransportLayerAddress_t", False),
    },
    "CancelAllWarningMessages_t": ("long", False),
    "CancelAllWarningMessages_true": ("e_CancelAllWarningMessages", False),
    "CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_u": {},
    "CancelledCellsInEAI_EUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CancelledCellsInEAI_EUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CancelledCellsInEAI_EUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInEAI_EUTRA_Item)", False),
    },
    "CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue_u": {},
    "CancelledCellsInEAI_NR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CancelledCellsInEAI_NR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CancelledCellsInEAI_NR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInEAI_NR_Item)", False),
    },
    "CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_u": {},
    "CancelledCellsInTAI_EUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CancelledCellsInTAI_EUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CancelledCellsInTAI_EUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInTAI_EUTRA_Item)", False),
    },
    "CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue_u": {},
    "CancelledCellsInTAI_NR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CancelledCellsInTAI_NR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CancelledCellsInTAI_NR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInTAI_NR_Item)", False),
    },
    "CauseMisc_control_processing_overload": ("e_CauseMisc", False),
    "CauseMisc_hardware_failure": ("e_CauseMisc", False),
    "CauseMisc_not_enough_user_plane_processing_resources": ("e_CauseMisc", False),
    "CauseMisc_om_intervention": ("e_CauseMisc", False),
    "CauseMisc_t": ("long", False),
    "CauseMisc_unknown_PLMN": ("e_CauseMisc", False),
    "CauseMisc_unspecified": ("e_CauseMisc", False),
    "CauseNas_authentication_failure": ("e_CauseNas", False),
    "CauseNas_deregister": ("e_CauseNas", False),
    "CauseNas_normal_release": ("e_CauseNas", False),
    "CauseNas_t": ("long", False),
    "CauseNas_unspecified": ("e_CauseNas", False),
    "CauseProtocol_abstract_syntax_error_falsely_constructed_message": (
        "e_CauseProtocol",
        False,
    ),
    "CauseProtocol_abstract_syntax_error_ignore_and_notify": ("e_CauseProtocol", False),
    "CauseProtocol_abstract_syntax_error_reject": ("e_CauseProtocol", False),
    "CauseProtocol_message_not_compatible_with_receiver_state": (
        "e_CauseProtocol",
        False,
    ),
    "CauseProtocol_semantic_error": ("e_CauseProtocol", False),
    "CauseProtocol_t": ("long", False),
    "CauseProtocol_transfer_syntax_error": ("e_CauseProtocol", False),
    "CauseProtocol_unspecified": ("e_CauseProtocol", False),
    "CauseRadioNetwork_cell_not_available": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_encryption_and_or_integrity_protection_algorithms_not_supported": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_failure_in_radio_interface_procedure": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_handover_cancelled": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_handover_desirable_for_radio_reason": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_ho_failure_in_target_5GC_ngran_node_or_target_system": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_ho_target_not_allowed": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_ims_voice_eps_fallback_or_rat_fallback_triggered": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_inconsistent_remote_UE_NGAP_ID": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_interaction_with_other_procedure": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_invalid_qos_combination": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_multiple_PDU_session_ID_instances": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_multiple_qos_flow_ID_instances": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_ng_inter_system_handover_triggered": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_ng_intra_system_handover_triggered": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_no_radio_resources_available_in_target_cell": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_not_supported_5QI_value": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_partial_handover": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_radio_connection_with_ue_lost": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_radio_resources_not_available": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_redirection": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_reduce_load_in_serving_cell": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_release_due_to_5gc_generated_reason": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_release_due_to_cn_detected_mobility": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_release_due_to_ngran_generated_reason": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_resource_optimisation_handover": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_resources_not_available_for_the_slice": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_slice_not_supported": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_successful_handover": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_t": ("long", False),
    "CauseRadioNetwork_time_critical_handover": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_tngrelocoverall_expiry": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_tngrelocprep_expiry": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_txnrelocoverall_expiry": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_ue_context_transfer": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_ue_in_rrc_inactive_state_not_reachable": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_ue_max_integrity_protected_data_rate_reason": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_unknown_PDU_session_ID": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_unknown_local_UE_NGAP_ID": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_unknown_targetID": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_unkown_qos_flow_ID": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_unspecified": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_up_confidentiality_protection_not_possible": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_up_integrity_protection_not_possible": (
        "e_CauseRadioNetwork",
        False,
    ),
    "CauseRadioNetwork_user_inactivity": ("e_CauseRadioNetwork", False),
    "CauseRadioNetwork_xn_handover_triggered": ("e_CauseRadioNetwork", False),
    "CauseTransport_t": ("long", False),
    "CauseTransport_transport_resource_unavailable": ("e_CauseTransport", False),
    "CauseTransport_unspecified": ("e_CauseTransport", False),
    "Cause_ExtIEs__value_PR_NOTHING": ("Cause_ExtIEs__value_PR", False),
    "Cause_ExtIEs__value_u": {},
    "Cause_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct Cause_ExtIEs__value", False),
    },
    "Cause_PR_NOTHING": ("Cause_PR", False),
    "Cause_PR_choice_Extensions": ("Cause_PR", False),
    "Cause_PR_misc": ("Cause_PR", False),
    "Cause_PR_nas": ("Cause_PR", False),
    "Cause_PR_protocol": ("Cause_PR", False),
    "Cause_PR_radioNetwork": ("Cause_PR", False),
    "Cause_PR_transport": ("Cause_PR", False),
    "Cause_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("Cause_u", False),
        "present": ("Cause_PR", False),
    },
    "Cause_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "misc": ("CauseMisc_t", False),
        "nas": ("CauseNas_t", False),
        "protocol": ("CauseProtocol_t", False),
        "radioNetwork": ("CauseRadioNetwork_t", False),
        "transport": ("CauseTransport_t", False),
    },
    "CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue_u": {},
    "CellIDBroadcastEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CellIDBroadcastEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "CellIDBroadcastEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDBroadcastEUTRA_Item)", False),
    },
    "CellIDBroadcastNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CellIDBroadcastNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CellIDBroadcastNR_Item_ExtIEs__extensionValue_u": {},
    "CellIDBroadcastNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CellIDBroadcastNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CellIDBroadcastNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
    },
    "CellIDBroadcastNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDBroadcastNR_Item)", False),
    },
    "CellIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CellIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CellIDCancelledEUTRA_Item_ExtIEs__extensionValue_u": {},
    "CellIDCancelledEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CellIDCancelledEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CellIDCancelledEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CellIDCancelledEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDCancelledEUTRA_Item)", False),
    },
    "CellIDCancelledNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CellIDCancelledNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CellIDCancelledNR_Item_ExtIEs__extensionValue_u": {},
    "CellIDCancelledNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CellIDCancelledNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CellIDCancelledNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
        "numberOfBroadcasts": ("NumberOfBroadcasts_t", False),
    },
    "CellIDCancelledNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDCancelledNR_Item)", False),
    },
    "CellIDListForRestart_ExtIEs__value_PR_NOTHING": (
        "CellIDListForRestart_ExtIEs__value_PR",
        False,
    ),
    "CellIDListForRestart_ExtIEs__value_u": {},
    "CellIDListForRestart_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "CellIDListForRestart_ExtIEs__value", False),
    },
    "CellIDListForRestart_PR_NOTHING": ("CellIDListForRestart_PR", False),
    "CellIDListForRestart_PR_choice_Extensions": ("CellIDListForRestart_PR", False),
    "CellIDListForRestart_PR_eUTRA_CGIListforRestart": (
        "CellIDListForRestart_PR",
        False,
    ),
    "CellIDListForRestart_PR_nR_CGIListforRestart": ("CellIDListForRestart_PR", False),
    "CellIDListForRestart_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDListForRestart_u", False),
        "present": ("CellIDListForRestart_PR", False),
    },
    "CellIDListForRestart_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "eUTRA_CGIListforRestart": ("struct EUTRA_CGIList", True),
        "nR_CGIListforRestart": ("struct NR_CGIList", True),
    },
    "CellSize_large": ("e_CellSize", False),
    "CellSize_medium": ("e_CellSize", False),
    "CellSize_small": ("e_CellSize", False),
    "CellSize_t": ("long", False),
    "CellSize_verysmall": ("e_CellSize", False),
    "CellTrafficTraceIEs__value_PR_AMF_UE_NGAP_ID": (
        "CellTrafficTraceIEs__value_PR",
        False,
    ),
    "CellTrafficTraceIEs__value_PR_NGRANTraceID": (
        "CellTrafficTraceIEs__value_PR",
        False,
    ),
    "CellTrafficTraceIEs__value_PR_NGRAN_CGI": ("CellTrafficTraceIEs__value_PR", False),
    "CellTrafficTraceIEs__value_PR_NOTHING": ("CellTrafficTraceIEs__value_PR", False),
    "CellTrafficTraceIEs__value_PR_RAN_UE_NGAP_ID": (
        "CellTrafficTraceIEs__value_PR",
        False,
    ),
    "CellTrafficTraceIEs__value_PR_TransportLayerAddress": (
        "CellTrafficTraceIEs__value_PR",
        False,
    ),
    "CellTrafficTraceIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NGRANTraceID": ("NGRANTraceID_t", False),
        "NGRAN_CGI": ("NGRAN_CGI_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "TransportLayerAddress": ("TransportLayerAddress_t", False),
    },
    "CellTrafficTraceIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct CellTrafficTraceIEs__value", False),
    },
    "CellTrafficTrace_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P71_t", False),
    },
    "CellType_ExtIEs__extensionValue_PR_NOTHING": (
        "CellType_ExtIEs__extensionValue_PR",
        False,
    ),
    "CellType_ExtIEs__extensionValue_u": {},
    "CellType_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "CellType_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CellType_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cellSize": ("CellSize_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
    },
    "CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_u": {},
    "CompletedCellsInEAI_EUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CompletedCellsInEAI_EUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "CompletedCellsInEAI_EUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInEAI_EUTRA_Item)", False),
    },
    "CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue_u": {},
    "CompletedCellsInEAI_NR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CompletedCellsInEAI_NR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
    },
    "CompletedCellsInEAI_NR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInEAI_NR_Item)", False),
    },
    "CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_u": {},
    "CompletedCellsInTAI_EUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CompletedCellsInTAI_EUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "CompletedCellsInTAI_EUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInTAI_EUTRA_Item)", False),
    },
    "CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue_u": {},
    "CompletedCellsInTAI_NR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CompletedCellsInTAI_NR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
    },
    "CompletedCellsInTAI_NR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInTAI_NR_Item)", False),
    },
    "ConcurrentWarningMessageInd_t": ("long", False),
    "ConcurrentWarningMessageInd_true": ("e_ConcurrentWarningMessageInd", False),
    "ConfidentialityProtectionIndication_not_needed": (
        "e_ConfidentialityProtectionIndication",
        False,
    ),
    "ConfidentialityProtectionIndication_preferred": (
        "e_ConfidentialityProtectionIndication",
        False,
    ),
    "ConfidentialityProtectionIndication_required": (
        "e_ConfidentialityProtectionIndication",
        False,
    ),
    "ConfidentialityProtectionIndication_t": ("long", False),
    "ConfidentialityProtectionResult_not_performed": (
        "e_ConfidentialityProtectionResult",
        False,
    ),
    "ConfidentialityProtectionResult_performed": (
        "e_ConfidentialityProtectionResult",
        False,
    ),
    "ConfidentialityProtectionResult_t": ("long", False),
    "CoreNetworkAssistanceInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "CoreNetworkAssistanceInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "CoreNetworkAssistanceInformation_ExtIEs__extensionValue_u": {},
    "CoreNetworkAssistanceInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CoreNetworkAssistanceInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CoreNetworkAssistanceInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "expectedUEBehaviour": ("struct " "ExpectedUEBehaviour", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "mICOModeIndication": ("MICOModeIndication_t", True),
        "periodicRegistrationUpdateTimer": ("PeriodicRegistrationUpdateTimer_t", False),
        "tAIListForInactive": ("TAIListForInactive_t", False),
        "uEIdentityIndexValue": ("UEIdentityIndexValue_t", False),
        "uESpecificDRX": ("PagingDRX_t", True),
    },
    "CriticalityDiagnostics_ExtIEs__extensionValue_PR_NOTHING": (
        "CriticalityDiagnostics_ExtIEs__extensionValue_PR",
        False,
    ),
    "CriticalityDiagnostics_ExtIEs__extensionValue_u": {},
    "CriticalityDiagnostics_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CriticalityDiagnostics_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue_u": {},
    "CriticalityDiagnostics_IE_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "CriticalityDiagnostics_IE_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iECriticality": ("Criticality_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "iE_ID": ("ProtocolIE_ID_t", False),
        "typeOfError": ("TypeOfError_t", False),
    },
    "CriticalityDiagnostics_IE_List_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CriticalityDiagnostics_IE_Item)", False),
    },
    "CriticalityDiagnostics_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "iEsCriticalityDiagnostics": ("struct " "CriticalityDiagnostics_IE_List", True),
        "procedureCode": ("ProcedureCode_t", True),
        "procedureCriticality": ("Criticality_t", True),
        "triggeringMessage": ("TriggeringMessage_t", True),
    },
    "Criticality_ignore": ("e_Criticality", False),
    "Criticality_notify": ("e_Criticality", False),
    "Criticality_reject": ("e_Criticality", False),
    "Criticality_t": ("long", False),
    "DLForwarding_dl_forwarding_proposed": ("e_DLForwarding", False),
    "DLForwarding_t": ("long", False),
    "DL_NGU_TNLInformationReused_t": ("long", False),
    "DL_NGU_TNLInformationReused_true": ("e_DL_NGU_TNLInformationReused", False),
    "DNN_t": {"len": ("uint8_t", False), "value": ("uint8_t", True)},
    "DRBStatusDL12_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBStatusDL12_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBStatusDL12_ExtIEs__extensionValue_u": {},
    "DRBStatusDL12_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "DRBStatusDL12_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBStatusDL12_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_COUNTValue": ("COUNTValueForPDCP_SN12_t", False),
        "iE_Extension": ("struct ProtocolExtensionContainer", True),
    },
    "DRBStatusDL18_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBStatusDL18_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBStatusDL18_ExtIEs__extensionValue_u": {},
    "DRBStatusDL18_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "DRBStatusDL18_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBStatusDL18_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_COUNTValue": ("COUNTValueForPDCP_SN18_t", False),
        "iE_Extension": ("struct ProtocolExtensionContainer", True),
    },
    "DRBStatusDL_ExtIEs__value_PR_NOTHING": ("DRBStatusDL_ExtIEs__value_PR", False),
    "DRBStatusDL_ExtIEs__value_u": {},
    "DRBStatusDL_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct DRBStatusDL_ExtIEs__value", False),
    },
    "DRBStatusDL_PR_NOTHING": ("DRBStatusDL_PR", False),
    "DRBStatusDL_PR_choice_Extensions": ("DRBStatusDL_PR", False),
    "DRBStatusDL_PR_dRBStatusDL12": ("DRBStatusDL_PR", False),
    "DRBStatusDL_PR_dRBStatusDL18": ("DRBStatusDL_PR", False),
    "DRBStatusDL_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusDL_u", False),
        "present": ("DRBStatusDL_PR", False),
    },
    "DRBStatusDL_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "dRBStatusDL12": ("struct DRBStatusDL12", True),
        "dRBStatusDL18": ("struct DRBStatusDL18", True),
    },
    "DRBStatusUL12_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBStatusUL12_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBStatusUL12_ExtIEs__extensionValue_u": {},
    "DRBStatusUL12_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "DRBStatusUL12_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBStatusUL12_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extension": ("struct ProtocolExtensionContainer", True),
        "receiveStatusOfUL_PDCP_SDUs": ("BIT_STRING_t", True),
        "uL_COUNTValue": ("COUNTValueForPDCP_SN12_t", False),
    },
    "DRBStatusUL18_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBStatusUL18_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBStatusUL18_ExtIEs__extensionValue_u": {},
    "DRBStatusUL18_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "DRBStatusUL18_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBStatusUL18_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extension": ("struct ProtocolExtensionContainer", True),
        "receiveStatusOfUL_PDCP_SDUs": ("BIT_STRING_t", True),
        "uL_COUNTValue": ("COUNTValueForPDCP_SN18_t", False),
    },
    "DRBStatusUL_ExtIEs__value_PR_NOTHING": ("DRBStatusUL_ExtIEs__value_PR", False),
    "DRBStatusUL_ExtIEs__value_u": {},
    "DRBStatusUL_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct DRBStatusUL_ExtIEs__value", False),
    },
    "DRBStatusUL_PR_NOTHING": ("DRBStatusUL_PR", False),
    "DRBStatusUL_PR_choice_Extensions": ("DRBStatusUL_PR", False),
    "DRBStatusUL_PR_dRBStatusUL12": ("DRBStatusUL_PR", False),
    "DRBStatusUL_PR_dRBStatusUL18": ("DRBStatusUL_PR", False),
    "DRBStatusUL_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusUL_u", False),
        "present": ("DRBStatusUL_PR", False),
    },
    "DRBStatusUL_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "dRBStatusUL12": ("struct DRBStatusUL12", True),
        "dRBStatusUL18": ("struct DRBStatusUL18", True),
    },
    "DRB_ID_t": ("long", False),
    "DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue_u": {},
    "DRBsSubjectToStatusTransferItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBsSubjectToStatusTransferItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dRBStatusDL": ("DRBStatusDL_t", False),
        "dRBStatusUL": ("DRBStatusUL_t", False),
        "dRB_ID": ("DRB_ID_t", False),
        "iE_Extension": ("struct " "ProtocolExtensionContainer", True),
    },
    "DRBsSubjectToStatusTransferList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBsSubjectToStatusTransferItem)", False),
    },
    "DRBsToQosFlowsMappingItem_ExtIEs__extensionValue_PR_NOTHING": (
        "DRBsToQosFlowsMappingItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "DRBsToQosFlowsMappingItem_ExtIEs__extensionValue_u": {},
    "DRBsToQosFlowsMappingItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "DRBsToQosFlowsMappingItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DRBsToQosFlowsMappingItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "associatedQosFlowList": ("AssociatedQosFlowList_t", False),
        "dRB_ID": ("DRB_ID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "DRBsToQosFlowsMappingList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBsToQosFlowsMappingItem)", False),
    },
    "DataCodingScheme_t": ("BIT_STRING_t", False),
    "DataForwardingAccepted_data_forwarding_accepted": (
        "e_DataForwardingAccepted",
        False,
    ),
    "DataForwardingAccepted_t": ("long", False),
    "DataForwardingNotPossible_data_forwarding_not_possible": (
        "e_DataForwardingNotPossible",
        False,
    ),
    "DataForwardingNotPossible_t": ("long", False),
    "DataForwardingResponseDRBItem_ExtIEs__extensionValue_PR_NOTHING": (
        "DataForwardingResponseDRBItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "DataForwardingResponseDRBItem_ExtIEs__extensionValue_u": {},
    "DataForwardingResponseDRBItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "DataForwardingResponseDRBItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "DataForwardingResponseDRBItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dLForwardingUP_TNLInformation": (
            "struct " "UPTransportLayerInformation",
            True,
        ),
        "dRB_ID": ("DRB_ID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uLForwardingUP_TNLInformation": (
            "struct " "UPTransportLayerInformation",
            True,
        ),
    },
    "DataForwardingResponseDRBList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DataForwardingResponseDRBItem)", False),
    },
    "DeactivateTraceIEs__value_PR_AMF_UE_NGAP_ID": (
        "DeactivateTraceIEs__value_PR",
        False,
    ),
    "DeactivateTraceIEs__value_PR_NGRANTraceID": (
        "DeactivateTraceIEs__value_PR",
        False,
    ),
    "DeactivateTraceIEs__value_PR_NOTHING": ("DeactivateTraceIEs__value_PR", False),
    "DeactivateTraceIEs__value_PR_RAN_UE_NGAP_ID": (
        "DeactivateTraceIEs__value_PR",
        False,
    ),
    "DeactivateTraceIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NGRANTraceID": ("NGRANTraceID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "DeactivateTraceIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct DeactivateTraceIEs__value", False),
    },
    "DeactivateTrace_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P70_t", False),
    },
    "DelayCritical_delay_critical": ("e_DelayCritical", False),
    "DelayCritical_non_delay_critical": ("e_DelayCritical", False),
    "DelayCritical_t": ("long", False),
    "DeregistrationAccept_t": {"mmHeader": ("_5gmmMsgHeader_t", False)},
    "DeregistrationRequest_t": {
        "_5gderegType": ("_5gDeregistrationType_t", False),
        "_5gmobileId": ("_5gMobileId_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "ngKsi": ("NaskeysetId_t", False),
    },
    "DirectForwardingPathAvailability_direct_path_available": (
        "e_DirectForwardingPathAvailability",
        False,
    ),
    "DirectForwardingPathAvailability_t": ("long", False),
    "DownlinkNASTransport_IEs__value_PR_AMFName": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_AMF_UE_NGAP_ID": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_AllowedNSSAI": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_IndexToRFSP": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_MobilityRestrictionList": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_NAS_PDU": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_NOTHING": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_RANPagingPriority": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_RAN_UE_NGAP_ID": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_PR_UEAggregateMaximumBitRate": (
        "DownlinkNASTransport_IEs__value_PR",
        False,
    ),
    "DownlinkNASTransport_IEs__value_u": {
        "AMFName": ("AMFName_t", False),
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "IndexToRFSP": ("IndexToRFSP_t", False),
        "MobilityRestrictionList": ("MobilityRestrictionList_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "RANPagingPriority": ("RANPagingPriority_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UEAggregateMaximumBitRate": ("UEAggregateMaximumBitRate_t", False),
    },
    "DownlinkNASTransport_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "DownlinkNASTransport_IEs__value", False),
    },
    "DownlinkNASTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P37_t", False),
    },
    "DownlinkNasTransport_t": {
        "container": ("PayloadContainer_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "payloadContainerType": ("uint8_t", False),
        "pduSessionId": ("PDUSessionId2_t", False),
        "presenceMask": ("uint32_t", False),
    },
    "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR_NOTHING": (
        "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR_NRPPa_PDU": (
        "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR_RoutingID": (
        "DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkNonUEAssociatedNRPPaTransportIEs__value_u": {
        "NRPPa_PDU": ("NRPPa_PDU_t", False),
        "RoutingID": ("RoutingID_t", False),
    },
    "DownlinkNonUEAssociatedNRPPaTransportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "DownlinkNonUEAssociatedNRPPaTransportIEs__value", False),
    },
    "DownlinkNonUEAssociatedNRPPaTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P66_t", False),
    },
    "DownlinkRANConfigurationTransferIEs__value_PR_NOTHING": (
        "DownlinkRANConfigurationTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANConfigurationTransferIEs__value_PR_SONConfigurationTransfer": (
        "DownlinkRANConfigurationTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANConfigurationTransferIEs__value_u": {
        "SONConfigurationTransfer": ("SONConfigurationTransfer_t", False)
    },
    "DownlinkRANConfigurationTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "DownlinkRANConfigurationTransferIEs__value", False),
    },
    "DownlinkRANConfigurationTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P57_t", False),
    },
    "DownlinkRANStatusTransferIEs__value_PR_AMF_UE_NGAP_ID": (
        "DownlinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANStatusTransferIEs__value_PR_NOTHING": (
        "DownlinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANStatusTransferIEs__value_PR_RANStatusTransfer_TransparentContainer": (
        "DownlinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANStatusTransferIEs__value_PR_RAN_UE_NGAP_ID": (
        "DownlinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "DownlinkRANStatusTransferIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RANStatusTransfer_TransparentContainer": (
            "RANStatusTransfer_TransparentContainer_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "DownlinkRANStatusTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "DownlinkRANStatusTransferIEs__value", False),
    },
    "DownlinkRANStatusTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P34_t", False),
    },
    "DownlinkUEAssociatedNRPPaTransportIEs__value_PR_AMF_UE_NGAP_ID": (
        "DownlinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkUEAssociatedNRPPaTransportIEs__value_PR_NOTHING": (
        "DownlinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkUEAssociatedNRPPaTransportIEs__value_PR_NRPPa_PDU": (
        "DownlinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkUEAssociatedNRPPaTransportIEs__value_PR_RAN_UE_NGAP_ID": (
        "DownlinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkUEAssociatedNRPPaTransportIEs__value_PR_RoutingID": (
        "DownlinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "DownlinkUEAssociatedNRPPaTransportIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NRPPa_PDU": ("NRPPa_PDU_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RoutingID": ("RoutingID_t", False),
    },
    "DownlinkUEAssociatedNRPPaTransportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "DownlinkUEAssociatedNRPPaTransportIEs__value", False),
    },
    "DownlinkUEAssociatedNRPPaTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P64_t", False),
    },
    "Dynamic5QIDescriptor_ExtIEs__extensionValue_PR_NOTHING": (
        "Dynamic5QIDescriptor_ExtIEs__extensionValue_PR",
        False,
    ),
    "Dynamic5QIDescriptor_ExtIEs__extensionValue_u": {},
    "Dynamic5QIDescriptor_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "Dynamic5QIDescriptor_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "Dynamic5QIDescriptor_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "averagingWindow": ("AveragingWindow_t", True),
        "delayCritical": ("DelayCritical_t", True),
        "fiveQI": ("FiveQI_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "maximumDataBurstVolume": ("MaximumDataBurstVolume_t", True),
        "packetDelayBudget": ("PacketDelayBudget_t", False),
        "packetErrorRate": ("PacketErrorRate_t", False),
        "priorityLevelQos": ("PriorityLevelQos_t", False),
    },
    "EPS_TAC_t": ("OCTET_STRING_t", False),
    "EPS_TAI_ExtIEs__extensionValue_PR_NOTHING": (
        "EPS_TAI_ExtIEs__extensionValue_PR",
        False,
    ),
    "EPS_TAI_ExtIEs__extensionValue_u": {},
    "EPS_TAI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "EPS_TAI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EPS_TAI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "ePS_TAC": ("EPS_TAC_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "EUTRACellIdentity_t": ("BIT_STRING_t", False),
    "EUTRA_CGIListForWarning_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct EUTRA_CGI)", False),
    },
    "EUTRA_CGIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct EUTRA_CGI)", False),
    },
    "EUTRA_CGI_ExtIEs__extensionValue_PR_NOTHING": (
        "EUTRA_CGI_ExtIEs__extensionValue_PR",
        False,
    ),
    "EUTRA_CGI_ExtIEs__extensionValue_u": {},
    "EUTRA_CGI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "EUTRA_CGI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EUTRA_CGI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRACellIdentity": ("EUTRACellIdentity_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "EUTRAencryptionAlgorithms_t": ("BIT_STRING_t", False),
    "EUTRAintegrityProtectionAlgorithms_t": ("BIT_STRING_t", False),
    "E_3GPP_ACCESS": ("_5gRegistrationResultValue_t", False),
    "E_3GPP_NON_3GPP_ACCESS": ("_5gRegistrationResultValue_t", False),
    "E_DATA": ("_5gServiceTypeValue_t", False),
    "E_EMERGENCY_SERVICES": ("_5gServiceTypeValue_t", False),
    "E_EMERGENCY_SERVICES_FALLBACK": ("_5gServiceTypeValue_t", False),
    "E_HIGH_PRIORITY_ACCESS": ("_5gServiceTypeValue_t", False),
    "E_MOBILE_TERMINATED_SERVICES": ("_5gServiceTypeValue_t", False),
    "E_NON_3GPP_ACCESS": ("_5gRegistrationResultValue_t", False),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_ALWAYS_ON_PDU_SESSION_INDICATION": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_AUTHORIZED_QOS_FLOW_DESCRIPTIONS": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_AUTHORIZED_QOS_RULES": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_EXTENDED_PROTOCOL_CONFIGURATION_OPTIONS": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_RQ_TIMER_VALUE": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMMAND_IEI_SESSION_AMBR": (
        "pduSessionModificationCommandIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_COMPLETE_IEI_5GSM_CAUSE": (
        "pduSessionModificationCompleteIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REJECT_IEI_BACK_OFF_TIMER_VALUE": (
        "pduSessionModificationRejectIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REJECT_IEI_EXTENDED_PROTOCOL_CONFIGURATION_OPTIONS": (
        "pduSessionModificationRejectIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_5GSM_CAUSE": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_ALWAYS_ON_PDU_SESSION_REQUESTED": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_EXTENDED_PROTOCOL_CONFIGURATION_OPTIONS": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_INTEGRITY_PROTECTION_MAXIMUM_DATA_RATE": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_MAXIMUM_NUMBER_OF_SUPPORTED_PACKET_FILTERS": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_REQUESTED_QOS_FLOW_DESCRIPTIONS": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_PDU_SESSION_MODIFICATION_REQUEST_IEI_REQUESTED_QOS_RULES": (
        "pduSessionModificationRequestIEI_t",
        False,
    ),
    "E_RABInformationItem_ExtIEs__extensionValue_PR_NOTHING": (
        "E_RABInformationItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "E_RABInformationItem_ExtIEs__extensionValue_u": {},
    "E_RABInformationItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "E_RABInformationItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "E_RABInformationItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dLForwarding": ("DLForwarding_t", True),
        "e_RAB_ID": ("E_RAB_ID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "E_RABInformationList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "E_RABInformationItem)", False),
    },
    "E_RAB_ID_t": ("long", False),
    "E_REG_ACCEPT_IEI_5G_GUTI": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_ALLOWED_NSSAI": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_PDU_SESSION_RESULT": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_PDU_SESSION_RESULT_CAUSE": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_PDU_SESSION_STATUS": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_REJ_NSSAI": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_T3512": ("registrationAcceptIEI_t", False),
    "E_REG_ACCEPT_IEI_TAI_LIST": ("registrationAcceptIEI_t", False),
    "E_REG_REQUEST_IEI_5GMM_CAPABILITY": ("registrationReqIEI_t", False),
    "E_REG_REQUEST_IEI_PDU_SESSION_STATUS": ("registrationReqIEI_t", False),
    "E_REG_REQUEST_IEI_REQ_NSSAI": ("registrationReqIEI_t", False),
    "E_REG_REQUEST_IEI_UE_SEC_CAPABILITY": ("registrationReqIEI_t", False),
    "E_REG_REQUEST_IEI_UPLINK_DATA_STATUS": ("registrationReqIEI_t", False),
    "E_RESERVED": ("_5gRegistrationResultValue_t", False),
    "E_SERV_ACCEPT_IEI_PDU_SESSION_RESULT": ("serviceAccIEI_t", False),
    "E_SERV_ACCEPT_IEI_PDU_SESSION_RESULT_CAUSE": ("serviceAccIEI_t", False),
    "E_SERV_ACCEPT_IEI_PDU_SESSION_STATUS": ("serviceAccIEI_t", False),
    "E_SERV_REJECT_IEI_PDU_SESSION_STATUS": ("serviceRejIEI_t", False),
    "E_SERV_REQUEST_IEI_PDU_SESSION_STATUS": ("serviceReqIEI_t", False),
    "E_SERV_REQUEST_IEI_UPLINK_DATA_STATUS": ("serviceReqIEI_t", False),
    "E_SIGNALLING": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_1": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_2": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_3": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_4": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_5": ("_5gServiceTypeValue_t", False),
    "E_UNUSED_6": ("_5gServiceTypeValue_t", False),
    "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue_u": {},
    "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EmergencyAreaIDBroadcastEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "completedCellsInEAI_EUTRA": ("CompletedCellsInEAI_EUTRA_t", False),
        "emergencyAreaID": ("EmergencyAreaID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "EmergencyAreaIDBroadcastEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EmergencyAreaIDBroadcastEUTRA_Item)", False),
    },
    "EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue_u": {},
    "EmergencyAreaIDBroadcastNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EmergencyAreaIDBroadcastNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "completedCellsInEAI_NR": ("CompletedCellsInEAI_NR_t", False),
        "emergencyAreaID": ("EmergencyAreaID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "EmergencyAreaIDBroadcastNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EmergencyAreaIDBroadcastNR_Item)", False),
    },
    "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue_u": {},
    "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EmergencyAreaIDCancelledEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cancelledCellsInEAI_EUTRA": ("CancelledCellsInEAI_EUTRA_t", False),
        "emergencyAreaID": ("EmergencyAreaID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "EmergencyAreaIDCancelledEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EmergencyAreaIDCancelledEUTRA_Item)", False),
    },
    "EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue_u": {},
    "EmergencyAreaIDCancelledNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EmergencyAreaIDCancelledNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cancelledCellsInEAI_NR": ("CancelledCellsInEAI_NR_t", False),
        "emergencyAreaID": ("EmergencyAreaID_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "EmergencyAreaIDCancelledNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EmergencyAreaIDCancelledNR_Item)", False),
    },
    "EmergencyAreaIDListForRestart_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(EmergencyAreaID_t)", False),
    },
    "EmergencyAreaIDList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(EmergencyAreaID_t)", False),
    },
    "EmergencyAreaID_t": ("OCTET_STRING_t", False),
    "EmergencyFallbackIndicator_ExtIEs__extensionValue_PR_NOTHING": (
        "EmergencyFallbackIndicator_ExtIEs__extensionValue_PR",
        False,
    ),
    "EmergencyFallbackIndicator_ExtIEs__extensionValue_u": {},
    "EmergencyFallbackIndicator_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "EmergencyFallbackIndicator_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "EmergencyFallbackIndicator_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "emergencyFallbackRequestIndicator": (
            "EmergencyFallbackRequestIndicator_t",
            False,
        ),
        "emergencyServiceTargetCN": ("EmergencyServiceTargetCN_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "EmergencyFallbackRequestIndicator_emergency_fallback_requested": (
        "e_EmergencyFallbackRequestIndicator",
        False,
    ),
    "EmergencyFallbackRequestIndicator_t": ("long", False),
    "EmergencyServiceTargetCN_epc": ("e_EmergencyServiceTargetCN", False),
    "EmergencyServiceTargetCN_fiveGC": ("e_EmergencyServiceTargetCN", False),
    "EmergencyServiceTargetCN_t": ("long", False),
    "EquivalentPLMNs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(PLMNIdentity_t)", False),
    },
    "ErrorIndicationIEs__value_PR_AMF_UE_NGAP_ID": (
        "ErrorIndicationIEs__value_PR",
        False,
    ),
    "ErrorIndicationIEs__value_PR_Cause": ("ErrorIndicationIEs__value_PR", False),
    "ErrorIndicationIEs__value_PR_CriticalityDiagnostics": (
        "ErrorIndicationIEs__value_PR",
        False,
    ),
    "ErrorIndicationIEs__value_PR_NOTHING": ("ErrorIndicationIEs__value_PR", False),
    "ErrorIndicationIEs__value_PR_RAN_UE_NGAP_ID": (
        "ErrorIndicationIEs__value_PR",
        False,
    ),
    "ErrorIndicationIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "ErrorIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct ErrorIndicationIEs__value", False),
    },
    "ErrorIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P53_t", False),
    },
    "EventType_cancel_location_reporting_for_the_ue": ("e_EventType", False),
    "EventType_change_of_serve_cell": ("e_EventType", False),
    "EventType_direct": ("e_EventType", False),
    "EventType_stop_change_of_serve_cell": ("e_EventType", False),
    "EventType_stop_ue_presence_in_area_of_interest": ("e_EventType", False),
    "EventType_t": ("long", False),
    "EventType_ue_presence_in_area_of_interest": ("e_EventType", False),
    "ExpectedActivityPeriod_t": ("long", False),
    "ExpectedHOInterval_long_time": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec120": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec15": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec180": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec30": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec60": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_sec90": ("e_ExpectedHOInterval", False),
    "ExpectedHOInterval_t": ("long", False),
    "ExpectedIdlePeriod_t": ("long", False),
    "ExpectedUEActivityBehaviour_ExtIEs__extensionValue_PR_NOTHING": (
        "ExpectedUEActivityBehaviour_ExtIEs__extensionValue_PR",
        False,
    ),
    "ExpectedUEActivityBehaviour_ExtIEs__extensionValue_u": {},
    "ExpectedUEActivityBehaviour_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "ExpectedUEActivityBehaviour_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ExpectedUEActivityBehaviour_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "expectedActivityPeriod": ("ExpectedActivityPeriod_t", True),
        "expectedIdlePeriod": ("ExpectedIdlePeriod_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "sourceOfUEActivityBehaviourInformation": (
            "SourceOfUEActivityBehaviourInformation_t",
            True,
        ),
    },
    "ExpectedUEBehaviour_ExtIEs__extensionValue_PR_NOTHING": (
        "ExpectedUEBehaviour_ExtIEs__extensionValue_PR",
        False,
    ),
    "ExpectedUEBehaviour_ExtIEs__extensionValue_u": {},
    "ExpectedUEBehaviour_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "ExpectedUEBehaviour_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ExpectedUEBehaviour_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "expectedHOInterval": ("ExpectedHOInterval_t", True),
        "expectedUEActivityBehaviour": ("struct " "ExpectedUEActivityBehaviour", True),
        "expectedUEMobility": ("ExpectedUEMobility_t", True),
        "expectedUEMovingTrajectory": ("struct " "ExpectedUEMovingTrajectory", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "ExpectedUEMobility_mobile": ("e_ExpectedUEMobility", False),
    "ExpectedUEMobility_stationary": ("e_ExpectedUEMobility", False),
    "ExpectedUEMobility_t": ("long", False),
    "ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue_PR_NOTHING": (
        "ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue_u": {},
    "ExpectedUEMovingTrajectoryItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ExpectedUEMovingTrajectoryItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nGRAN_CGI": ("NGRAN_CGI_t", False),
        "timeStayedInCell": ("long", True),
    },
    "ExpectedUEMovingTrajectory_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ExpectedUEMovingTrajectoryItem)", False),
    },
    "ExtendedProtocolConfigurationOptions_t": {
        "extendedProtocolConfigurationOptionsContents": ("uint8_t", True),
        "lengthOfExtendedProtocolConfigurationOptionsContents": ("uint16_t", False),
    },
    "FiveG_S_TMSI_ExtIEs__extensionValue_PR_NOTHING": (
        "FiveG_S_TMSI_ExtIEs__extensionValue_PR",
        False,
    ),
    "FiveG_S_TMSI_ExtIEs__extensionValue_u": {},
    "FiveG_S_TMSI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "FiveG_S_TMSI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "FiveG_S_TMSI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMFPointer": ("AMFPointer_t", False),
        "aMFSetID": ("AMFSetID_t", False),
        "fiveG_TMSI": ("FiveG_TMSI_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
    },
    "FiveG_TMSI_t": ("OCTET_STRING_t", False),
    "FiveQI_t": ("long", False),
    "FlowLabel_t": {"flowLabel": ("uint32_t", False), "spare": ("uint8_t", False)},
    "ForbiddenAreaInformation_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "ForbiddenAreaInformation_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "ForbiddenAreaInformation_Item_ExtIEs__extensionValue_u": {},
    "ForbiddenAreaInformation_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "ForbiddenAreaInformation_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ForbiddenAreaInformation_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "forbiddenTACs": ("ForbiddenTACs_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "ForbiddenAreaInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ForbiddenAreaInformation_Item)", False),
    },
    "ForbiddenTACs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(TAC_t)", False),
    },
    "GBR_QosInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "GBR_QosInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "GBR_QosInformation_ExtIEs__extensionValue_u": {},
    "GBR_QosInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "GBR_QosInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GBR_QosInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "guaranteedFlowBitRateDL": ("BitRate_t", False),
        "guaranteedFlowBitRateUL": ("BitRate_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "maximumFlowBitRateDL": ("BitRate_t", False),
        "maximumFlowBitRateUL": ("BitRate_t", False),
        "maximumPacketLossRateDL": ("PacketLossRate_t", True),
        "maximumPacketLossRateUL": ("PacketLossRate_t", True),
        "notificationControl": ("NotificationControl_t", True),
    },
    "GBR_t": {
        "DL_GBR": ("uint64_t", False),
        "IEI": ("uint16_t", False),
        "UL_GBR": ("uint64_t", False),
    },
    "GNB_ID_ExtIEs__value_PR_NOTHING": ("GNB_ID_ExtIEs__value_PR", False),
    "GNB_ID_ExtIEs__value_u": {},
    "GNB_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct GNB_ID_ExtIEs__value", False),
    },
    "GNB_ID_PR_NOTHING": ("GNB_ID_PR", False),
    "GNB_ID_PR_choice_Extensions": ("GNB_ID_PR", False),
    "GNB_ID_PR_gNB_ID": ("GNB_ID_PR", False),
    "GNB_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GNB_ID_u", False),
        "present": ("GNB_ID_PR", False),
    },
    "GNB_ID_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "gNB_ID": ("BIT_STRING_t", False),
    },
    "GTPTunnel_ExtIEs__extensionValue_PR_NOTHING": (
        "GTPTunnel_ExtIEs__extensionValue_PR",
        False,
    ),
    "GTPTunnel_ExtIEs__extensionValue_u": {},
    "GTPTunnel_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "GTPTunnel_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GTPTunnel_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "gTP_TEID": ("GTP_TEID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "transportLayerAddress": ("TransportLayerAddress_t", False),
    },
    "GTP_TEID_t": ("OCTET_STRING_t", False),
    "GUAMI_ExtIEs__extensionValue_PR_NOTHING": (
        "GUAMI_ExtIEs__extensionValue_PR",
        False,
    ),
    "GUAMI_ExtIEs__extensionValue_u": {},
    "GUAMI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct GUAMI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GUAMI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMFPointer": ("AMFPointer_t", False),
        "aMFRegionID": ("AMFRegionID_t", False),
        "aMFSetID": ("AMFSetID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "GlobalGNB_ID_ExtIEs__extensionValue_PR_NOTHING": (
        "GlobalGNB_ID_ExtIEs__extensionValue_PR",
        False,
    ),
    "GlobalGNB_ID_ExtIEs__extensionValue_u": {},
    "GlobalGNB_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "GlobalGNB_ID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GlobalGNB_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "gNB_ID": ("GNB_ID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "GlobalN3IWF_ID_ExtIEs__extensionValue_PR_NOTHING": (
        "GlobalN3IWF_ID_ExtIEs__extensionValue_PR",
        False,
    ),
    "GlobalN3IWF_ID_ExtIEs__extensionValue_u": {},
    "GlobalN3IWF_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "GlobalN3IWF_ID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GlobalN3IWF_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "n3IWF_ID": ("N3IWF_ID_t", False),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "GlobalNgENB_ID_ExtIEs__extensionValue_PR_NOTHING": (
        "GlobalNgENB_ID_ExtIEs__extensionValue_PR",
        False,
    ),
    "GlobalNgENB_ID_ExtIEs__extensionValue_u": {},
    "GlobalNgENB_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "GlobalNgENB_ID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "GlobalNgENB_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "ngENB_ID": ("NgENB_ID_t", False),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "GlobalRANNodeID_ExtIEs__value_PR_NOTHING": (
        "GlobalRANNodeID_ExtIEs__value_PR",
        False,
    ),
    "GlobalRANNodeID_ExtIEs__value_u": {},
    "GlobalRANNodeID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct GlobalRANNodeID_ExtIEs__value", False),
    },
    "GlobalRANNodeID_PR_NOTHING": ("GlobalRANNodeID_PR", False),
    "GlobalRANNodeID_PR_choice_Extensions": ("GlobalRANNodeID_PR", False),
    "GlobalRANNodeID_PR_globalGNB_ID": ("GlobalRANNodeID_PR", False),
    "GlobalRANNodeID_PR_globalN3IWF_ID": ("GlobalRANNodeID_PR", False),
    "GlobalRANNodeID_PR_globalNgENB_ID": ("GlobalRANNodeID_PR", False),
    "GlobalRANNodeID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GlobalRANNodeID_u", False),
        "present": ("GlobalRANNodeID_PR", False),
    },
    "GlobalRANNodeID_u": {
        "choice_Extensions": ("ProtocolIE_SingleContainer_t", True),
        "globalGNB_ID": ("GlobalGNB_ID_t", True),
        "globalN3IWF_ID": ("GlobalN3IWF_ID_t", True),
        "globalNgENB_ID": ("GlobalNgENB_ID_t", True),
    },
    "GprsTimer3_t": {
        "lengthOfGprsTimer3Contents": ("uint8_t", False),
        "timerValue": ("uint8_t", False),
        "unit": ("uint8_t", False),
    },
    "GprsTimer_t": {"timerValue": ("uint8_t", False), "unit": ("uint8_t", False)},
    "HandoverCancelAcknowledgeIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverCancelAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverCancelAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "HandoverCancelAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverCancelAcknowledgeIEs__value_PR_NOTHING": (
        "HandoverCancelAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverCancelAcknowledgeIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverCancelAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverCancelAcknowledgeIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "HandoverCancelAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "HandoverCancelAcknowledgeIEs__value", False),
    },
    "HandoverCancelAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P32_t", False),
    },
    "HandoverCancelIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverCancelIEs__value_PR",
        False,
    ),
    "HandoverCancelIEs__value_PR_Cause": ("HandoverCancelIEs__value_PR", False),
    "HandoverCancelIEs__value_PR_NOTHING": ("HandoverCancelIEs__value_PR", False),
    "HandoverCancelIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverCancelIEs__value_PR",
        False,
    ),
    "HandoverCancelIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "HandoverCancelIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverCancelIEs__value", False),
    },
    "HandoverCancel_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P31_t", False),
    },
    "HandoverCommandIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_CriticalityDiagnostics": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_HandoverType": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_NASSecurityParametersFromNGRAN": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_NOTHING": ("HandoverCommandIEs__value_PR", False),
    "HandoverCommandIEs__value_PR_PDUSessionResourceHandoverList": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_PDUSessionResourceToReleaseListHOCmd": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_PR_TargetToSource_TransparentContainer": (
        "HandoverCommandIEs__value_PR",
        False,
    ),
    "HandoverCommandIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "HandoverType": ("HandoverType_t", False),
        "NASSecurityParametersFromNGRAN": ("NASSecurityParametersFromNGRAN_t", False),
        "PDUSessionResourceHandoverList": ("PDUSessionResourceHandoverList_t", False),
        "PDUSessionResourceToReleaseListHOCmd": (
            "PDUSessionResourceToReleaseListHOCmd_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "TargetToSource_TransparentContainer": (
            "TargetToSource_TransparentContainer_t",
            False,
        ),
    },
    "HandoverCommandIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverCommandIEs__value", False),
    },
    "HandoverCommandTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "HandoverCommandTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "HandoverCommandTransfer_ExtIEs__extensionValue_u": {},
    "HandoverCommandTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "HandoverCommandTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "HandoverCommandTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dLForwardingUP_TNLInformation": (
            "struct " "UPTransportLayerInformation",
            True,
        ),
        "dataForwardingResponseDRBList": (
            "struct " "DataForwardingResponseDRBList",
            True,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowToBeForwardedList": ("struct " "QosFlowToBeForwardedList", True),
    },
    "HandoverCommand_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P22_t", False),
    },
    "HandoverFailureIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverFailureIEs__value_PR",
        False,
    ),
    "HandoverFailureIEs__value_PR_Cause": ("HandoverFailureIEs__value_PR", False),
    "HandoverFailureIEs__value_PR_CriticalityDiagnostics": (
        "HandoverFailureIEs__value_PR",
        False,
    ),
    "HandoverFailureIEs__value_PR_NOTHING": ("HandoverFailureIEs__value_PR", False),
    "HandoverFailureIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
    },
    "HandoverFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverFailureIEs__value", False),
    },
    "HandoverFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P26_t", False),
    },
    "HandoverNotifyIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverNotifyIEs__value_PR",
        False,
    ),
    "HandoverNotifyIEs__value_PR_NOTHING": ("HandoverNotifyIEs__value_PR", False),
    "HandoverNotifyIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverNotifyIEs__value_PR",
        False,
    ),
    "HandoverNotifyIEs__value_PR_UserLocationInformation": (
        "HandoverNotifyIEs__value_PR",
        False,
    ),
    "HandoverNotifyIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "HandoverNotifyIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverNotifyIEs__value", False),
    },
    "HandoverNotify_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P27_t", False),
    },
    "HandoverPreparationFailureIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverPreparationFailureIEs__value_PR",
        False,
    ),
    "HandoverPreparationFailureIEs__value_PR_Cause": (
        "HandoverPreparationFailureIEs__value_PR",
        False,
    ),
    "HandoverPreparationFailureIEs__value_PR_CriticalityDiagnostics": (
        "HandoverPreparationFailureIEs__value_PR",
        False,
    ),
    "HandoverPreparationFailureIEs__value_PR_NOTHING": (
        "HandoverPreparationFailureIEs__value_PR",
        False,
    ),
    "HandoverPreparationFailureIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverPreparationFailureIEs__value_PR",
        False,
    ),
    "HandoverPreparationFailureIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "HandoverPreparationFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "HandoverPreparationFailureIEs__value", False),
    },
    "HandoverPreparationFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P23_t", False),
    },
    "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "HandoverPreparationUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "HandoverPreparationUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "HandoverRequestAcknowledgeIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_NOTHING": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_PDUSessionResourceAdmittedList": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_PDUSessionResourceFailedToSetupListHOAck": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_PR_TargetToSource_TransparentContainer": (
        "HandoverRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "HandoverRequestAcknowledgeIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceAdmittedList": ("PDUSessionResourceAdmittedList_t", False),
        "PDUSessionResourceFailedToSetupListHOAck": (
            "PDUSessionResourceFailedToSetupListHOAck_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "TargetToSource_TransparentContainer": (
            "TargetToSource_TransparentContainer_t",
            False,
        ),
    },
    "HandoverRequestAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "HandoverRequestAcknowledgeIEs__value", False),
    },
    "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue_u": {},
    "HandoverRequestAcknowledgeTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "HandoverRequestAcknowledgeTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dLForwardingUP_TNLInformation": (
            "struct " "UPTransportLayerInformation",
            True,
        ),
        "dL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
        "dataForwardingResponseDRBList": (
            "struct " "DataForwardingResponseDRBList",
            True,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowFailedToSetupList": ("struct " "QosFlowList", True),
        "qosFlowSetupResponseList": ("QosFlowSetupResponseListHOReqAck_t", False),
        "securityResult": ("struct " "SecurityResult", True),
    },
    "HandoverRequestAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P25_t", False),
    },
    "HandoverRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_AllowedNSSAI": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_Cause": ("HandoverRequestIEs__value_PR", False),
    "HandoverRequestIEs__value_PR_CoreNetworkAssistanceInformation": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_GUAMI": ("HandoverRequestIEs__value_PR", False),
    "HandoverRequestIEs__value_PR_HandoverType": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_LocationReportingRequestType": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_MaskedIMEISV": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_MobilityRestrictionList": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_NAS_PDU": ("HandoverRequestIEs__value_PR", False),
    "HandoverRequestIEs__value_PR_NOTHING": ("HandoverRequestIEs__value_PR", False),
    "HandoverRequestIEs__value_PR_NewSecurityContextInd": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_PDUSessionResourceSetupListHOReq": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_RRCInactiveTransitionReportRequest": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_SecurityContext": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_SourceToTarget_TransparentContainer": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_TraceActivation": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_UEAggregateMaximumBitRate": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_PR_UESecurityCapabilities": (
        "HandoverRequestIEs__value_PR",
        False,
    ),
    "HandoverRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "Cause": ("Cause_t", False),
        "CoreNetworkAssistanceInformation": (
            "CoreNetworkAssistanceInformation_t",
            False,
        ),
        "GUAMI": ("GUAMI_t", False),
        "HandoverType": ("HandoverType_t", False),
        "LocationReportingRequestType": ("LocationReportingRequestType_t", False),
        "MaskedIMEISV": ("MaskedIMEISV_t", False),
        "MobilityRestrictionList": ("MobilityRestrictionList_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "NewSecurityContextInd": ("NewSecurityContextInd_t", False),
        "PDUSessionResourceSetupListHOReq": (
            "PDUSessionResourceSetupListHOReq_t",
            False,
        ),
        "RRCInactiveTransitionReportRequest": (
            "RRCInactiveTransitionReportRequest_t",
            False,
        ),
        "SecurityContext": ("SecurityContext_t", False),
        "SourceToTarget_TransparentContainer": (
            "SourceToTarget_TransparentContainer_t",
            False,
        ),
        "TraceActivation": ("TraceActivation_t", False),
        "UEAggregateMaximumBitRate": ("UEAggregateMaximumBitRate_t", False),
        "UESecurityCapabilities": ("UESecurityCapabilities_t", False),
    },
    "HandoverRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverRequestIEs__value", False),
    },
    "HandoverRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P24_t", False),
    },
    "HandoverRequiredIEs__value_PR_AMF_UE_NGAP_ID": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_Cause": ("HandoverRequiredIEs__value_PR", False),
    "HandoverRequiredIEs__value_PR_DirectForwardingPathAvailability": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_HandoverType": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_NOTHING": ("HandoverRequiredIEs__value_PR", False),
    "HandoverRequiredIEs__value_PR_PDUSessionResourceListHORqd": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_RAN_UE_NGAP_ID": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_SourceToTarget_TransparentContainer": (
        "HandoverRequiredIEs__value_PR",
        False,
    ),
    "HandoverRequiredIEs__value_PR_TargetID": ("HandoverRequiredIEs__value_PR", False),
    "HandoverRequiredIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "DirectForwardingPathAvailability": (
            "DirectForwardingPathAvailability_t",
            False,
        ),
        "HandoverType": ("HandoverType_t", False),
        "PDUSessionResourceListHORqd": ("PDUSessionResourceListHORqd_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "SourceToTarget_TransparentContainer": (
            "SourceToTarget_TransparentContainer_t",
            False,
        ),
        "TargetID": ("TargetID_t", False),
    },
    "HandoverRequiredIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct HandoverRequiredIEs__value", False),
    },
    "HandoverRequiredTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "HandoverRequiredTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "HandoverRequiredTransfer_ExtIEs__extensionValue_u": {},
    "HandoverRequiredTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "HandoverRequiredTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "HandoverRequiredTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "directForwardingPathAvailability": (
            "DirectForwardingPathAvailability_t",
            True,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "HandoverRequired_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P21_t", False),
    },
    "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "HandoverResourceAllocationUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "criticalityDiagnostics": ("struct " "CriticalityDiagnostics", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "HandoverType_eps_to_5gs": ("e_HandoverType", False),
    "HandoverType_fivegs_to_eps": ("e_HandoverType", False),
    "HandoverType_intra5gs": ("e_HandoverType", False),
    "HandoverType_t": ("long", False),
    "HttpRequest": ("json", False),
    "HttpResponse": ("json", False),
    "IMSVoiceSupportIndicator_not_supported": ("e_IMSVoiceSupportIndicator", False),
    "IMSVoiceSupportIndicator_supported": ("e_IMSVoiceSupportIndicator", False),
    "IMSVoiceSupportIndicator_t": ("long", False),
    "INTEGER_t": ("ASN__PRIMITIVE_TYPE_t", False),
    "IPFilterRule_t": {
        "action": ("e_IPFilterRuleAction", False),
        "destNode": ("IPFilterRuleNode_t", False),
        "dir": ("e_IPFilterRuleDirection", False),
        "proto": ("e_IPFilterRuleProtocol", False),
        "srcNode": ("IPFilterRuleNode_t", False),
    },
    "IndexToRFSP_t": ("long", False),
    "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue_PR_NOTHING": (
        "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue_PR",
        False,
    ),
    "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue_u": {},
    "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "InfoOnRecommendedCellsAndRANNodesForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "recommendRANNodesForPaging": ("RecommendedRANNodesForPaging_t", False),
        "recommendedCellsForPaging": ("RecommendedCellsForPaging_t", False),
    },
    "InitialContextSetupFailureIEs__value_PR_AMF_UE_NGAP_ID": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_PR_Cause": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_PR_CriticalityDiagnostics": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_PR_NOTHING": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_PR_PDUSessionResourceFailedToSetupListCxtFail": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_PR_RAN_UE_NGAP_ID": (
        "InitialContextSetupFailureIEs__value_PR",
        False,
    ),
    "InitialContextSetupFailureIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceFailedToSetupListCxtFail": (
            "PDUSessionResourceFailedToSetupListCxtFail_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "InitialContextSetupFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "InitialContextSetupFailureIEs__value", False),
    },
    "InitialContextSetupFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P13_t", False),
    },
    "InitialContextSetupRequestIEs__value_PR_AMFName": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_AllowedNSSAI": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_CoreNetworkAssistanceInformation": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_EmergencyFallbackIndicator": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_GUAMI": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_IndexToRFSP": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_MaskedIMEISV": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_MobilityRestrictionList": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_NAS_PDU": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_NOTHING": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_PDUSessionResourceSetupListCxtReq": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_RRCInactiveTransitionReportRequest": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_SecurityKey": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_TraceActivation": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_UEAggregateMaximumBitRate": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_UERadioCapability": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_UERadioCapabilityForPaging": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_PR_UESecurityCapabilities": (
        "InitialContextSetupRequestIEs__value_PR",
        False,
    ),
    "InitialContextSetupRequestIEs__value_u": {
        "AMFName": ("AMFName_t", False),
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "CoreNetworkAssistanceInformation": (
            "CoreNetworkAssistanceInformation_t",
            False,
        ),
        "EmergencyFallbackIndicator": ("EmergencyFallbackIndicator_t", False),
        "GUAMI": ("GUAMI_t", False),
        "IndexToRFSP": ("IndexToRFSP_t", False),
        "MaskedIMEISV": ("MaskedIMEISV_t", False),
        "MobilityRestrictionList": ("MobilityRestrictionList_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "PDUSessionResourceSetupListCxtReq": (
            "PDUSessionResourceSetupListCxtReq_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCInactiveTransitionReportRequest": (
            "RRCInactiveTransitionReportRequest_t",
            False,
        ),
        "SecurityKey": ("SecurityKey_t", False),
        "TraceActivation": ("TraceActivation_t", False),
        "UEAggregateMaximumBitRate": ("UEAggregateMaximumBitRate_t", False),
        "UERadioCapability": ("UERadioCapability_t", False),
        "UERadioCapabilityForPaging": ("UERadioCapabilityForPaging_t", False),
        "UESecurityCapabilities": ("UESecurityCapabilities_t", False),
    },
    "InitialContextSetupRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "InitialContextSetupRequestIEs__value", False),
    },
    "InitialContextSetupRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P11_t", False),
    },
    "InitialContextSetupResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_PR_CriticalityDiagnostics": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_PR_NOTHING": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_PR_PDUSessionResourceFailedToSetupListCxtRes": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_PR_PDUSessionResourceSetupListCxtRes": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "InitialContextSetupResponseIEs__value_PR",
        False,
    ),
    "InitialContextSetupResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceFailedToSetupListCxtRes": (
            "PDUSessionResourceFailedToSetupListCxtRes_t",
            False,
        ),
        "PDUSessionResourceSetupListCxtRes": (
            "PDUSessionResourceSetupListCxtRes_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "InitialContextSetupResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "InitialContextSetupResponseIEs__value", False),
    },
    "InitialContextSetupResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P12_t", False),
    },
    "InitialUEMessage_IEs__value_PR_AMFSetID": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_AllowedNSSAI": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_FiveG_S_TMSI": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_NAS_PDU": ("InitialUEMessage_IEs__value_PR", False),
    "InitialUEMessage_IEs__value_PR_NOTHING": ("InitialUEMessage_IEs__value_PR", False),
    "InitialUEMessage_IEs__value_PR_RAN_UE_NGAP_ID": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_RRCEstablishmentCause": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_UEContextRequest": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_PR_UserLocationInformation": (
        "InitialUEMessage_IEs__value_PR",
        False,
    ),
    "InitialUEMessage_IEs__value_u": {
        "AMFSetID": ("AMFSetID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "FiveG_S_TMSI": ("FiveG_S_TMSI_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCEstablishmentCause": ("RRCEstablishmentCause_t", False),
        "UEContextRequest": ("UEContextRequest_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "InitialUEMessage_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct InitialUEMessage_IEs__value", False),
    },
    "InitialUEMessage_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P36_t", False),
    },
    "InitiatingMessage__value_PR_AMFConfigurationUpdate": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_AMFStatusIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_CellTrafficTrace": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DeactivateTrace": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DownlinkNASTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DownlinkNonUEAssociatedNRPPaTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DownlinkRANConfigurationTransfer": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DownlinkRANStatusTransfer": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_DownlinkUEAssociatedNRPPaTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_ErrorIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_HandoverCancel": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_HandoverNotify": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_HandoverRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_HandoverRequired": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_InitialContextSetupRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_InitialUEMessage": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_LocationReport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_LocationReportingControl": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_LocationReportingFailureIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_NASNonDeliveryIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_NGReset": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_NGSetupRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_NOTHING": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_OverloadStart": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_OverloadStop": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_PDUSessionResourceModifyIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PDUSessionResourceModifyRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PDUSessionResourceNotify": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PDUSessionResourceReleaseCommand": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PDUSessionResourceSetupRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PWSCancelRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PWSFailureIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PWSRestartIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_Paging": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_PathSwitchRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_PrivateMessage": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_RANConfigurationUpdate": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_RRCInactiveTransitionReport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_RerouteNASRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_TraceFailureIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_TraceStart": ("InitiatingMessage__value_PR", False),
    "InitiatingMessage__value_PR_UEContextModificationRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UEContextReleaseCommand": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UEContextReleaseRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UERadioCapabilityCheckRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UERadioCapabilityInfoIndication": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UETNLABindingReleaseRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UplinkNASTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UplinkNonUEAssociatedNRPPaTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UplinkRANConfigurationTransfer": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UplinkRANStatusTransfer": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_UplinkUEAssociatedNRPPaTransport": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_PR_WriteReplaceWarningRequest": (
        "InitiatingMessage__value_PR",
        False,
    ),
    "InitiatingMessage__value_u": {
        "AMFConfigurationUpdate": ("AMFConfigurationUpdate_t", False),
        "AMFStatusIndication": ("AMFStatusIndication_t", False),
        "CellTrafficTrace": ("CellTrafficTrace_t", False),
        "DeactivateTrace": ("DeactivateTrace_t", False),
        "DownlinkNASTransport": ("DownlinkNASTransport_t", False),
        "DownlinkNonUEAssociatedNRPPaTransport": (
            "DownlinkNonUEAssociatedNRPPaTransport_t",
            False,
        ),
        "DownlinkRANConfigurationTransfer": (
            "DownlinkRANConfigurationTransfer_t",
            False,
        ),
        "DownlinkRANStatusTransfer": ("DownlinkRANStatusTransfer_t", False),
        "DownlinkUEAssociatedNRPPaTransport": (
            "DownlinkUEAssociatedNRPPaTransport_t",
            False,
        ),
        "ErrorIndication": ("ErrorIndication_t", False),
        "HandoverCancel": ("HandoverCancel_t", False),
        "HandoverNotify": ("HandoverNotify_t", False),
        "HandoverRequest": ("HandoverRequest_t", False),
        "HandoverRequired": ("HandoverRequired_t", False),
        "InitialContextSetupRequest": ("InitialContextSetupRequest_t", False),
        "InitialUEMessage": ("InitialUEMessage_t", False),
        "LocationReport": ("LocationReport_t", False),
        "LocationReportingControl": ("LocationReportingControl_t", False),
        "LocationReportingFailureIndication": (
            "LocationReportingFailureIndication_t",
            False,
        ),
        "NASNonDeliveryIndication": ("NASNonDeliveryIndication_t", False),
        "NGReset": ("NGReset_t", False),
        "NGSetupRequest": ("NGSetupRequest_t", False),
        "OverloadStart": ("OverloadStart_t", False),
        "OverloadStop": ("OverloadStop_t", False),
        "PDUSessionResourceModifyIndication": (
            "PDUSessionResourceModifyIndication_t",
            False,
        ),
        "PDUSessionResourceModifyRequest": ("PDUSessionResourceModifyRequest_t", False),
        "PDUSessionResourceNotify": ("PDUSessionResourceNotify_t", False),
        "PDUSessionResourceReleaseCommand": (
            "PDUSessionResourceReleaseCommand_t",
            False,
        ),
        "PDUSessionResourceSetupRequest": ("PDUSessionResourceSetupRequest_t", False),
        "PWSCancelRequest": ("PWSCancelRequest_t", False),
        "PWSFailureIndication": ("PWSFailureIndication_t", False),
        "PWSRestartIndication": ("PWSRestartIndication_t", False),
        "Paging": ("Paging_t", False),
        "PathSwitchRequest": ("PathSwitchRequest_t", False),
        "PrivateMessage": ("PrivateMessage_t", False),
        "RANConfigurationUpdate": ("RANConfigurationUpdate_t", False),
        "RRCInactiveTransitionReport": ("RRCInactiveTransitionReport_t", False),
        "RerouteNASRequest": ("RerouteNASRequest_t", False),
        "TraceFailureIndication": ("TraceFailureIndication_t", False),
        "TraceStart": ("TraceStart_t", False),
        "UEContextModificationRequest": ("UEContextModificationRequest_t", False),
        "UEContextReleaseCommand": ("UEContextReleaseCommand_t", False),
        "UEContextReleaseRequest": ("UEContextReleaseRequest_t", False),
        "UERadioCapabilityCheckRequest": ("UERadioCapabilityCheckRequest_t", False),
        "UERadioCapabilityInfoIndication": ("UERadioCapabilityInfoIndication_t", False),
        "UETNLABindingReleaseRequest": ("UETNLABindingReleaseRequest_t", False),
        "UplinkNASTransport": ("UplinkNASTransport_t", False),
        "UplinkNonUEAssociatedNRPPaTransport": (
            "UplinkNonUEAssociatedNRPPaTransport_t",
            False,
        ),
        "UplinkRANConfigurationTransfer": ("UplinkRANConfigurationTransfer_t", False),
        "UplinkRANStatusTransfer": ("UplinkRANStatusTransfer_t", False),
        "UplinkUEAssociatedNRPPaTransport": (
            "UplinkUEAssociatedNRPPaTransport_t",
            False,
        ),
        "WriteReplaceWarningRequest": ("WriteReplaceWarningRequest_t", False),
    },
    "InitiatingMessage_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "procedureCode": ("ProcedureCode_t", False),
        "value": ("struct InitiatingMessage__value", False),
    },
    "IntegrityProtectionIndication_not_needed": (
        "e_IntegrityProtectionIndication",
        False,
    ),
    "IntegrityProtectionIndication_preferred": (
        "e_IntegrityProtectionIndication",
        False,
    ),
    "IntegrityProtectionIndication_required": (
        "e_IntegrityProtectionIndication",
        False,
    ),
    "IntegrityProtectionIndication_t": ("long", False),
    "IntegrityProtectionMaximumDataRate_t": {
        "maximumDataRatePerUeForUserPlaneIntegrityProtectionForDownlink": (
            "uint8_t",
            False,
        ),
        "maximumDataRatePerUeForUserPlaneIntegrityProtectionForUplink": (
            "uint8_t",
            False,
        ),
    },
    "IntegrityProtectionResult_not_performed": ("e_IntegrityProtectionResult", False),
    "IntegrityProtectionResult_performed": ("e_IntegrityProtectionResult", False),
    "IntegrityProtectionResult_t": ("long", False),
    "IntendedNumberOfPagingAttempts_t": ("long", False),
    "InterfacesToTrace_t": ("BIT_STRING_t", False),
    "Ipv4AddressType_t": {
        "ipv4Address": ("uint32_t", False),
        "ipv4Mask": ("uint32_t", False),
    },
    "Ipv6AddressType_t": {
        "ipv6Address": ("uint8_t", True),
        "prefixLength": ("uint8_t", False),
    },
    "LastVisitedCellInformation_ExtIEs__value_PR_NOTHING": (
        "LastVisitedCellInformation_ExtIEs__value_PR",
        False,
    ),
    "LastVisitedCellInformation_ExtIEs__value_u": {},
    "LastVisitedCellInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "LastVisitedCellInformation_ExtIEs__value", False),
    },
    "LastVisitedCellInformation_PR_NOTHING": ("LastVisitedCellInformation_PR", False),
    "LastVisitedCellInformation_PR_choice_Extensions": (
        "LastVisitedCellInformation_PR",
        False,
    ),
    "LastVisitedCellInformation_PR_eUTRANCell": (
        "LastVisitedCellInformation_PR",
        False,
    ),
    "LastVisitedCellInformation_PR_gERANCell": ("LastVisitedCellInformation_PR", False),
    "LastVisitedCellInformation_PR_nGRANCell": ("LastVisitedCellInformation_PR", False),
    "LastVisitedCellInformation_PR_uTRANCell": ("LastVisitedCellInformation_PR", False),
    "LastVisitedCellInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LastVisitedCellInformation_u", False),
        "present": ("LastVisitedCellInformation_PR", False),
    },
    "LastVisitedCellInformation_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "eUTRANCell": ("LastVisitedEUTRANCellInformation_t", False),
        "gERANCell": ("LastVisitedGERANCellInformation_t", False),
        "nGRANCell": ("struct " "LastVisitedNGRANCellInformation", True),
        "uTRANCell": ("LastVisitedUTRANCellInformation_t", False),
    },
    "LastVisitedCellItem_ExtIEs__extensionValue_PR_NOTHING": (
        "LastVisitedCellItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "LastVisitedCellItem_ExtIEs__extensionValue_u": {},
    "LastVisitedCellItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "LastVisitedCellItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "LastVisitedCellItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "lastVisitedCellInformation": ("LastVisitedCellInformation_t", False),
    },
    "LastVisitedEUTRANCellInformation_t": ("OCTET_STRING_t", False),
    "LastVisitedGERANCellInformation_t": ("OCTET_STRING_t", False),
    "LastVisitedNGRANCellInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "LastVisitedNGRANCellInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "LastVisitedNGRANCellInformation_ExtIEs__extensionValue_u": {},
    "LastVisitedNGRANCellInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "LastVisitedNGRANCellInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "LastVisitedNGRANCellInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cellType": ("CellType_t", False),
        "globalCellID": ("NGRAN_CGI_t", False),
        "hOCauseValue": ("struct Cause", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "timeUEStayedInCell": ("TimeUEStayedInCell_t", False),
        "timeUEStayedInCellEnhancedGranularity": (
            "TimeUEStayedInCellEnhancedGranularity_t",
            True,
        ),
    },
    "LastVisitedUTRANCellInformation_t": ("OCTET_STRING_t", False),
    "Location": ("string", False),
    "LocationReportIEs__value_PR_AMF_UE_NGAP_ID": (
        "LocationReportIEs__value_PR",
        False,
    ),
    "LocationReportIEs__value_PR_LocationReportingRequestType": (
        "LocationReportIEs__value_PR",
        False,
    ),
    "LocationReportIEs__value_PR_NOTHING": ("LocationReportIEs__value_PR", False),
    "LocationReportIEs__value_PR_RAN_UE_NGAP_ID": (
        "LocationReportIEs__value_PR",
        False,
    ),
    "LocationReportIEs__value_PR_UEPresenceInAreaOfInterestList": (
        "LocationReportIEs__value_PR",
        False,
    ),
    "LocationReportIEs__value_PR_UserLocationInformation": (
        "LocationReportIEs__value_PR",
        False,
    ),
    "LocationReportIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "LocationReportingRequestType": ("LocationReportingRequestType_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UEPresenceInAreaOfInterestList": ("UEPresenceInAreaOfInterestList_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "LocationReportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct LocationReportIEs__value", False),
    },
    "LocationReport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P74_t", False),
    },
    "LocationReportingControlIEs__value_PR_AMF_UE_NGAP_ID": (
        "LocationReportingControlIEs__value_PR",
        False,
    ),
    "LocationReportingControlIEs__value_PR_LocationReportingRequestType": (
        "LocationReportingControlIEs__value_PR",
        False,
    ),
    "LocationReportingControlIEs__value_PR_NOTHING": (
        "LocationReportingControlIEs__value_PR",
        False,
    ),
    "LocationReportingControlIEs__value_PR_RAN_UE_NGAP_ID": (
        "LocationReportingControlIEs__value_PR",
        False,
    ),
    "LocationReportingControlIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "LocationReportingRequestType": ("LocationReportingRequestType_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "LocationReportingControlIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "LocationReportingControlIEs__value", False),
    },
    "LocationReportingControl_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P72_t", False),
    },
    "LocationReportingFailureIndicationIEs__value_PR_AMF_UE_NGAP_ID": (
        "LocationReportingFailureIndicationIEs__value_PR",
        False,
    ),
    "LocationReportingFailureIndicationIEs__value_PR_Cause": (
        "LocationReportingFailureIndicationIEs__value_PR",
        False,
    ),
    "LocationReportingFailureIndicationIEs__value_PR_NOTHING": (
        "LocationReportingFailureIndicationIEs__value_PR",
        False,
    ),
    "LocationReportingFailureIndicationIEs__value_PR_RAN_UE_NGAP_ID": (
        "LocationReportingFailureIndicationIEs__value_PR",
        False,
    ),
    "LocationReportingFailureIndicationIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "LocationReportingFailureIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "LocationReportingFailureIndicationIEs__value", False),
    },
    "LocationReportingFailureIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P73_t", False),
    },
    "LocationReportingReferenceID_t": ("long", False),
    "LocationReportingRequestType_ExtIEs__extensionValue_PR_NOTHING": (
        "LocationReportingRequestType_ExtIEs__extensionValue_PR",
        False,
    ),
    "LocationReportingRequestType_ExtIEs__extensionValue_u": {},
    "LocationReportingRequestType_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "LocationReportingRequestType_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "LocationReportingRequestType_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "areaOfInterestList": ("struct " "AreaOfInterestList", True),
        "eventType": ("EventType_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "locationReportingReferenceIDToBeCancelled": (
            "LocationReportingReferenceID_t",
            True,
        ),
        "reportArea": ("ReportArea_t", False),
    },
    "MBR_t": {
        "DL_MBR": ("uint64_t", False),
        "IEI": ("uint16_t", False),
        "UL_MBR": ("uint64_t", False),
    },
    "MICOModeIndication_t": ("long", False),
    "MICOModeIndication_true": ("e_MICOModeIndication", False),
    "MaskedIMEISV_t": ("BIT_STRING_t", False),
    "MaximumDataBurstVolume_t": ("long", False),
    "MaximumIntegrityProtectedDataRate_bitrate64kbs": (
        "e_MaximumIntegrityProtectedDataRate",
        False,
    ),
    "MaximumIntegrityProtectedDataRate_maximum_UE_rate": (
        "e_MaximumIntegrityProtectedDataRate",
        False,
    ),
    "MaximumIntegrityProtectedDataRate_t": ("long", False),
    "MaximumNumberOfSupportedPacketFilters_t": {
        "maximumNumberOfSupportedPacketFilters": ("uint16_t", False),
        "spare": ("uint8_t", False),
    },
    "MessageIdentifier_t": ("BIT_STRING_t", False),
    "MobilityRestrictionList_ExtIEs__extensionValue_PR_NOTHING": (
        "MobilityRestrictionList_ExtIEs__extensionValue_PR",
        False,
    ),
    "MobilityRestrictionList_ExtIEs__extensionValue_u": {},
    "MobilityRestrictionList_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "MobilityRestrictionList_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "MobilityRestrictionList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "equivalentPLMNs": ("struct EquivalentPLMNs", True),
        "forbiddenAreaInformation": ("struct " "ForbiddenAreaInformation", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "rATRestrictions": ("struct RATRestrictions", True),
        "serviceAreaInformation": ("struct " "ServiceAreaInformation", True),
        "servingPLMN": ("PLMNIdentity_t", False),
    },
    "MultipleTNLInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "MultipleTNLInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "MultipleTNLInformation_ExtIEs__extensionValue_u": {},
    "MultipleTNLInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "MultipleTNLInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "MultipleTNLInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tNLInformationList": ("TNLInformationList_t", False),
    },
    "N3IWF_ID_ExtIEs__value_PR_NOTHING": ("N3IWF_ID_ExtIEs__value_PR", False),
    "N3IWF_ID_ExtIEs__value_u": {},
    "N3IWF_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct N3IWF_ID_ExtIEs__value", False),
    },
    "N3IWF_ID_PR_NOTHING": ("N3IWF_ID_PR", False),
    "N3IWF_ID_PR_choice_Extensions": ("N3IWF_ID_PR", False),
    "N3IWF_ID_PR_n3IWF_ID": ("N3IWF_ID_PR", False),
    "N3IWF_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("N3IWF_ID_u", False),
        "present": ("N3IWF_ID_PR", False),
    },
    "N3IWF_ID_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "n3IWF_ID": ("BIT_STRING_t", False),
    },
    "NASNonDeliveryIndication_IEs__value_PR_AMF_UE_NGAP_ID": (
        "NASNonDeliveryIndication_IEs__value_PR",
        False,
    ),
    "NASNonDeliveryIndication_IEs__value_PR_Cause": (
        "NASNonDeliveryIndication_IEs__value_PR",
        False,
    ),
    "NASNonDeliveryIndication_IEs__value_PR_NAS_PDU": (
        "NASNonDeliveryIndication_IEs__value_PR",
        False,
    ),
    "NASNonDeliveryIndication_IEs__value_PR_NOTHING": (
        "NASNonDeliveryIndication_IEs__value_PR",
        False,
    ),
    "NASNonDeliveryIndication_IEs__value_PR_RAN_UE_NGAP_ID": (
        "NASNonDeliveryIndication_IEs__value_PR",
        False,
    ),
    "NASNonDeliveryIndication_IEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "NASNonDeliveryIndication_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "NASNonDeliveryIndication_IEs__value", False),
    },
    "NASNonDeliveryIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P39_t", False),
    },
    "NASSecurityParametersFromNGRAN_t": ("OCTET_STRING_t", False),
    "NAS_PDU_t": ("OCTET_STRING_t", False),
    "NFServiceVersion": ("JSON", False),
    "NGAP_PDU_PR_NOTHING": ("NGAP_PDU_PR", False),
    "NGAP_PDU_PR_initiatingMessage": ("NGAP_PDU_PR", False),
    "NGAP_PDU_PR_successfulOutcome": ("NGAP_PDU_PR", False),
    "NGAP_PDU_PR_unsuccessfulOutcome": ("NGAP_PDU_PR", False),
    "NGAP_PDU_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGAP_PDU_u", False),
        "present": ("NGAP_PDU_PR", False),
    },
    "NGAP_PDU_u": {
        "initiatingMessage": ("struct InitiatingMessage", True),
        "successfulOutcome": ("struct SuccessfulOutcome", True),
        "unsuccessfulOutcome": ("struct UnsuccessfulOutcome", True),
    },
    "NGRANTraceID_t": ("OCTET_STRING_t", False),
    "NGRAN_CGI_ExtIEs__value_PR_NOTHING": ("NGRAN_CGI_ExtIEs__value_PR", False),
    "NGRAN_CGI_ExtIEs__value_u": {},
    "NGRAN_CGI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGRAN_CGI_ExtIEs__value", False),
    },
    "NGRAN_CGI_PR_NOTHING": ("NGRAN_CGI_PR", False),
    "NGRAN_CGI_PR_choice_Extensions": ("NGRAN_CGI_PR", False),
    "NGRAN_CGI_PR_eUTRA_CGI": ("NGRAN_CGI_PR", False),
    "NGRAN_CGI_PR_nR_CGI": ("NGRAN_CGI_PR", False),
    "NGRAN_CGI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGRAN_CGI_u", False),
        "present": ("NGRAN_CGI_PR", False),
    },
    "NGRAN_CGI_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "eUTRA_CGI": ("struct EUTRA_CGI", True),
        "nR_CGI": ("struct NR_CGI", True),
    },
    "NGResetAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "NGResetAcknowledgeIEs__value_PR",
        False,
    ),
    "NGResetAcknowledgeIEs__value_PR_NOTHING": (
        "NGResetAcknowledgeIEs__value_PR",
        False,
    ),
    "NGResetAcknowledgeIEs__value_PR_UE_associatedLogicalNG_connectionList": (
        "NGResetAcknowledgeIEs__value_PR",
        False,
    ),
    "NGResetAcknowledgeIEs__value_u": {
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "UE_associatedLogicalNG_connectionList": (
            "UE_associatedLogicalNG_connectionList_t",
            False,
        ),
    },
    "NGResetAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGResetAcknowledgeIEs__value", False),
    },
    "NGResetAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P52_t", False),
    },
    "NGResetIEs__value_PR_Cause": ("NGResetIEs__value_PR", False),
    "NGResetIEs__value_PR_NOTHING": ("NGResetIEs__value_PR", False),
    "NGResetIEs__value_PR_ResetType": ("NGResetIEs__value_PR", False),
    "NGResetIEs__value_u": {
        "Cause": ("Cause_t", False),
        "ResetType": ("ResetType_t", False),
    },
    "NGResetIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGResetIEs__value", False),
    },
    "NGReset_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P51_t", False),
    },
    "NGSetupFailureIEs__value_PR_Cause": ("NGSetupFailureIEs__value_PR", False),
    "NGSetupFailureIEs__value_PR_CriticalityDiagnostics": (
        "NGSetupFailureIEs__value_PR",
        False,
    ),
    "NGSetupFailureIEs__value_PR_NOTHING": ("NGSetupFailureIEs__value_PR", False),
    "NGSetupFailureIEs__value_PR_TimeToWait": ("NGSetupFailureIEs__value_PR", False),
    "NGSetupFailureIEs__value_u": {
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "TimeToWait": ("TimeToWait_t", False),
    },
    "NGSetupFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGSetupFailureIEs__value", False),
    },
    "NGSetupFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P43_t", False),
    },
    "NGSetupRequestIEs__value_PR_GlobalRANNodeID": (
        "NGSetupRequestIEs__value_PR",
        False,
    ),
    "NGSetupRequestIEs__value_PR_NOTHING": ("NGSetupRequestIEs__value_PR", False),
    "NGSetupRequestIEs__value_PR_PagingDRX": ("NGSetupRequestIEs__value_PR", False),
    "NGSetupRequestIEs__value_PR_RANNodeName": ("NGSetupRequestIEs__value_PR", False),
    "NGSetupRequestIEs__value_PR_SupportedTAList": (
        "NGSetupRequestIEs__value_PR",
        False,
    ),
    "NGSetupRequestIEs__value_u": {
        "GlobalRANNodeID": ("GlobalRANNodeID_t", False),
        "PagingDRX": ("PagingDRX_t", False),
        "RANNodeName": ("RANNodeName_t", False),
        "SupportedTAList": ("SupportedTAList_t", False),
    },
    "NGSetupRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGSetupRequestIEs__value", False),
    },
    "NGSetupRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P41_t", False),
    },
    "NGSetupResponseIEs__value_PR_AMFName": ("NGSetupResponseIEs__value_PR", False),
    "NGSetupResponseIEs__value_PR_CriticalityDiagnostics": (
        "NGSetupResponseIEs__value_PR",
        False,
    ),
    "NGSetupResponseIEs__value_PR_NOTHING": ("NGSetupResponseIEs__value_PR", False),
    "NGSetupResponseIEs__value_PR_PLMNSupportList": (
        "NGSetupResponseIEs__value_PR",
        False,
    ),
    "NGSetupResponseIEs__value_PR_RelativeAMFCapacity": (
        "NGSetupResponseIEs__value_PR",
        False,
    ),
    "NGSetupResponseIEs__value_PR_ServedGUAMIList": (
        "NGSetupResponseIEs__value_PR",
        False,
    ),
    "NGSetupResponseIEs__value_u": {
        "AMFName": ("AMFName_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PLMNSupportList": ("PLMNSupportList_t", False),
        "RelativeAMFCapacity": ("RelativeAMFCapacity_t", False),
        "ServedGUAMIList": ("ServedGUAMIList_t", False),
    },
    "NGSetupResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NGSetupResponseIEs__value", False),
    },
    "NGSetupResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P42_t", False),
    },
    "NRCellIdentity_t": ("BIT_STRING_t", False),
    "NRPPa_PDU_t": ("OCTET_STRING_t", False),
    "NR_CGIListForWarning_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct NR_CGI)", False),
    },
    "NR_CGIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct NR_CGI)", False),
    },
    "NR_CGI_ExtIEs__extensionValue_PR_NOTHING": (
        "NR_CGI_ExtIEs__extensionValue_PR",
        False,
    ),
    "NR_CGI_ExtIEs__extensionValue_u": {},
    "NR_CGI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct NR_CGI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "NR_CGI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "nRCellIdentity": ("NRCellIdentity_t", False),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "NRencryptionAlgorithms_t": ("BIT_STRING_t", False),
    "NRintegrityProtectionAlgorithms_t": ("BIT_STRING_t", False),
    "NasKeySetIdentifier_t": {
        "nasKeySetIdentifier": ("uint8_t", False),
        "tsc": ("uint8_t", False),
    },
    "NasSecurityAlgorithm_t": {
        "encryptionAlgo": ("uint8_t", False),
        "integrityAlgo": ("uint8_t", False),
    },
    "NaskeysetId_t": {
        "ngksi": ("uint8_t", False),
        "tsc": ("uint8_t", False),
        "uint8_t": ("", False),
    },
    "Nausf_UEAuthentication_Authenticate": ("JSON", False),
    "Nausf_UEAuthentication_Authenticate-response": ("JSON", False),
    "Nausf_auth": ("JSON", False),
    "Nausf_auth-response": ("JSON", False),
    "NetworkInstance_t": ("long", False),
    "NetworkSlicingIndication_t": {
        "dcni": ("uint8_t", False),
        "nssci": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "NewSecurityContextInd_t": ("long", False),
    "NewSecurityContextInd_true": ("e_NewSecurityContextInd", False),
    "NextHopChainingCount_t": ("long", False),
    "NextPagingAreaScope_changed": ("e_NextPagingAreaScope", False),
    "NextPagingAreaScope_same": ("e_NextPagingAreaScope", False),
    "NextPagingAreaScope_t": ("long", False),
    "NgENB_ID_ExtIEs__value_PR_NOTHING": ("NgENB_ID_ExtIEs__value_PR", False),
    "NgENB_ID_ExtIEs__value_u": {},
    "NgENB_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct NgENB_ID_ExtIEs__value", False),
    },
    "NgENB_ID_PR_NOTHING": ("NgENB_ID_PR", False),
    "NgENB_ID_PR_choice_Extensions": ("NgENB_ID_PR", False),
    "NgENB_ID_PR_longMacroNgENB_ID": ("NgENB_ID_PR", False),
    "NgENB_ID_PR_macroNgENB_ID": ("NgENB_ID_PR", False),
    "NgENB_ID_PR_shortMacroNgENB_ID": ("NgENB_ID_PR", False),
    "NgENB_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NgENB_ID_u", False),
        "present": ("NgENB_ID_PR", False),
    },
    "NgENB_ID_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "longMacroNgENB_ID": ("BIT_STRING_t", False),
        "macroNgENB_ID": ("BIT_STRING_t", False),
        "shortMacroNgENB_ID": ("BIT_STRING_t", False),
    },
    "Nnrf_disc": ("JSON", False),
    "Nnrf_disc-response": ("JSON", False),
    "NonDynamic5QIDescriptor_ExtIEs__extensionValue_PR_NOTHING": (
        "NonDynamic5QIDescriptor_ExtIEs__extensionValue_PR",
        False,
    ),
    "NonDynamic5QIDescriptor_ExtIEs__extensionValue_u": {},
    "NonDynamic5QIDescriptor_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "NonDynamic5QIDescriptor_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "NonDynamic5QIDescriptor_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "averagingWindow": ("AveragingWindow_t", True),
        "fiveQI": ("FiveQI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "maximumDataBurstVolume": ("MaximumDataBurstVolume_t", True),
        "priorityLevelQos": ("PriorityLevelQos_t", True),
    },
    "NotAllowedTACs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(TAC_t)", False),
    },
    "NotificationCause_fulfilled": ("e_NotificationCause", False),
    "NotificationCause_not_fulfilled": ("e_NotificationCause", False),
    "NotificationCause_t": ("long", False),
    "NotificationControl_notification_requested": ("e_NotificationControl", False),
    "NotificationControl_t": ("long", False),
    "Nudm_SDM_Get": ("JSON", False),
    "Nudm_SDM_Get-response": ("JSON", False),
    "Nudm_UECM_Registration": ("JSON", False),
    "Nudm_UECM_Registration-response": ("JSON", False),
    "NumberOfBroadcastsRequested_t": ("long", False),
    "NumberOfBroadcasts_t": ("long", False),
    "OBJECT_IDENTIFIER_t": ("ASN__PRIMITIVE_TYPE_t", False),
    "OCTET_STRING_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "buf": ("uint8_t", True),
        "size": ("size_t", False),
    },
    "OverloadAction_permit_emergency_sessions_and_mobile_terminated_services_only": (
        "e_OverloadAction",
        False,
    ),
    "OverloadAction_permit_high_priority_sessions_and_mobile_terminated_services_only": (
        "e_OverloadAction",
        False,
    ),
    "OverloadAction_reject_non_emergency_mo_dt": ("e_OverloadAction", False),
    "OverloadAction_reject_rrc_cr_signalling": ("e_OverloadAction", False),
    "OverloadAction_t": ("long", False),
    "OverloadResponse_ExtIEs__value_PR_NOTHING": (
        "OverloadResponse_ExtIEs__value_PR",
        False,
    ),
    "OverloadResponse_ExtIEs__value_u": {},
    "OverloadResponse_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "OverloadResponse_ExtIEs__value", False),
    },
    "OverloadResponse_PR_NOTHING": ("OverloadResponse_PR", False),
    "OverloadResponse_PR_choice_Extensions": ("OverloadResponse_PR", False),
    "OverloadResponse_PR_overloadAction": ("OverloadResponse_PR", False),
    "OverloadResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("OverloadResponse_u", False),
        "present": ("OverloadResponse_PR", False),
    },
    "OverloadResponse_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "overloadAction": ("OverloadAction_t", False),
    },
    "OverloadStartIEs__value_PR_NOTHING": ("OverloadStartIEs__value_PR", False),
    "OverloadStartIEs__value_PR_OverloadResponse": (
        "OverloadStartIEs__value_PR",
        False,
    ),
    "OverloadStartIEs__value_PR_OverloadStartNSSAIList": (
        "OverloadStartIEs__value_PR",
        False,
    ),
    "OverloadStartIEs__value_PR_TrafficLoadReductionIndication": (
        "OverloadStartIEs__value_PR",
        False,
    ),
    "OverloadStartIEs__value_u": {
        "OverloadResponse": ("OverloadResponse_t", False),
        "OverloadStartNSSAIList": ("OverloadStartNSSAIList_t", False),
        "TrafficLoadReductionIndication": ("TrafficLoadReductionIndication_t", False),
    },
    "OverloadStartIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct OverloadStartIEs__value", False),
    },
    "OverloadStartNSSAIItem_ExtIEs__extensionValue_PR_NOTHING": (
        "OverloadStartNSSAIItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "OverloadStartNSSAIItem_ExtIEs__extensionValue_u": {},
    "OverloadStartNSSAIItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "OverloadStartNSSAIItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "OverloadStartNSSAIItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "sliceOverloadList": ("SliceOverloadList_t", False),
        "sliceOverloadResponse": ("struct " "OverloadResponse", True),
        "sliceTrafficLoadReductionIndication": (
            "TrafficLoadReductionIndication_t",
            True,
        ),
    },
    "OverloadStartNSSAIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "OverloadStartNSSAIItem)", False),
    },
    "OverloadStart_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P54_t", False),
    },
    "OverloadStopIEs__value_PR_NOTHING": ("OverloadStopIEs__value_PR", False),
    "OverloadStopIEs__value_u": {},
    "OverloadStopIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct OverloadStopIEs__value", False),
    },
    "OverloadStop_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P55_t", False),
    },
    "PCP_DEI_TAG_t": {
        "dei": ("uint8_t", False),
        "pcp": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue_u": {},
    "PDUSessionAggregateMaximumBitRate_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionAggregateMaximumBitRate_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionAggregateMaximumBitRateDL": ("BitRate_t", False),
        "pDUSessionAggregateMaximumBitRateUL": ("BitRate_t", False),
    },
    "PDUSessionID_t": ("long", False),
    "PDUSessionId2_t": {"value": ("uint8_t", False)},
    "PDUSessionResourceAdmittedItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceAdmittedItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceAdmittedItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceAdmittedItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceAdmittedItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceAdmittedItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverRequestAcknowledgeTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceAdmittedList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceAdmittedItem)", False),
    },
    "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToModifyItemModCfm_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyIndicationUnsuccessfulTransfer": (
            "OCTET_STRING_t",
            False,
        ),
    },
    "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToModifyItemModRes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToModifyItemModRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceFailedToModifyListModCfm_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToModifyItemModCfm)",
            False,
        ),
    },
    "PDUSessionResourceFailedToModifyListModRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToModifyItemModRes)",
            False,
        ),
    },
    "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemCxtFail_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemCxtRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemHOAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverResourceAllocationUnsuccessfulTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemPSReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pathSwitchRequestSetupFailedTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceFailedToSetupItemSURes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceFailedToSetupItemSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceFailedToSetupListCxtFail_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemCxtFail)",
            False,
        ),
    },
    "PDUSessionResourceFailedToSetupListCxtRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemCxtRes)",
            False,
        ),
    },
    "PDUSessionResourceFailedToSetupListHOAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemHOAck)",
            False,
        ),
    },
    "PDUSessionResourceFailedToSetupListPSReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemPSReq)",
            False,
        ),
    },
    "PDUSessionResourceFailedToSetupListSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemSURes)",
            False,
        ),
    },
    "PDUSessionResourceHandoverItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceHandoverItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceHandoverItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceHandoverItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceHandoverItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceHandoverItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverCommandTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceHandoverList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceHandoverItem)", False),
    },
    "PDUSessionResourceInformationItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceInformationItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceInformationItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceInformationItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceInformationItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceInformationItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dRBsToQosFlowsMappingList": ("struct " "DRBsToQosFlowsMappingList", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "qosFlowInformationList": ("QosFlowInformationList_t", False),
    },
    "PDUSessionResourceInformationList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceInformationItem)", False),
    },
    "PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceItemCxtRelCpl_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceItemCxtRelCpl_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceItemCxtRelReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceItemCxtRelReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceItemHORqd_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceItemHORqd_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceItemHORqd_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceItemHORqd_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceItemHORqd_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceItemHORqd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverRequiredTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceListCxtRelCpl_t": {"_asn_ctx": ("asn_struct_ctx_t", False)},
    "PDUSessionResourceListCxtRelReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceItemCxtRelReq)", False),
    },
    "PDUSessionResourceListHORqd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceItemHORqd)", False),
    },
    "PDUSessionResourceModifyConfirmIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_PR_CriticalityDiagnostics": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_PR_NOTHING": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_PR_PDUSessionResourceFailedToModifyListModCfm": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_PR_PDUSessionResourceModifyListModCfm": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceModifyConfirmIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceFailedToModifyListModCfm": (
            "PDUSessionResourceFailedToModifyListModCfm_t",
            False,
        ),
        "PDUSessionResourceModifyListModCfm": (
            "PDUSessionResourceModifyListModCfm_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceModifyConfirmIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceModifyConfirmIEs__value", False),
    },
    "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyConfirmTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyConfirmTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowFailedToModifyList": ("struct " "QosFlowList", True),
        "qosFlowModifyConfirmList": ("QosFlowModifyConfirmList_t", False),
        "tNLMappingList": ("struct " "TNLMappingList", True),
    },
    "PDUSessionResourceModifyConfirm_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P10_t", False),
    },
    "PDUSessionResourceModifyIndicationIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceModifyIndicationIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationIEs__value_PR_NOTHING": (
        "PDUSessionResourceModifyIndicationIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationIEs__value_PR_PDUSessionResourceModifyListModInd": (
        "PDUSessionResourceModifyIndicationIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceModifyIndicationIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "PDUSessionResourceModifyListModInd": (
            "PDUSessionResourceModifyListModInd_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceModifyIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceModifyIndicationIEs__value", False),
    },
    "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyIndicationTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyIndicationTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_UP_TNLInformation": ("struct " "UP_TNLInformation", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceModifyIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P9_t", False),
    },
    "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyItemModCfm_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyItemModCfm_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyConfirmTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyItemModInd_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyItemModInd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyIndicationTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyItemModReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyItemModReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nAS_PDU": ("NAS_PDU_t", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyRequestTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyItemModRes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyItemModRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceModifyResponseTransfer": ("OCTET_STRING_t", True),
    },
    "PDUSessionResourceModifyListModCfm_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModCfm)", False),
    },
    "PDUSessionResourceModifyListModInd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModInd)", False),
    },
    "PDUSessionResourceModifyListModReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModReq)", False),
    },
    "PDUSessionResourceModifyListModRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModRes)", False),
    },
    "PDUSessionResourceModifyRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceModifyRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestIEs__value_PR_NOTHING": (
        "PDUSessionResourceModifyRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestIEs__value_PR_PDUSessionResourceModifyListModReq": (
        "PDUSessionResourceModifyRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestIEs__value_PR_RANPagingPriority": (
        "PDUSessionResourceModifyRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceModifyRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "PDUSessionResourceModifyListModReq": (
            "PDUSessionResourceModifyListModReq_t",
            False,
        ),
        "RANPagingPriority": ("RANPagingPriority_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceModifyRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceModifyRequestIEs__value", False),
    },
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_NOTHING": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_NetworkInstance": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_PDUSessionAggregateMaximumBitRate": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_QosFlowAddOrModifyRequestList": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_QosFlowList": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_UL_NGU_UP_TNLModifyList": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_PR_UPTransportLayerInformation": (
        "PDUSessionResourceModifyRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyRequestTransferIEs__value_u": {
        "NetworkInstance": ("NetworkInstance_t", False),
        "PDUSessionAggregateMaximumBitRate": (
            "PDUSessionAggregateMaximumBitRate_t",
            False,
        ),
        "QosFlowAddOrModifyRequestList": ("QosFlowAddOrModifyRequestList_t", False),
        "QosFlowList": ("QosFlowList_t", False),
        "UL_NGU_UP_TNLModifyList": ("UL_NGU_UP_TNLModifyList_t", False),
        "UPTransportLayerInformation": ("UPTransportLayerInformation_t", False),
    },
    "PDUSessionResourceModifyRequestTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceModifyRequestTransferIEs__value", False),
    },
    "PDUSessionResourceModifyRequestTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P0_t", False),
    },
    "PDUSessionResourceModifyRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P6_t", False),
    },
    "PDUSessionResourceModifyResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_CriticalityDiagnostics": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_NOTHING": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_PDUSessionResourceFailedToModifyListModRes": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_PDUSessionResourceModifyListModRes": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_PR_UserLocationInformation": (
        "PDUSessionResourceModifyResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceFailedToModifyListModRes": (
            "PDUSessionResourceFailedToModifyListModRes_t",
            False,
        ),
        "PDUSessionResourceModifyListModRes": (
            "PDUSessionResourceModifyListModRes_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "PDUSessionResourceModifyResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceModifyResponseIEs__value", False),
    },
    "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyResponseTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyResponseTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "additionalQosFlowPerTNLInformation": (
            "struct " "QosFlowPerTNLInformation",
            True,
        ),
        "dL_NGU_UP_TNLInformation": ("struct " "UPTransportLayerInformation", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowAddOrModifyResponseList": (
            "struct " "QosFlowAddOrModifyResponseList",
            True,
        ),
        "qosFlowFailedToAddOrModifyList": ("struct " "QosFlowList", True),
        "uL_NGU_UP_TNLInformation": ("struct " "UPTransportLayerInformation", True),
    },
    "PDUSessionResourceModifyResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P7_t", False),
    },
    "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceModifyUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "criticalityDiagnostics": ("struct " "CriticalityDiagnostics", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceNotifyIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_PR_NOTHING": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_PR_PDUSessionResourceNotifyList": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_PR_PDUSessionResourceReleasedListNot": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_PR_UserLocationInformation": (
        "PDUSessionResourceNotifyIEs__value_PR",
        False,
    ),
    "PDUSessionResourceNotifyIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "PDUSessionResourceNotifyList": ("PDUSessionResourceNotifyList_t", False),
        "PDUSessionResourceReleasedListNot": (
            "PDUSessionResourceReleasedListNot_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "PDUSessionResourceNotifyIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceNotifyIEs__value", False),
    },
    "PDUSessionResourceNotifyItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceNotifyItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceNotifyItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceNotifyItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceNotifyItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceNotifyItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceNotifyTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceNotifyList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceNotifyItem)", False),
    },
    "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceNotifyReleasedTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceNotifyReleasedTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceNotifyTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceNotifyTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowNotifyList": ("struct " "QosFlowNotifyList", True),
        "qosFlowReleasedList": ("struct " "QosFlowList", True),
    },
    "PDUSessionResourceNotify_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P8_t", False),
    },
    "PDUSessionResourceReleaseCommandIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_PR_NAS_PDU": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_PR_NOTHING": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_PR_PDUSessionResourceToReleaseListRelCmd": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_PR_RANPagingPriority": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceReleaseCommandIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "PDUSessionResourceToReleaseListRelCmd": (
            "PDUSessionResourceToReleaseListRelCmd_t",
            False,
        ),
        "RANPagingPriority": ("RANPagingPriority_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceReleaseCommandIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceReleaseCommandIEs__value", False),
    },
    "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleaseCommandTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleaseCommandTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceReleaseCommand_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P4_t", False),
    },
    "PDUSessionResourceReleaseResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_PR_CriticalityDiagnostics": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_PR_NOTHING": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_PR_PDUSessionResourceReleasedListRelRes": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_PR_UserLocationInformation": (
        "PDUSessionResourceReleaseResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceReleasedListRelRes": (
            "PDUSessionResourceReleasedListRelRes_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "PDUSessionResourceReleaseResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceReleaseResponseIEs__value", False),
    },
    "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleaseResponseTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleaseResponseTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceReleaseResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P5_t", False),
    },
    "PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleasedItemNot_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleasedItemNot_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceNotifyReleasedTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleasedItemPSAck_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleasedItemPSAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pathSwitchRequestUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleasedItemPSFail_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleasedItemPSFail_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pathSwitchRequestUnsuccessfulTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceReleasedItemRelRes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceReleasedItemRelRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceReleaseResponseTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceReleasedListNot_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemNot)", False),
    },
    "PDUSessionResourceReleasedListPSAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemPSAck)", False),
    },
    "PDUSessionResourceReleasedListPSFail_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemPSFail)",
            False,
        ),
    },
    "PDUSessionResourceReleasedListRelRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemRelRes)",
            False,
        ),
    },
    "PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupItemCxtReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupItemCxtReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nAS_PDU": ("NAS_PDU_t", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupRequestTransfer": ("OCTET_STRING_t", False),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupItemCxtRes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupItemCxtRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupResponseTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupItemHOReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupItemHOReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverRequestTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupItemSUReq_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupItemSUReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionNAS_PDU": ("NAS_PDU_t", True),
        "pDUSessionResourceSetupRequestTransfer": ("OCTET_STRING_t", False),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupItemSURes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupItemSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceSetupResponseTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceSetupListCxtReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemCxtReq)", False),
    },
    "PDUSessionResourceSetupListCxtRes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemCxtRes)", False),
    },
    "PDUSessionResourceSetupListHOReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemHOReq)", False),
    },
    "PDUSessionResourceSetupListSUReq_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemSUReq)", False),
    },
    "PDUSessionResourceSetupListSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemSURes)", False),
    },
    "PDUSessionResourceSetupRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_PR_NAS_PDU": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_PR_NOTHING": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_PR_PDUSessionResourceSetupListSUReq": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_PR_RANPagingPriority": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceSetupRequestIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "PDUSessionResourceSetupListSUReq": (
            "PDUSessionResourceSetupListSUReq_t",
            False,
        ),
        "RANPagingPriority": ("RANPagingPriority_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceSetupRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceSetupRequestIEs__value", False),
    },
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_DataForwardingNotPossible": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_NOTHING": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_NetworkInstance": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_PDUSessionAggregateMaximumBitRate": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_PDUSessionType": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_QosFlowSetupRequestList": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_SecurityIndication": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_UPTransportLayerInformation": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_PR_UPTransportLayerInformation_1": (
        "PDUSessionResourceSetupRequestTransferIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupRequestTransferIEs__value_u": {
        "DataForwardingNotPossible": ("DataForwardingNotPossible_t", False),
        "NetworkInstance": ("NetworkInstance_t", False),
        "PDUSessionAggregateMaximumBitRate": (
            "PDUSessionAggregateMaximumBitRate_t",
            False,
        ),
        "PDUSessionType": ("PDUSessionType_t", False),
        "QosFlowSetupRequestList": ("QosFlowSetupRequestList_t", False),
        "SecurityIndication": ("SecurityIndication_t", False),
        "UPTransportLayerInformation": ("UPTransportLayerInformation_t", False),
        "UPTransportLayerInformation_1": ("UPTransportLayerInformation_t", False),
    },
    "PDUSessionResourceSetupRequestTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceSetupRequestTransferIEs__value", False),
    },
    "PDUSessionResourceSetupRequestTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P1_t", False),
    },
    "PDUSessionResourceSetupRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P2_t", False),
    },
    "PDUSessionResourceSetupResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_PR_CriticalityDiagnostics": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_PR_NOTHING": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_PR_PDUSessionResourceFailedToSetupListSURes": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_PR_PDUSessionResourceSetupListSURes": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "PDUSessionResourceSetupResponseIEs__value_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceFailedToSetupListSURes": (
            "PDUSessionResourceFailedToSetupListSURes_t",
            False,
        ),
        "PDUSessionResourceSetupListSURes": (
            "PDUSessionResourceSetupListSURes_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PDUSessionResourceSetupResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PDUSessionResourceSetupResponseIEs__value", False),
    },
    "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupResponseTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupResponseTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "additionalQosFlowPerTNLInformation": (
            "struct " "QosFlowPerTNLInformation",
            True,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowFailedToSetupList": ("struct " "QosFlowList", True),
        "qosFlowPerTNLInformation": ("QosFlowPerTNLInformation_t", False),
        "securityResult": ("struct " "SecurityResult", True),
    },
    "PDUSessionResourceSetupResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P3_t", False),
    },
    "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSetupUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "criticalityDiagnostics": ("struct " "CriticalityDiagnostics", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PDUSessionResourceSwitchedItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceSwitchedItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceSwitchedItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceSwitchedItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceSwitchedItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceSwitchedItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pathSwitchRequestAcknowledgeTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceSwitchedList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSwitchedItem)", False),
    },
    "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceToBeSwitchedDLItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceToBeSwitchedDLItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pathSwitchRequestTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceToBeSwitchedDLList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToBeSwitchedDLItem)",
            False,
        ),
    },
    "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceToReleaseItemHOCmd_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceToReleaseItemHOCmd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "handoverPreparationUnsuccessfulTransfer": ("OCTET_STRING_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
    },
    "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue_PR_NOTHING": (
        "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue_PR",
        False,
    ),
    "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue_u": {},
    "PDUSessionResourceToReleaseItemRelCmd_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PDUSessionResourceToReleaseItemRelCmd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pDUSessionID": ("PDUSessionID_t", False),
        "pDUSessionResourceReleaseCommandTransfer": ("OCTET_STRING_t", False),
    },
    "PDUSessionResourceToReleaseListHOCmd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToReleaseItemHOCmd)",
            False,
        ),
    },
    "PDUSessionResourceToReleaseListRelCmd_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToReleaseItemRelCmd)",
            False,
        ),
    },
    "PDUSessionType_ethernet": ("e_PDUSessionType", False),
    "PDUSessionType_ipv4": ("e_PDUSessionType", False),
    "PDUSessionType_ipv4v6": ("e_PDUSessionType", False),
    "PDUSessionType_ipv6": ("e_PDUSessionType", False),
    "PDUSessionType_t": ("long", False),
    "PDUSessionType_unstructured": ("e_PDUSessionType", False),
    "PLMNIdentity_t": ("OCTET_STRING_t", False),
    "PLMNSupportItem_ExtIEs__extensionValue_PR_NOTHING": (
        "PLMNSupportItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "PLMNSupportItem_ExtIEs__extensionValue_u": {},
    "PLMNSupportItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "PLMNSupportItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PLMNSupportItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
        "sliceSupportList": ("SliceSupportList_t", False),
    },
    "PLMNSupportList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct PLMNSupportItem)", False),
    },
    "PWSCancelRequestIEs__value_PR_CancelAllWarningMessages": (
        "PWSCancelRequestIEs__value_PR",
        False,
    ),
    "PWSCancelRequestIEs__value_PR_MessageIdentifier": (
        "PWSCancelRequestIEs__value_PR",
        False,
    ),
    "PWSCancelRequestIEs__value_PR_NOTHING": ("PWSCancelRequestIEs__value_PR", False),
    "PWSCancelRequestIEs__value_PR_SerialNumber": (
        "PWSCancelRequestIEs__value_PR",
        False,
    ),
    "PWSCancelRequestIEs__value_PR_WarningAreaList": (
        "PWSCancelRequestIEs__value_PR",
        False,
    ),
    "PWSCancelRequestIEs__value_u": {
        "CancelAllWarningMessages": ("CancelAllWarningMessages_t", False),
        "MessageIdentifier": ("MessageIdentifier_t", False),
        "SerialNumber": ("SerialNumber_t", False),
        "WarningAreaList": ("WarningAreaList_t", False),
    },
    "PWSCancelRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct PWSCancelRequestIEs__value", False),
    },
    "PWSCancelRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P60_t", False),
    },
    "PWSCancelResponseIEs__value_PR_BroadcastCancelledAreaList": (
        "PWSCancelResponseIEs__value_PR",
        False,
    ),
    "PWSCancelResponseIEs__value_PR_CriticalityDiagnostics": (
        "PWSCancelResponseIEs__value_PR",
        False,
    ),
    "PWSCancelResponseIEs__value_PR_MessageIdentifier": (
        "PWSCancelResponseIEs__value_PR",
        False,
    ),
    "PWSCancelResponseIEs__value_PR_NOTHING": ("PWSCancelResponseIEs__value_PR", False),
    "PWSCancelResponseIEs__value_PR_SerialNumber": (
        "PWSCancelResponseIEs__value_PR",
        False,
    ),
    "PWSCancelResponseIEs__value_u": {
        "BroadcastCancelledAreaList": ("BroadcastCancelledAreaList_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "MessageIdentifier": ("MessageIdentifier_t", False),
        "SerialNumber": ("SerialNumber_t", False),
    },
    "PWSCancelResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct PWSCancelResponseIEs__value", False),
    },
    "PWSCancelResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P61_t", False),
    },
    "PWSFailedCellIDList_ExtIEs__value_PR_NOTHING": (
        "PWSFailedCellIDList_ExtIEs__value_PR",
        False,
    ),
    "PWSFailedCellIDList_ExtIEs__value_u": {},
    "PWSFailedCellIDList_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PWSFailedCellIDList_ExtIEs__value", False),
    },
    "PWSFailedCellIDList_PR_NOTHING": ("PWSFailedCellIDList_PR", False),
    "PWSFailedCellIDList_PR_choice_Extensions": ("PWSFailedCellIDList_PR", False),
    "PWSFailedCellIDList_PR_eUTRA_CGI_PWSFailedList": ("PWSFailedCellIDList_PR", False),
    "PWSFailedCellIDList_PR_nR_CGI_PWSFailedList": ("PWSFailedCellIDList_PR", False),
    "PWSFailedCellIDList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSFailedCellIDList_u", False),
        "present": ("PWSFailedCellIDList_PR", False),
    },
    "PWSFailedCellIDList_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "eUTRA_CGI_PWSFailedList": ("struct EUTRA_CGIList", True),
        "nR_CGI_PWSFailedList": ("struct NR_CGIList", True),
    },
    "PWSFailureIndicationIEs__value_PR_GlobalRANNodeID": (
        "PWSFailureIndicationIEs__value_PR",
        False,
    ),
    "PWSFailureIndicationIEs__value_PR_NOTHING": (
        "PWSFailureIndicationIEs__value_PR",
        False,
    ),
    "PWSFailureIndicationIEs__value_PR_PWSFailedCellIDList": (
        "PWSFailureIndicationIEs__value_PR",
        False,
    ),
    "PWSFailureIndicationIEs__value_u": {
        "GlobalRANNodeID": ("GlobalRANNodeID_t", False),
        "PWSFailedCellIDList": ("PWSFailedCellIDList_t", False),
    },
    "PWSFailureIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PWSFailureIndicationIEs__value", False),
    },
    "PWSFailureIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P63_t", False),
    },
    "PWSRestartIndicationIEs__value_PR_CellIDListForRestart": (
        "PWSRestartIndicationIEs__value_PR",
        False,
    ),
    "PWSRestartIndicationIEs__value_PR_EmergencyAreaIDListForRestart": (
        "PWSRestartIndicationIEs__value_PR",
        False,
    ),
    "PWSRestartIndicationIEs__value_PR_GlobalRANNodeID": (
        "PWSRestartIndicationIEs__value_PR",
        False,
    ),
    "PWSRestartIndicationIEs__value_PR_NOTHING": (
        "PWSRestartIndicationIEs__value_PR",
        False,
    ),
    "PWSRestartIndicationIEs__value_PR_TAIListForRestart": (
        "PWSRestartIndicationIEs__value_PR",
        False,
    ),
    "PWSRestartIndicationIEs__value_u": {
        "CellIDListForRestart": ("CellIDListForRestart_t", False),
        "EmergencyAreaIDListForRestart": ("EmergencyAreaIDListForRestart_t", False),
        "GlobalRANNodeID": ("GlobalRANNodeID_t", False),
        "TAIListForRestart": ("TAIListForRestart_t", False),
    },
    "PWSRestartIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PWSRestartIndicationIEs__value", False),
    },
    "PWSRestartIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P62_t", False),
    },
    "PXML_COMMENT": ("pxml_chunk_type_e", False),
    "PXML_COMMENT_END": ("pxml_chunk_type_e", False),
    "PXML_TAG": ("pxml_chunk_type_e", False),
    "PXML_TAG_END": ("pxml_chunk_type_e", False),
    "PXML_TEXT": ("pxml_chunk_type_e", False),
    "PacketDelayBudget_t": ("long", False),
    "PacketErrorRate_ExtIEs__extensionValue_PR_NOTHING": (
        "PacketErrorRate_ExtIEs__extensionValue_PR",
        False,
    ),
    "PacketErrorRate_ExtIEs__extensionValue_u": {},
    "PacketErrorRate_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "PacketErrorRate_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PacketErrorRate_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pERExponent": ("long", False),
        "pERScalar": ("long", False),
    },
    "PacketFilterContents_t": {"pfcMask": ("uint32_t", False)},
    "PacketFilterListCreate_t": {
        "lengthOfPacketFilterContents": ("uint8_t", False),
        "packetFilterContents": ("PacketFilterContents_t", False),
        "packetFilterDirection": ("uint8_t", False),
        "packetFilterIdentifier": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "PacketFilterListDelete_t": {
        "packetFilterIdentifier": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "PacketLossRate_t": ("long", False),
    "PagingAttemptCount_t": ("long", False),
    "PagingAttemptInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "PagingAttemptInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "PagingAttemptInformation_ExtIEs__extensionValue_u": {},
    "PagingAttemptInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PagingAttemptInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PagingAttemptInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "intendedNumberOfPagingAttempts": ("IntendedNumberOfPagingAttempts_t", False),
        "nextPagingAreaScope": ("NextPagingAreaScope_t", True),
        "pagingAttemptCount": ("PagingAttemptCount_t", False),
    },
    "PagingDRX_t": ("long", False),
    "PagingDRX_v128": ("e_PagingDRX", False),
    "PagingDRX_v256": ("e_PagingDRX", False),
    "PagingDRX_v32": ("e_PagingDRX", False),
    "PagingDRX_v64": ("e_PagingDRX", False),
    "PagingIEs__value_PR_AssistanceDataForPaging": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_NOTHING": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_PagingDRX": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_PagingOrigin": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_PagingPriority": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_TAIListForPaging": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_UEPagingIdentity": ("PagingIEs__value_PR", False),
    "PagingIEs__value_PR_UERadioCapabilityForPaging": ("PagingIEs__value_PR", False),
    "PagingIEs__value_u": {
        "AssistanceDataForPaging": ("AssistanceDataForPaging_t", False),
        "PagingDRX": ("PagingDRX_t", False),
        "PagingOrigin": ("PagingOrigin_t", False),
        "PagingPriority": ("PagingPriority_t", False),
        "TAIListForPaging": ("TAIListForPaging_t", False),
        "UEPagingIdentity": ("UEPagingIdentity_t", False),
        "UERadioCapabilityForPaging": ("UERadioCapabilityForPaging_t", False),
    },
    "PagingIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct PagingIEs__value", False),
    },
    "PagingOrigin_non_3gpp": ("e_PagingOrigin", False),
    "PagingOrigin_t": ("long", False),
    "PagingPriority_priolevel1": ("e_PagingPriority", False),
    "PagingPriority_priolevel2": ("e_PagingPriority", False),
    "PagingPriority_priolevel3": ("e_PagingPriority", False),
    "PagingPriority_priolevel4": ("e_PagingPriority", False),
    "PagingPriority_priolevel5": ("e_PagingPriority", False),
    "PagingPriority_priolevel6": ("e_PagingPriority", False),
    "PagingPriority_priolevel7": ("e_PagingPriority", False),
    "PagingPriority_priolevel8": ("e_PagingPriority", False),
    "PagingPriority_t": ("long", False),
    "Paging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P35_t", False),
    },
    "Parameter_t": {
        "lengthOfParameterContents": ("uint8_t", False),
        "parameterContents": ("uint8_t", True),
        "parameterIdentifier": ("uint8_t", False),
    },
    "PathSwitchRequestAcknowledgeIEs__value_PR_AMF_UE_NGAP_ID": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_AllowedNSSAI": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_CoreNetworkAssistanceInformation": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_NOTHING": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_NewSecurityContextInd": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_PDUSessionResourceReleasedListPSAck": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_PDUSessionResourceSwitchedList": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_RAN_UE_NGAP_ID": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_RRCInactiveTransitionReportRequest": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_SecurityContext": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_PR_UESecurityCapabilities": (
        "PathSwitchRequestAcknowledgeIEs__value_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "CoreNetworkAssistanceInformation": (
            "CoreNetworkAssistanceInformation_t",
            False,
        ),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "NewSecurityContextInd": ("NewSecurityContextInd_t", False),
        "PDUSessionResourceReleasedListPSAck": (
            "PDUSessionResourceReleasedListPSAck_t",
            False,
        ),
        "PDUSessionResourceSwitchedList": ("PDUSessionResourceSwitchedList_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCInactiveTransitionReportRequest": (
            "RRCInactiveTransitionReportRequest_t",
            False,
        ),
        "SecurityContext": ("SecurityContext_t", False),
        "UESecurityCapabilities": ("UESecurityCapabilities_t", False),
    },
    "PathSwitchRequestAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PathSwitchRequestAcknowledgeIEs__value", False),
    },
    "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue_u": {},
    "PathSwitchRequestAcknowledgeTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PathSwitchRequestAcknowledgeTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "securityIndication": ("struct " "SecurityIndication", True),
        "uL_NGU_UP_TNLInformation": ("struct " "UPTransportLayerInformation", True),
    },
    "PathSwitchRequestAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P29_t", False),
    },
    "PathSwitchRequestFailureIEs__value_PR_AMF_UE_NGAP_ID": (
        "PathSwitchRequestFailureIEs__value_PR",
        False,
    ),
    "PathSwitchRequestFailureIEs__value_PR_CriticalityDiagnostics": (
        "PathSwitchRequestFailureIEs__value_PR",
        False,
    ),
    "PathSwitchRequestFailureIEs__value_PR_NOTHING": (
        "PathSwitchRequestFailureIEs__value_PR",
        False,
    ),
    "PathSwitchRequestFailureIEs__value_PR_PDUSessionResourceReleasedListPSFail": (
        "PathSwitchRequestFailureIEs__value_PR",
        False,
    ),
    "PathSwitchRequestFailureIEs__value_PR_RAN_UE_NGAP_ID": (
        "PathSwitchRequestFailureIEs__value_PR",
        False,
    ),
    "PathSwitchRequestFailureIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "PDUSessionResourceReleasedListPSFail": (
            "PDUSessionResourceReleasedListPSFail_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "PathSwitchRequestFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "PathSwitchRequestFailureIEs__value", False),
    },
    "PathSwitchRequestFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P30_t", False),
    },
    "PathSwitchRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_PR_NOTHING": ("PathSwitchRequestIEs__value_PR", False),
    "PathSwitchRequestIEs__value_PR_PDUSessionResourceFailedToSetupListPSReq": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_PR_PDUSessionResourceToBeSwitchedDLList": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_PR_UESecurityCapabilities": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_PR_UserLocationInformation": (
        "PathSwitchRequestIEs__value_PR",
        False,
    ),
    "PathSwitchRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "PDUSessionResourceFailedToSetupListPSReq": (
            "PDUSessionResourceFailedToSetupListPSReq_t",
            False,
        ),
        "PDUSessionResourceToBeSwitchedDLList": (
            "PDUSessionResourceToBeSwitchedDLList_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UESecurityCapabilities": ("UESecurityCapabilities_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "PathSwitchRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct PathSwitchRequestIEs__value", False),
    },
    "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue_u": {},
    "PathSwitchRequestSetupFailedTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PathSwitchRequestSetupFailedTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PathSwitchRequestTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PathSwitchRequestTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PathSwitchRequestTransfer_ExtIEs__extensionValue_u": {},
    "PathSwitchRequestTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PathSwitchRequestTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PathSwitchRequestTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_NGU_TNLInformationReused": ("DL_NGU_TNLInformationReused_t", True),
        "dL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowAcceptedList": ("QosFlowAcceptedList_t", False),
        "userPlaneSecurityInformation": (
            "struct " "UserPlaneSecurityInformation",
            True,
        ),
    },
    "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue_u": {},
    "PathSwitchRequestUnsuccessfulTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "PathSwitchRequestUnsuccessfulTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "PathSwitchRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P28_t", False),
    },
    "PayloadContainer_t": {"Length": ("uint16_t", False), "content": ("uint8_t", True)},
    "PduSessionModificationCommand_t": {
        "alwaysOnPduSessionIndication": ("AlwaysOnPduSessionIndication_t", False),
        "authorizedQosFlowDescriptions": ("QosFlowDescriptions_t", False),
        "authorizedQosRules": ("QosRules_t", False),
        "extendedProtocolConfigurationOptions": (
            "ExtendedProtocolConfigurationOptions_t",
            False,
        ),
        "presenceMask": ("uint32_t", False),
        "rqTimerValue": ("GprsTimer_t", False),
        "sessionAmbr": ("SessionAmbr_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "PduSessionModificationComplete_t": {
        "_5gsmCause": ("_5gsmCause_t", False),
        "presenceMask": ("uint32_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "PduSessionModificationReject_t": {
        "_5gsmCause": ("_5gsmCause_t", False),
        "backOffTimerValue": ("GprsTimer3_t", False),
        "extendedProtocolConfigurationOptions": (
            "ExtendedProtocolConfigurationOptions_t",
            False,
        ),
        "presenceMask": ("uint32_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "PduSessionModificationRequest_t": {
        "_5gsmCause": ("_5gsmCause_t", False),
        "alwaysOnPduSessionRequested": ("AlwaysOnPduSessionRequested_t", False),
        "extendedProtocolConfigurationOptions": (
            "ExtendedProtocolConfigurationOptions_t",
            False,
        ),
        "integrityProtectionMaximumDataRate": (
            "IntegrityProtectionMaximumDataRate_t",
            False,
        ),
        "maximumNumberOfSupportedPacketFilters": (
            "MaximumNumberOfSupportedPacketFilters_t",
            False,
        ),
        "presenceMask": ("uint32_t", False),
        "requestedQosFlowDescriptions": ("QosFlowDescriptions_t", False),
        "requestedQosRules": ("QosRules_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "PeriodicRegistrationUpdateTimer_t": ("BIT_STRING_t", False),
    "PortNumber_t": ("OCTET_STRING_t", False),
    "PortRange_t": {"max": ("uint16_t", False), "min": ("uint16_t", False)},
    "Pre_emptionCapability_may_trigger_pre_emption": ("e_Pre_emptionCapability", False),
    "Pre_emptionCapability_shall_not_trigger_pre_emption": (
        "e_Pre_emptionCapability",
        False,
    ),
    "Pre_emptionCapability_t": ("long", False),
    "Pre_emptionVulnerability_not_pre_emptable": ("e_Pre_emptionVulnerability", False),
    "Pre_emptionVulnerability_pre_emptable": ("e_Pre_emptionVulnerability", False),
    "Pre_emptionVulnerability_t": ("long", False),
    "Presence_conditional": ("e_Presence", False),
    "Presence_mandatory": ("e_Presence", False),
    "Presence_optional": ("e_Presence", False),
    "Presence_t": ("long", False),
    "PrintableString_t": ("OCTET_STRING_t", False),
    "PriorityLevelARP_t": ("long", False),
    "PriorityLevelQos_t": ("long", False),
    "PrivateIE_Container_191P0_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PrivateMessageIEs)", False),
    },
    "PrivateIE_ID_PR_NOTHING": ("PrivateIE_ID_PR", False),
    "PrivateIE_ID_PR_global": ("PrivateIE_ID_PR", False),
    "PrivateIE_ID_PR_local": ("PrivateIE_ID_PR", False),
    "PrivateIE_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PrivateIE_ID_u", False),
        "present": ("PrivateIE_ID_PR", False),
    },
    "PrivateIE_ID_u": {
        "global": ("OBJECT_IDENTIFIER_t", False),
        "local": ("long", False),
    },
    "PrivateMessageIEs__value_PR_NOTHING": ("PrivateMessageIEs__value_PR", False),
    "PrivateMessageIEs__value_u": {},
    "PrivateMessageIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("PrivateIE_ID_t", False),
        "value": ("struct PrivateMessageIEs__value", False),
    },
    "PrivateMessage_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "privateIEs": ("PrivateIE_Container_191P0_t", False),
    },
    "ProcedureCode_t": ("long", False),
    "ProtocolExtensionContainer_175P0_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "AllocationAndRetentionPriority_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P100_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P101_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModRes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P102_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P103_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceNotifyItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P104_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceNotifyReleasedTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P105_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceNotifyTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P106_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleaseCommandTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P107_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemNot_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P108_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemPSAck_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P109_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemPSFail_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P10_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestTAIItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P110_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleasedItemRelRes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P111_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleaseResponseTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P112_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemCxtReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P113_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemCxtRes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P114_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemHOReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P115_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemSUReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P116_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupItemSURes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P117_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupResponseTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P118_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P119_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSwitchedItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P11_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AssistanceDataForPaging_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P120_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToBeSwitchedDLItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P121_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToReleaseItemHOCmd_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P122_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceToReleaseItemRelCmd_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P123_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PLMNSupportItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P124_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowAcceptedItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P125_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "QosFlowAddOrModifyRequestItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P126_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "QosFlowAddOrModifyResponseItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P127_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowInformationItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P128_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowLevelQosParameters_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P129_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P12_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "AssistanceDataForRecommendedCells_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P130_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowModifyConfirmItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P131_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowNotifyItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P132_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowPerTNLInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P133_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowSetupRequestItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P134_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "QosFlowSetupResponseItemHOReqAck_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P135_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "QosFlowSetupResponseItemSURes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P136_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowToBeForwardedItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P137_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "RANStatusTransfer_TransparentContainer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P138_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RATRestrictions_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P139_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RecommendedCellsForPaging_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P13_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AssociatedQosFlowItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P140_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RecommendedCellItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P141_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RecommendedRANNodesForPaging_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P142_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RecommendedRANNodeItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P143_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SecurityContext_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P144_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SecurityIndication_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P145_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SecurityResult_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P146_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ServedGUAMIItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P147_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ServiceAreaInformation_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P148_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SingleTNLInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P149_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SliceOverloadItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P14_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "BroadcastPLMNItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P150_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SliceSupportItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P151_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "S_NSSAI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P152_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SONConfigurationTransfer_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P153_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SONInformationReply_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P154_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P155_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SourceRANNodeID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P156_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "SupportedTAItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P157_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P158_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIBroadcastEUTRA_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P159_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIBroadcastNR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P15_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CancelledCellsInEAI_EUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P160_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAICancelledEUTRA_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P161_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAICancelledNR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P162_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIListForInactiveItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P163_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIListForPagingItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P164_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TargeteNB_ID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P165_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P166_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TargetRANNodeID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P167_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TNLAssociationItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P168_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TNLInformationItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P169_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TNLMappingItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P16_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInEAI_NR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P170_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TraceActivation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P171_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEAggregateMaximumBitRate_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P172_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "UE_associatedLogicalNG_connectionItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P173_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UE_NGAP_ID_pair_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P174_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "UEPresenceInAreaOfInterestItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P175_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UERadioCapabilityForPaging_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P176_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UESecurityCapabilities_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P177_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UL_NGU_UP_TNLModifyItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P178_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UnavailableGUAMIItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P179_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UserLocationInformationEUTRA_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P17_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CancelledCellsInTAI_EUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P180_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UserLocationInformationN3IWF_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P181_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UserLocationInformationNR_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P182_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UserPlaneSecurityInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P183_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "XnExtTLA_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P184_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "XnTNLConfigurationInfo_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P18_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CancelledCellsInTAI_NR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P19_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDBroadcastEUTRA_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P1_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AllowedNSSAI_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P20_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDBroadcastNR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P21_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDCancelledEUTRA_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P22_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellIDCancelledNR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P23_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellType_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P24_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CompletedCellsInEAI_EUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P25_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInEAI_NR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P26_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CompletedCellsInTAI_EUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P27_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CompletedCellsInTAI_NR_Item_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P28_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CoreNetworkAssistanceInformation_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P29_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "COUNTValueForPDCP_SN12_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P2_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationSetupItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P30_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "COUNTValueForPDCP_SN18_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P31_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CriticalityDiagnostics_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P32_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "CriticalityDiagnostics_IE_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P33_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "DataForwardingResponseDRBItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P34_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "DRBsSubjectToStatusTransferItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P35_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBStatusDL12_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P36_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBStatusDL18_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P37_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBStatusUL12_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P38_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBStatusUL18_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P39_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DRBsToQosFlowsMappingItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P3_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMF_TNLAssociationToAddItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P40_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "Dynamic5QIDescriptor_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P41_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P42_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "EmergencyAreaIDBroadcastNR_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P43_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P44_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "EmergencyAreaIDCancelledNR_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P45_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EmergencyFallbackIndicator_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P46_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EPS_TAI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P47_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "E_RABInformationItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P48_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "EUTRA_CGI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P49_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ExpectedUEActivityBehaviour_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P4_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "AMF_TNLAssociationToRemoveItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P50_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ExpectedUEBehaviour_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P51_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "ExpectedUEMovingTrajectoryItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P52_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "FiveG_S_TMSI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P53_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "ForbiddenAreaInformation_Item_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P54_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GBR_QosInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P55_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GlobalGNB_ID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P56_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GlobalN3IWF_ID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P57_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GlobalNgENB_ID_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P58_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GTPTunnel_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P59_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "GUAMI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P5_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "AMF_TNLAssociationToUpdateItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P60_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverCommandTransfer_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P61_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "HandoverPreparationUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P62_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "HandoverRequestAcknowledgeTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P63_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverRequiredTransfer_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P64_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P65_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P66_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "LastVisitedCellItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P67_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "LastVisitedNGRANCellInformation_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P68_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "LocationReportingRequestType_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P69_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "MobilityRestrictionList_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P6_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterest_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P70_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "MultipleTNLInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P71_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NonDynamic5QIDescriptor_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P72_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NR_CGI_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P73_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "OverloadStartNSSAIItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P74_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PacketErrorRate_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P75_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PagingAttemptInformation_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P76_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PathSwitchRequestAcknowledgeTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P77_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PathSwitchRequestSetupFailedTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P78_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PathSwitchRequestTransfer_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P79_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PathSwitchRequestUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P7_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestCellItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P80_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionAggregateMaximumBitRate_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P81_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceAdmittedItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P82_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P83_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceFailedToModifyItemModRes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P84_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P85_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P86_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P87_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P88_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceFailedToSetupItemSURes_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P89_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceHandoverItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P8_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestItem_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P90_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceInformationItem_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P91_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceItemCxtRelCpl_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P92_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceItemCxtRelReq_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P93_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceItemHORqd_ExtIEs)", False),
    },
    "ProtocolExtensionContainer_175P94_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyConfirmTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P95_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P96_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyResponseTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P97_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct "
            "PDUSessionResourceModifyIndicationTransfer_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P98_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModCfm_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P99_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyItemModInd_ExtIEs)",
            False,
        ),
    },
    "ProtocolExtensionContainer_175P9_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AreaOfInterestRANNodeItem_ExtIEs)", False),
    },
    "ProtocolExtensionID_t": ("long", False),
    "ProtocolIE_Container_124P0_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyRequestTransferIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P10_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyConfirmIEs)", False),
    },
    "ProtocolIE_Container_124P11_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "InitialContextSetupRequestIEs)", False),
    },
    "ProtocolIE_Container_124P12_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "InitialContextSetupResponseIEs)", False),
    },
    "ProtocolIE_Container_124P13_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "InitialContextSetupFailureIEs)", False),
    },
    "ProtocolIE_Container_124P14_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextReleaseRequest_IEs)", False),
    },
    "ProtocolIE_Container_124P15_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextReleaseCommand_IEs)", False),
    },
    "ProtocolIE_Container_124P16_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextReleaseComplete_IEs)", False),
    },
    "ProtocolIE_Container_124P17_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextModificationRequestIEs)", False),
    },
    "ProtocolIE_Container_124P18_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextModificationResponseIEs)", False),
    },
    "ProtocolIE_Container_124P19_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEContextModificationFailureIEs)", False),
    },
    "ProtocolIE_Container_124P1_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceSetupRequestTransferIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P20_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RRCInactiveTransitionReportIEs)", False),
    },
    "ProtocolIE_Container_124P21_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverRequiredIEs)", False),
    },
    "ProtocolIE_Container_124P22_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverCommandIEs)", False),
    },
    "ProtocolIE_Container_124P23_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverPreparationFailureIEs)", False),
    },
    "ProtocolIE_Container_124P24_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverRequestIEs)", False),
    },
    "ProtocolIE_Container_124P25_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverRequestAcknowledgeIEs)", False),
    },
    "ProtocolIE_Container_124P26_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverFailureIEs)", False),
    },
    "ProtocolIE_Container_124P27_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverNotifyIEs)", False),
    },
    "ProtocolIE_Container_124P28_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PathSwitchRequestIEs)", False),
    },
    "ProtocolIE_Container_124P29_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PathSwitchRequestAcknowledgeIEs)", False),
    },
    "ProtocolIE_Container_124P2_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupRequestIEs)", False),
    },
    "ProtocolIE_Container_124P30_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PathSwitchRequestFailureIEs)", False),
    },
    "ProtocolIE_Container_124P31_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverCancelIEs)", False),
    },
    "ProtocolIE_Container_124P32_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "HandoverCancelAcknowledgeIEs)", False),
    },
    "ProtocolIE_Container_124P33_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UplinkRANStatusTransferIEs)", False),
    },
    "ProtocolIE_Container_124P34_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DownlinkRANStatusTransferIEs)", False),
    },
    "ProtocolIE_Container_124P35_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct PagingIEs)", False),
    },
    "ProtocolIE_Container_124P36_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "InitialUEMessage_IEs)", False),
    },
    "ProtocolIE_Container_124P37_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DownlinkNASTransport_IEs)", False),
    },
    "ProtocolIE_Container_124P38_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UplinkNASTransport_IEs)", False),
    },
    "ProtocolIE_Container_124P39_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NASNonDeliveryIndication_IEs)", False),
    },
    "ProtocolIE_Container_124P3_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceSetupResponseIEs)", False),
    },
    "ProtocolIE_Container_124P40_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RerouteNASRequest_IEs)", False),
    },
    "ProtocolIE_Container_124P41_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NGSetupRequestIEs)", False),
    },
    "ProtocolIE_Container_124P42_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NGSetupResponseIEs)", False),
    },
    "ProtocolIE_Container_124P43_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NGSetupFailureIEs)", False),
    },
    "ProtocolIE_Container_124P44_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RANConfigurationUpdateIEs)", False),
    },
    "ProtocolIE_Container_124P45_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "RANConfigurationUpdateAcknowledgeIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P46_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RANConfigurationUpdateFailureIEs)", False),
    },
    "ProtocolIE_Container_124P47_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMFConfigurationUpdateIEs)", False),
    },
    "ProtocolIE_Container_124P48_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "AMFConfigurationUpdateAcknowledgeIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P49_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMFConfigurationUpdateFailureIEs)", False),
    },
    "ProtocolIE_Container_124P4_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceReleaseCommandIEs)", False),
    },
    "ProtocolIE_Container_124P50_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "AMFStatusIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P51_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct NGResetIEs)", False),
    },
    "ProtocolIE_Container_124P52_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "NGResetAcknowledgeIEs)", False),
    },
    "ProtocolIE_Container_124P53_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ErrorIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P54_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "OverloadStartIEs)", False),
    },
    "ProtocolIE_Container_124P55_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "OverloadStopIEs)", False),
    },
    "ProtocolIE_Container_124P56_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UplinkRANConfigurationTransferIEs)", False),
    },
    "ProtocolIE_Container_124P57_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DownlinkRANConfigurationTransferIEs)", False),
    },
    "ProtocolIE_Container_124P58_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "WriteReplaceWarningRequestIEs)", False),
    },
    "ProtocolIE_Container_124P59_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "WriteReplaceWarningResponseIEs)", False),
    },
    "ProtocolIE_Container_124P5_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceReleaseResponseIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P60_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PWSCancelRequestIEs)", False),
    },
    "ProtocolIE_Container_124P61_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PWSCancelResponseIEs)", False),
    },
    "ProtocolIE_Container_124P62_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PWSRestartIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P63_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PWSFailureIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P64_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "DownlinkUEAssociatedNRPPaTransportIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P65_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UplinkUEAssociatedNRPPaTransportIEs)", False),
    },
    "ProtocolIE_Container_124P66_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "DownlinkNonUEAssociatedNRPPaTransportIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P67_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "UplinkNonUEAssociatedNRPPaTransportIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P68_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TraceStartIEs)", False),
    },
    "ProtocolIE_Container_124P69_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TraceFailureIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P6_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyRequestIEs)", False),
    },
    "ProtocolIE_Container_124P70_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "DeactivateTraceIEs)", False),
    },
    "ProtocolIE_Container_124P71_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "CellTrafficTraceIEs)", False),
    },
    "ProtocolIE_Container_124P72_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "LocationReportingControlIEs)", False),
    },
    "ProtocolIE_Container_124P73_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "LocationReportingFailureIndicationIEs)",
            False,
        ),
    },
    "ProtocolIE_Container_124P74_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "LocationReportIEs)", False),
    },
    "ProtocolIE_Container_124P75_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UETNLABindingReleaseRequestIEs)", False),
    },
    "ProtocolIE_Container_124P76_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UERadioCapabilityInfoIndicationIEs)", False),
    },
    "ProtocolIE_Container_124P77_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UERadioCapabilityCheckRequestIEs)", False),
    },
    "ProtocolIE_Container_124P78_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UERadioCapabilityCheckResponseIEs)", False),
    },
    "ProtocolIE_Container_124P7_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceModifyResponseIEs)", False),
    },
    "ProtocolIE_Container_124P8_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "PDUSessionResourceNotifyIEs)", False),
    },
    "ProtocolIE_Container_124P9_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "PDUSessionResourceModifyIndicationIEs)",
            False,
        ),
    },
    "ProtocolIE_ID_t": ("long", False),
    "ProtocolIE_SingleContainer_127P0_t": ("AMFPagingTarget_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P10_t": (
        "LastVisitedCellInformation_ExtIEs_t",
        False,
    ),
    "ProtocolIE_SingleContainer_127P11_t": ("N3IWF_ID_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P12_t": ("NgENB_ID_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P13_t": ("NGRAN_CGI_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P14_t": ("OverloadResponse_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P15_t": ("PWSFailedCellIDList_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P16_t": ("QosCharacteristics_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P17_t": ("ResetType_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P18_t": ("SONInformation_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P19_t": ("TargetID_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P1_t": (
        "BroadcastCancelledAreaList_ExtIEs_t",
        False,
    ),
    "ProtocolIE_SingleContainer_127P20_t": ("UEIdentityIndexValue_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P21_t": ("UE_NGAP_IDs_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P22_t": ("UEPagingIdentity_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P23_t": ("UP_TNLInformation_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P24_t": (
        "UPTransportLayerInformation_ExtIEs_t",
        False,
    ),
    "ProtocolIE_SingleContainer_127P25_t": ("UserLocationInformation_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P26_t": ("WarningAreaList_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P2_t": (
        "BroadcastCompletedAreaList_ExtIEs_t",
        False,
    ),
    "ProtocolIE_SingleContainer_127P3_t": ("Cause_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P4_t": ("CellIDListForRestart_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P5_t": (
        "CPTransportLayerInformation_ExtIEs_t",
        False,
    ),
    "ProtocolIE_SingleContainer_127P6_t": ("DRBStatusDL_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P7_t": ("DRBStatusUL_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P8_t": ("GlobalRANNodeID_ExtIEs_t", False),
    "ProtocolIE_SingleContainer_127P9_t": ("GNB_ID_ExtIEs_t", False),
    "QFI_t": {"IEI": ("uint16_t", False), "value": ("uint8_t", False)},
    "QerCorrelationID_t": {"IEI": ("uint16_t", False), "value": ("uint32_t", False)},
    "QosCharacteristics_ExtIEs__value_PR_NOTHING": (
        "QosCharacteristics_ExtIEs__value_PR",
        False,
    ),
    "QosCharacteristics_ExtIEs__value_u": {},
    "QosCharacteristics_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "QosCharacteristics_ExtIEs__value", False),
    },
    "QosCharacteristics_PR_NOTHING": ("QosCharacteristics_PR", False),
    "QosCharacteristics_PR_choice_Extensions": ("QosCharacteristics_PR", False),
    "QosCharacteristics_PR_dynamic5QI": ("QosCharacteristics_PR", False),
    "QosCharacteristics_PR_nonDynamic5QI": ("QosCharacteristics_PR", False),
    "QosCharacteristics_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosCharacteristics_u", False),
        "present": ("QosCharacteristics_PR", False),
    },
    "QosCharacteristics_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "dynamic5QI": ("struct Dynamic5QIDescriptor", True),
        "nonDynamic5QI": ("struct NonDynamic5QIDescriptor", True),
    },
    "QosFlowAcceptedItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowAcceptedItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowAcceptedItem_ExtIEs__extensionValue_u": {},
    "QosFlowAcceptedItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowAcceptedItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowAcceptedItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowAcceptedList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct QosFlowAcceptedItem)", False),
    },
    "QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue_u": {},
    "QosFlowAddOrModifyRequestItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowAddOrModifyRequestItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "e_RAB_ID": ("E_RAB_ID_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
        "qosFlowLevelQosParameters": ("struct " "QosFlowLevelQosParameters", True),
    },
    "QosFlowAddOrModifyRequestList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowAddOrModifyRequestItem)", False),
    },
    "QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue_u": {},
    "QosFlowAddOrModifyResponseItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowAddOrModifyResponseItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowAddOrModifyResponseList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowAddOrModifyResponseItem)", False),
    },
    "QosFlowDescription_t": {
        "e": ("uint8_t", False),
        "numberOfParameters": ("uint8_t", False),
        "operationCode": ("uint8_t", False),
        "parameter": ("Parameter_t", True),
        "qfi": ("uint8_t", False),
        "spare1": ("uint8_t", False),
        "spare2": ("uint8_t", False),
        "spare3": ("uint8_t", False),
    },
    "QosFlowDescriptions_t": {
        "lengthOfQosFlowDescriptionsContents": ("uint16_t", False),
        "noOfQosFlowDescription": ("uint8_t", False),
        "qosFlowDescription": ("QosFlowDescription_t", True),
    },
    "QosFlowIdentifier_t": ("long", False),
    "QosFlowInformationItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowInformationItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowInformationItem_ExtIEs__extensionValue_u": {},
    "QosFlowInformationItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowInformationItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowInformationItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dLForwarding": ("DLForwarding_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowInformationList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowInformationItem)", False),
    },
    "QosFlowItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowItem_ExtIEs__extensionValue_u": {},
    "QosFlowItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "QosFlowItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowLevelQosParameters_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowLevelQosParameters_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowLevelQosParameters_ExtIEs__extensionValue_u": {},
    "QosFlowLevelQosParameters_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowLevelQosParameters_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowLevelQosParameters_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "additionalQosFlowInformation": ("AdditionalQosFlowInformation_t", True),
        "allocationAndRetentionPriority": ("AllocationAndRetentionPriority_t", False),
        "gBR_QosInformation": ("struct " "GBR_QosInformation", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosCharacteristics": ("QosCharacteristics_t", False),
        "reflectiveQosAttribute": ("ReflectiveQosAttribute_t", True),
    },
    "QosFlowList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct QosFlowItem)", False),
    },
    "QosFlowModifyConfirmItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowModifyConfirmItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowModifyConfirmItem_ExtIEs__extensionValue_u": {},
    "QosFlowModifyConfirmItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowModifyConfirmItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowModifyConfirmItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowModifyConfirmList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowModifyConfirmItem)", False),
    },
    "QosFlowNotifyItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowNotifyItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowNotifyItem_ExtIEs__extensionValue_u": {},
    "QosFlowNotifyItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "QosFlowNotifyItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowNotifyItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "notificationCause": ("NotificationCause_t", False),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowNotifyList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct QosFlowNotifyItem)", False),
    },
    "QosFlowPerTNLInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowPerTNLInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowPerTNLInformation_ExtIEs__extensionValue_u": {},
    "QosFlowPerTNLInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowPerTNLInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowPerTNLInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "associatedQosFlowList": ("AssociatedQosFlowList_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uPTransportLayerInformation": ("UPTransportLayerInformation_t", False),
    },
    "QosFlowSetupRequestItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowSetupRequestItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowSetupRequestItem_ExtIEs__extensionValue_u": {},
    "QosFlowSetupRequestItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowSetupRequestItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowSetupRequestItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "e_RAB_ID": ("E_RAB_ID_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
        "qosFlowLevelQosParameters": ("QosFlowLevelQosParameters_t", False),
    },
    "QosFlowSetupRequestList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowSetupRequestItem)", False),
    },
    "QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue_u": {},
    "QosFlowSetupResponseItemHOReqAck_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowSetupResponseItemHOReqAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dataForwardingAccepted": ("DataForwardingAccepted_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowSetupResponseItemSURes_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowSetupResponseItemSURes_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowSetupResponseItemSURes_ExtIEs__extensionValue_u": {},
    "QosFlowSetupResponseItemSURes_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowSetupResponseItemSURes_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowSetupResponseItemSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowSetupResponseListHOReqAck_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowSetupResponseItemHOReqAck)", False),
    },
    "QosFlowSetupResponseListSURes_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowSetupResponseItemSURes)", False),
    },
    "QosFlowToBeForwardedItem_ExtIEs__extensionValue_PR_NOTHING": (
        "QosFlowToBeForwardedItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "QosFlowToBeForwardedItem_ExtIEs__extensionValue_u": {},
    "QosFlowToBeForwardedItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "QosFlowToBeForwardedItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "QosFlowToBeForwardedItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "qosFlowIdentifier": ("QosFlowIdentifier_t", False),
    },
    "QosFlowToBeForwardedList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "QosFlowToBeForwardedItem)", False),
    },
    "QosRule_t": {
        "dqrBit": ("uint8_t", False),
        "lengthOfQosRule": ("uint16_t", False),
        "numberOfPacketFilters": ("uint8_t", False),
        "packetFilterListChoice": ("packetFilterList", False),
        "qfi": ("uint8_t", False),
        "qosRuleIdentifier": ("uint8_t", False),
        "qosRulePrecedence": ("uint8_t", False),
        "ruleOperationCode": ("uint8_t", False),
        "segregation": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "QosRules_t": {
        "lengthOfQosRulesIe": ("uint16_t", False),
        "noOfQosRule": ("uint8_t", False),
        "qosRule": ("QosRule_t", True),
    },
    "RANConfigurationUpdateAcknowledgeIEs__value_PR_CriticalityDiagnostics": (
        "RANConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateAcknowledgeIEs__value_PR_NOTHING": (
        "RANConfigurationUpdateAcknowledgeIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateAcknowledgeIEs__value_u": {
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False)
    },
    "RANConfigurationUpdateAcknowledgeIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "RANConfigurationUpdateAcknowledgeIEs__value", False),
    },
    "RANConfigurationUpdateAcknowledge_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P45_t", False),
    },
    "RANConfigurationUpdateFailureIEs__value_PR_Cause": (
        "RANConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateFailureIEs__value_PR_CriticalityDiagnostics": (
        "RANConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateFailureIEs__value_PR_NOTHING": (
        "RANConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateFailureIEs__value_PR_TimeToWait": (
        "RANConfigurationUpdateFailureIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateFailureIEs__value_u": {
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "TimeToWait": ("TimeToWait_t", False),
    },
    "RANConfigurationUpdateFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "RANConfigurationUpdateFailureIEs__value", False),
    },
    "RANConfigurationUpdateFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P46_t", False),
    },
    "RANConfigurationUpdateIEs__value_PR_NOTHING": (
        "RANConfigurationUpdateIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateIEs__value_PR_PagingDRX": (
        "RANConfigurationUpdateIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateIEs__value_PR_RANNodeName": (
        "RANConfigurationUpdateIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateIEs__value_PR_SupportedTAList": (
        "RANConfigurationUpdateIEs__value_PR",
        False,
    ),
    "RANConfigurationUpdateIEs__value_u": {
        "PagingDRX": ("PagingDRX_t", False),
        "RANNodeName": ("RANNodeName_t", False),
        "SupportedTAList": ("SupportedTAList_t", False),
    },
    "RANConfigurationUpdateIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "RANConfigurationUpdateIEs__value", False),
    },
    "RANConfigurationUpdate_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P44_t", False),
    },
    "RAND_t": {"RAND": ("uint8_t", True)},
    "RANNodeName_t": ("PrintableString_t", False),
    "RANPagingPriority_t": ("long", False),
    "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue_PR_NOTHING": (
        "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue_PR",
        False,
    ),
    "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue_u": {},
    "RANStatusTransfer_TransparentContainer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RANStatusTransfer_TransparentContainer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dRBsSubjectToStatusTransferList": ("DRBsSubjectToStatusTransferList_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "RAN_UE_NGAP_ID_t": ("long", False),
    "RATRestrictionInformation_t": ("BIT_STRING_t", False),
    "RATRestrictions_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "RATRestrictions_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "RATRestrictions_Item_ExtIEs__extensionValue_u": {},
    "RATRestrictions_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RATRestrictions_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RATRestrictions_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
        "rATRestrictionInformation": ("RATRestrictionInformation_t", False),
    },
    "RATRestrictions_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct RATRestrictions_Item)", False),
    },
    "RRCContainer_t": ("OCTET_STRING_t", False),
    "RRCEstablishmentCause_emergency": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_highPriorityAccess": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mcs_PriorityAccess": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mo_Data": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mo_SMS": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mo_Signalling": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mo_VideoCall": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mo_VoiceCall": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mps_PriorityAccess": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_mt_Access": ("e_RRCEstablishmentCause", False),
    "RRCEstablishmentCause_t": ("long", False),
    "RRCInactiveTransitionReportIEs__value_PR_AMF_UE_NGAP_ID": (
        "RRCInactiveTransitionReportIEs__value_PR",
        False,
    ),
    "RRCInactiveTransitionReportIEs__value_PR_NOTHING": (
        "RRCInactiveTransitionReportIEs__value_PR",
        False,
    ),
    "RRCInactiveTransitionReportIEs__value_PR_RAN_UE_NGAP_ID": (
        "RRCInactiveTransitionReportIEs__value_PR",
        False,
    ),
    "RRCInactiveTransitionReportIEs__value_PR_RRCState": (
        "RRCInactiveTransitionReportIEs__value_PR",
        False,
    ),
    "RRCInactiveTransitionReportIEs__value_PR_UserLocationInformation": (
        "RRCInactiveTransitionReportIEs__value_PR",
        False,
    ),
    "RRCInactiveTransitionReportIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCState": ("RRCState_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "RRCInactiveTransitionReportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "RRCInactiveTransitionReportIEs__value", False),
    },
    "RRCInactiveTransitionReportRequest_cancel_report": (
        "e_RRCInactiveTransitionReportRequest",
        False,
    ),
    "RRCInactiveTransitionReportRequest_single_rrc_connected_state_report": (
        "e_RRCInactiveTransitionReportRequest",
        False,
    ),
    "RRCInactiveTransitionReportRequest_subsequent_state_transition_report": (
        "e_RRCInactiveTransitionReportRequest",
        False,
    ),
    "RRCInactiveTransitionReportRequest_t": ("long", False),
    "RRCInactiveTransitionReport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P20_t", False),
    },
    "RRCState_connected": ("e_RRCState", False),
    "RRCState_inactive": ("e_RRCState", False),
    "RRCState_t": ("long", False),
    "RecommendedCellItem_ExtIEs__extensionValue_PR_NOTHING": (
        "RecommendedCellItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "RecommendedCellItem_ExtIEs__extensionValue_u": {},
    "RecommendedCellItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RecommendedCellItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RecommendedCellItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nGRAN_CGI": ("NGRAN_CGI_t", False),
        "timeStayedInCell": ("long", True),
    },
    "RecommendedCellList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct RecommendedCellItem)", False),
    },
    "RecommendedCellsForPaging_ExtIEs__extensionValue_PR_NOTHING": (
        "RecommendedCellsForPaging_ExtIEs__extensionValue_PR",
        False,
    ),
    "RecommendedCellsForPaging_ExtIEs__extensionValue_u": {},
    "RecommendedCellsForPaging_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RecommendedCellsForPaging_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RecommendedCellsForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "recommendedCellList": ("RecommendedCellList_t", False),
    },
    "RecommendedRANNodeItem_ExtIEs__extensionValue_PR_NOTHING": (
        "RecommendedRANNodeItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "RecommendedRANNodeItem_ExtIEs__extensionValue_u": {},
    "RecommendedRANNodeItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RecommendedRANNodeItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RecommendedRANNodeItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMFPagingTarget": ("AMFPagingTarget_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
    },
    "RecommendedRANNodeList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "RecommendedRANNodeItem)", False),
    },
    "RecommendedRANNodesForPaging_ExtIEs__extensionValue_PR_NOTHING": (
        "RecommendedRANNodesForPaging_ExtIEs__extensionValue_PR",
        False,
    ),
    "RecommendedRANNodesForPaging_ExtIEs__extensionValue_u": {},
    "RecommendedRANNodesForPaging_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "RecommendedRANNodesForPaging_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "RecommendedRANNodesForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "recommendedRANNodeList": ("RecommendedRANNodeList_t", False),
    },
    "ReferenceID_t": ("long", False),
    "ReflectiveQosAttribute_subject_to": ("e_ReflectiveQosAttribute", False),
    "ReflectiveQosAttribute_t": ("long", False),
    "RegistrationAcceptMsg_t": {
        "_5gmobileId": ("_5gMobileId_t", False),
        "_5gregResult": ("_5gRegistrationResult_t", False),
        "allowedNssai": ("nssai_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "pduSessionResult": ("pduSessionResult_t", False),
        "pduSessionResultCause": ("pduSessionResultCause_t", False),
        "pduSessionStatus": ("pduSessionStatus_t", False),
        "presenceMask": ("uint32_t", False),
        "rejectedNssai": ("rejectedNssai_t", False),
        "taiList": ("tAIList_t", False),
        "timer3512": ("t3512_t", False),
    },
    "RegistrationCompleteMsg_t": {"mmHeader": ("_5gmmMsgHeader_t", False)},
    "RegistrationReject_t": {
        "_5gmmCause": ("uint8_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
    },
    "RegistrationRequest_t": {
        "_5gmmCapability": ("_5gmmCapability_t", False),
        "_5gmobileId": ("_5gMobileId_t", False),
        "_5gregType": ("_5gRegistrationType_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "ngKsi": ("NaskeysetId_t", False),
        "pduSessionStatus": ("pduSessionStatus_t", False),
        "presenceMask": ("uint32_t", False),
        "requestedNssai": ("nssai_t", False),
        "ueSecuCapability": ("UeSecurityCapability_t", False),
        "uplinkDataStatus": ("UplinkDataStatus_t", False),
    },
    "RelativeAMFCapacity_t": ("long", False),
    "RepetitionPeriod_t": ("long", False),
    "ReportArea_cell": ("e_ReportArea", False),
    "ReportArea_t": ("long", False),
    "RerouteNASRequest_IEs__value_PR_AMFSetID": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_PR_AMF_UE_NGAP_ID": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_PR_AllowedNSSAI": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_PR_NOTHING": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_PR_OCTET_STRING": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_PR_RAN_UE_NGAP_ID": (
        "RerouteNASRequest_IEs__value_PR",
        False,
    ),
    "RerouteNASRequest_IEs__value_u": {
        "AMFSetID": ("AMFSetID_t", False),
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AllowedNSSAI": ("AllowedNSSAI_t", False),
        "OCTET_STRING": ("OCTET_STRING_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "RerouteNASRequest_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct RerouteNASRequest_IEs__value", False),
    },
    "RerouteNASRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P40_t", False),
    },
    "ResetAll_reset_all": ("e_ResetAll", False),
    "ResetAll_t": ("long", False),
    "ResetType_ExtIEs__value_PR_NOTHING": ("ResetType_ExtIEs__value_PR", False),
    "ResetType_ExtIEs__value_u": {},
    "ResetType_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct ResetType_ExtIEs__value", False),
    },
    "ResetType_PR_NOTHING": ("ResetType_PR", False),
    "ResetType_PR_choice_Extensions": ("ResetType_PR", False),
    "ResetType_PR_nG_Interface": ("ResetType_PR", False),
    "ResetType_PR_partOfNG_Interface": ("ResetType_PR", False),
    "ResetType_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ResetType_u", False),
        "present": ("ResetType_PR", False),
    },
    "ResetType_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "nG_Interface": ("ResetAll_t", False),
        "partOfNG_Interface": ("struct " "UE_associatedLogicalNG_connectionList", True),
    },
    "RoutingID_t": ("OCTET_STRING_t", False),
    "SD": ("int", False),
    "SD_t": ("OCTET_STRING_t", False),
    "SMF": ("JSON", True),
    "SONConfigurationTransfer_ExtIEs__extensionValue_PR_NOTHING": (
        "SONConfigurationTransfer_ExtIEs__extensionValue_PR",
        False,
    ),
    "SONConfigurationTransfer_ExtIEs__extensionValue_u": {},
    "SONConfigurationTransfer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "SONConfigurationTransfer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SONConfigurationTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "sONInformation": ("SONInformation_t", False),
        "sourceRANNodeID": ("SourceRANNodeID_t", False),
        "targetRANNodeID": ("TargetRANNodeID_t", False),
        "xnTNLConfigurationInfo": ("XnTNLConfigurationInfo_t", False),
    },
    "SONInformationReply_ExtIEs__extensionValue_PR_NOTHING": (
        "SONInformationReply_ExtIEs__extensionValue_PR",
        False,
    ),
    "SONInformationReply_ExtIEs__extensionValue_u": {},
    "SONInformationReply_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "SONInformationReply_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SONInformationReply_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "xnTNLConfigurationInfo": ("struct " "XnTNLConfigurationInfo", True),
    },
    "SONInformationRequest_t": ("long", False),
    "SONInformationRequest_xn_TNL_configuration_info": (
        "e_SONInformationRequest",
        False,
    ),
    "SONInformation_ExtIEs__value_PR_NOTHING": (
        "SONInformation_ExtIEs__value_PR",
        False,
    ),
    "SONInformation_ExtIEs__value_u": {},
    "SONInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct SONInformation_ExtIEs__value", False),
    },
    "SONInformation_PR_NOTHING": ("SONInformation_PR", False),
    "SONInformation_PR_choice_Extensions": ("SONInformation_PR", False),
    "SONInformation_PR_sONInformationReply": ("SONInformation_PR", False),
    "SONInformation_PR_sONInformationRequest": ("SONInformation_PR", False),
    "SONInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SONInformation_u", False),
        "present": ("SONInformation_PR", False),
    },
    "SONInformation_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "sONInformationReply": ("struct SONInformationReply", True),
        "sONInformationRequest": ("SONInformationRequest_t", False),
    },
    "SST_t": ("OCTET_STRING_t", False),
    "S_NSSAI": ("JSON", False),
    "S_NSSAI_ExtIEs__extensionValue_PR_NOTHING": (
        "S_NSSAI_ExtIEs__extensionValue_PR",
        False,
    ),
    "S_NSSAI_ExtIEs__extensionValue_u": {},
    "S_NSSAI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "S_NSSAI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "S_NSSAI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "sD": ("SD_t", True),
        "sST": ("SST_t", False),
    },
    "SecurityContext_ExtIEs__extensionValue_PR_NOTHING": (
        "SecurityContext_ExtIEs__extensionValue_PR",
        False,
    ),
    "SecurityContext_ExtIEs__extensionValue_u": {},
    "SecurityContext_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SecurityContext_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SecurityContext_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "nextHopChainingCount": ("NextHopChainingCount_t", False),
        "nextHopNH": ("SecurityKey_t", False),
    },
    "SecurityIndication_ExtIEs__extensionValue_PR_NOTHING": (
        "SecurityIndication_ExtIEs__extensionValue_PR",
        False,
    ),
    "SecurityIndication_ExtIEs__extensionValue_u": {},
    "SecurityIndication_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "SecurityIndication_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SecurityIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "confidentialityProtectionIndication": (
            "ConfidentialityProtectionIndication_t",
            False,
        ),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "integrityProtectionIndication": ("IntegrityProtectionIndication_t", False),
        "maximumIntegrityProtectedDataRate": (
            "MaximumIntegrityProtectedDataRate_t",
            True,
        ),
    },
    "SecurityKey_t": ("BIT_STRING_t", False),
    "SecurityModeCommand_t": {
        "hashAmf": ("hashAmf_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "nasSecurityAlgorithm": ("NasSecurityAlgorithm_t", False),
        "ngKsi": ("NaskeysetId_t", False),
        "ueSecuCapability": ("UeSecurityCapability_t", False),
    },
    "SecurityModeComplete_t": {"mmHeader": ("_5gmmMsgHeader_t", False)},
    "SecurityModeReject_t": {
        "_5gmmCause": ("uint8_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
    },
    "SecurityResult_ExtIEs__extensionValue_PR_NOTHING": (
        "SecurityResult_ExtIEs__extensionValue_PR",
        False,
    ),
    "SecurityResult_ExtIEs__extensionValue_u": {},
    "SecurityResult_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SecurityResult_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SecurityResult_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "confidentialityProtectionResult": ("ConfidentialityProtectionResult_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "integrityProtectionResult": ("IntegrityProtectionResult_t", False),
    },
    "SerialNumber_t": ("BIT_STRING_t", False),
    "ServedGUAMIItem_ExtIEs__extensionValue_PR_NOTHING": (
        "ServedGUAMIItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "ServedGUAMIItem_ExtIEs__extensionValue_u": {},
    "ServedGUAMIItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "ServedGUAMIItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ServedGUAMIItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "backupAMFName": ("AMFName_t", True),
        "gUAMI": ("GUAMI_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
    },
    "ServedGUAMIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct ServedGUAMIItem)", False),
    },
    "ServiceAccept_t": {
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "pduSessionResult": ("pduSessionResult_t", False),
        "pduSessionResultCause": ("pduSessionResultCause_t", False),
        "pduSessionStatus": ("pduSessionStatus_t", False),
        "presenceMask": ("uint32_t", False),
    },
    "ServiceAreaInformation_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "ServiceAreaInformation_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "ServiceAreaInformation_Item_ExtIEs__extensionValue_u": {},
    "ServiceAreaInformation_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "ServiceAreaInformation_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "ServiceAreaInformation_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "allowedTACs": ("struct AllowedTACs", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "notAllowedTACs": ("struct NotAllowedTACs", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
    },
    "ServiceAreaInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "ServiceAreaInformation_Item)", False),
    },
    "ServiceReject_t": {
        "_5gmmCause": ("_5gmmCause_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "pduSessionStatus": ("pduSessionStatus_t", False),
        "presenceMask": ("uint32_t", False),
    },
    "ServiceRequest_t": {
        "_5gsTmsi": ("_5gsTmsi_t", False),
        "_5gservType": ("_5gServiceType_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "ngKsi": ("NaskeysetId_t", False),
        "pduSessionStatus": ("pduSessionStatus_t", False),
        "presenceMask": ("uint32_t", False),
        "uplinkDataStatus": ("UplinkDataStatus_t", False),
    },
    "SessionAMBR_t": {
        "downlinkUnit": ("uint8_t", False),
        "downlinkValue": ("uint16_t", False),
        "len": ("uint8_t", False),
        "uplinkUnit": ("uint8_t", False),
        "uplinkValue": ("uint16_t", False),
    },
    "SessionAmbr_t": {
        "lengthOfSessionAmbrContents": ("uint8_t", False),
        "sessionAmbrForDownlink": ("uint16_t", False),
        "sessionAmbrForUplink": ("uint16_t", False),
        "unitForSessionAmbrForDownlink": ("uint8_t", False),
        "unitForSessionAmbrForUplink": ("uint8_t", False),
    },
    "SessionEstdAccept_t": {
        "_5gsmCause": ("_5gsmCause_t", False),
        "ambr": ("SessionAMBR_t", False),
        "authorizedQoSFlowDesc": ("QosFlowDescriptions_t", False),
        "authorizedQosRules": ("QosRules_t", False),
        "dnn": ("DNN_t", False),
        "pduAddress": ("pduAddress_t", False),
        "presenceMask": ("uint32_t", False),
        "selected_pduSessionType": ("pduSessionType_t", False),
        "selected_sscMode": ("sscMode_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "SessionEstdReject_t": {
        "_5gsmCause": ("_5gsmCause_t", False),
        "presenceMask": ("uint32_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "SessionEstdRequest_t": {
        "_5gsmCapability": ("_5gsmCapability_t", False),
        "ipmdr": ("integProtMaxDataRate_t", False),
        "maxNoSupportedPacketFilters": ("maxNoSupPackFilts_t", False),
        "pduSessionType": ("pduSessionType_t", False),
        "presenceMask": ("uint32_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
        "sscMode": ("sscMode_t", False),
    },
    "SessionRelCommand_t": {
        "_5gsmCause": ("uint8_t", False),
        "smHeader": ("_5gsmMsgHeader_t", False),
    },
    "SessionRelComplete_t": {"smHeader": ("_5gsmMsgHeader_t", False)},
    "SessionRelReq_t": {"smHeader": ("_5gsmMsgHeader_t", False)},
    "SingleTNLInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "SingleTNLInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "SingleTNLInformation_ExtIEs__extensionValue_u": {},
    "SingleTNLInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "SingleTNLInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SingleTNLInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uPTransportLayerInformation": ("UPTransportLayerInformation_t", False),
    },
    "SliceOverloadItem_ExtIEs__extensionValue_PR_NOTHING": (
        "SliceOverloadItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "SliceOverloadItem_ExtIEs__extensionValue_u": {},
    "SliceOverloadItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SliceOverloadItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SliceOverloadItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "SliceOverloadList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct SliceOverloadItem)", False),
    },
    "SliceSupportItem_ExtIEs__extensionValue_PR_NOTHING": (
        "SliceSupportItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "SliceSupportItem_ExtIEs__extensionValue_u": {},
    "SliceSupportItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SliceSupportItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SliceSupportItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "s_NSSAI": ("S_NSSAI_t", False),
    },
    "SliceSupportList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct SliceSupportItem)", False),
    },
    "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR_NOTHING": (
        "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR",
        False,
    ),
    "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue_u": {},
    "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "e_RABInformationList": ("struct " "E_RABInformationList", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "indexToRFSP": ("IndexToRFSP_t", True),
        "pDUSessionResourceInformationList": (
            "struct " "PDUSessionResourceInformationList",
            True,
        ),
        "rRCContainer": ("RRCContainer_t", False),
        "targetCell_ID": ("NGRAN_CGI_t", False),
        "uEHistoryInformation": ("UEHistoryInformation_t", False),
    },
    "SourceOfUEActivityBehaviourInformation_statistics": (
        "e_SourceOfUEActivityBehaviourInformation",
        False,
    ),
    "SourceOfUEActivityBehaviourInformation_subscription_information": (
        "e_SourceOfUEActivityBehaviourInformation",
        False,
    ),
    "SourceOfUEActivityBehaviourInformation_t": ("long", False),
    "SourceRANNodeID_ExtIEs__extensionValue_PR_NOTHING": (
        "SourceRANNodeID_ExtIEs__extensionValue_PR",
        False,
    ),
    "SourceRANNodeID_ExtIEs__extensionValue_u": {},
    "SourceRANNodeID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SourceRANNodeID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SourceRANNodeID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "globalRANNodeID": ("GlobalRANNodeID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "selectedTAI": ("TAI_t", False),
    },
    "SourceToTarget_TransparentContainer_t": ("OCTET_STRING_t", False),
    "SuccessfulOutcome__value_PR_AMFConfigurationUpdateAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_HandoverCancelAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_HandoverCommand": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_HandoverRequestAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_InitialContextSetupResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_NGResetAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_NGSetupResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_NOTHING": ("SuccessfulOutcome__value_PR", False),
    "SuccessfulOutcome__value_PR_PDUSessionResourceModifyConfirm": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_PDUSessionResourceModifyResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_PDUSessionResourceReleaseResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_PDUSessionResourceSetupResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_PWSCancelResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_PathSwitchRequestAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_RANConfigurationUpdateAcknowledge": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_UEContextModificationResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_UEContextReleaseComplete": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_UERadioCapabilityCheckResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_PR_WriteReplaceWarningResponse": (
        "SuccessfulOutcome__value_PR",
        False,
    ),
    "SuccessfulOutcome__value_u": {
        "AMFConfigurationUpdateAcknowledge": (
            "AMFConfigurationUpdateAcknowledge_t",
            False,
        ),
        "HandoverCancelAcknowledge": ("HandoverCancelAcknowledge_t", False),
        "HandoverCommand": ("HandoverCommand_t", False),
        "HandoverRequestAcknowledge": ("HandoverRequestAcknowledge_t", False),
        "InitialContextSetupResponse": ("InitialContextSetupResponse_t", False),
        "NGResetAcknowledge": ("NGResetAcknowledge_t", False),
        "NGSetupResponse": ("NGSetupResponse_t", False),
        "PDUSessionResourceModifyConfirm": ("PDUSessionResourceModifyConfirm_t", False),
        "PDUSessionResourceModifyResponse": (
            "PDUSessionResourceModifyResponse_t",
            False,
        ),
        "PDUSessionResourceReleaseResponse": (
            "PDUSessionResourceReleaseResponse_t",
            False,
        ),
        "PDUSessionResourceSetupResponse": ("PDUSessionResourceSetupResponse_t", False),
        "PWSCancelResponse": ("PWSCancelResponse_t", False),
        "PathSwitchRequestAcknowledge": ("PathSwitchRequestAcknowledge_t", False),
        "RANConfigurationUpdateAcknowledge": (
            "RANConfigurationUpdateAcknowledge_t",
            False,
        ),
        "UEContextModificationResponse": ("UEContextModificationResponse_t", False),
        "UEContextReleaseComplete": ("UEContextReleaseComplete_t", False),
        "UERadioCapabilityCheckResponse": ("UERadioCapabilityCheckResponse_t", False),
        "WriteReplaceWarningResponse": ("WriteReplaceWarningResponse_t", False),
    },
    "SuccessfulOutcome_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "procedureCode": ("ProcedureCode_t", False),
        "value": ("struct SuccessfulOutcome__value", False),
    },
    "SupportedPLMN": ("JSON", True),
    "SupportedTAItem_ExtIEs__extensionValue_PR_NOTHING": (
        "SupportedTAItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "SupportedTAItem_ExtIEs__extensionValue_u": {},
    "SupportedTAItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "SupportedTAItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "SupportedTAItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "broadcastPLMNList": ("BroadcastPLMNList_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "tAC": ("TAC_t", False),
    },
    "SupportedTAList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct SupportedTAItem)", False),
    },
    "TAC_t": ("OCTET_STRING_t", False),
    "TAIBroadcastEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "TAIBroadcastEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAIBroadcastEUTRA_Item_ExtIEs__extensionValue_u": {},
    "TAIBroadcastEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAIBroadcastEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAIBroadcastEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "completedCellsInTAI_EUTRA": ("CompletedCellsInTAI_EUTRA_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAIBroadcastEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIBroadcastEUTRA_Item)", False),
    },
    "TAIBroadcastNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "TAIBroadcastNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAIBroadcastNR_Item_ExtIEs__extensionValue_u": {},
    "TAIBroadcastNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAIBroadcastNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAIBroadcastNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "completedCellsInTAI_NR": ("CompletedCellsInTAI_NR_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAIBroadcastNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TAIBroadcastNR_Item)", False),
    },
    "TAICancelledEUTRA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "TAICancelledEUTRA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAICancelledEUTRA_Item_ExtIEs__extensionValue_u": {},
    "TAICancelledEUTRA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAICancelledEUTRA_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAICancelledEUTRA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cancelledCellsInTAI_EUTRA": ("CancelledCellsInTAI_EUTRA_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAICancelledEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAICancelledEUTRA_Item)", False),
    },
    "TAICancelledNR_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "TAICancelledNR_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAICancelledNR_Item_ExtIEs__extensionValue_u": {},
    "TAICancelledNR_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAICancelledNR_Item_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAICancelledNR_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cancelledCellsInTAI_NR": ("CancelledCellsInTAI_NR_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAICancelledNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TAICancelledNR_Item)", False),
    },
    "TAIListForInactiveItem_ExtIEs__extensionValue_PR_NOTHING": (
        "TAIListForInactiveItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAIListForInactiveItem_ExtIEs__extensionValue_u": {},
    "TAIListForInactiveItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAIListForInactiveItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAIListForInactiveItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAIListForInactive_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "TAIListForInactiveItem)", False),
    },
    "TAIListForPagingItem_ExtIEs__extensionValue_PR_NOTHING": (
        "TAIListForPagingItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "TAIListForPagingItem_ExtIEs__extensionValue_u": {},
    "TAIListForPagingItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TAIListForPagingItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAIListForPagingItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
    },
    "TAIListForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TAIListForPagingItem)", False),
    },
    "TAIListForRestart_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TAI)", False),
    },
    "TAIListForWarning_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TAI)", False),
    },
    "TAI_ExtIEs__extensionValue_PR_NOTHING": ("TAI_ExtIEs__extensionValue_PR", False),
    "TAI_ExtIEs__extensionValue_u": {},
    "TAI_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct TAI_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TAI_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "pLMNIdentity": ("PLMNIdentity_t", False),
        "tAC": ("TAC_t", False),
    },
    "TEIDstart": ("int", False),
    "TNLAddressWeightFactor_t": ("long", False),
    "TNLAssociationItem_ExtIEs__extensionValue_PR_NOTHING": (
        "TNLAssociationItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "TNLAssociationItem_ExtIEs__extensionValue_u": {},
    "TNLAssociationItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TNLAssociationItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TNLAssociationItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "cause": ("Cause_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "tNLAssociationAddress": ("CPTransportLayerInformation_t", False),
    },
    "TNLAssociationList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TNLAssociationItem)", False),
    },
    "TNLAssociationUsage_both": ("e_TNLAssociationUsage", False),
    "TNLAssociationUsage_non_ue": ("e_TNLAssociationUsage", False),
    "TNLAssociationUsage_t": ("long", False),
    "TNLAssociationUsage_ue": ("e_TNLAssociationUsage", False),
    "TNLInformationItem_ExtIEs__extensionValue_PR_NOTHING": (
        "TNLInformationItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "TNLInformationItem_ExtIEs__extensionValue_u": {},
    "TNLInformationItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "TNLInformationItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TNLInformationItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "qosFlowPerTNLInformation": ("QosFlowPerTNLInformation_t", False),
    },
    "TNLInformationList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TNLInformationItem)", False),
    },
    "TNLMappingItem_ExtIEs__extensionValue_PR_NOTHING": (
        "TNLMappingItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "TNLMappingItem_ExtIEs__extensionValue_u": {},
    "TNLMappingItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "TNLMappingItem_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TNLMappingItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "uL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
    },
    "TNLMappingList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct TNLMappingItem)", False),
    },
    "TOS_TC_t": {"field": ("uint8_t", False), "mask": ("uint8_t", False)},
    "TargetID_ExtIEs__value_PR_NOTHING": ("TargetID_ExtIEs__value_PR", False),
    "TargetID_ExtIEs__value_u": {},
    "TargetID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct TargetID_ExtIEs__value", False),
    },
    "TargetID_PR_NOTHING": ("TargetID_PR", False),
    "TargetID_PR_choice_Extensions": ("TargetID_PR", False),
    "TargetID_PR_targetRANNodeID": ("TargetID_PR", False),
    "TargetID_PR_targeteNB_ID": ("TargetID_PR", False),
    "TargetID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TargetID_u", False),
        "present": ("TargetID_PR", False),
    },
    "TargetID_u": {
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "targetRANNodeID": ("struct TargetRANNodeID", True),
        "targeteNB_ID": ("struct TargeteNB_ID", True),
    },
    "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR_NOTHING": (
        "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR",
        False,
    ),
    "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue_u": {},
    "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct "
            "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "rRCContainer": ("RRCContainer_t", False),
    },
    "TargetRANNodeID_ExtIEs__extensionValue_PR_NOTHING": (
        "TargetRANNodeID_ExtIEs__extensionValue_PR",
        False,
    ),
    "TargetRANNodeID_ExtIEs__extensionValue_u": {},
    "TargetRANNodeID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "TargetRANNodeID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TargetRANNodeID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "globalRANNodeID": ("GlobalRANNodeID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "selectedTAI": ("TAI_t", False),
    },
    "TargetToSource_TransparentContainer_t": ("OCTET_STRING_t", False),
    "TargeteNB_ID_ExtIEs__extensionValue_PR_NOTHING": (
        "TargeteNB_ID_ExtIEs__extensionValue_PR",
        False,
    ),
    "TargeteNB_ID_ExtIEs__extensionValue_u": {},
    "TargeteNB_ID_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "TargeteNB_ID_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TargeteNB_ID_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "globalENB_ID": ("GlobalNgENB_ID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "selected_EPS_TAI": ("EPS_TAI_t", False),
    },
    "TimeStamp_t": ("OCTET_STRING_t", False),
    "TimeToWait_t": ("long", False),
    "TimeToWait_v10s": ("e_TimeToWait", False),
    "TimeToWait_v1s": ("e_TimeToWait", False),
    "TimeToWait_v20s": ("e_TimeToWait", False),
    "TimeToWait_v2s": ("e_TimeToWait", False),
    "TimeToWait_v5s": ("e_TimeToWait", False),
    "TimeToWait_v60s": ("e_TimeToWait", False),
    "TimeUEStayedInCellEnhancedGranularity_t": ("long", False),
    "TimeUEStayedInCell_t": ("long", False),
    "TimerApproachForGUAMIRemoval_apply_timer": (
        "e_TimerApproachForGUAMIRemoval",
        False,
    ),
    "TimerApproachForGUAMIRemoval_t": ("long", False),
    "TraceActivation_ExtIEs__extensionValue_PR_NOTHING": (
        "TraceActivation_ExtIEs__extensionValue_PR",
        False,
    ),
    "TraceActivation_ExtIEs__extensionValue_u": {},
    "TraceActivation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "TraceActivation_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "TraceActivation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "interfacesToTrace": ("InterfacesToTrace_t", False),
        "nGRANTraceID": ("NGRANTraceID_t", False),
        "traceCollectionEntityIPAddress": ("TransportLayerAddress_t", False),
        "traceDepth": ("TraceDepth_t", False),
    },
    "TraceDepth_maximum": ("e_TraceDepth", False),
    "TraceDepth_maximumWithoutVendorSpecificExtension": ("e_TraceDepth", False),
    "TraceDepth_medium": ("e_TraceDepth", False),
    "TraceDepth_mediumWithoutVendorSpecificExtension": ("e_TraceDepth", False),
    "TraceDepth_minimum": ("e_TraceDepth", False),
    "TraceDepth_minimumWithoutVendorSpecificExtension": ("e_TraceDepth", False),
    "TraceDepth_t": ("long", False),
    "TraceFailureIndicationIEs__value_PR_AMF_UE_NGAP_ID": (
        "TraceFailureIndicationIEs__value_PR",
        False,
    ),
    "TraceFailureIndicationIEs__value_PR_Cause": (
        "TraceFailureIndicationIEs__value_PR",
        False,
    ),
    "TraceFailureIndicationIEs__value_PR_NGRANTraceID": (
        "TraceFailureIndicationIEs__value_PR",
        False,
    ),
    "TraceFailureIndicationIEs__value_PR_NOTHING": (
        "TraceFailureIndicationIEs__value_PR",
        False,
    ),
    "TraceFailureIndicationIEs__value_PR_RAN_UE_NGAP_ID": (
        "TraceFailureIndicationIEs__value_PR",
        False,
    ),
    "TraceFailureIndicationIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "NGRANTraceID": ("NGRANTraceID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "TraceFailureIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "TraceFailureIndicationIEs__value", False),
    },
    "TraceFailureIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P69_t", False),
    },
    "TraceStartIEs__value_PR_AMF_UE_NGAP_ID": ("TraceStartIEs__value_PR", False),
    "TraceStartIEs__value_PR_NOTHING": ("TraceStartIEs__value_PR", False),
    "TraceStartIEs__value_PR_RAN_UE_NGAP_ID": ("TraceStartIEs__value_PR", False),
    "TraceStartIEs__value_PR_TraceActivation": ("TraceStartIEs__value_PR", False),
    "TraceStartIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "TraceActivation": ("TraceActivation_t", False),
    },
    "TraceStartIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct TraceStartIEs__value", False),
    },
    "TraceStart_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P68_t", False),
    },
    "TrafficLoadReductionIndication_t": ("long", False),
    "TransportLayerAddress_t": ("BIT_STRING_t", False),
    "TriggeringMessage_initiating_message": ("e_TriggeringMessage", False),
    "TriggeringMessage_successful_outcome": ("e_TriggeringMessage", False),
    "TriggeringMessage_t": ("long", False),
    "TriggeringMessage_unsuccessfull_outcome": ("e_TriggeringMessage", False),
    "TypeOfError_missing": ("e_TypeOfError", False),
    "TypeOfError_not_understood": ("e_TypeOfError", False),
    "TypeOfError_t": ("long", False),
    "UEAggregateMaximumBitRate_ExtIEs__extensionValue_PR_NOTHING": (
        "UEAggregateMaximumBitRate_ExtIEs__extensionValue_PR",
        False,
    ),
    "UEAggregateMaximumBitRate_ExtIEs__extensionValue_u": {},
    "UEAggregateMaximumBitRate_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UEAggregateMaximumBitRate_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UEAggregateMaximumBitRate_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uEAggregateMaximumBitRateDL": ("BitRate_t", False),
        "uEAggregateMaximumBitRateUL": ("BitRate_t", False),
    },
    "UEContextModificationFailureIEs__value_PR_AMF_UE_NGAP_ID": (
        "UEContextModificationFailureIEs__value_PR",
        False,
    ),
    "UEContextModificationFailureIEs__value_PR_Cause": (
        "UEContextModificationFailureIEs__value_PR",
        False,
    ),
    "UEContextModificationFailureIEs__value_PR_CriticalityDiagnostics": (
        "UEContextModificationFailureIEs__value_PR",
        False,
    ),
    "UEContextModificationFailureIEs__value_PR_NOTHING": (
        "UEContextModificationFailureIEs__value_PR",
        False,
    ),
    "UEContextModificationFailureIEs__value_PR_RAN_UE_NGAP_ID": (
        "UEContextModificationFailureIEs__value_PR",
        False,
    ),
    "UEContextModificationFailureIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UEContextModificationFailureIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextModificationFailureIEs__value", False),
    },
    "UEContextModificationFailure_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P19_t", False),
    },
    "UEContextModificationRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_AMF_UE_NGAP_ID_1": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_CoreNetworkAssistanceInformation": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_EmergencyFallbackIndicator": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_IndexToRFSP": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_NOTHING": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_RANPagingPriority": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_RRCInactiveTransitionReportRequest": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_SecurityKey": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_UEAggregateMaximumBitRate": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_PR_UESecurityCapabilities": (
        "UEContextModificationRequestIEs__value_PR",
        False,
    ),
    "UEContextModificationRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "AMF_UE_NGAP_ID_1": ("AMF_UE_NGAP_ID_t", False),
        "CoreNetworkAssistanceInformation": (
            "CoreNetworkAssistanceInformation_t",
            False,
        ),
        "EmergencyFallbackIndicator": ("EmergencyFallbackIndicator_t", False),
        "IndexToRFSP": ("IndexToRFSP_t", False),
        "RANPagingPriority": ("RANPagingPriority_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCInactiveTransitionReportRequest": (
            "RRCInactiveTransitionReportRequest_t",
            False,
        ),
        "SecurityKey": ("SecurityKey_t", False),
        "UEAggregateMaximumBitRate": ("UEAggregateMaximumBitRate_t", False),
        "UESecurityCapabilities": ("UESecurityCapabilities_t", False),
    },
    "UEContextModificationRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextModificationRequestIEs__value", False),
    },
    "UEContextModificationRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P17_t", False),
    },
    "UEContextModificationResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_PR_CriticalityDiagnostics": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_PR_NOTHING": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_PR_RRCState": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_PR_UserLocationInformation": (
        "UEContextModificationResponseIEs__value_PR",
        False,
    ),
    "UEContextModificationResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RRCState": ("RRCState_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "UEContextModificationResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextModificationResponseIEs__value", False),
    },
    "UEContextModificationResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P18_t", False),
    },
    "UEContextReleaseCommand_IEs__value_PR_Cause": (
        "UEContextReleaseCommand_IEs__value_PR",
        False,
    ),
    "UEContextReleaseCommand_IEs__value_PR_NOTHING": (
        "UEContextReleaseCommand_IEs__value_PR",
        False,
    ),
    "UEContextReleaseCommand_IEs__value_PR_UE_NGAP_IDs": (
        "UEContextReleaseCommand_IEs__value_PR",
        False,
    ),
    "UEContextReleaseCommand_IEs__value_u": {
        "Cause": ("Cause_t", False),
        "UE_NGAP_IDs": ("UE_NGAP_IDs_t", False),
    },
    "UEContextReleaseCommand_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextReleaseCommand_IEs__value", False),
    },
    "UEContextReleaseCommand_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P15_t", False),
    },
    "UEContextReleaseComplete_IEs__value_PR_AMF_UE_NGAP_ID": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_CriticalityDiagnostics": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_InfoOnRecommendedCellsAndRANNodesForPaging": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_NOTHING": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_PDUSessionResourceListCxtRelCpl": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_RAN_UE_NGAP_ID": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_PR_UserLocationInformation": (
        "UEContextReleaseComplete_IEs__value_PR",
        False,
    ),
    "UEContextReleaseComplete_IEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "InfoOnRecommendedCellsAndRANNodesForPaging": (
            "InfoOnRecommendedCellsAndRANNodesForPaging_t",
            False,
        ),
        "PDUSessionResourceListCxtRelCpl": ("PDUSessionResourceListCxtRelCpl_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "UEContextReleaseComplete_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextReleaseComplete_IEs__value", False),
    },
    "UEContextReleaseComplete_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P16_t", False),
    },
    "UEContextReleaseRequest_IEs__value_PR_AMF_UE_NGAP_ID": (
        "UEContextReleaseRequest_IEs__value_PR",
        False,
    ),
    "UEContextReleaseRequest_IEs__value_PR_Cause": (
        "UEContextReleaseRequest_IEs__value_PR",
        False,
    ),
    "UEContextReleaseRequest_IEs__value_PR_NOTHING": (
        "UEContextReleaseRequest_IEs__value_PR",
        False,
    ),
    "UEContextReleaseRequest_IEs__value_PR_PDUSessionResourceListCxtRelReq": (
        "UEContextReleaseRequest_IEs__value_PR",
        False,
    ),
    "UEContextReleaseRequest_IEs__value_PR_RAN_UE_NGAP_ID": (
        "UEContextReleaseRequest_IEs__value_PR",
        False,
    ),
    "UEContextReleaseRequest_IEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "Cause": ("Cause_t", False),
        "PDUSessionResourceListCxtRelReq": ("PDUSessionResourceListCxtRelReq_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UEContextReleaseRequest_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEContextReleaseRequest_IEs__value", False),
    },
    "UEContextReleaseRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P14_t", False),
    },
    "UEContextRequest_requested": ("e_UEContextRequest", False),
    "UEContextRequest_t": ("long", False),
    "UEHistoryInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "LastVisitedCellItem)", False),
    },
    "UEIdentityIndexValue_ExtIEs__value_PR_NOTHING": (
        "UEIdentityIndexValue_ExtIEs__value_PR",
        False,
    ),
    "UEIdentityIndexValue_ExtIEs__value_u": {},
    "UEIdentityIndexValue_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEIdentityIndexValue_ExtIEs__value", False),
    },
    "UEIdentityIndexValue_PR_NOTHING": ("UEIdentityIndexValue_PR", False),
    "UEIdentityIndexValue_PR_choice_Extensions": ("UEIdentityIndexValue_PR", False),
    "UEIdentityIndexValue_PR_indexLength10": ("UEIdentityIndexValue_PR", False),
    "UEIdentityIndexValue_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEIdentityIndexValue_u", False),
        "present": ("UEIdentityIndexValue_PR", False),
    },
    "UEIdentityIndexValue_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "indexLength10": ("BIT_STRING_t", False),
    },
    "UEPagingIdentity_ExtIEs__value_PR_NOTHING": (
        "UEPagingIdentity_ExtIEs__value_PR",
        False,
    ),
    "UEPagingIdentity_ExtIEs__value_u": {},
    "UEPagingIdentity_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UEPagingIdentity_ExtIEs__value", False),
    },
    "UEPagingIdentity_PR_NOTHING": ("UEPagingIdentity_PR", False),
    "UEPagingIdentity_PR_choice_Extensions": ("UEPagingIdentity_PR", False),
    "UEPagingIdentity_PR_fiveG_S_TMSI": ("UEPagingIdentity_PR", False),
    "UEPagingIdentity_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEPagingIdentity_u", False),
        "present": ("UEPagingIdentity_PR", False),
    },
    "UEPagingIdentity_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "fiveG_S_TMSI": ("struct FiveG_S_TMSI", True),
    },
    "UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue_PR_NOTHING": (
        "UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue_u": {},
    "UEPresenceInAreaOfInterestItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UEPresenceInAreaOfInterestItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "locationReportingReferenceID": ("LocationReportingReferenceID_t", False),
        "uEPresence": ("UEPresence_t", False),
    },
    "UEPresenceInAreaOfInterestList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UEPresenceInAreaOfInterestItem)", False),
    },
    "UEPresence_in": ("e_UEPresence", False),
    "UEPresence_out": ("e_UEPresence", False),
    "UEPresence_t": ("long", False),
    "UEPresence_unknown": ("e_UEPresence", False),
    "UERadioCapabilityCheckRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "UERadioCapabilityCheckRequestIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckRequestIEs__value_PR_NOTHING": (
        "UERadioCapabilityCheckRequestIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "UERadioCapabilityCheckRequestIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckRequestIEs__value_PR_UERadioCapability": (
        "UERadioCapabilityCheckRequestIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UERadioCapability": ("UERadioCapability_t", False),
    },
    "UERadioCapabilityCheckRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UERadioCapabilityCheckRequestIEs__value", False),
    },
    "UERadioCapabilityCheckRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P77_t", False),
    },
    "UERadioCapabilityCheckResponseIEs__value_PR_AMF_UE_NGAP_ID": (
        "UERadioCapabilityCheckResponseIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckResponseIEs__value_PR_CriticalityDiagnostics": (
        "UERadioCapabilityCheckResponseIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckResponseIEs__value_PR_IMSVoiceSupportIndicator": (
        "UERadioCapabilityCheckResponseIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckResponseIEs__value_PR_NOTHING": (
        "UERadioCapabilityCheckResponseIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckResponseIEs__value_PR_RAN_UE_NGAP_ID": (
        "UERadioCapabilityCheckResponseIEs__value_PR",
        False,
    ),
    "UERadioCapabilityCheckResponseIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "IMSVoiceSupportIndicator": ("IMSVoiceSupportIndicator_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UERadioCapabilityCheckResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UERadioCapabilityCheckResponseIEs__value", False),
    },
    "UERadioCapabilityCheckResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P78_t", False),
    },
    "UERadioCapabilityForPagingOfEUTRA_t": ("OCTET_STRING_t", False),
    "UERadioCapabilityForPagingOfNR_t": ("OCTET_STRING_t", False),
    "UERadioCapabilityForPaging_ExtIEs__extensionValue_PR_NOTHING": (
        "UERadioCapabilityForPaging_ExtIEs__extensionValue_PR",
        False,
    ),
    "UERadioCapabilityForPaging_ExtIEs__extensionValue_u": {},
    "UERadioCapabilityForPaging_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UERadioCapabilityForPaging_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UERadioCapabilityForPaging_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uERadioCapabilityForPagingOfEUTRA": (
            "UERadioCapabilityForPagingOfEUTRA_t",
            True,
        ),
        "uERadioCapabilityForPagingOfNR": ("UERadioCapabilityForPagingOfNR_t", True),
    },
    "UERadioCapabilityInfoIndicationIEs__value_PR_AMF_UE_NGAP_ID": (
        "UERadioCapabilityInfoIndicationIEs__value_PR",
        False,
    ),
    "UERadioCapabilityInfoIndicationIEs__value_PR_NOTHING": (
        "UERadioCapabilityInfoIndicationIEs__value_PR",
        False,
    ),
    "UERadioCapabilityInfoIndicationIEs__value_PR_RAN_UE_NGAP_ID": (
        "UERadioCapabilityInfoIndicationIEs__value_PR",
        False,
    ),
    "UERadioCapabilityInfoIndicationIEs__value_PR_UERadioCapability": (
        "UERadioCapabilityInfoIndicationIEs__value_PR",
        False,
    ),
    "UERadioCapabilityInfoIndicationIEs__value_PR_UERadioCapabilityForPaging": (
        "UERadioCapabilityInfoIndicationIEs__value_PR",
        False,
    ),
    "UERadioCapabilityInfoIndicationIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UERadioCapability": ("UERadioCapability_t", False),
        "UERadioCapabilityForPaging": ("UERadioCapabilityForPaging_t", False),
    },
    "UERadioCapabilityInfoIndicationIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UERadioCapabilityInfoIndicationIEs__value", False),
    },
    "UERadioCapabilityInfoIndication_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P76_t", False),
    },
    "UERadioCapability_t": ("OCTET_STRING_t", False),
    "UESecurityCapabilities_ExtIEs__extensionValue_PR_NOTHING": (
        "UESecurityCapabilities_ExtIEs__extensionValue_PR",
        False,
    ),
    "UESecurityCapabilities_ExtIEs__extensionValue_u": {},
    "UESecurityCapabilities_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UESecurityCapabilities_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UESecurityCapabilities_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRAencryptionAlgorithms": ("EUTRAencryptionAlgorithms_t", False),
        "eUTRAintegrityProtectionAlgorithms": (
            "EUTRAintegrityProtectionAlgorithms_t",
            False,
        ),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nRencryptionAlgorithms": ("NRencryptionAlgorithms_t", False),
        "nRintegrityProtectionAlgorithms": ("NRintegrityProtectionAlgorithms_t", False),
    },
    "UETNLABindingReleaseRequestIEs__value_PR_AMF_UE_NGAP_ID": (
        "UETNLABindingReleaseRequestIEs__value_PR",
        False,
    ),
    "UETNLABindingReleaseRequestIEs__value_PR_NOTHING": (
        "UETNLABindingReleaseRequestIEs__value_PR",
        False,
    ),
    "UETNLABindingReleaseRequestIEs__value_PR_RAN_UE_NGAP_ID": (
        "UETNLABindingReleaseRequestIEs__value_PR",
        False,
    ),
    "UETNLABindingReleaseRequestIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UETNLABindingReleaseRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UETNLABindingReleaseRequestIEs__value", False),
    },
    "UETNLABindingReleaseRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P75_t", False),
    },
    "UE_NGAP_ID_pair_ExtIEs__extensionValue_PR_NOTHING": (
        "UE_NGAP_ID_pair_ExtIEs__extensionValue_PR",
        False,
    ),
    "UE_NGAP_ID_pair_ExtIEs__extensionValue_u": {},
    "UE_NGAP_ID_pair_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "UE_NGAP_ID_pair_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UE_NGAP_ID_pair_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "rAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UE_NGAP_IDs_ExtIEs__value_PR_NOTHING": ("UE_NGAP_IDs_ExtIEs__value_PR", False),
    "UE_NGAP_IDs_ExtIEs__value_u": {},
    "UE_NGAP_IDs_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct UE_NGAP_IDs_ExtIEs__value", False),
    },
    "UE_NGAP_IDs_PR_NOTHING": ("UE_NGAP_IDs_PR", False),
    "UE_NGAP_IDs_PR_aMF_UE_NGAP_ID": ("UE_NGAP_IDs_PR", False),
    "UE_NGAP_IDs_PR_choice_Extensions": ("UE_NGAP_IDs_PR", False),
    "UE_NGAP_IDs_PR_uE_NGAP_ID_pair": ("UE_NGAP_IDs_PR", False),
    "UE_NGAP_IDs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UE_NGAP_IDs_u", False),
        "present": ("UE_NGAP_IDs_PR", False),
    },
    "UE_NGAP_IDs_u": {
        "aMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "choice_Extensions": ("struct ProtocolIE_SingleContainer", True),
        "uE_NGAP_ID_pair": ("struct UE_NGAP_ID_pair", True),
    },
    "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue_PR_NOTHING": (
        "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue_u": {},
    "UE_associatedLogicalNG_connectionItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UE_associatedLogicalNG_connectionItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "aMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", True),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "rAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", True),
    },
    "UE_associatedLogicalNG_connectionList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": (
            "A_SEQUENCE_OF(struct " "UE_associatedLogicalNG_connectionItem)",
            False,
        ),
    },
    "UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue_PR_NOTHING": (
        "UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue_u": {},
    "UL_NGU_UP_TNLModifyItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UL_NGU_UP_TNLModifyItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "dL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "uL_NGU_UP_TNLInformation": ("UPTransportLayerInformation_t", False),
    },
    "UL_NGU_UP_TNLModifyList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UL_NGU_UP_TNLModifyItem)", False),
    },
    "UPTransportLayerInformation_ExtIEs__value_PR_NOTHING": (
        "UPTransportLayerInformation_ExtIEs__value_PR",
        False,
    ),
    "UPTransportLayerInformation_ExtIEs__value_u": {},
    "UPTransportLayerInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UPTransportLayerInformation_ExtIEs__value", False),
    },
    "UPTransportLayerInformation_PR_NOTHING": ("UPTransportLayerInformation_PR", False),
    "UPTransportLayerInformation_PR_choice_Extensions": (
        "UPTransportLayerInformation_PR",
        False,
    ),
    "UPTransportLayerInformation_PR_gTPTunnel": (
        "UPTransportLayerInformation_PR",
        False,
    ),
    "UPTransportLayerInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UPTransportLayerInformation_u", False),
        "present": ("UPTransportLayerInformation_PR", False),
    },
    "UPTransportLayerInformation_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "gTPTunnel": ("GTPTunnel_t", True),
    },
    "UP_TNLInformation_ExtIEs__value_PR_NOTHING": (
        "UP_TNLInformation_ExtIEs__value_PR",
        False,
    ),
    "UP_TNLInformation_ExtIEs__value_u": {},
    "UP_TNLInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UP_TNLInformation_ExtIEs__value", False),
    },
    "UP_TNLInformation_PR_NOTHING": ("UP_TNLInformation_PR", False),
    "UP_TNLInformation_PR_choice_Extensions": ("UP_TNLInformation_PR", False),
    "UP_TNLInformation_PR_multipleTNLInformation": ("UP_TNLInformation_PR", False),
    "UP_TNLInformation_PR_singleTNLInformation": ("UP_TNLInformation_PR", False),
    "UP_TNLInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UP_TNLInformation_u", False),
        "present": ("UP_TNLInformation_PR", False),
    },
    "UP_TNLInformation_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "multipleTNLInformation": ("struct " "MultipleTNLInformation", True),
        "singleTNLInformation": ("struct SingleTNLInformation", True),
    },
    "UeSecurityCapability_t": {
        "_5gASEncAlgo": ("uint8_t", False),
        "_5gASIntAlgo": ("uint8_t", False),
        "_5gNASEncAlgo": ("uint8_t", False),
        "_5gNASIntAlgo": ("uint8_t", False),
        "len": ("uint8_t", False),
    },
    "UnavailableGUAMIItem_ExtIEs__extensionValue_PR_NOTHING": (
        "UnavailableGUAMIItem_ExtIEs__extensionValue_PR",
        False,
    ),
    "UnavailableGUAMIItem_ExtIEs__extensionValue_u": {},
    "UnavailableGUAMIItem_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UnavailableGUAMIItem_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UnavailableGUAMIItem_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "backupAMFName": ("AMFName_t", True),
        "gUAMI": ("GUAMI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "timerApproachForGUAMIRemoval": ("TimerApproachForGUAMIRemoval_t", True),
    },
    "UnavailableGUAMIList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct " "UnavailableGUAMIItem)", False),
    },
    "UnsuccessfulOutcome__value_PR_AMFConfigurationUpdateFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_HandoverFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_HandoverPreparationFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_InitialContextSetupFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_NGSetupFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_NOTHING": ("UnsuccessfulOutcome__value_PR", False),
    "UnsuccessfulOutcome__value_PR_PathSwitchRequestFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_RANConfigurationUpdateFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_PR_UEContextModificationFailure": (
        "UnsuccessfulOutcome__value_PR",
        False,
    ),
    "UnsuccessfulOutcome__value_u": {
        "AMFConfigurationUpdateFailure": ("AMFConfigurationUpdateFailure_t", False),
        "HandoverFailure": ("HandoverFailure_t", False),
        "HandoverPreparationFailure": ("HandoverPreparationFailure_t", False),
        "InitialContextSetupFailure": ("InitialContextSetupFailure_t", False),
        "NGSetupFailure": ("NGSetupFailure_t", False),
        "PathSwitchRequestFailure": ("PathSwitchRequestFailure_t", False),
        "RANConfigurationUpdateFailure": ("RANConfigurationUpdateFailure_t", False),
        "UEContextModificationFailure": ("UEContextModificationFailure_t", False),
    },
    "UnsuccessfulOutcome_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "procedureCode": ("ProcedureCode_t", False),
        "value": ("struct UnsuccessfulOutcome__value", False),
    },
    "UplinkDataStatus_t": {"len": ("uint8_t", False), "psi": ("uint16_t", False)},
    "UplinkNASTransport_IEs__value_PR_AMF_UE_NGAP_ID": (
        "UplinkNASTransport_IEs__value_PR",
        False,
    ),
    "UplinkNASTransport_IEs__value_PR_NAS_PDU": (
        "UplinkNASTransport_IEs__value_PR",
        False,
    ),
    "UplinkNASTransport_IEs__value_PR_NOTHING": (
        "UplinkNASTransport_IEs__value_PR",
        False,
    ),
    "UplinkNASTransport_IEs__value_PR_RAN_UE_NGAP_ID": (
        "UplinkNASTransport_IEs__value_PR",
        False,
    ),
    "UplinkNASTransport_IEs__value_PR_UserLocationInformation": (
        "UplinkNASTransport_IEs__value_PR",
        False,
    ),
    "UplinkNASTransport_IEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NAS_PDU": ("NAS_PDU_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "UserLocationInformation": ("UserLocationInformation_t", False),
    },
    "UplinkNASTransport_IEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct UplinkNASTransport_IEs__value", False),
    },
    "UplinkNASTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P38_t", False),
    },
    "UplinkNasTransport_t": {
        "container": ("PayloadContainer_t", False),
        "dnn": ("DNN_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
        "payloadContainerType": ("uint8_t", False),
        "pduSessionId": ("PDUSessionId2_t", False),
        "presenceMask": ("uint32_t", False),
        "requestType": ("requestType_t", False),
        "snssai": ("s_nssai_t", False),
    },
    "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR_NOTHING": (
        "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR_NRPPa_PDU": (
        "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR_RoutingID": (
        "UplinkNonUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkNonUEAssociatedNRPPaTransportIEs__value_u": {
        "NRPPa_PDU": ("NRPPa_PDU_t", False),
        "RoutingID": ("RoutingID_t", False),
    },
    "UplinkNonUEAssociatedNRPPaTransportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UplinkNonUEAssociatedNRPPaTransportIEs__value", False),
    },
    "UplinkNonUEAssociatedNRPPaTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P67_t", False),
    },
    "UplinkRANConfigurationTransferIEs__value_PR_NOTHING": (
        "UplinkRANConfigurationTransferIEs__value_PR",
        False,
    ),
    "UplinkRANConfigurationTransferIEs__value_PR_SONConfigurationTransfer": (
        "UplinkRANConfigurationTransferIEs__value_PR",
        False,
    ),
    "UplinkRANConfigurationTransferIEs__value_u": {
        "SONConfigurationTransfer": ("SONConfigurationTransfer_t", False)
    },
    "UplinkRANConfigurationTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UplinkRANConfigurationTransferIEs__value", False),
    },
    "UplinkRANConfigurationTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P56_t", False),
    },
    "UplinkRANStatusTransferIEs__value_PR_AMF_UE_NGAP_ID": (
        "UplinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "UplinkRANStatusTransferIEs__value_PR_NOTHING": (
        "UplinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "UplinkRANStatusTransferIEs__value_PR_RANStatusTransfer_TransparentContainer": (
        "UplinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "UplinkRANStatusTransferIEs__value_PR_RAN_UE_NGAP_ID": (
        "UplinkRANStatusTransferIEs__value_PR",
        False,
    ),
    "UplinkRANStatusTransferIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "RANStatusTransfer_TransparentContainer": (
            "RANStatusTransfer_TransparentContainer_t",
            False,
        ),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
    },
    "UplinkRANStatusTransferIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UplinkRANStatusTransferIEs__value", False),
    },
    "UplinkRANStatusTransfer_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P33_t", False),
    },
    "UplinkUEAssociatedNRPPaTransportIEs__value_PR_AMF_UE_NGAP_ID": (
        "UplinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkUEAssociatedNRPPaTransportIEs__value_PR_NOTHING": (
        "UplinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkUEAssociatedNRPPaTransportIEs__value_PR_NRPPa_PDU": (
        "UplinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkUEAssociatedNRPPaTransportIEs__value_PR_RAN_UE_NGAP_ID": (
        "UplinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkUEAssociatedNRPPaTransportIEs__value_PR_RoutingID": (
        "UplinkUEAssociatedNRPPaTransportIEs__value_PR",
        False,
    ),
    "UplinkUEAssociatedNRPPaTransportIEs__value_u": {
        "AMF_UE_NGAP_ID": ("AMF_UE_NGAP_ID_t", False),
        "NRPPa_PDU": ("NRPPa_PDU_t", False),
        "RAN_UE_NGAP_ID": ("RAN_UE_NGAP_ID_t", False),
        "RoutingID": ("RoutingID_t", False),
    },
    "UplinkUEAssociatedNRPPaTransportIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UplinkUEAssociatedNRPPaTransportIEs__value", False),
    },
    "UplinkUEAssociatedNRPPaTransport_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P65_t", False),
    },
    "UserLocationInformationEUTRA_ExtIEs__extensionValue_PR_NOTHING": (
        "UserLocationInformationEUTRA_ExtIEs__extensionValue_PR",
        False,
    ),
    "UserLocationInformationEUTRA_ExtIEs__extensionValue_u": {},
    "UserLocationInformationEUTRA_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UserLocationInformationEUTRA_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UserLocationInformationEUTRA_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "eUTRA_CGI": ("EUTRA_CGI_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "tAI": ("TAI_t", False),
        "timeStamp": ("TimeStamp_t", True),
    },
    "UserLocationInformationN3IWF_ExtIEs__extensionValue_PR_NOTHING": (
        "UserLocationInformationN3IWF_ExtIEs__extensionValue_PR",
        False,
    ),
    "UserLocationInformationN3IWF_ExtIEs__extensionValue_u": {},
    "UserLocationInformationN3IWF_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UserLocationInformationN3IWF_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UserLocationInformationN3IWF_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "iPAddress": ("TransportLayerAddress_t", False),
        "portNumber": ("PortNumber_t", False),
    },
    "UserLocationInformationNR_ExtIEs__extensionValue_PR_NOTHING": (
        "UserLocationInformationNR_ExtIEs__extensionValue_PR",
        False,
    ),
    "UserLocationInformationNR_ExtIEs__extensionValue_u": {},
    "UserLocationInformationNR_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UserLocationInformationNR_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UserLocationInformationNR_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "nR_CGI": ("NR_CGI_t", False),
        "tAI": ("TAI_t", False),
        "timeStamp": ("TimeStamp_t", True),
    },
    "UserLocationInformation_ExtIEs__value_PR_NOTHING": (
        "UserLocationInformation_ExtIEs__value_PR",
        False,
    ),
    "UserLocationInformation_ExtIEs__value_u": {},
    "UserLocationInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "UserLocationInformation_ExtIEs__value", False),
    },
    "UserLocationInformation_PR_NOTHING": ("UserLocationInformation_PR", False),
    "UserLocationInformation_PR_choice_Extensions": (
        "UserLocationInformation_PR",
        False,
    ),
    "UserLocationInformation_PR_userLocationInformationEUTRA": (
        "UserLocationInformation_PR",
        False,
    ),
    "UserLocationInformation_PR_userLocationInformationN3IWF": (
        "UserLocationInformation_PR",
        False,
    ),
    "UserLocationInformation_PR_userLocationInformationNR": (
        "UserLocationInformation_PR",
        False,
    ),
    "UserLocationInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserLocationInformation_u", False),
        "present": ("UserLocationInformation_PR", False),
    },
    "UserLocationInformation_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "userLocationInformationEUTRA": (
            "struct " "UserLocationInformationEUTRA",
            True,
        ),
        "userLocationInformationN3IWF": (
            "struct " "UserLocationInformationN3IWF",
            True,
        ),
        "userLocationInformationNR": ("struct " "UserLocationInformationNR", True),
    },
    "UserPlaneSecurityInformation_ExtIEs__extensionValue_PR_NOTHING": (
        "UserPlaneSecurityInformation_ExtIEs__extensionValue_PR",
        False,
    ),
    "UserPlaneSecurityInformation_ExtIEs__extensionValue_u": {},
    "UserPlaneSecurityInformation_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "UserPlaneSecurityInformation_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "UserPlaneSecurityInformation_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "securityIndication": ("SecurityIndication_t", False),
        "securityResult": ("SecurityResult_t", False),
    },
    "VID_TAG_t": {"spare": ("uint8_t", False), "vid": ("uint16_t", False)},
    "WarningAreaCoordinates_t": ("OCTET_STRING_t", False),
    "WarningAreaList_ExtIEs__value_PR_NOTHING": (
        "WarningAreaList_ExtIEs__value_PR",
        False,
    ),
    "WarningAreaList_ExtIEs__value_u": {},
    "WarningAreaList_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct WarningAreaList_ExtIEs__value", False),
    },
    "WarningAreaList_PR_NOTHING": ("WarningAreaList_PR", False),
    "WarningAreaList_PR_choice_Extensions": ("WarningAreaList_PR", False),
    "WarningAreaList_PR_eUTRA_CGIListForWarning": ("WarningAreaList_PR", False),
    "WarningAreaList_PR_emergencyAreaIDList": ("WarningAreaList_PR", False),
    "WarningAreaList_PR_nR_CGIListForWarning": ("WarningAreaList_PR", False),
    "WarningAreaList_PR_tAIListForWarning": ("WarningAreaList_PR", False),
    "WarningAreaList_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("WarningAreaList_u", False),
        "present": ("WarningAreaList_PR", False),
    },
    "WarningAreaList_u": {
        "choice_Extensions": ("struct " "ProtocolIE_SingleContainer", True),
        "eUTRA_CGIListForWarning": ("struct " "EUTRA_CGIListForWarning", True),
        "emergencyAreaIDList": ("struct EmergencyAreaIDList", True),
        "nR_CGIListForWarning": ("struct NR_CGIListForWarning", True),
        "tAIListForWarning": ("struct TAIListForWarning", True),
    },
    "WarningMessageContents_t": ("OCTET_STRING_t", False),
    "WarningSecurityInfo_t": ("OCTET_STRING_t", False),
    "WarningType_t": ("OCTET_STRING_t", False),
    "WriteReplaceWarningRequestIEs__value_PR_ConcurrentWarningMessageInd": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_DataCodingScheme": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_MessageIdentifier": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_NOTHING": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_NumberOfBroadcastsRequested": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_RepetitionPeriod": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_SerialNumber": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_WarningAreaCoordinates": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_WarningAreaList": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_WarningMessageContents": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_WarningSecurityInfo": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_PR_WarningType": (
        "WriteReplaceWarningRequestIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningRequestIEs__value_u": {
        "ConcurrentWarningMessageInd": ("ConcurrentWarningMessageInd_t", False),
        "DataCodingScheme": ("DataCodingScheme_t", False),
        "MessageIdentifier": ("MessageIdentifier_t", False),
        "NumberOfBroadcastsRequested": ("NumberOfBroadcastsRequested_t", False),
        "RepetitionPeriod": ("RepetitionPeriod_t", False),
        "SerialNumber": ("SerialNumber_t", False),
        "WarningAreaCoordinates": ("WarningAreaCoordinates_t", False),
        "WarningAreaList": ("WarningAreaList_t", False),
        "WarningMessageContents": ("WarningMessageContents_t", False),
        "WarningSecurityInfo": ("WarningSecurityInfo_t", False),
        "WarningType": ("WarningType_t", False),
    },
    "WriteReplaceWarningRequestIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "WriteReplaceWarningRequestIEs__value", False),
    },
    "WriteReplaceWarningRequest_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P58_t", False),
    },
    "WriteReplaceWarningResponseIEs__value_PR_BroadcastCompletedAreaList": (
        "WriteReplaceWarningResponseIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningResponseIEs__value_PR_CriticalityDiagnostics": (
        "WriteReplaceWarningResponseIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningResponseIEs__value_PR_MessageIdentifier": (
        "WriteReplaceWarningResponseIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningResponseIEs__value_PR_NOTHING": (
        "WriteReplaceWarningResponseIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningResponseIEs__value_PR_SerialNumber": (
        "WriteReplaceWarningResponseIEs__value_PR",
        False,
    ),
    "WriteReplaceWarningResponseIEs__value_u": {
        "BroadcastCompletedAreaList": ("BroadcastCompletedAreaList_t", False),
        "CriticalityDiagnostics": ("CriticalityDiagnostics_t", False),
        "MessageIdentifier": ("MessageIdentifier_t", False),
        "SerialNumber": ("SerialNumber_t", False),
    },
    "WriteReplaceWarningResponseIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "id": ("ProtocolIE_ID_t", False),
        "value": ("struct " "WriteReplaceWarningResponseIEs__value", False),
    },
    "WriteReplaceWarningResponse_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "protocolIEs": ("ProtocolIE_Container_124P59_t", False),
    },
    "XCT_BOTH": ("xer_check_tag_e", False),
    "XCT_BROKEN": ("xer_check_tag_e", False),
    "XCT_CLOSING": ("xer_check_tag_e", False),
    "XCT_OPENING": ("xer_check_tag_e", False),
    "XCT_UNKNOWN_BO": ("xer_check_tag_e", False),
    "XCT_UNKNOWN_CL": ("xer_check_tag_e", False),
    "XCT_UNKNOWN_OP": ("xer_check_tag_e", False),
    "XCT__UNK__MASK": ("xer_check_tag_e", False),
    "XnExtTLA_Item_ExtIEs__extensionValue_PR_NOTHING": (
        "XnExtTLA_Item_ExtIEs__extensionValue_PR",
        False,
    ),
    "XnExtTLA_Item_ExtIEs__extensionValue_u": {},
    "XnExtTLA_Item_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": ("struct " "XnExtTLA_Item_ExtIEs__extensionValue", False),
        "id": ("ProtocolExtensionID_t", False),
    },
    "XnExtTLA_Item_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "gTP_TLAs": ("struct XnGTP_TLAs", True),
        "iE_Extensions": ("struct ProtocolExtensionContainer", True),
        "iPsecTLA": ("TransportLayerAddress_t", True),
    },
    "XnExtTLAs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(struct XnExtTLA_Item)", False),
    },
    "XnGTP_TLAs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(TransportLayerAddress_t)", False),
    },
    "XnTLAs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "list": ("A_SEQUENCE_OF(TransportLayerAddress_t)", False),
    },
    "XnTNLConfigurationInfo_ExtIEs__extensionValue_PR_NOTHING": (
        "XnTNLConfigurationInfo_ExtIEs__extensionValue_PR",
        False,
    ),
    "XnTNLConfigurationInfo_ExtIEs__extensionValue_u": {},
    "XnTNLConfigurationInfo_ExtIEs_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "criticality": ("Criticality_t", False),
        "extensionValue": (
            "struct " "XnTNLConfigurationInfo_ExtIEs__extensionValue",
            False,
        ),
        "id": ("ProtocolExtensionID_t", False),
    },
    "XnTNLConfigurationInfo_t": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "iE_Extensions": ("struct " "ProtocolExtensionContainer", True),
        "xnExtendedTransportLayerAddresses": ("struct " "XnExtTLAs", True),
        "xnTransportLayerAddresses": ("XnTLAs_t", False),
    },
    "_5GSMMsg_t": {
        "SessionEstdAccept": ("SessionEstdAccept_t", False),
        "SessionEstdReject": ("SessionEstdReject_t", False),
        "SessionEstdRequest": ("SessionEstdRequest_t", False),
        "SessionModReject": ("PduSessionModificationReject_t", False),
        "SessionModRequest": ("PduSessionModificationRequest_t", False),
        "SessionRelReq": ("SessionRelReq_t", False),
        "sessionModCommand": ("PduSessionModificationCommand_t", False),
        "sessionModComplete": ("PduSessionModificationComplete_t", False),
        "sessionRelCommand": ("SessionRelCommand_t", False),
        "sessionRelComplete": ("SessionRelComplete_t", False),
        "smheader": ("_5gsmMsgHeader_t", False),
    },
    "_5gDeregistrationType_t": {
        "accessType": ("uint8_t", False),
        "regRequired": ("uint8_t", False),
        "switchoff": ("uint8_t", False),
        "uint8_t": ("", False),
    },
    "_5gMMMsg_t": {
        "_5gmmStatus": ("_5gmmStatus_t", False),
        "authFailMsg": ("AuthenticationFailureMsg_t", False),
        "authRej": ("AuthenticationRejectMsg_t", False),
        "authReqMsg": ("AuthenticationRequestMsg_t", False),
        "authRespMsg": ("AuthenticationResponseMsg_t", False),
        "deregAcceptMsg": ("DeregistrationAccept_t", False),
        "deregReqMsg": ("DeregistrationRequest_t", False),
        "downlinkNasTransport": ("DownlinkNasTransport_t", False),
        "mmheader": ("_5gmmMsgHeader_t", False),
        "regAcceptMsg": ("RegistrationAcceptMsg_t", False),
        "regComplMsg": ("RegistrationCompleteMsg_t", False),
        "regReject": ("RegistrationReject_t", False),
        "regReqMsg": ("RegistrationRequest_t", False),
        "secModeCmdMsg": ("SecurityModeCommand_t", False),
        "secModeCompMsg": ("SecurityModeComplete_t", False),
        "secModeRejMsg": ("SecurityModeReject_t", False),
        "servAccMsg": ("ServiceAccept_t", False),
        "servRejMsg": ("ServiceReject_t", False),
        "servReqMsg": ("ServiceRequest_t", False),
        "uplinkNasTransport": ("UplinkNasTransport_t", False),
    },
    "_5gMobileId_t": {
        "guti5gMobileId": ("guti_5gMobileId_t", False),
        "len": ("uint16_t", False),
        "suci5gMobileId": ("suci_5gMobileId_t", False),
    },
    "_5gRegistrationResult_t": {
        "len": ("uint8_t", False),
        "smsAllowed": ("uint8_t", False),
        "spare": ("uint8_t", False),
        "value": ("uint8_t", False),
    },
    "_5gRegistrationType_t": {
        "FOR": ("uint8_t", False),
        "spare": ("uint8_t", False),
        "value": ("uint8_t", False),
    },
    "_5gServiceType_t": {"spare": ("uint8_t", False), "value": ("uint8_t", False)},
    "_5gTmsi_t": {"value": ("uint32_t", False)},
    "_5gmmCapability_t": {"hoS1": ("uint8_t", False), "len": ("uint8_t", False)},
    "_5gmmCause_t": {"causeValue": ("uint8_t", False)},
    "_5gmmMsgHeader_t": {
        "align": ("uint8_t", True),
        "epd": ("ExtendedProtocolDiscriminator_t", False),
        "msgType": ("NasMessageType_t", False),
        "secuHeader": ("SecurityHeaderType_t", False),
    },
    "_5gmmStatus_t": {
        "_5gmmCause": ("uint8_t", False),
        "mmHeader": ("_5gmmMsgHeader_t", False),
    },
    "_5gsRegistrationType_t": {
        "_5gsRegistrationTypeValue": ("uint8_t", False),
        "for1": ("uint8_t", False),
    },
    "_5gsTmsi_t": {
        "_5gTmsi": ("_5gTmsi_t", False),
        "amfPointer": ("uint16_t", False),
        "amfSetID": ("uint16_t", False),
        "idType": ("uint8_t", False),
        "len": ("uint16_t", False),
        "setBits": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "_5gsTrackingAreaIdentity_t": {
        "mccDigit1": ("uint8_t", False),
        "mccDigit2": ("uint8_t", False),
        "mccDigit3": ("uint8_t", False),
        "mncDigit1": ("uint8_t", False),
        "mncDigit2": ("uint8_t", False),
        "mncDigit3": ("uint8_t", False),
        "tac": ("uint32_t", False),
    },
    "_5gsmCapability_t": {
        "lengthOf5gsmCapabilityContents": ("uint8_t", False),
        "mh6Pdu": ("uint8_t", False),
        "rqos": ("uint8_t", False),
        "spare": ("uint8_t", False),
        "spare1": ("uint8_t", True),
    },
    "_5gsmCause_t": {"causeValue": ("uint8_t", False)},
    "_5gsmMsgHeader_t": {
        "PduSessionid": ("PduSessionid_t", False),
        "Pti": ("Pti_t", False),
        "align": ("uint8_t", True),
        "epd": ("ExtendedProtocolDiscriminator_t", False),
        "msgType": ("NasMessageType_t", False),
    },
    "_links": ("string", True),
    "additionalSnssaiData": ("additionalSnssaiDataEl", True),
    "additionalSnssaiDataEl": ("JSON", False),
    "allowedSessionTypes": ("string", True),
    "allowedSessionTypesEl": ("string", False),
    "allowedSscModes": ("allowedSscModesEl", True),
    "allowedSscModesEl": ("string", False),
    "amf-id": ("string", False),
    "amf-nssai": ("JSON", False),
    "amf-s-nssai-list": ("JSON", False),
    "amfId": ("string", False),
    "amfInstanceId": ("string", False),
    "amfPointer": ("int", False),
    "amfRegionId": ("int", False),
    "amfSetId": ("int", False),
    "anType": ("string", False),
    "apiFullVersion": ("string", False),
    "apiVersionInUri": ("string", False),
    "applyAction_t": {
        "BUFF": ("uint8_t", False),
        "DROP": ("uint8_t", False),
        "DUPL": ("uint8_t", False),
        "FORW": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "NOCP": ("uint8_t", False),
    },
    "arp": ("JSON", False),
    "asn_CHOICE_specifics_t": {
        "ctx_offset": ("unsigned", False),
        "ext_start": ("signed", False),
        "from_canonical_order": ("const unsigned", True),
        "pres_offset": ("unsigned", False),
        "pres_size": ("unsigned", False),
        "struct_size": ("unsigned", False),
        "tag2el": ("const asn_TYPE_tag2member_t", True),
        "tag2el_count": ("unsigned", False),
        "to_canonical_order": ("const unsigned", True),
    },
    "asn_INTEGER_enum_map_t": {
        "enum_len": ("size_t", False),
        "enum_name": ("const char", True),
        "nat_value": ("long", False),
    },
    "asn_INTEGER_specifics_t": {
        "enum2value": ("const unsigned int", True),
        "extension": ("int", False),
        "field_unsigned": ("int", False),
        "field_width": ("int", False),
        "map_count": ("int", False),
        "strict_enumeration": ("int", False),
        "value2enum": ("const asn_INTEGER_enum_map_t", True),
    },
    "asn_SEQUENCE_specifics_t": {
        "aoms_count": ("unsigned", False),
        "ctx_offset": ("unsigned", False),
        "first_extension": ("signed", False),
        "oms": ("const int", True),
        "roms_count": ("unsigned", False),
        "struct_size": ("unsigned", False),
        "tag2el": ("const asn_TYPE_tag2member_t", True),
        "tag2el_count": ("unsigned", False),
    },
    "asn_SET_OF_specifics_t": {
        "as_XMLValueList": ("int", False),
        "ctx_offset": ("unsigned", False),
        "struct_size": ("unsigned", False),
    },
    "asn_TYPE_descriptor_t": {
        "all_tags": ("const ber_tlv_tag_t", True),
        "all_tags_count": ("unsigned", False),
        "elements": ("struct asn_TYPE_member_s", True),
        "elements_count": ("unsigned", False),
        "encoding_constraints": ("asn_encoding_constraints_t", False),
        "name": ("const char", True),
        "op": ("asn_TYPE_operation_t", True),
        "specifics": ("const void", True),
        "tags": ("const ber_tlv_tag_t", True),
        "tags_count": ("unsigned", False),
        "xml_tag": ("const char", True),
    },
    "asn_TYPE_member_t": {
        "*sptr)": ("int (*default_value_set)(void", True),
        "encoding_constraints": ("asn_encoding_constraints_t", False),
        "flags": ("enum asn_TYPE_flags_e", False),
        "memb_offset": ("unsigned", False),
        "name": ("const char", True),
        "optional": ("unsigned", False),
        "sptr)": ("int (*default_value_cmp)(const void", True),
        "tag": ("ber_tlv_tag_t", False),
        "tag_mode": ("int", False),
        "type": ("asn_TYPE_descriptor_t", True),
        "type_selector": ("asn_type_selector_f", True),
    },
    "asn_TYPE_operation_t": {
        "": ("", False),
        "aper_decoder": ("per_type_decoder_f", True),
        "aper_encoder": ("per_type_encoder_f", True),
        "asn_TYPE_operation_": ("typedef struct", False),
        "ber_decoder": ("ber_type_decoder_f", True),
        "compare_struct": ("asn_struct_compare_f", True),
        "der_encoder": ("der_type_encoder_f", True),
        "free_struct": ("asn_struct_free_f", True),
        "oer_decoder": ("oer_type_decoder_f", True),
        "oer_encoder": ("oer_type_encoder_f", True),
        "outmost_tag": ("asn_outmost_tag_f", True),
        "parent_structure_ptr)": ("const void", True),
        "print_struct": ("asn_struct_print_f", True),
        "random_fill": ("asn_random_fill_f", True),
        "uper_decoder": ("per_type_decoder_f", True),
        "uper_encoder": ("per_type_encoder_f", True),
        "xer_decoder": ("xer_type_decoder_f", True),
        "xer_encoder": ("xer_type_encoder_f", True),
    },
    "asn_TYPE_tag2member_t": {
        "el_no": ("unsigned", False),
        "el_tag": ("ber_tlv_tag_t", False),
        "toff_first": ("int", False),
        "toff_last": ("int", False),
    },
    "asn_enc_rval_t": {"encoded": ("ssize_t", False)},
    "asn_encoding_constraints_t": {
        "general_constraints": ("asn_constr_check_f", True),
        "oer_constraints": ("const struct " "asn_oer_constraints_s", True),
        "per_constraints": ("const struct " "asn_per_constraints_s", True),
    },
    "asn_oer_constraint_number_t": {
        "positive": ("unsigned", False),
        "width": ("unsigned", False),
    },
    "asn_oer_constraints_t": {
        "size": ("ssize_t", False),
        "value": ("asn_oer_constraint_number_t", False),
    },
    "asn_oid_arc_t": ("uint32_t", False),
    "asn_per_constraints_t": {
        "code)": ("int (*code2value)(unsigned int", False),
        "size": ("asn_per_constraint_t", False),
        "value": ("asn_per_constraint_t", False),
        "value)": ("int (*value2code)(unsigned int", False),
    },
    "asn_per_data_t": ("asn_bit_data_s", False),
    "asn_per_outp_t": ("asn_bit_outp_s", False),
    "asn_struct_ctx_t": {
        "context": ("int", False),
        "left": ("ber_tlv_len_t", False),
        "phase": ("short", False),
        "ptr": ("void", True),
        "step": ("short", False),
    },
    "asn_type_selector_result_t": {
        "": ("", False),
        "app_key)": ("asn_app_consume_bytes_f " "*callback, void", True),
        "asn_TYPE_outmost_tag": ("asn_outmost_tag_f", False),
        "asn_struct_free_method)": ("void *struct_ptr, " "enum", False),
        "asn_type_selector_result_": ("typedef struct", False),
        "ber_tlv_tag_t(asn_outmost_tag_f)": ("typedef", False),
        "int(asn_struct_compare_f)": ("typedef", False),
        "int(asn_struct_print_f)": (
            "(asn_DEF).op->free_struct(&(asn_DEF), " "(ptr), " "ASFM_FREE_UNDERLYING)",
            False,
        ),
        "level": ("int", False),
        "presence_index": ("unsigned", False),
        "struct_A": ("const void", True),
        "struct_B)": ("const void", True),
        "struct_ptr": ("const void", True),
        "tag)": ("const void *struct_ptr, int " "tag_mode, ber_tlv_tag_t", False),
        "type_descriptor": ("const struct " "asn_TYPE_descriptor_s", True),
    },
    "authData": ("string", False),
    "authDefQos": ("JSON", False),
    "authResult": ("string", False),
    "authSessAmbr": ("JSON", False),
    "authType": ("string", False),
    "autn": ("string", False),
    "ber_tlv_len_t": ("ssize_t", False),
    "ber_tlv_tag_t": ("unsigned", False),
    "body": ("JSON", False),
    "createBAR_ANY_t": ("pfcpAny_t", False),
    "createBAR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "createFAR_ANY_t": ("pfcpAny_t", False),
    "createFAR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "createPDR_ANY_t": ("pfcpAny_t", False),
    "createPDR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "createQER_ANY_t": ("pfcpAny_t", False),
    "createQER_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "createdPDR_ANY_t": ("pfcpAny_t", False),
    "createdPDR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "defQosFlowIndication": ("boolean", False),
    "default-dnn": ("string", False),
    "default-dnn-for-smf-selection": ("string", False),
    "defaultDnnIndicator": ("boolean", False),
    "defaultSessionType": ("string", False),
    "defaultSingleNssais": ("defaultSingleNssaisEl", True),
    "defaultSingleNssaisEl": ("JSON", False),
    "defaultSscMode": ("string", False),
    "deregCallbackUri": ("string", False),
    "dlDataReport_ANY_t": ("pfcpAny_t", False),
    "dnn": ("string", False),
    "dnn-list": ("JSON", True),
    "dnn1.slice1.net": ("JSON", False),
    "dnnConfigurations": ("JSON", False),
    "dnnInfosEl": ("JSON", False),
    "downlink": ("string", False),
    "downlinkDataReport_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "downlinkValue": ("int", False),
    "emergencyRegistration": ("_5gRegistrationTypeValue_t", False),
    "expiry": ("string", False),
    "failedRuleId_t": {"IEI": ("uint16_t", False), "ruleIdType": ("uint8_t", False)},
    "flags": {
        "": ("", False),
        "0x": ("APC_EXTENSIBLE =", False),
        "0x0": ("APC_UNCONSTRAINED =", False),
        "0x1": ("APC_SEMI_CONSTRAINED =", False),
        "0x2": ("APC_CONSTRAINED =", False),
        "asn_per_constraint_flag": ("enum", False),
    },
    "flowDescription": ("string", False),
    "flowDirection": ("string", False),
    "flowInfos": ("flowInfosEl", True),
    "flowInfosEl": ("JSON", False),
    "fteid_t": {
        "CH": ("uint8_t", False),
        "CHID": ("uint8_t", False),
        "TEID": ("uint32_t", False),
        "V4": ("uint8_t", False),
        "V6": ("uint8_t", False),
        "chooseId": ("uint8_t", False),
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
    },
    "fwdParam_ANY_t": ("pfcpAny_t", False),
    "fwdParam_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "gateStatus_t": {
        "DL_GATE": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "UL_GATE": ("uint8_t", False),
    },
    "gbr_t": {"DL_GBR": ("uint64_t", False), "UL_GBR": ("uint64_t", False)},
    "guami": ("JSON", False),
    "guamiAndGutiInfo": ("JSON", False),
    "guti_5gMobileId_t": {
        "_5gTMSI": ("uint32_t", False),
        "amfPointer": ("uint16_t", False),
        "amfRegionId": ("uint8_t", False),
        "amfSetId": ("uint16_t", False),
        "identityType": ("uint8_t", False),
        "mccDigit1": ("uint8_t", False),
        "mccDigit2": ("uint8_t", False),
        "mccDigit3": ("uint8_t", False),
        "mncDigit1": ("uint8_t", False),
        "mncDigit2": ("uint8_t", False),
        "mncDigit3": ("uint8_t", False),
        "reserved": ("uint8_t", False),
        "spare": ("uint8_t", False),
    },
    "header": ("JSON", False),
    "heartBeatTimer": ("int", False),
    "hxresStar": ("string", False),
    "initialRegistration": ("_5gRegistrationTypeValue_t", False),
    "integProtMaxDataRate_t": {
        "downlinkRate": ("uint8_t", False),
        "uplinkRate": ("uint8_t", False),
    },
    "ipEndPointEl": ("JSON", False),
    "ipEndPoints": ("ipEndPointEl", True),
    "ipv4Address": ("string", False),
    "ipv4Addresses": ("string", True),
    "ipv4addresses": ("string", True),
    "json": ("JSON", False),
    "kSeaf": ("string", False),
    "maxNoSupPackFilts_t": {
        "spare": ("uint8_t", False),
        "supportedPacketFilters": ("uint16_t", False),
    },
    "maxNumOfUEsSupported": ("int", False),
    "mbr_t": {"DL_MBR": ("uint64_t", False), "UL_MBR": ("uint64_t", False)},
    "mcc": ("string", False),
    "method": ("string", False),
    "mnc": ("string", False),
    "mobilityRegistrationUpdating": ("_5gRegistrationTypeValue_t", False),
    "multipart": {"parts": ("string", True)},
    "multipart_body": ("multipart", False),
    "multiplePayloads_t": {
        "entry": ("payloadEntry_t", True),
        "numberOfEntries": ("int", False),
    },
    "myNodeId": ("string", False),
    "myNodeIdType": ("string", False),
    "n1MessageClass": ("string", False),
    "n1MessageContainer": ("JSON", False),
    "n2InfoContainer": ("JSON", False),
    "n2InfoContent": ("JSON", False),
    "n2InformationClass": ("string", False),
    "n2SmInfoType": ("string", False),
    "name": ("string", False),
    "namf-communication": ("JSON", False),
    "namf-communication-response": ("JSON", False),
    "nasMessagePlain_t": {
        "_5gmmMsg": ("_5gMMMsg_t", False),
        "_5gsmMsg": ("_5GSMMsg_t", False),
    },
    "nasMessageSecurityHeader_t": {
        "epd": ("ExtendedProtocolDiscriminator_t", False),
        "macCode": ("uint32_t", False),
        "pduSessionId": ("uint8_t", False),
        "pti": ("uint8_t", False),
        "secuHeader": ("SecurityHeaderType_t", False),
        "sqnNum": ("uint8_t", False),
    },
    "nasMessage_t": {
        "header": ("nasMessageSecurityHeader_t", False),
        "plain": ("nasMessagePlain_t", False),
    },
    "networkIP": ("string", False),
    "networkName": ("string", False),
    "nfInstance": ("JSON", False),
    "nfInstanceId": ("string", False),
    "nfInstances": ("nfInstance", True),
    "nfService": ("JSON", False),
    "nfServiceStatus": ("string", False),
    "nfServices": ("nfService", True),
    "nfStatus": ("string", False),
    "nfType": ("string", False),
    "ngapIeType": ("string", False),
    "nodeId_t": {"IEI": ("uint16_t", False), "nodeIdType": ("uint8_t", False)},
    "notificationUri": ("string", False),
    "npcf-smpolicycontrol": ("JSON", False),
    "npcf-smpolicycontrol-response": ("JSON", False),
    "nsmf-pdusession-create": ("JSON", False),
    "nsmf-pdusession-create-response": ("JSON", False),
    "nsmf-pdusession-modify": ("JSON", False),
    "nsmf-pdusession-modify-response": ("JSON", False),
    "nssai_t": {"Nssai": ("s_nssai_t", True), "no_of_slices": ("uint8_t", False)},
    "nudm-sdm": ("JSON", False),
    "nudm-sdm-response": ("nudm-sdm-responseEl", True),
    "nudm-sdm-responseEl": ("JSON", False),
    "nudm-uecm": ("JSON", False),
    "nudm-uecm-response": ("JSON", False),
    "num-slices": ("int", False),
    "offendingIE_t": {"IEI": ("uint16_t", False), "offendingIEI": ("uint16_t", False)},
    "ohc_t": {
        "description": ("uint16_t", False),
        "ipv4Addr": ("uint8_t", True),
        "ipv6Addr": ("uint8_t", True),
        "port": ("uint16_t", False),
        "teid": ("uint32_t", False),
    },
    "ohr_t": {
        "description": ("uint8_t", False),
        "gtpUextensionHdrDel": ("uint8_t", False),
    },
    "outHdrCreatn_t": {
        "IEI": ("uint16_t", False),
        "description": ("uint16_t", False),
        "ipv4Addr": ("uint8_t", True),
        "ipv6Addr": ("uint8_t", True),
        "port": ("uint16_t", False),
        "teid": ("uint32_t", False),
    },
    "outerHdrRemoval_t": {
        "IEI": ("uint16_t", False),
        "description": ("uint8_t", False),
        "gtpUextensionHdrDel": ("uint8_t", False),
    },
    "packFiltId": ("string", False),
    "packetFilterList": {
        "packetFilterListCreate": ("PacketFilterListCreate_t", True),
        "packetFilterListDelete": ("PacketFilterListDelete_t", True),
    },
    "packetRate_t": {
        "DLPR": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "ULPR": ("uint8_t", False),
        "downlinkTimeUnit": ("uint8_t", False),
        "maximumDownlinkPacketRate": ("uint16_t", False),
        "maximumUplinkPacketRate": ("uint16_t", False),
        "uplinkTimeUnit": ("uint8_t", False),
        "value": ("uint32_t", False),
    },
    "partialTAIList_t": {
        "listType": ("uint8_t", False),
        "numOfElmnts": ("uint8_t", False),
        "tAI": ("tAI_t", True),
    },
    "payloadEntry_t": {
        "containerType": ("uint8_t", False),
        "content": ("uint8_t", True),
        "contentLen": ("uint8_t", False),
        "numOfIEs": ("uint8_t", False),
        "optIEs": ("payloadOptIE_t", True),
    },
    "payloadOptIE_t": {"IEI": ("uint8_t", False)},
    "pccRuleId": ("string", False),
    "pccRules": ("JSON", False),
    "pduAddress_t": {
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
        "type": ("uint8_t", False),
        "uint8_t": ("", False),
    },
    "pduSessionId": ("int", False),
    "pduSessionResultCause_t": {
        "length": ("uint16_t", False),
        "psiCause": ("psiCause_t", True),
    },
    "pduSessionResult_t": {"len": ("uint8_t", False), "psi": ("uint16_t", False)},
    "pduSessionStatus_t": {"len": ("uint8_t", False), "psi": ("uint16_t", False)},
    "pduSessionType": ("string", False),
    "pduSessionType_t": {
        "pdu_session_type_value": ("uint8_t", False),
        "uint8_t": ("", False),
    },
    "pduSessionTypes": ("JSON", False),
    "periodicRegistrationUpdating": ("_5gRegistrationTypeValue_t", False),
    "pfcpAny_t": {
        "IEI": ("uint16_t", False),
        "bufLen": ("uint16_t", False),
        "buffer": ("uint8_t", True),
    },
    "pfcpBarID_t": {"IEI": ("uint16_t", False), "value": ("uint8_t", False)},
    "pfcpCause_t": {"IEI": ("uint16_t", False), "cause": ("uint8_t", False)},
    "pfcpDLDataNotificationDelay_t": {
        "IEI": ("uint16_t", False),
        "value": ("uint8_t", False),
    },
    "pfcpDlvWS_t": {
        "buffer": ("uint8_t", True),
        "encodedLen": ("uint16_t", False),
        "msgType": ("int", False),
        "peerIpAddr": ("std::string", False),
        "pfcpClientId": ("uint", False),
        "seid": ("uint32_t", False),
        "sin": ("struct sockaddr_in", False),
    },
    "pfcpFSEID_t": {
        "IEI": ("uint16_t", False),
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
        "seid": ("uint64_t", False),
        "v4v6": ("uint8_t", False),
    },
    "pfcpFTEID_t": {
        "CH": ("uint8_t", False),
        "CHID": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "TEID": ("uint32_t", False),
        "V4": ("uint8_t", False),
        "V6": ("uint8_t", False),
        "chooseId": ("uint8_t", False),
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
    },
    "pfcpFarID_t": {"IEI": ("uint16_t", False), "value": ("uint32_t", False)},
    "pfcpHeader_t": {
        "MP": ("uint8_t", False),
        "MessagePriority": ("uint8_t", False),
        "MessageType": ("uint8_t", False),
        "S": ("uint8_t", False),
        "SEID": ("uint64_t", False),
        "SequenceNumber": ("uint32_t", False),
        "spare": ("uint8_t", False),
        "version": ("uint8_t", False),
    },
    "pfcpIE_t": {
        "": ("", False),
        "IEI": ("uint16_t", False),
        "MP": ("uint8_t", False),
        "MessagePriority": ("uint8_t", False),
        "MessageType": ("uint8_t", False),
        "S": ("uint8_t", False),
        "SEID": ("uint64_t", False),
        "SequenceNumber": ("uint32_t", False),
        "applyAction": ("applyAction_t", False),
        "barId": ("pfcpBarID_t", False),
        "cause": ("pfcpCause_t", False),
        "createBARany": ("createBAR_ANY_t", False),
        "createFARany": ("createFAR_ANY_t", False),
        "createPDRany": ("createPDR_ANY_t", False),
        "createQERany": ("createQER_ANY_t", False),
        "createdPDRany": ("createdPDR_ANY_t", False),
        "destIface": ("sdIface_t", False),
        "dlDataNotifDelay": ("pfcpDLDataNotificationDelay_t", False),
        "dlDataReportany": ("dlDataReport_ANY_t", False),
        "failedRuleId": ("failedRuleId_t", False),
        "farId": ("pfcpFarID_t", False),
        "fseid": ("pfcpFSEID_t", False),
        "fteid": ("pfcpFTEID_t", False),
        "fwdParamAny": ("fwdParam_ANY_t", False),
        "gateStatus": ("gateStatus_t", False),
        "gbr": ("GBR_t", False),
        "mbr": ("MBR_t", False),
        "nodeId": ("nodeId_t", False),
        "offendingIE": ("offendingIE_t", False),
        "outerHdrCreatn": ("outHdrCreatn_t", False),
        "outerHdrRem": ("outerHdrRemoval_t", False),
        "packetRate": ("packetRate_t", False),
        "pdiAny": ("pfcpPDI_ANY_t", False),
        "pdrId": ("pfcpPdrId_t", False),
        "pfcpI": ("typedef union", False),
        "precedence": ("precedence_t", False),
        "qerCorrelationId": ("QerCorrelationID_t", False),
        "qerId": ("pfcpQerID_t", False),
        "qfi": ("QFI_t", False),
        "recTimeStamp": ("recTimeStamp_t", False),
        "removeBARany": ("removeBAR_ANY_t", False),
        "removeFARany": ("removeFAR_ANY_t", False),
        "removePDRany": ("removePDR_ANY_t", False),
        "removeQERany": ("removeQER_ANY_t", False),
        "reportType": ("reportType_t", False),
        "sdfFilter": ("sdfFilter_t", False),
        "spare": ("uint8_t", False),
        "srcIface": ("sdIface_t", False),
        "sugBufPktCnt": ("pfcpSuggestedBufPktCount_t", False),
        "ueIpAddr": ("ueIpaddress_t", False),
        "upIpResInfo": ("usrPlaneIpResInfo_t", False),
        "updateFARany": ("updateFAR_ANY_t", False),
        "updateFwdParamany": ("updateFwdParam_ANY_t", False),
        "updatePDRany": ("updatePDR_ANY_t", False),
        "updateQERany": ("updateQER_ANY_t", False),
        "updatedPDRany": ("updatedPDR_ANY_t", False),
        "version": ("uint8_t", False),
    },
    "pfcpIEdata_t": {"flags": ("uint16_t", False)},
    "pfcpIEops_t": {
        "decodedLen)": ("uint16_t", True),
        "encodedLen)": ("uint16_t", True),
        "ptr": ("int (*decode)(uint8_t *buffer, uint16_t bufLen, void", True),
    },
    "pfcpMessage_t": {
        "body": ("std::vector<pfcpIE_t>", False),
        "header": ("pfcpHeader_t", False),
    },
    "pfcpPDI_ANY_t": ("pfcpAny_t", False),
    "pfcpPDI_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "pfcpPdrId_t": {"IEI": ("uint16_t", False), "ruleId": ("uint16_t", False)},
    "pfcpQerID_t": {"IEI": ("uint16_t", False), "value": ("uint32_t", False)},
    "pfcpRelInstance_t": {
        "smContextId)": ("void (*pfcpTimeoutCB)(uint32_t seqN, " "uint32_t", False),
        "streamId)": (
            "void (*pfcpRespCB)(pfcpMessage_t *msg, " "uint Id, uint16_t",
            False,
        ),
    },
    "pfcpSuggestedBufPktCount_t": {
        "IEI": ("uint16_t", False),
        "value": ("uint8_t", False),
    },
    "pktRate_t": {
        "DLPR": ("uint8_t", False),
        "ULPR": ("uint8_t", False),
        "downlinkTimeUnit": ("uint8_t", False),
        "maximumDownlinkPacketRate": ("uint16_t", False),
        "maximumUplinkPacketRate": ("uint16_t", False),
        "uplinkTimeUnit": ("uint8_t", False),
    },
    "plmn": ("JSON", False),
    "plmn-id": ("string", False),
    "plmn-mcc": ("int", False),
    "plmn-mnc": ("int", False),
    "plmn-mnc-size": ("int", False),
    "plmnId": ("JSON", False),
    "port": ("int", False),
    "precedence": ("int", False),
    "precedence_t": {"IEI": ("uint16_t", False), "precedence": ("uint32_t", False)},
    "preemptCap": ("string", False),
    "preemptVuln": ("string", False),
    "priorityLevel": ("int", False),
    "psiCause_t": {"_5gmmCause": ("_5gmmCause_t", False), "psi": ("uint8_t", False)},
    "pxer_chunk_type_e": {
        "": ("", False),
        "*struct_ptr": (
            "const struct asn_TYPE_descriptor_s " "*type_descriptor, void",
            True,
        ),
        "PXER_COMMEN": ("", False),
        "PXER_TAG": ("", False),
        "PXER_TEXT": ("", False),
        "PXER_WMORE": ("", False),
        "chunk_buf": ("ssize_t (*body_receiver)(void " "*struct_key, const void", True),
        "chunk_size)": ("size_t", False),
        "ctx": ("asn_struct_ctx_t", True),
        "have_more))": ("size_t chunk_size, int", False),
        "opt_codec_ctx": ("const asn_codec_ctx_t", True),
        "opt_mname": ("const char", True),
        "pxer_chunk_typ": ("typedef enum", False),
        "size": ("const void *buf_ptr, size_t", False),
        "size)": ("const void *buf_ptr, size_t", False),
        "struct_key": ("void", True),
        "xer_decode_general": ("asn_dec_rval_t", False),
        "xml_tag": ("const char", True),
    },
    "qfi": ("int", False),
    "qfi_t": {"value": ("uint8_t", False)},
    "qosDecs": ("JSON", False),
    "qosId": ("string", False),
    "query": ("JSON", False),
    "queryParams": ("JSON", False),
    "rand": ("string", False),
    "ratType": ("string", False),
    "recTimeStamp_t": {"IEI": ("uint16_t", False), "timestamp": ("uint8_t", True)},
    "refQosData": ("refQosDataEl", True),
    "refQosDataEl": ("string", False),
    "rejectedNssai_t": {
        "Nssai": ("rejected_s_nssai_t", True),
        "no_of_slices": ("uint8_t", False),
    },
    "rejected_s_nssai_t": {
        "len_s_nssai": ("uint8_t", False),
        "reject_cause": ("uint8_t", False),
        "sD": ("uint32_t", False),
        "sST": ("uint8_t", False),
    },
    "relativeAMFcapacity": ("int", False),
    "removeBAR_ANY_t": ("pfcpAny_t", False),
    "removeBAR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "removeFAR_ANY_t": ("pfcpAny_t", False),
    "removeFAR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "removePDR_ANY_t": ("pfcpAny_t", False),
    "removePDR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "removeQER_ANY_t": ("pfcpAny_t", False),
    "removeQER_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "reportType_t": {
        "IEI": ("uint16_t", False),
        "dldr": ("uint8_t", False),
        "erir": ("uint8_t", False),
        "uint8_t": ("", False),
        "upir": ("uint8_t", False),
        "usar": ("uint8_t", False),
    },
    "requestType_t": {"value": ("uint8_t", False)},
    "requester-nf-type": ("string", False),
    "requiredAuthnAuthz": ("boolean", False),
    "resStar": ("string", False),
    "reservedValue": ("_5gRegistrationTypeValue_t", False),
    "resource": ("string", False),
    "s-nssai-list": ("JSON", True),
    "sNssai": ("JSON", False),
    "s_nssai_t": {
        "len_s_nssai": ("uint8_t", False),
        "sD": ("uint32_t", False),
        "sST": ("uint8_t", False),
    },
    "scheme": ("string", False),
    "sd": ("string", False),
    "sdIface_t": {"IEI": ("uint16_t", False), "interfaceValue": ("uint8_t", False)},
    "sdfFilter_t": {
        "BID": ("uint8_t", False),
        "FD": ("uint8_t", False),
        "FL": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "SPI": ("uint8_t", False),
        "TTC": ("uint8_t", False),
        "flowDescription": ("uint8_t", True),
        "flowLabel": ("uint8_t", True),
        "lengthOfFlowDescription": ("uint16_t", False),
        "presenceMask": ("uint32_t", False),
        "sdfFilterId": ("uint8_t", True),
        "securityParameterIndex": ("uint8_t", True),
        "spare": ("uint16_t", False),
        "tosTrafficClass": ("uint8_t", True),
    },
    "secContext_t": {"secAlgo": ("securityAlgo_t", False)},
    "securityAlgo_t": {
        "nasEncAlgo": ("uint8_t", False),
        "nasIntAlgo": ("uint8_t", False),
    },
    "service-names": ("string", False),
    "serviceInstanceId": ("string", False),
    "serviceName": ("string", False),
    "servingNetwork": ("JSON", False),
    "servingNetworkName": ("string", False),
    "servingNfId": ("string", False),
    "sessRuleId": ("string", False),
    "sessRules": ("JSON", False),
    "sessionAmbr": ("JSON", False),
    "single-nssai": ("string", False),
    "singleNssai": ("JSON", False),
    "singleNssais": ("singleNssaisEl", True),
    "singleNssaisEl": ("JSON", False),
    "sliceInfo": ("JSON", False),
    "smContextStatusUri": ("string", False),
    "smInfo": ("JSON", False),
    "smf-id": ("string", False),
    "smfInstanceId": ("string", False),
    "snssais": ("string", False),
    "sscMode_t": {"ssc_mode_value": ("uint8_t", False), "uint8_t": ("", False)},
    "sscModes": ("JSON", False),
    "sst": ("int", False),
    "status-code": ("int", False),
    "statuscode": ("int", False),
    "struct AMFConfigurationUpdateAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFConfigurationUpdateAcknowledgeIEs__value_u", False),
        "present": ("AMFConfigurationUpdateAcknowledgeIEs__value_PR", False),
    },
    "struct AMFConfigurationUpdateFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFConfigurationUpdateFailureIEs__value_u", False),
        "present": ("AMFConfigurationUpdateFailureIEs__value_PR", False),
    },
    "struct AMFConfigurationUpdateIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFConfigurationUpdateIEs__value_u", False),
        "present": ("AMFConfigurationUpdateIEs__value_PR", False),
    },
    "struct AMFPagingTarget_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFPagingTarget_ExtIEs__value_u", False),
        "present": ("AMFPagingTarget_ExtIEs__value_PR", False),
    },
    "struct AMFStatusIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMFStatusIndicationIEs__value_u", False),
        "present": ("AMFStatusIndicationIEs__value_PR", False),
    },
    "struct AMF_TNLAssociationSetupItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMF_TNLAssociationSetupItem_ExtIEs__extensionValue_u", False),
        "present": ("AMF_TNLAssociationSetupItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AMF_TNLAssociationToAddItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMF_TNLAssociationToAddItem_ExtIEs__extensionValue_u", False),
        "present": ("AMF_TNLAssociationToAddItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue_u", False),
        "present": ("AMF_TNLAssociationToRemoveItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue_u", False),
        "present": ("AMF_TNLAssociationToUpdateItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AllocationAndRetentionPriority_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AllocationAndRetentionPriority_ExtIEs__extensionValue_u", False),
        "present": ("AllocationAndRetentionPriority_ExtIEs__extensionValue_PR", False),
    },
    "struct AllowedNSSAI_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AllowedNSSAI_Item_ExtIEs__extensionValue_u", False),
        "present": ("AllowedNSSAI_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct AreaOfInterestCellItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AreaOfInterestCellItem_ExtIEs__extensionValue_u", False),
        "present": ("AreaOfInterestCellItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AreaOfInterestItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AreaOfInterestItem_ExtIEs__extensionValue_u", False),
        "present": ("AreaOfInterestItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AreaOfInterestRANNodeItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AreaOfInterestRANNodeItem_ExtIEs__extensionValue_u", False),
        "present": ("AreaOfInterestRANNodeItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AreaOfInterestTAIItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AreaOfInterestTAIItem_ExtIEs__extensionValue_u", False),
        "present": ("AreaOfInterestTAIItem_ExtIEs__extensionValue_PR", False),
    },
    "struct AreaOfInterest_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AreaOfInterest_ExtIEs__extensionValue_u", False),
        "present": ("AreaOfInterest_ExtIEs__extensionValue_PR", False),
    },
    "struct AssistanceDataForPaging_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AssistanceDataForPaging_ExtIEs__extensionValue_u", False),
        "present": ("AssistanceDataForPaging_ExtIEs__extensionValue_PR", False),
    },
    "struct AssistanceDataForRecommendedCells_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AssistanceDataForRecommendedCells_ExtIEs__extensionValue_u", False),
        "present": (
            "AssistanceDataForRecommendedCells_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct AssociatedQosFlowItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("AssociatedQosFlowItem_ExtIEs__extensionValue_u", False),
        "present": ("AssociatedQosFlowItem_ExtIEs__extensionValue_PR", False),
    },
    "struct BroadcastCancelledAreaList_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("BroadcastCancelledAreaList_ExtIEs__value_u", False),
        "present": ("BroadcastCancelledAreaList_ExtIEs__value_PR", False),
    },
    "struct BroadcastCompletedAreaList_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("BroadcastCompletedAreaList_ExtIEs__value_u", False),
        "present": ("BroadcastCompletedAreaList_ExtIEs__value_PR", False),
    },
    "struct BroadcastPLMNItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("BroadcastPLMNItem_ExtIEs__extensionValue_u", False),
        "present": ("BroadcastPLMNItem_ExtIEs__extensionValue_PR", False),
    },
    "struct COUNTValueForPDCP_SN12_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("COUNTValueForPDCP_SN12_ExtIEs__extensionValue_u", False),
        "present": ("COUNTValueForPDCP_SN12_ExtIEs__extensionValue_PR", False),
    },
    "struct COUNTValueForPDCP_SN18_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("COUNTValueForPDCP_SN18_ExtIEs__extensionValue_u", False),
        "present": ("COUNTValueForPDCP_SN18_ExtIEs__extensionValue_PR", False),
    },
    "struct CPTransportLayerInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CPTransportLayerInformation_ExtIEs__value_u", False),
        "present": ("CPTransportLayerInformation_ExtIEs__value_PR", False),
    },
    "struct CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CancelledCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CancelledCellsInEAI_NR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CancelledCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CancelledCellsInTAI_NR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct Cause_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("Cause_ExtIEs__value_u", False),
        "present": ("Cause_ExtIEs__value_PR", False),
    },
    "struct CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CellIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CellIDBroadcastNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDBroadcastNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CellIDBroadcastNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CellIDCancelledEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDCancelledEUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CellIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CellIDCancelledNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDCancelledNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CellIDCancelledNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CellIDListForRestart_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellIDListForRestart_ExtIEs__value_u", False),
        "present": ("CellIDListForRestart_ExtIEs__value_PR", False),
    },
    "struct CellTrafficTraceIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellTrafficTraceIEs__value_u", False),
        "present": ("CellTrafficTraceIEs__value_PR", False),
    },
    "struct CellType_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CellType_ExtIEs__extensionValue_u", False),
        "present": ("CellType_ExtIEs__extensionValue_PR", False),
    },
    "struct CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CompletedCellsInEAI_EUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CompletedCellsInEAI_NR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("CompletedCellsInTAI_EUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue_u", False),
        "present": ("CompletedCellsInTAI_NR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct CoreNetworkAssistanceInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CoreNetworkAssistanceInformation_ExtIEs__extensionValue_u", False),
        "present": (
            "CoreNetworkAssistanceInformation_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct CriticalityDiagnostics_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CriticalityDiagnostics_ExtIEs__extensionValue_u", False),
        "present": ("CriticalityDiagnostics_ExtIEs__extensionValue_PR", False),
    },
    "struct CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue_u", False),
        "present": ("CriticalityDiagnostics_IE_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBStatusDL12_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusDL12_ExtIEs__extensionValue_u", False),
        "present": ("DRBStatusDL12_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBStatusDL18_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusDL18_ExtIEs__extensionValue_u", False),
        "present": ("DRBStatusDL18_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBStatusDL_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusDL_ExtIEs__value_u", False),
        "present": ("DRBStatusDL_ExtIEs__value_PR", False),
    },
    "struct DRBStatusUL12_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusUL12_ExtIEs__extensionValue_u", False),
        "present": ("DRBStatusUL12_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBStatusUL18_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusUL18_ExtIEs__extensionValue_u", False),
        "present": ("DRBStatusUL18_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBStatusUL_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBStatusUL_ExtIEs__value_u", False),
        "present": ("DRBStatusUL_ExtIEs__value_PR", False),
    },
    "struct DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue_u", False),
        "present": ("DRBsSubjectToStatusTransferItem_ExtIEs__extensionValue_PR", False),
    },
    "struct DRBsToQosFlowsMappingItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DRBsToQosFlowsMappingItem_ExtIEs__extensionValue_u", False),
        "present": ("DRBsToQosFlowsMappingItem_ExtIEs__extensionValue_PR", False),
    },
    "struct DataForwardingResponseDRBItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DataForwardingResponseDRBItem_ExtIEs__extensionValue_u", False),
        "present": ("DataForwardingResponseDRBItem_ExtIEs__extensionValue_PR", False),
    },
    "struct DeactivateTraceIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DeactivateTraceIEs__value_u", False),
        "present": ("DeactivateTraceIEs__value_PR", False),
    },
    "struct DownlinkNASTransport_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DownlinkNASTransport_IEs__value_u", False),
        "present": ("DownlinkNASTransport_IEs__value_PR", False),
    },
    "struct DownlinkNonUEAssociatedNRPPaTransportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DownlinkNonUEAssociatedNRPPaTransportIEs__value_u", False),
        "present": ("DownlinkNonUEAssociatedNRPPaTransportIEs__value_PR", False),
    },
    "struct DownlinkRANConfigurationTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DownlinkRANConfigurationTransferIEs__value_u", False),
        "present": ("DownlinkRANConfigurationTransferIEs__value_PR", False),
    },
    "struct DownlinkRANStatusTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DownlinkRANStatusTransferIEs__value_u", False),
        "present": ("DownlinkRANStatusTransferIEs__value_PR", False),
    },
    "struct DownlinkUEAssociatedNRPPaTransportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("DownlinkUEAssociatedNRPPaTransportIEs__value_u", False),
        "present": ("DownlinkUEAssociatedNRPPaTransportIEs__value_PR", False),
    },
    "struct Dynamic5QIDescriptor_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("Dynamic5QIDescriptor_ExtIEs__extensionValue_u", False),
        "present": ("Dynamic5QIDescriptor_ExtIEs__extensionValue_PR", False),
    },
    "struct EPS_TAI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("EPS_TAI_ExtIEs__extensionValue_u", False),
        "present": ("EPS_TAI_ExtIEs__extensionValue_PR", False),
    },
    "struct EUTRA_CGI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("EUTRA_CGI_ExtIEs__extensionValue_u", False),
        "present": ("EUTRA_CGI_ExtIEs__extensionValue_PR", False),
    },
    "struct E_RABInformationItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("E_RABInformationItem_ExtIEs__extensionValue_u", False),
        "present": ("E_RABInformationItem_ExtIEs__extensionValue_PR", False),
    },
    "struct EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "EmergencyAreaIDBroadcastEUTRA_Item_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("EmergencyAreaIDBroadcastNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "EmergencyAreaIDCancelledEUTRA_Item_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("EmergencyAreaIDCancelledNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct EmergencyFallbackIndicator_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("EmergencyFallbackIndicator_ExtIEs__extensionValue_u", False),
        "present": ("EmergencyFallbackIndicator_ExtIEs__extensionValue_PR", False),
    },
    "struct ErrorIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ErrorIndicationIEs__value_u", False),
        "present": ("ErrorIndicationIEs__value_PR", False),
    },
    "struct ExpectedUEActivityBehaviour_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ExpectedUEActivityBehaviour_ExtIEs__extensionValue_u", False),
        "present": ("ExpectedUEActivityBehaviour_ExtIEs__extensionValue_PR", False),
    },
    "struct ExpectedUEBehaviour_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ExpectedUEBehaviour_ExtIEs__extensionValue_u", False),
        "present": ("ExpectedUEBehaviour_ExtIEs__extensionValue_PR", False),
    },
    "struct ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue_u", False),
        "present": ("ExpectedUEMovingTrajectoryItem_ExtIEs__extensionValue_PR", False),
    },
    "struct FiveG_S_TMSI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("FiveG_S_TMSI_ExtIEs__extensionValue_u", False),
        "present": ("FiveG_S_TMSI_ExtIEs__extensionValue_PR", False),
    },
    "struct ForbiddenAreaInformation_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ForbiddenAreaInformation_Item_ExtIEs__extensionValue_u", False),
        "present": ("ForbiddenAreaInformation_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct GBR_QosInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GBR_QosInformation_ExtIEs__extensionValue_u", False),
        "present": ("GBR_QosInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct GNB_ID_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GNB_ID_ExtIEs__value_u", False),
        "present": ("GNB_ID_ExtIEs__value_PR", False),
    },
    "struct GTPTunnel_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GTPTunnel_ExtIEs__extensionValue_u", False),
        "present": ("GTPTunnel_ExtIEs__extensionValue_PR", False),
    },
    "struct GUAMI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GUAMI_ExtIEs__extensionValue_u", False),
        "present": ("GUAMI_ExtIEs__extensionValue_PR", False),
    },
    "struct GlobalGNB_ID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GlobalGNB_ID_ExtIEs__extensionValue_u", False),
        "present": ("GlobalGNB_ID_ExtIEs__extensionValue_PR", False),
    },
    "struct GlobalN3IWF_ID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GlobalN3IWF_ID_ExtIEs__extensionValue_u", False),
        "present": ("GlobalN3IWF_ID_ExtIEs__extensionValue_PR", False),
    },
    "struct GlobalNgENB_ID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GlobalNgENB_ID_ExtIEs__extensionValue_u", False),
        "present": ("GlobalNgENB_ID_ExtIEs__extensionValue_PR", False),
    },
    "struct GlobalRANNodeID_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("GlobalRANNodeID_ExtIEs__value_u", False),
        "present": ("GlobalRANNodeID_ExtIEs__value_PR", False),
    },
    "struct HandoverCancelAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverCancelAcknowledgeIEs__value_u", False),
        "present": ("HandoverCancelAcknowledgeIEs__value_PR", False),
    },
    "struct HandoverCancelIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverCancelIEs__value_u", False),
        "present": ("HandoverCancelIEs__value_PR", False),
    },
    "struct HandoverCommandIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverCommandIEs__value_u", False),
        "present": ("HandoverCommandIEs__value_PR", False),
    },
    "struct HandoverCommandTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverCommandTransfer_ExtIEs__extensionValue_u", False),
        "present": ("HandoverCommandTransfer_ExtIEs__extensionValue_PR", False),
    },
    "struct HandoverFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverFailureIEs__value_u", False),
        "present": ("HandoverFailureIEs__value_PR", False),
    },
    "struct HandoverNotifyIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverNotifyIEs__value_u", False),
        "present": ("HandoverNotifyIEs__value_PR", False),
    },
    "struct HandoverPreparationFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverPreparationFailureIEs__value_u", False),
        "present": ("HandoverPreparationFailureIEs__value_PR", False),
    },
    "struct HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "HandoverPreparationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct HandoverRequestAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverRequestAcknowledgeIEs__value_u", False),
        "present": ("HandoverRequestAcknowledgeIEs__value_PR", False),
    },
    "struct HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "HandoverRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct HandoverRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverRequestIEs__value_u", False),
        "present": ("HandoverRequestIEs__value_PR", False),
    },
    "struct HandoverRequiredIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverRequiredIEs__value_u", False),
        "present": ("HandoverRequiredIEs__value_PR", False),
    },
    "struct HandoverRequiredTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("HandoverRequiredTransfer_ExtIEs__extensionValue_u", False),
        "present": ("HandoverRequiredTransfer_ExtIEs__extensionValue_PR", False),
    },
    "struct HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "HandoverResourceAllocationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "InfoOnRecommendedCellsAndRANNodesForPaging_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct InitialContextSetupFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("InitialContextSetupFailureIEs__value_u", False),
        "present": ("InitialContextSetupFailureIEs__value_PR", False),
    },
    "struct InitialContextSetupRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("InitialContextSetupRequestIEs__value_u", False),
        "present": ("InitialContextSetupRequestIEs__value_PR", False),
    },
    "struct InitialContextSetupResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("InitialContextSetupResponseIEs__value_u", False),
        "present": ("InitialContextSetupResponseIEs__value_PR", False),
    },
    "struct InitialUEMessage_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("InitialUEMessage_IEs__value_u", False),
        "present": ("InitialUEMessage_IEs__value_PR", False),
    },
    "struct InitiatingMessage__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("InitiatingMessage__value_u", False),
        "present": ("InitiatingMessage__value_PR", False),
    },
    "struct LastVisitedCellInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LastVisitedCellInformation_ExtIEs__value_u", False),
        "present": ("LastVisitedCellInformation_ExtIEs__value_PR", False),
    },
    "struct LastVisitedCellItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LastVisitedCellItem_ExtIEs__extensionValue_u", False),
        "present": ("LastVisitedCellItem_ExtIEs__extensionValue_PR", False),
    },
    "struct LastVisitedNGRANCellInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LastVisitedNGRANCellInformation_ExtIEs__extensionValue_u", False),
        "present": ("LastVisitedNGRANCellInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct LocationReportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LocationReportIEs__value_u", False),
        "present": ("LocationReportIEs__value_PR", False),
    },
    "struct LocationReportingControlIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LocationReportingControlIEs__value_u", False),
        "present": ("LocationReportingControlIEs__value_PR", False),
    },
    "struct LocationReportingFailureIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LocationReportingFailureIndicationIEs__value_u", False),
        "present": ("LocationReportingFailureIndicationIEs__value_PR", False),
    },
    "struct LocationReportingRequestType_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("LocationReportingRequestType_ExtIEs__extensionValue_u", False),
        "present": ("LocationReportingRequestType_ExtIEs__extensionValue_PR", False),
    },
    "struct MobilityRestrictionList_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("MobilityRestrictionList_ExtIEs__extensionValue_u", False),
        "present": ("MobilityRestrictionList_ExtIEs__extensionValue_PR", False),
    },
    "struct MultipleTNLInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("MultipleTNLInformation_ExtIEs__extensionValue_u", False),
        "present": ("MultipleTNLInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct N3IWF_ID_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("N3IWF_ID_ExtIEs__value_u", False),
        "present": ("N3IWF_ID_ExtIEs__value_PR", False),
    },
    "struct NASNonDeliveryIndication_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NASNonDeliveryIndication_IEs__value_u", False),
        "present": ("NASNonDeliveryIndication_IEs__value_PR", False),
    },
    "struct NGRAN_CGI_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGRAN_CGI_ExtIEs__value_u", False),
        "present": ("NGRAN_CGI_ExtIEs__value_PR", False),
    },
    "struct NGResetAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGResetAcknowledgeIEs__value_u", False),
        "present": ("NGResetAcknowledgeIEs__value_PR", False),
    },
    "struct NGResetIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGResetIEs__value_u", False),
        "present": ("NGResetIEs__value_PR", False),
    },
    "struct NGSetupFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGSetupFailureIEs__value_u", False),
        "present": ("NGSetupFailureIEs__value_PR", False),
    },
    "struct NGSetupRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGSetupRequestIEs__value_u", False),
        "present": ("NGSetupRequestIEs__value_PR", False),
    },
    "struct NGSetupResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NGSetupResponseIEs__value_u", False),
        "present": ("NGSetupResponseIEs__value_PR", False),
    },
    "struct NR_CGI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NR_CGI_ExtIEs__extensionValue_u", False),
        "present": ("NR_CGI_ExtIEs__extensionValue_PR", False),
    },
    "struct NgENB_ID_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NgENB_ID_ExtIEs__value_u", False),
        "present": ("NgENB_ID_ExtIEs__value_PR", False),
    },
    "struct NonDynamic5QIDescriptor_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("NonDynamic5QIDescriptor_ExtIEs__extensionValue_u", False),
        "present": ("NonDynamic5QIDescriptor_ExtIEs__extensionValue_PR", False),
    },
    "struct OverloadResponse_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("OverloadResponse_ExtIEs__value_u", False),
        "present": ("OverloadResponse_ExtIEs__value_PR", False),
    },
    "struct OverloadStartIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("OverloadStartIEs__value_u", False),
        "present": ("OverloadStartIEs__value_PR", False),
    },
    "struct OverloadStartNSSAIItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("OverloadStartNSSAIItem_ExtIEs__extensionValue_u", False),
        "present": ("OverloadStartNSSAIItem_ExtIEs__extensionValue_PR", False),
    },
    "struct OverloadStopIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("OverloadStopIEs__value_u", False),
        "present": ("OverloadStopIEs__value_PR", False),
    },
    "struct PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionAggregateMaximumBitRate_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceAdmittedItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceAdmittedItem_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceAdmittedItem_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToModifyItemModCfm_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToModifyItemModRes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToSetupItemCxtFail_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToSetupItemCxtRes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToSetupItemHOAck_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToSetupItemPSReq_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceFailedToSetupItemSURes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceHandoverItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceHandoverItem_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceHandoverItem_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceInformationItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceInformationItem_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceInformationItem_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceItemCxtRelCpl_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceItemCxtRelReq_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceItemHORqd_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceItemHORqd_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceItemHORqd_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceModifyConfirmIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceModifyConfirmIEs__value_u", False),
        "present": ("PDUSessionResourceModifyConfirmIEs__value_PR", False),
    },
    "struct PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyConfirmTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceModifyIndicationIEs__value_u", False),
        "present": ("PDUSessionResourceModifyIndicationIEs__value_PR", False),
    },
    "struct PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyIndicationTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyIndicationUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyItemModCfm_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyItemModInd_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyItemModReq_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyItemModRes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceModifyRequestIEs__value_u", False),
        "present": ("PDUSessionResourceModifyRequestIEs__value_PR", False),
    },
    "struct PDUSessionResourceModifyRequestTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceModifyRequestTransferIEs__value_u", False),
        "present": ("PDUSessionResourceModifyRequestTransferIEs__value_PR", False),
    },
    "struct PDUSessionResourceModifyResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceModifyResponseIEs__value_u", False),
        "present": ("PDUSessionResourceModifyResponseIEs__value_PR", False),
    },
    "struct PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyResponseTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceModifyUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceNotifyIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceNotifyIEs__value_u", False),
        "present": ("PDUSessionResourceNotifyIEs__value_PR", False),
    },
    "struct PDUSessionResourceNotifyItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceNotifyItem_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceNotifyItem_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceNotifyReleasedTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceNotifyTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleaseCommandIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceReleaseCommandIEs__value_u", False),
        "present": ("PDUSessionResourceReleaseCommandIEs__value_PR", False),
    },
    "struct PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceReleaseCommandTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleaseResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceReleaseResponseIEs__value_u", False),
        "present": ("PDUSessionResourceReleaseResponseIEs__value_PR", False),
    },
    "struct PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceReleaseResponseTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceReleasedItemNot_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceReleasedItemPSAck_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceReleasedItemPSFail_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceReleasedItemRelRes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceSetupItemCxtReq_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceSetupItemCxtRes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceSetupItemHOReq_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceSetupItemSUReq_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue_u", False),
        "present": (
            "PDUSessionResourceSetupItemSURes_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupRequestIEs__value_u", False),
        "present": ("PDUSessionResourceSetupRequestIEs__value_PR", False),
    },
    "struct PDUSessionResourceSetupRequestTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupRequestTransferIEs__value_u", False),
        "present": ("PDUSessionResourceSetupRequestTransferIEs__value_PR", False),
    },
    "struct PDUSessionResourceSetupResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSetupResponseIEs__value_u", False),
        "present": ("PDUSessionResourceSetupResponseIEs__value_PR", False),
    },
    "struct PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceSetupResponseTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceSetupUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceSwitchedItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PDUSessionResourceSwitchedItem_ExtIEs__extensionValue_u", False),
        "present": ("PDUSessionResourceSwitchedItem_ExtIEs__extensionValue_PR", False),
    },
    "struct PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceToBeSwitchedDLItem_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceToReleaseItemHOCmd_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PDUSessionResourceToReleaseItemRelCmd_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PLMNSupportItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PLMNSupportItem_ExtIEs__extensionValue_u", False),
        "present": ("PLMNSupportItem_ExtIEs__extensionValue_PR", False),
    },
    "struct PWSCancelRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSCancelRequestIEs__value_u", False),
        "present": ("PWSCancelRequestIEs__value_PR", False),
    },
    "struct PWSCancelResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSCancelResponseIEs__value_u", False),
        "present": ("PWSCancelResponseIEs__value_PR", False),
    },
    "struct PWSFailedCellIDList_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSFailedCellIDList_ExtIEs__value_u", False),
        "present": ("PWSFailedCellIDList_ExtIEs__value_PR", False),
    },
    "struct PWSFailureIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSFailureIndicationIEs__value_u", False),
        "present": ("PWSFailureIndicationIEs__value_PR", False),
    },
    "struct PWSRestartIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PWSRestartIndicationIEs__value_u", False),
        "present": ("PWSRestartIndicationIEs__value_PR", False),
    },
    "struct PacketErrorRate_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PacketErrorRate_ExtIEs__extensionValue_u", False),
        "present": ("PacketErrorRate_ExtIEs__extensionValue_PR", False),
    },
    "struct PagingAttemptInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PagingAttemptInformation_ExtIEs__extensionValue_u", False),
        "present": ("PagingAttemptInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct PagingIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PagingIEs__value_u", False),
        "present": ("PagingIEs__value_PR", False),
    },
    "struct PathSwitchRequestAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PathSwitchRequestAcknowledgeIEs__value_u", False),
        "present": ("PathSwitchRequestAcknowledgeIEs__value_PR", False),
    },
    "struct PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PathSwitchRequestAcknowledgeTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PathSwitchRequestFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PathSwitchRequestFailureIEs__value_u", False),
        "present": ("PathSwitchRequestFailureIEs__value_PR", False),
    },
    "struct PathSwitchRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PathSwitchRequestIEs__value_u", False),
        "present": ("PathSwitchRequestIEs__value_PR", False),
    },
    "struct PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PathSwitchRequestSetupFailedTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PathSwitchRequestTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PathSwitchRequestTransfer_ExtIEs__extensionValue_u", False),
        "present": ("PathSwitchRequestTransfer_ExtIEs__extensionValue_PR", False),
    },
    "struct PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "PathSwitchRequestUnsuccessfulTransfer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct PrivateMessageIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("PrivateMessageIEs__value_u", False),
        "present": ("PrivateMessageIEs__value_PR", False),
    },
    "struct QosCharacteristics_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosCharacteristics_ExtIEs__value_u", False),
        "present": ("QosCharacteristics_ExtIEs__value_PR", False),
    },
    "struct QosFlowAcceptedItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowAcceptedItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowAcceptedItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowAddOrModifyRequestItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowAddOrModifyResponseItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowInformationItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowInformationItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowInformationItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowLevelQosParameters_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowLevelQosParameters_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowLevelQosParameters_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowModifyConfirmItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowModifyConfirmItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowModifyConfirmItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowNotifyItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowNotifyItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowNotifyItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowPerTNLInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowPerTNLInformation_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowPerTNLInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowSetupRequestItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowSetupRequestItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowSetupRequestItem_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue_u", False),
        "present": (
            "QosFlowSetupResponseItemHOReqAck_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct QosFlowSetupResponseItemSURes_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowSetupResponseItemSURes_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowSetupResponseItemSURes_ExtIEs__extensionValue_PR", False),
    },
    "struct QosFlowToBeForwardedItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("QosFlowToBeForwardedItem_ExtIEs__extensionValue_u", False),
        "present": ("QosFlowToBeForwardedItem_ExtIEs__extensionValue_PR", False),
    },
    "struct RANConfigurationUpdateAcknowledgeIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RANConfigurationUpdateAcknowledgeIEs__value_u", False),
        "present": ("RANConfigurationUpdateAcknowledgeIEs__value_PR", False),
    },
    "struct RANConfigurationUpdateFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RANConfigurationUpdateFailureIEs__value_u", False),
        "present": ("RANConfigurationUpdateFailureIEs__value_PR", False),
    },
    "struct RANConfigurationUpdateIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RANConfigurationUpdateIEs__value_u", False),
        "present": ("RANConfigurationUpdateIEs__value_PR", False),
    },
    "struct RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "RANStatusTransfer_TransparentContainer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct RATRestrictions_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RATRestrictions_Item_ExtIEs__extensionValue_u", False),
        "present": ("RATRestrictions_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct RRCInactiveTransitionReportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RRCInactiveTransitionReportIEs__value_u", False),
        "present": ("RRCInactiveTransitionReportIEs__value_PR", False),
    },
    "struct RecommendedCellItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RecommendedCellItem_ExtIEs__extensionValue_u", False),
        "present": ("RecommendedCellItem_ExtIEs__extensionValue_PR", False),
    },
    "struct RecommendedCellsForPaging_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RecommendedCellsForPaging_ExtIEs__extensionValue_u", False),
        "present": ("RecommendedCellsForPaging_ExtIEs__extensionValue_PR", False),
    },
    "struct RecommendedRANNodeItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RecommendedRANNodeItem_ExtIEs__extensionValue_u", False),
        "present": ("RecommendedRANNodeItem_ExtIEs__extensionValue_PR", False),
    },
    "struct RecommendedRANNodesForPaging_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RecommendedRANNodesForPaging_ExtIEs__extensionValue_u", False),
        "present": ("RecommendedRANNodesForPaging_ExtIEs__extensionValue_PR", False),
    },
    "struct RerouteNASRequest_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("RerouteNASRequest_IEs__value_u", False),
        "present": ("RerouteNASRequest_IEs__value_PR", False),
    },
    "struct ResetType_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ResetType_ExtIEs__value_u", False),
        "present": ("ResetType_ExtIEs__value_PR", False),
    },
    "struct SONConfigurationTransfer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SONConfigurationTransfer_ExtIEs__extensionValue_u", False),
        "present": ("SONConfigurationTransfer_ExtIEs__extensionValue_PR", False),
    },
    "struct SONInformationReply_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SONInformationReply_ExtIEs__extensionValue_u", False),
        "present": ("SONInformationReply_ExtIEs__extensionValue_PR", False),
    },
    "struct SONInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SONInformation_ExtIEs__value_u", False),
        "present": ("SONInformation_ExtIEs__value_PR", False),
    },
    "struct S_NSSAI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("S_NSSAI_ExtIEs__extensionValue_u", False),
        "present": ("S_NSSAI_ExtIEs__extensionValue_PR", False),
    },
    "struct SecurityContext_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SecurityContext_ExtIEs__extensionValue_u", False),
        "present": ("SecurityContext_ExtIEs__extensionValue_PR", False),
    },
    "struct SecurityIndication_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SecurityIndication_ExtIEs__extensionValue_u", False),
        "present": ("SecurityIndication_ExtIEs__extensionValue_PR", False),
    },
    "struct SecurityResult_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SecurityResult_ExtIEs__extensionValue_u", False),
        "present": ("SecurityResult_ExtIEs__extensionValue_PR", False),
    },
    "struct ServedGUAMIItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ServedGUAMIItem_ExtIEs__extensionValue_u", False),
        "present": ("ServedGUAMIItem_ExtIEs__extensionValue_PR", False),
    },
    "struct ServiceAreaInformation_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("ServiceAreaInformation_Item_ExtIEs__extensionValue_u", False),
        "present": ("ServiceAreaInformation_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct SingleTNLInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SingleTNLInformation_ExtIEs__extensionValue_u", False),
        "present": ("SingleTNLInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct SliceOverloadItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SliceOverloadItem_ExtIEs__extensionValue_u", False),
        "present": ("SliceOverloadItem_ExtIEs__extensionValue_PR", False),
    },
    "struct SliceSupportItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SliceSupportItem_ExtIEs__extensionValue_u", False),
        "present": ("SliceSupportItem_ExtIEs__extensionValue_PR", False),
    },
    "struct SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "SourceNGRANNode_ToTargetNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct SourceRANNodeID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SourceRANNodeID_ExtIEs__extensionValue_u", False),
        "present": ("SourceRANNodeID_ExtIEs__extensionValue_PR", False),
    },
    "struct SuccessfulOutcome__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SuccessfulOutcome__value_u", False),
        "present": ("SuccessfulOutcome__value_PR", False),
    },
    "struct SupportedTAItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("SupportedTAItem_ExtIEs__extensionValue_u", False),
        "present": ("SupportedTAItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TAIBroadcastEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAIBroadcastEUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("TAIBroadcastEUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct TAIBroadcastNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAIBroadcastNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("TAIBroadcastNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct TAICancelledEUTRA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAICancelledEUTRA_Item_ExtIEs__extensionValue_u", False),
        "present": ("TAICancelledEUTRA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct TAICancelledNR_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAICancelledNR_Item_ExtIEs__extensionValue_u", False),
        "present": ("TAICancelledNR_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct TAIListForInactiveItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAIListForInactiveItem_ExtIEs__extensionValue_u", False),
        "present": ("TAIListForInactiveItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TAIListForPagingItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAIListForPagingItem_ExtIEs__extensionValue_u", False),
        "present": ("TAIListForPagingItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TAI_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TAI_ExtIEs__extensionValue_u", False),
        "present": ("TAI_ExtIEs__extensionValue_PR", False),
    },
    "struct TNLAssociationItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TNLAssociationItem_ExtIEs__extensionValue_u", False),
        "present": ("TNLAssociationItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TNLInformationItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TNLInformationItem_ExtIEs__extensionValue_u", False),
        "present": ("TNLInformationItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TNLMappingItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TNLMappingItem_ExtIEs__extensionValue_u", False),
        "present": ("TNLMappingItem_ExtIEs__extensionValue_PR", False),
    },
    "struct TargetID_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TargetID_ExtIEs__value_u", False),
        "present": ("TargetID_ExtIEs__value_PR", False),
    },
    "struct TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "TargetNGRANNode_ToSourceNGRANNode_TransparentContainer_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct TargetRANNodeID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TargetRANNodeID_ExtIEs__extensionValue_u", False),
        "present": ("TargetRANNodeID_ExtIEs__extensionValue_PR", False),
    },
    "struct TargeteNB_ID_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TargeteNB_ID_ExtIEs__extensionValue_u", False),
        "present": ("TargeteNB_ID_ExtIEs__extensionValue_PR", False),
    },
    "struct TraceActivation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TraceActivation_ExtIEs__extensionValue_u", False),
        "present": ("TraceActivation_ExtIEs__extensionValue_PR", False),
    },
    "struct TraceFailureIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TraceFailureIndicationIEs__value_u", False),
        "present": ("TraceFailureIndicationIEs__value_PR", False),
    },
    "struct TraceStartIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("TraceStartIEs__value_u", False),
        "present": ("TraceStartIEs__value_PR", False),
    },
    "struct UEAggregateMaximumBitRate_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEAggregateMaximumBitRate_ExtIEs__extensionValue_u", False),
        "present": ("UEAggregateMaximumBitRate_ExtIEs__extensionValue_PR", False),
    },
    "struct UEContextModificationFailureIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextModificationFailureIEs__value_u", False),
        "present": ("UEContextModificationFailureIEs__value_PR", False),
    },
    "struct UEContextModificationRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextModificationRequestIEs__value_u", False),
        "present": ("UEContextModificationRequestIEs__value_PR", False),
    },
    "struct UEContextModificationResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextModificationResponseIEs__value_u", False),
        "present": ("UEContextModificationResponseIEs__value_PR", False),
    },
    "struct UEContextReleaseCommand_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextReleaseCommand_IEs__value_u", False),
        "present": ("UEContextReleaseCommand_IEs__value_PR", False),
    },
    "struct UEContextReleaseComplete_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextReleaseComplete_IEs__value_u", False),
        "present": ("UEContextReleaseComplete_IEs__value_PR", False),
    },
    "struct UEContextReleaseRequest_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEContextReleaseRequest_IEs__value_u", False),
        "present": ("UEContextReleaseRequest_IEs__value_PR", False),
    },
    "struct UEIdentityIndexValue_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEIdentityIndexValue_ExtIEs__value_u", False),
        "present": ("UEIdentityIndexValue_ExtIEs__value_PR", False),
    },
    "struct UEPagingIdentity_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEPagingIdentity_ExtIEs__value_u", False),
        "present": ("UEPagingIdentity_ExtIEs__value_PR", False),
    },
    "struct UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue_u", False),
        "present": ("UEPresenceInAreaOfInterestItem_ExtIEs__extensionValue_PR", False),
    },
    "struct UERadioCapabilityCheckRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UERadioCapabilityCheckRequestIEs__value_u", False),
        "present": ("UERadioCapabilityCheckRequestIEs__value_PR", False),
    },
    "struct UERadioCapabilityCheckResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UERadioCapabilityCheckResponseIEs__value_u", False),
        "present": ("UERadioCapabilityCheckResponseIEs__value_PR", False),
    },
    "struct UERadioCapabilityForPaging_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UERadioCapabilityForPaging_ExtIEs__extensionValue_u", False),
        "present": ("UERadioCapabilityForPaging_ExtIEs__extensionValue_PR", False),
    },
    "struct UERadioCapabilityInfoIndicationIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UERadioCapabilityInfoIndicationIEs__value_u", False),
        "present": ("UERadioCapabilityInfoIndicationIEs__value_PR", False),
    },
    "struct UESecurityCapabilities_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UESecurityCapabilities_ExtIEs__extensionValue_u", False),
        "present": ("UESecurityCapabilities_ExtIEs__extensionValue_PR", False),
    },
    "struct UETNLABindingReleaseRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UETNLABindingReleaseRequestIEs__value_u", False),
        "present": ("UETNLABindingReleaseRequestIEs__value_PR", False),
    },
    "struct UE_NGAP_ID_pair_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UE_NGAP_ID_pair_ExtIEs__extensionValue_u", False),
        "present": ("UE_NGAP_ID_pair_ExtIEs__extensionValue_PR", False),
    },
    "struct UE_NGAP_IDs_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UE_NGAP_IDs_ExtIEs__value_u", False),
        "present": ("UE_NGAP_IDs_ExtIEs__value_PR", False),
    },
    "struct UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": (
            "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue_u",
            False,
        ),
        "present": (
            "UE_associatedLogicalNG_connectionItem_ExtIEs__extensionValue_PR",
            False,
        ),
    },
    "struct UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue_u", False),
        "present": ("UL_NGU_UP_TNLModifyItem_ExtIEs__extensionValue_PR", False),
    },
    "struct UPTransportLayerInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UPTransportLayerInformation_ExtIEs__value_u", False),
        "present": ("UPTransportLayerInformation_ExtIEs__value_PR", False),
    },
    "struct UP_TNLInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UP_TNLInformation_ExtIEs__value_u", False),
        "present": ("UP_TNLInformation_ExtIEs__value_PR", False),
    },
    "struct UnavailableGUAMIItem_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UnavailableGUAMIItem_ExtIEs__extensionValue_u", False),
        "present": ("UnavailableGUAMIItem_ExtIEs__extensionValue_PR", False),
    },
    "struct UnsuccessfulOutcome__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UnsuccessfulOutcome__value_u", False),
        "present": ("UnsuccessfulOutcome__value_PR", False),
    },
    "struct UplinkNASTransport_IEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UplinkNASTransport_IEs__value_u", False),
        "present": ("UplinkNASTransport_IEs__value_PR", False),
    },
    "struct UplinkNonUEAssociatedNRPPaTransportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UplinkNonUEAssociatedNRPPaTransportIEs__value_u", False),
        "present": ("UplinkNonUEAssociatedNRPPaTransportIEs__value_PR", False),
    },
    "struct UplinkRANConfigurationTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UplinkRANConfigurationTransferIEs__value_u", False),
        "present": ("UplinkRANConfigurationTransferIEs__value_PR", False),
    },
    "struct UplinkRANStatusTransferIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UplinkRANStatusTransferIEs__value_u", False),
        "present": ("UplinkRANStatusTransferIEs__value_PR", False),
    },
    "struct UplinkUEAssociatedNRPPaTransportIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UplinkUEAssociatedNRPPaTransportIEs__value_u", False),
        "present": ("UplinkUEAssociatedNRPPaTransportIEs__value_PR", False),
    },
    "struct UserLocationInformationEUTRA_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserLocationInformationEUTRA_ExtIEs__extensionValue_u", False),
        "present": ("UserLocationInformationEUTRA_ExtIEs__extensionValue_PR", False),
    },
    "struct UserLocationInformationN3IWF_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserLocationInformationN3IWF_ExtIEs__extensionValue_u", False),
        "present": ("UserLocationInformationN3IWF_ExtIEs__extensionValue_PR", False),
    },
    "struct UserLocationInformationNR_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserLocationInformationNR_ExtIEs__extensionValue_u", False),
        "present": ("UserLocationInformationNR_ExtIEs__extensionValue_PR", False),
    },
    "struct UserLocationInformation_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserLocationInformation_ExtIEs__value_u", False),
        "present": ("UserLocationInformation_ExtIEs__value_PR", False),
    },
    "struct UserPlaneSecurityInformation_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("UserPlaneSecurityInformation_ExtIEs__extensionValue_u", False),
        "present": ("UserPlaneSecurityInformation_ExtIEs__extensionValue_PR", False),
    },
    "struct WarningAreaList_ExtIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("WarningAreaList_ExtIEs__value_u", False),
        "present": ("WarningAreaList_ExtIEs__value_PR", False),
    },
    "struct WriteReplaceWarningRequestIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("WriteReplaceWarningRequestIEs__value_u", False),
        "present": ("WriteReplaceWarningRequestIEs__value_PR", False),
    },
    "struct WriteReplaceWarningResponseIEs__value": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("WriteReplaceWarningResponseIEs__value_u", False),
        "present": ("WriteReplaceWarningResponseIEs__value_PR", False),
    },
    "struct XnExtTLA_Item_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("XnExtTLA_Item_ExtIEs__extensionValue_u", False),
        "present": ("XnExtTLA_Item_ExtIEs__extensionValue_PR", False),
    },
    "struct XnTNLConfigurationInfo_ExtIEs__extensionValue": {
        "_asn_ctx": ("asn_struct_ctx_t", False),
        "choice": ("XnTNLConfigurationInfo_ExtIEs__extensionValue_u", False),
        "present": ("XnTNLConfigurationInfo_ExtIEs__extensionValue_PR", False),
    },
    "subnetmask": ("int", False),
    "subsDefQos": ("JSON", False),
    "subsSessAmbr": ("JSON", False),
    "subvariant": {
        "": ("enum asn_OS_Subvariant", False),
        "ASN_OSUBV_ANY": ("", False),
        "ASN_OSUBV_BIT": ("", False),
        "ASN_OSUBV_STR": ("", False),
        "ASN_OSUBV_U16": ("", False),
        "ASN_OSUBV_U3": ("", False),
        "ctx_offset": ("unsigned", False),
    },
    "suci_5gMobileId_t": {
        "homeNtwrkPKI": ("uint8_t", False),
        "identityType": ("uint8_t", False),
        "mccDigit1": ("uint8_t", False),
        "mccDigit2": ("uint8_t", False),
        "mccDigit3": ("uint8_t", False),
        "mncDigit1": ("uint8_t", False),
        "mncDigit2": ("uint8_t", False),
        "mncDigit3": ("uint8_t", False),
        "protectionSchId": ("uint8_t", False),
        "routingInc1": ("uint8_t", False),
        "routingInc2": ("uint8_t", False),
        "routingInc3": ("uint8_t", False),
        "routingInc4": ("uint8_t", False),
        "schemeOutput": ("uint8_t", True),
        "spare": ("uint8_t", False),
        "spare1": ("uint8_t", False),
        "spare2": ("uint8_t", False),
        "supiFormat": ("uint8_t", False),
    },
    "supi": ("string", False),
    "supiOrSuci": ("string", False),
    "support3Gpp": ("boolean", False),
    "supportNon3Gpp": ("boolean", False),
    "t3512_t": {
        "len": ("uint8_t", False),
        "unit": ("uint8_t", False),
        "value": ("uint8_t", False),
    },
    "tAIList_t": {
        "filled": ("uint8_t", False),
        "len": ("uint8_t", False),
        "pTAI": ("partialTAIList_t", True),
    },
    "tAI_t": {
        "mcc1": ("uint8_t", False),
        "mcc2": ("uint8_t", False),
        "mcc3": ("uint8_t", False),
        "mnc1": ("uint8_t", False),
        "mnc2": ("uint8_t", False),
        "mnc3": ("uint8_t", False),
        "tac": ("uint8_t", True),
    },
    "target-nf-type": ("string", False),
    "test": ("int", False),
    "transport": ("string", False),
    "ueIp": ("string", False),
    "ueIpaddress_t": {
        "IEI": ("uint16_t", False),
        "IPv6D": ("uint8_t", False),
        "SrcOrDest": ("uint8_t", False),
        "V4": ("uint8_t", False),
        "V6": ("uint8_t", False),
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
        "ipv6PrefixDelegBits": ("uint8_t", False),
    },
    "upCnxState": ("string", False),
    "updateFAR_ANY_t": ("pfcpAny_t", False),
    "updateFAR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "updateFwdParam_ANY_t": ("pfcpAny_t", False),
    "updateFwdParam_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "updatePDR_ANY_t": ("pfcpAny_t", False),
    "updatePDR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "updateQER_ANY_t": ("pfcpAny_t", False),
    "updateQER_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "updatedPDR_ANY_t": ("pfcpAny_t", False),
    "updatedPDR_t": {"IElist": ("std::vector<pfcpIE_t>", False)},
    "uplink": ("string", False),
    "uplinkValue": ("int", False),
    "uri": ("string", False),
    "usrPlaneIpResInfo_t": {
        "ASSO_NI": ("uint8_t", False),
        "ASSO_SI": ("uint8_t", False),
        "IEI": ("uint16_t", False),
        "TEIDRI": ("uint8_t", False),
        "V4": ("uint8_t", False),
        "V6": ("uint8_t", False),
        "ipv4Address": ("uint8_t", True),
        "ipv6Address": ("uint8_t", True),
        "netwInst": ("uint8_t", True),
        "netwInstLen": ("uint8_t", False),
        "srcIface": ("uint8_t", False),
        "teidRange": ("uint8_t", False),
        "uint8_t": ("", False),
    },
    "validityPeriod": ("int", False),
    "version": ("string", False),
    "versions": ("version", True),
    "void(oer_type_decoder_f)(void)": ("typedef", False),
    "void(oer_type_encoder_f)(void)": ("typedef", False),
}
