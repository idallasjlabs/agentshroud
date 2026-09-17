---
source_file: "gateway/soc/contributors.py"
type: "code"
community: "Community 226"
location: "L24"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_226
---

# ContributorManager

## Connections
- [[dot-__init__()_100]] - `method` [EXTRACTED]
- [[dot-_build_record()]] - `method` [EXTRACTED]
- [[dot-_ensure_rbac()]] - `method` [EXTRACTED]
- [[dot-_ensure_teams()]] - `method` [EXTRACTED]
- [[dot-_load_paused_ids()]] - `method` [EXTRACTED]
- [[dot-get_contributor()]] - `method` [EXTRACTED]
- [[dot-list_contributors()]] - `method` [EXTRACTED]
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_real_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_suspended_level()]] - `calls` [EXTRACTED]
- [[dot-test_list_contributors_populates_paused_per_user()]] - `calls` [EXTRACTED]
- [[dot-test_non_paused_user_reports_paused_false()]] - `calls` [EXTRACTED]
- [[dot-test_paused_is_independent_of_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_paused_user_reports_paused_true()]] - `calls` [EXTRACTED]
- [[AddCollaboratorRequest]] - `uses` [INFERRED]
- [[AddGroupMemberRequest]] - `uses` [INFERRED]
- [[Any_23]] - `uses` [INFERRED]
- [[ApprovalDecisionRequest]] - `uses` [INFERRED]
- [[AuditResult]] - `uses` [INFERRED]
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - `rationale_for` [EXTRACTED]
- [[ContributorRecord_1]] - `uses` [INFERRED]
- [[CreateDelegationRequest]] - `uses` [INFERRED]
- [[CreateGroupRequest]] - `uses` [INFERRED]
- [[DisconnectRequest]] - `uses` [INFERRED]
- [[EgressApproveRequest]] - `uses` [INFERRED]
- [[EgressRuleOverrideRequest]] - `uses` [INFERRED]
- [[EgressScopeRequest]] - `uses` [INFERRED]
- [[EmergencyBlockRequest]] - `uses` [INFERRED]
- [[GET users endpoint]] - `calls` [EXTRACTED]
- [[JSONResponse]] - `uses` [INFERRED]
- [[LoginRequest]] - `uses` [INFERRED]
- [[Platform]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `calls` [EXTRACTED]
- [[RBACConfig_2]] - `references` [EXTRACTED]
- [[RenameGroupRequest]] - `uses` [INFERRED]
- [[Request_6]] - `uses` [INFERRED]
- [[SCLCaller_2]] - `uses` [INFERRED]
- [[SCLInterface]] - `uses` [INFERRED]
- [[ScanRequest_1]] - `uses` [INFERRED]
- [[ServiceActionRequest]] - `uses` [INFERRED]
- [[SetLogLevelRequest]] - `uses` [INFERRED]
- [[SetModeRequest]] - `uses` [INFERRED]
- [[SetModuleModeRequest]] - `uses` [INFERRED]
- [[SetRoleRequest]] - `uses` [INFERRED]
- [[SetUserModeRequest]] - `uses` [INFERRED]
- [[TestLockdownLevelWiring]] - `uses` [INFERRED]
- [[TestPausedFieldWiring]] - `uses` [INFERRED]
- [[UpdateDisplayNameRequest]] - `uses` [INFERRED]
- [[UserRole]] - `uses` [INFERRED]
- [[WebSocket_2]] - `uses` [INFERRED]
- [[_FakeRBAC_1]] - `uses` [INFERRED]
- [[contributors.py]] - `contains` [EXTRACTED]
- [[get_user()]] - `calls` [EXTRACTED]
- [[list_users()]] - `calls` [EXTRACTED]
- [[load_paused_collaborator_ids()]] - `calls` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_soc_contributors.py]] - `tests` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_226