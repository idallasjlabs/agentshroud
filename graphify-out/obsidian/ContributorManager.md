---
source_file: "gateway/soc/contributors.py"
type: "code"
community: "Community 10"
location: "L24"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_10
---

# ContributorManager

## Connections
- [[.__init__()_145]] - `method` [EXTRACTED]
- [[._build_record()]] - `method` [EXTRACTED]
- [[._ensure_rbac()]] - `method` [EXTRACTED]
- [[._ensure_teams()]] - `method` [EXTRACTED]
- [[._load_paused_ids()]] - `method` [EXTRACTED]
- [[.get_contributor()]] - `method` [EXTRACTED]
- [[.list_contributors()]] - `method` [EXTRACTED]
- [[.test_build_record_defaults_to_normal_when_no_lockdown_state()]] - `calls` [EXTRACTED]
- [[.test_build_record_does_not_crash_if_lockdown_missing()]] - `calls` [EXTRACTED]
- [[.test_build_record_prefers_app_wide_progressive_lockdown()]] - `calls` [EXTRACTED]
- [[.test_build_record_reports_real_lockdown_level()]] - `calls` [EXTRACTED]
- [[.test_build_record_reports_suspended_level()]] - `calls` [EXTRACTED]
- [[.test_list_contributors_populates_paused_per_user()]] - `calls` [EXTRACTED]
- [[.test_non_paused_user_reports_paused_false()]] - `calls` [EXTRACTED]
- [[.test_paused_is_independent_of_lockdown_level()]] - `calls` [EXTRACTED]
- [[.test_paused_user_reports_paused_true()]] - `calls` [EXTRACTED]
- [[AddCollaboratorRequest]] - `uses` [INFERRED]
- [[AddGroupMemberRequest]] - `uses` [INFERRED]
- [[Any_77]] - `uses` [INFERRED]
- [[ApprovalDecisionRequest]] - `uses` [INFERRED]
- [[AuditResult_1]] - `uses` [INFERRED]
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - `rationale_for` [EXTRACTED]
- [[ContributorRecord_1]] - `uses` [INFERRED]
- [[CreateDelegationRequest]] - `uses` [INFERRED]
- [[CreateGroupRequest]] - `uses` [INFERRED]
- [[DisconnectRequest]] - `uses` [INFERRED]
- [[EdgeEnrollRequest]] - `uses` [INFERRED]
- [[EdgeKillRequest]] - `uses` [INFERRED]
- [[EdgeUnkillRequest]] - `uses` [INFERRED]
- [[EgressApproveRequest]] - `uses` [INFERRED]
- [[EgressRuleOverrideRequest]] - `uses` [INFERRED]
- [[EgressScopeRequest]] - `uses` [INFERRED]
- [[EmergencyBlockRequest]] - `uses` [INFERRED]
- [[HTTPException]] - `uses` [INFERRED]
- [[JSONResponse_1]] - `uses` [INFERRED]
- [[LoginRequest]] - `uses` [INFERRED]
- [[Platform]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `calls` [EXTRACTED]
- [[RBACConfig_1]] - `references` [EXTRACTED]
- [[RenameGroupRequest]] - `uses` [INFERRED]
- [[Request_7]] - `uses` [INFERRED]
- [[SCLCaller_1]] - `uses` [INFERRED]
- [[SCLInterface_1]] - `uses` [INFERRED]
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
- [[UserRole_1]] - `uses` [INFERRED]
- [[WebSocket_5]] - `uses` [INFERRED]
- [[_FakeRBAC_1]] - `uses` [INFERRED]
- [[contributors.py]] - `contains` [EXTRACTED]
- [[get_user()]] - `calls` [EXTRACTED]
- [[list_users()]] - `calls` [EXTRACTED]
- [[load_paused_collaborator_ids()]] - `calls` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[test_soc_contributors.py]] - `tests` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_10