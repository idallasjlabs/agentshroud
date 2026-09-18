---
type: community
cohesion: 0.09
members: 71
---

# BaseModel

**Cohesion:** 0.09 - loosely connected
**Members:** 71 nodes

## Members
- [[.__init__()_66]] - code - gateway/soc/auth.py
- [[.__init__()_100]] - code - gateway/soc/contributors.py
- [[.__init__()_101]] - code - gateway/tests/test_soc_contributors.py
- [[._build_record()]] - code - gateway/soc/contributors.py
- [[._ensure_rbac()]] - code - gateway/soc/contributors.py
- [[._ensure_teams()]] - code - gateway/soc/contributors.py
- [[._load_paused_ids()]] - code - gateway/soc/contributors.py
- [[.get_contributor()]] - code - gateway/soc/contributors.py
- [[.get_user_role()_2]] - code - gateway/tests/test_soc_contributors.py
- [[.is_group_admin()]] - code - gateway/soc/auth.py
- [[.is_owner()_2]] - code - gateway/soc/auth.py
- [[.list_contributors()]] - code - gateway/soc/contributors.py
- [[.require()]] - code - gateway/soc/auth.py
- [[.test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[Action_2]] - code - gateway/soc/auth.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_22]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult]] - code - gateway/soc/router.py
- [[AuditResult_1]] - code - gateway/soc/models.py
- [[BaseModel]] - code
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[CreateDelegationRequest]] - code - gateway/soc/router.py
- [[CreateGroupRequest]] - code - gateway/soc/router.py
- [[DisconnectRequest]] - code - gateway/soc/router.py
- [[EgressApproveRequest]] - code - gateway/soc/router.py
- [[EgressRuleOverrideRequest]] - code - gateway/soc/router.py
- [[EgressScopeRequest]] - code - gateway/soc/router.py
- [[EmergencyBlockRequest]] - code - gateway/soc/router.py
- [[GET users endpoint]] - code - gateway/soc/router.py
- [[LoginRequest]] - code - gateway/soc/router.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_6]] - code - gateway/soc/router.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Resource_2]] - code - gateway/soc/auth.py
- [[Role_14]] - code - gateway/soc/auth.py
- [[SCLCaller_1]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface]] - code - gateway/soc/router.py
- [[SCLInterface_1]] - code - gateway/soc/models.py
- [[ScanRequest_1]] - code - gateway/soc/router.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WebSocket_2]] - code - gateway/soc/router.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BaseModel
SORT file.name ASC
```

## Connections to other communities
- 71 edges to [[_COMMUNITY_socrouter.py]]
- 24 edges to [[_COMMUNITY_ServiceManager]]
- 23 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 16 edges to [[_COMMUNITY_ingest_apimain.py]]
- 9 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 6 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 6 edges to [[_COMMUNITY__FakeRBAC]]
- 6 edges to [[_COMMUNITY_SSHProxy]]
- 5 edges to [[_COMMUNITY_ApprovalRequest]]
- 4 edges to [[_COMMUNITY_forward.py]]
- 4 edges to [[_COMMUNITY_Enum]]
- 3 edges to [[_COMMUNITY_IntelReportStore]]
- 3 edges to [[_COMMUNITY_TeamsConfig]]
- 3 edges to [[_COMMUNITY_ModeRequest]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_chatbotmain.py]]
- 2 edges to [[_COMMUNITY_SecurityConfig]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_DraftEntry]]
- 2 edges to [[_COMMUNITY_detect_runtime()]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 2 edges to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_test_config_hot_reload.py]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_StatusResponse]]
- 1 edge to [[_COMMUNITY_SecurityEvent]]

## Top bridge nodes
- [[BaseModel]] - degree 86, connects to 23 communities
- [[ContributorManager]] - degree 58, connects to 5 communities
- [[SCLCaller_1]] - degree 46, connects to 5 communities
- [[AuditResult_1]] - degree 31, connects to 3 communities
- [[SCLInterface_1]] - degree 31, connects to 3 communities