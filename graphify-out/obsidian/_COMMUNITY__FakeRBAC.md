---
type: community
cohesion: 0.10
members: 65
---

# _FakeRBAC

**Cohesion:** 0.10 - loosely connected
**Members:** 65 nodes

## Members
- [[dot-__init__()_148]] - code - gateway/soc/auth.py
- [[dot-__init__()_149]] - code - gateway/soc/contributors.py
- [[dot-__init__()_150]] - code - gateway/tests/test_soc_contributors.py
- [[dot-get_user_role()_2]] - code - gateway/tests/test_soc_contributors.py
- [[dot-is_group_admin()_2]] - code - gateway/soc/auth.py
- [[dot-is_owner()_4]] - code - gateway/soc/auth.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_53]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult]] - code - gateway/soc/router.py
- [[AuditResult_1]] - code - gateway/soc/models.py
- [[BaseModel_1]] - code
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[CreateDelegationRequest]] - code - gateway/soc/router.py
- [[CreateGroupRequest]] - code - gateway/soc/router.py
- [[DisconnectRequest]] - code - gateway/soc/router.py
- [[EgressApproveRequest]] - code - gateway/soc/router.py
- [[EgressRuleOverrideRequest]] - code - gateway/soc/router.py
- [[EgressScopeRequest]] - code - gateway/soc/router.py
- [[EmergencyBlockRequest]] - code - gateway/soc/router.py
- [[LoginRequest]] - code - gateway/soc/router.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_5]] - code - gateway/soc/router.py
- [[Request to execute an SSH command]] - rationale - gateway/ingest_api/models.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Response from POST sshwrite_file.      success reflects whether the remote wri]] - rationale - gateway/ingest_api/models.py
- [[Response from SSH command execution]] - rationale - gateway/ingest_api/models.py
- [[Role_57]] - code - gateway/soc/auth.py
- [[SCLCaller_2]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface]] - code - gateway/soc/router.py
- [[SCLInterface_1]] - code - gateway/soc/models.py
- [[SSHExecRequest_1]] - code - gateway/ingest_api/models.py
- [[SSHExecResponse]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileResponse]] - code - gateway/ingest_api/models.py
- [[ScanRequest]] - code - gateway/soc/router.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WebSocket_5]] - code - gateway/soc/router.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 71 edges to [[_COMMUNITY_socrouter.py]]
- 25 edges to [[_COMMUNITY_ServiceManager_1]]
- 23 edges to [[_COMMUNITY__FakeRBAC_1]]
- 19 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 6 edges to [[_COMMUNITY_create_auth_dependency]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 3 edges to [[_COMMUNITY_test_forward_stream.py]]
- 3 edges to [[_COMMUNITY_ModeRequest]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py]]
- 3 edges to [[_COMMUNITY_AgentTarget_1]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 3 edges to [[_COMMUNITY_api.py_1]]
- 2 edges to [[_COMMUNITY_test_prompt_guard.py_2]]
- 2 edges to [[_COMMUNITY_All Dependencies_1]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection_1]]
- 2 edges to [[_COMMUNITY_chatbotmain.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 2 edges to [[_COMMUNITY_upgrade]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager_5]]
- 1 edge to [[_COMMUNITY_soc_dashboard]]
- 1 edge to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]

## Top bridge nodes
- [[BaseModel_1]] - degree 84, connects to 28 communities
- [[ContributorManager]] - degree 57, connects to 5 communities
- [[SCLCaller_2]] - degree 46, connects to 4 communities
- [[AuditResult_1]] - degree 31, connects to 4 communities
- [[SCLInterface_1]] - degree 31, connects to 4 communities
