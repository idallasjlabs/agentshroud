---
source_file: "gateway/soc/auth.py"
type: "code"
community: "SOC Dashboard"
location: "L138"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SOC_Dashboard
---

# SCLCaller

## Connections
- [[.__init__()_125]] - `method` [EXTRACTED]
- [[.is_group_admin()_1]] - `method` [EXTRACTED]
- [[.is_owner()_2]] - `method` [EXTRACTED]
- [[.require()]] - `method` [EXTRACTED]
- [[.test_get_caller_passthrough()]] - `calls` [EXTRACTED]
- [[.test_is_group_admin_with_teams_config()]] - `calls` [EXTRACTED]
- [[.test_is_group_admin_without_teams_config()]] - `calls` [EXTRACTED]
- [[.test_is_owner_delegates_to_config()]] - `calls` [EXTRACTED]
- [[.test_require_allowed_does_not_raise()]] - `calls` [EXTRACTED]
- [[.test_require_denied_raises_403_with_reason()]] - `calls` [EXTRACTED]
- [[.test_require_denied_without_reason_uses_forbidden()]] - `calls` [EXTRACTED]
- [[AddCollaboratorRequest]] - `uses` [INFERRED]
- [[AddGroupMemberRequest]] - `uses` [INFERRED]
- [[Any_64]] - `uses` [INFERRED]
- [[ApprovalDecisionRequest]] - `uses` [INFERRED]
- [[AuditResult_1]] - `uses` [INFERRED]
- [[CreateDelegationRequest]] - `uses` [INFERRED]
- [[CreateGroupRequest]] - `uses` [INFERRED]
- [[DisconnectRequest]] - `uses` [INFERRED]
- [[EgressApproveRequest]] - `uses` [INFERRED]
- [[EgressRuleOverrideRequest]] - `uses` [INFERRED]
- [[EgressScopeRequest]] - `uses` [INFERRED]
- [[EmergencyBlockRequest]] - `uses` [INFERRED]
- [[JSONResponse]] - `uses` [INFERRED]
- [[LoginRequest]] - `uses` [INFERRED]
- [[RenameGroupRequest]] - `uses` [INFERRED]
- [[Request_7]] - `uses` [INFERRED]
- [[Resolved identity of the SCL caller, including role and user_id.]] - `rationale_for` [EXTRACTED]
- [[SCLCaller_1]] - `uses` [INFERRED]
- [[SCLCaller_3]] - `uses` [INFERRED]
- [[SCLInterface_1]] - `uses` [INFERRED]
- [[ScanRequest_1]] - `uses` [INFERRED]
- [[ServiceActionRequest]] - `uses` [INFERRED]
- [[SetLogLevelRequest]] - `uses` [INFERRED]
- [[SetModeRequest]] - `uses` [INFERRED]
- [[SetModuleModeRequest]] - `uses` [INFERRED]
- [[SetRoleRequest]] - `uses` [INFERRED]
- [[SetUserModeRequest]] - `uses` [INFERRED]
- [[UpdateDisplayNameRequest]] - `uses` [INFERRED]
- [[WebSocket_6]] - `uses` [INFERRED]
- [[_make_owner_caller()]] - `calls` [EXTRACTED]
- [[_resolve_caller()]] - `references` [EXTRACTED]
- [[auth.py_1]] - `contains` [EXTRACTED]
- [[get_caller()]] - `references` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SOC_Dashboard