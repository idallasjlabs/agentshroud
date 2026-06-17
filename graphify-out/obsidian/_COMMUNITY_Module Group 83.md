---
type: community
cohesion: 0.24
members: 47
---

# Module Group 83

**Cohesion:** 0.24 - loosely connected
**Members:** 47 nodes

## Members
- [[.__init__()_104]] - code - gateway/soc/contributors.py
- [[.__init__()_106]] - code - gateway/soc/websocket.py
- [[.is_group_admin()_1]] - code - gateway/soc/auth.py
- [[.is_owner()_1]] - code - gateway/soc/auth.py
- [[.test_confirmation_required()]] - code - gateway/tests/test_soc_models.py
- [[.test_error_model()]] - code - gateway/tests/test_soc_models.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_60]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult_1]] - code - gateway/soc/router.py
- [[AuditResult]] - code - gateway/soc/models.py
- [[BaseModel]] - code
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[CreateDelegationRequest]] - code - gateway/soc/router.py
- [[CreateGroupRequest]] - code - gateway/soc/router.py
- [[DisconnectRequest]] - code - gateway/soc/router.py
- [[EgressApproveRequest]] - code - gateway/soc/router.py
- [[EgressRuleOverrideRequest]] - code - gateway/soc/router.py
- [[EgressScopeRequest]] - code - gateway/soc/router.py
- [[EmergencyBlockRequest]] - code - gateway/soc/router.py
- [[LoginRequest]] - code - gateway/soc/router.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_5]] - code - gateway/soc/router.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[SCLCaller]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLError]] - code - gateway/soc/models.py
- [[SCLInterface_1]] - code - gateway/soc/router.py
- [[SCLInterface]] - code - gateway/soc/models.py
- [[ScanRequest_1]] - code - gateway/soc/router.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[Severity_1]] - code - gateway/soc/models.py
- [[TestSCLError]] - code - gateway/tests/test_soc_models.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WSEvent_1]] - code - gateway/soc/websocket.py
- [[WSEventType]] - code - gateway/soc/models.py
- [[WebSocket_5]] - code - gateway/soc/router.py
- [[WebSocket_6]] - code - gateway/soc/websocket.py
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_83
SORT file.name ASC
```

## Connections to other communities
- 83 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 30 edges to [[_COMMUNITY_SOC Services & Health Status]]
- 24 edges to [[_COMMUNITY_SOC Services]]
- 13 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 13 edges to [[_COMMUNITY_Module Group 120]]
- 12 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 8 edges to [[_COMMUNITY_SOC Authentication]]
- 5 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 5 edges to [[_COMMUNITY_Module Group 206]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 3 edges to [[_COMMUNITY_Module Group 270]]
- 2 edges to [[_COMMUNITY_Module Group 312]]
- 2 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 2 edges to [[_COMMUNITY_Version Routes & Manager Tools]]
- 2 edges to [[_COMMUNITY_Group Config & Teams]]
- 2 edges to [[_COMMUNITY_Web API & Dashboard UI]]
- 2 edges to [[_COMMUNITY_Module Group 70]]
- 2 edges to [[_COMMUNITY_Module Group 229]]
- 2 edges to [[_COMMUNITY_Module Group 150]]
- 2 edges to [[_COMMUNITY_Module Group 315]]
- 1 edge to [[_COMMUNITY_Module Group 127]]
- 1 edge to [[_COMMUNITY_Ledger Config & Test Infra]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 94]]
- 1 edge to [[_COMMUNITY_Module Group 195]]
- 1 edge to [[_COMMUNITY_Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Module Group 126]]
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_Module Group 544]]
- 1 edge to [[_COMMUNITY_Module Group 556]]

## Top bridge nodes
- [[BaseModel]] - degree 79, connects to 24 communities
- [[Severity_1]] - degree 43, connects to 7 communities
- [[SCLCaller]] - degree 46, connects to 6 communities
- [[WSEventType]] - degree 38, connects to 5 communities
- [[SCLConfirmationRequired]] - degree 35, connects to 3 communities