---
type: community
cohesion: 0.04
members: 131
---

# ServiceManager

**Cohesion:** 0.04 - loosely connected
**Members:** 131 nodes

## Members
- [[dot-__init__()_81]] - code - gateway/soc/auth.py
- [[dot-__init__()_82]] - code - gateway/soc/contributors.py
- [[dot-__init__()_83]] - code - gateway/tests/test_soc_contributors.py
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_get_engine()]] - code - gateway/soc/services.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-_logs_via_socket()]] - code - gateway/soc/services.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-get_logs()_1]] - code - gateway/soc/services.py
- [[dot-get_user_role()_1]] - code - gateway/tests/test_soc_contributors.py
- [[dot-is_group_admin()_2]] - code - gateway/soc/auth.py
- [[dot-is_owner()_2]] - code - gateway/soc/auth.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[dot-mgr_with_engine()]] - code - gateway/tests/test_soc_services.py
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-require()_1]] - code - gateway/soc/auth.py
- [[dot-restart_service()_1]] - code - gateway/soc/services.py
- [[dot-start_service()]] - code - gateway/soc/services.py
- [[dot-stop_service()_1]] - code - gateway/soc/services.py
- [[dot-test_all_actions_false_without_engine()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_empty_info_means_container_not_found()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_engine_failure_falls_back_to_socket_data()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_engine_failure_falls_back_to_socket_then_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_full_running_descriptor()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_get_logs_module_filter_case_insensitive()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_empty_returns_all()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_excludes_non_matching()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_keeps_matching_lines()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_engine_returns_empty()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_filter_returns_tail()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_import()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_injected_engine_returned()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_instantiate_without_engine()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_internal_probe_failure_keeps_container_descriptors()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_internal_services_status_mapping()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_malformed_sections_fall_back_to_defaults()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_parse_exception_returns_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_resolution_failure_returns_none()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_resolved_from_runtime_module()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_restart_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_start_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_stop_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_unparseable_started_at_yields_no_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_engine_without_pull_support()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_pull_failure_still_restarts()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_pull_then_restart()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_restart_failure_returns_false()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_zero_started_at_skips_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-update_service()]] - code - gateway/soc/services.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[Action]] - code - gateway/soc/auth.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_28]] - code - gateway/soc/router.py
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
- [[RBACManager]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[Read container logs via Docker Unix socket — fallback when engine unavailable.]] - rationale - gateway/soc/services.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_4]] - code - gateway/soc/router.py
- [[Request to execute an SSH command]] - rationale - gateway/ingest_api/models.py
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - rationale - gateway/ingest_api/models.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Resource]] - code - gateway/soc/auth.py
- [[Response from POST sshwrite_file.      success reflects whether the remote wri]] - rationale - gateway/ingest_api/models.py
- [[Response from SSH command execution]] - rationale - gateway/ingest_api/models.py
- [[Return the container engine from app_state if not injected.]] - rationale - gateway/soc/services.py
- [[Role_18]] - code - gateway/soc/auth.py
- [[SCLCaller_1]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface]] - code - gateway/soc/router.py
- [[SCLInterface_1]] - code - gateway/soc/models.py
- [[SSHExecRequest_1]] - code - gateway/ingest_api/models.py
- [[SSHExecResponse]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileRequest_1]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileResponse]] - code - gateway/ingest_api/models.py
- [[ScanRequest]] - code - gateway/soc/router.py
- [[ServiceManager]] - code - gateway/soc/services.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestDescribeService]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestGetEngine]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestLifecycleActions]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestListServices]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestServiceManagerGetLogs]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerImport]] - code - gateway/tests/test_soc_services.py
- [[Thin wrapper around the container engine that produces ServiceDescriptors.]] - rationale - gateway/soc/services.py
- [[Unit tests for ServiceManager.get_logs — including module_filter behaviour.]] - rationale - gateway/tests/test_soc_services.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[Verify ServiceManager can be imported without a running container engine.]] - rationale - gateway/tests/test_soc_services.py
- [[WebSocket_1]] - code - gateway/soc/router.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_full_inspect_info()]] - code - gateway/tests/test_soc_services_coverage.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceManager
SORT file.name ASC
```

## Connections to other communities
- 86 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 46 edges to [[_COMMUNITY_Enum]]
- 26 edges to [[_COMMUNITY_test_soc_services_coverage.py]]
- 18 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 9 edges to [[_COMMUNITY_AlertDispatcher (3)]]
- 7 edges to [[_COMMUNITY__make_proxy()]]
- 4 edges to [[_COMMUNITY_ContextSegment]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager]]
- 4 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 3 edges to [[_COMMUNITY_colima-health-check.sh]]
- 3 edges to [[_COMMUNITY_GroupConfig]]
- 3 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor (3)]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_sync-llm-settings.sh]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine (2)]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_upgrade]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2) (2)]]
- 2 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_pick_latest_stable]]
- 1 edge to [[_COMMUNITY_TestEnforceDefaults]]
- 1 edge to [[_COMMUNITY_PathIsolationManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (3)]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_test_fieldflare_route_strips_unsupported_fields_streaming]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)]]
- 1 edge to [[_COMMUNITY_Workflow (follow in order)]]

## Top bridge nodes
- [[BaseModel_1]] - degree 84, connects to 25 communities
- [[ContributorManager]] - degree 57, connects to 4 communities
- [[ServiceManager]] - degree 106, connects to 3 communities
- [[SCLCaller_1]] - degree 46, connects to 3 communities
- [[SCLConfirmationRequired]] - degree 35, connects to 2 communities
