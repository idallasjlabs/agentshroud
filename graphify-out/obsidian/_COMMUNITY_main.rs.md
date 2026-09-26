---
type: community
cohesion: 0.06
members: 105
---

# main.rs

**Cohesion:** 0.06 - loosely connected
**Members:** 105 nodes

## Members
- [[.__init__()_129]] - code - gateway/soc/auth.py
- [[.__init__()_130]] - code - gateway/soc/contributors.py
- [[.__init__()_181]] - code - gateway/tests/test_soc_contributors.py
- [[._build_record()]] - code - gateway/soc/contributors.py
- [[._ensure_rbac()]] - code - gateway/soc/contributors.py
- [[._ensure_teams()]] - code - gateway/soc/contributors.py
- [[._get_engine()]] - code - gateway/soc/services.py
- [[._load_paused_ids()]] - code - gateway/soc/contributors.py
- [[._logs_via_socket()]] - code - gateway/soc/services.py
- [[.get_contributor()]] - code - gateway/soc/contributors.py
- [[.get_logs()_1]] - code - gateway/soc/services.py
- [[.get_user_role()_3]] - code - gateway/tests/test_soc_contributors.py
- [[.is_group_admin()_1]] - code - gateway/soc/auth.py
- [[.is_owner()_2]] - code - gateway/soc/auth.py
- [[.list_contributors()]] - code - gateway/soc/contributors.py
- [[.restart_service()_1]] - code - gateway/soc/services.py
- [[.start_service()]] - code - gateway/soc/services.py
- [[.stop_service()_1]] - code - gateway/soc/services.py
- [[.test_all_actions_false_without_engine()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_empty_info_means_container_not_found()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_engine_failure_falls_back_to_socket_data()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_engine_failure_falls_back_to_socket_then_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_full_running_descriptor()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_injected_engine_returned()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_internal_probe_failure_keeps_container_descriptors()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_internal_services_status_mapping()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_malformed_sections_fall_back_to_defaults()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_parse_exception_returns_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_resolution_failure_returns_none()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_resolved_from_runtime_module()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_restart_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_start_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_stop_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_unparseable_started_at_yields_no_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_update_engine_without_pull_support()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_update_pull_failure_still_restarts()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_update_pull_then_restart()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_update_restart_failure_returns_false()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.test_zero_started_at_skips_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[.update_service()]] - code - gateway/soc/services.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_67]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult_1]] - code - gateway/soc/router.py
- [[AuditResult]] - code - gateway/soc/models.py
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
- [[LoginRequest]] - code - gateway/soc/router.py
- [[Pull the latest image then restart the container.]] - rationale - gateway/soc/services.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[Read container logs via Docker Unix socket — fallback when engine unavailable.]] - rationale - gateway/soc/services.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_6]] - code - gateway/soc/router.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Return the container engine from app_state if not injected.]] - rationale - gateway/soc/services.py
- [[Role_2]] - code - gateway/soc/auth.py
- [[SCLCaller]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface_1]] - code - gateway/soc/router.py
- [[SCLInterface]] - code - gateway/soc/models.py
- [[ScanRequest_1]] - code - gateway/soc/router.py
- [[ServiceManager]] - code - gateway/soc/services.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestDescribeService]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestGetEngine_1]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestLifecycleActions]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestListServices]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[Thin wrapper around the container engine that produces ServiceDescriptors.]] - rationale - gateway/soc/services.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WebSocket_5]] - code - gateway/soc/router.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_full_inspect_info()]] - code - gateway/tests/test_soc_services_coverage.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mainrs
SORT file.name ASC
```

## Connections to other communities
- 84 edges to [[_COMMUNITY_socrouter.py]]
- 28 edges to [[_COMMUNITY_EncryptedStore]]
- 26 edges to [[_COMMUNITY_EgressAction]]
- 20 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 19 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY_SSHProxy]]
- 9 edges to [[_COMMUNITY_IntelReportStore]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_RateLimiter]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_ApprovalRequest]]
- 3 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 2 edges to [[_COMMUNITY_server.py]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY__call_agent_stream()]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_get_trivy_summary()]]
- 2 edges to [[_COMMUNITY_SCLClient]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_OpenClaw Bot Container]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_REPORT STRUCTURE]]
- 1 edge to [[_COMMUNITY_TestClamavSummary]]

## Top bridge nodes
- [[BaseModel]] - degree 86, connects to 29 communities
- [[ServiceManager]] - degree 106, connects to 5 communities
- [[ContributorManager]] - degree 57, connects to 5 communities
- [[SCLCaller]] - degree 46, connects to 4 communities
- [[SCLConfirmationRequired]] - degree 35, connects to 2 communities