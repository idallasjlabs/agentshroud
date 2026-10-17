---
type: community
members: 71
---

# _FakeRBAC

**Members:** 71 nodes

## Members
- [[dot-__init__()_163]] - code - gateway/soc/auth.py
- [[dot-__init__()_164]] - code - gateway/soc/contributors.py
- [[dot-__init__()_165]] - code - gateway/tests/test_soc_contributors.py
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-get_user_role()_3]] - code - gateway/tests/test_soc_contributors.py
- [[dot-is_group_admin()_2]] - code - gateway/soc/auth.py
- [[dot-is_owner()_3]] - code - gateway/soc/auth.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[dot-require()_1]] - code - gateway/soc/auth.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[Action_3]] - code - gateway/soc/auth.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_68]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult]] - code - gateway/soc/router.py
- [[AuditResult_1]] - code - gateway/soc/models.py
- [[BaseModel_2]] - code
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[ContributorRecord_1]] - code - gateway/soc/contributors.py
- [[CreateDelegationRequest]] - code - gateway/soc/router.py
- [[CreateGroupRequest]] - code - gateway/soc/router.py
- [[DisconnectRequest]] - code - gateway/soc/router.py
- [[EgressApproveRequest]] - code - gateway/soc/router.py
- [[EgressRuleOverrideRequest]] - code - gateway/soc/router.py
- [[EgressScopeRequest]] - code - gateway/soc/router.py
- [[EmergencyBlockRequest]] - code - gateway/soc/router.py
- [[LoginRequest]] - code - gateway/soc/router.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_9]] - code - gateway/soc/router.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Resource_2]] - code - gateway/soc/auth.py
- [[Role_66]] - code - gateway/soc/auth.py
- [[SCLCaller_2]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface]] - code - gateway/soc/router.py
- [[SCLInterface_1]] - code - gateway/soc/models.py
- [[ScanRequest]] - code - gateway/soc/router.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WebSocket_8]] - code - gateway/soc/router.py
- [[_FakeRBAC_2]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 73 edges to [[_COMMUNITY_socrouter.py]]
- 26 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 24 edges to [[_COMMUNITY_ServiceManager]]
- 19 edges to [[_COMMUNITY_MiddlewareManager]]
- 13 edges to [[_COMMUNITY_create_auth_dependency]]
- 9 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection (2)]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py (3)]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_upgrade]]
- 2 edges to [[_COMMUNITY_chatbotmain.py]]
- 2 edges to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_ServiceManager (2)]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 1 edge to [[_COMMUNITY_RBACConfig (2)]]

## Top bridge nodes
- [[BaseModel_2]] - degree 84, connects to 26 communities
- [[ContributorManager]] - degree 57, connects to 5 communities
- [[SCLCaller_2]] - degree 46, connects to 3 communities
- [[SCLConfirmationRequired]] - degree 35, connects to 2 communities
- [[AuditLogEntry]] - degree 31, connects to 2 communities
