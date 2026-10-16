---
type: community
cohesion: 0.04
members: 90
---

# ServiceManager

**Cohesion:** 0.04 - loosely connected
**Members:** 90 nodes

## Members
- [[dot-__init__()_182]] - code - gateway/soc/services.py
- [[dot-_describe_service()]] - code - gateway/soc/services.py
- [[dot-_get_engine()]] - code - gateway/soc/services.py
- [[dot-_logs_via_socket()]] - code - gateway/soc/services.py
- [[dot-get_logs()_1]] - code - gateway/soc/services.py
- [[dot-get_service()]] - code - gateway/soc/services.py
- [[dot-list_services()]] - code - gateway/soc/services.py
- [[dot-mgr_with_engine()]] - code - gateway/tests/test_soc_services.py
- [[dot-restart_service()_1]] - code - gateway/soc/services.py
- [[dot-start_service()]] - code - gateway/soc/services.py
- [[dot-stop_service()_1]] - code - gateway/soc/services.py
- [[dot-test_all_actions_false_without_engine()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_bytes_payload_is_decoded()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_empty_info_means_container_not_found()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_engine_error_falls_back_to_socket()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_engine_failure_falls_back_to_socket_data()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_engine_failure_falls_back_to_socket_then_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_full_running_descriptor()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_get_logs_module_filter_case_insensitive()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_empty_returns_all()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_excludes_non_matching()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_keeps_matching_lines()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_engine_returns_empty()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_filter_returns_tail()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_import()_1]] - code - gateway/tests/test_soc_services.py
- [[dot-test_injected_engine_returned()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_instantiate_without_engine()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_internal_probe_failure_keeps_container_descriptors()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_internal_services_status_mapping()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_malformed_sections_fall_back_to_defaults()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_no_engine_no_socket()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_parse_exception_returns_unknown()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_resolution_failure_returns_none()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_resolved_from_runtime_module()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_restart_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_socket_fallback_empty_lines()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_standby_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_start_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_stop_success_and_failure()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_stopped_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_unhealthy_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_unparseable_started_at_yields_no_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_engine_without_pull_support()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_pull_failure_still_restarts()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_pull_then_restart()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_update_restart_failure_returns_false()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_zero_started_at_skips_uptime()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-update_service()]] - code - gateway/soc/services.py
- [[Any_77]] - code - gateway/soc/services.py
- [[HealthStatus]] - code - gateway/soc/services.py
- [[HealthStatus_1]] - code - gateway/soc/models.py
- [[Pull the latest image then restart the container.]] - rationale - gateway/soc/services.py
- [[Query Docker daemon directly via Unix socket — no CLI needed.]] - rationale - gateway/soc/services.py
- [[Read container logs via Docker Unix socket — fallback when engine unavailable.]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for clamd (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for fluent-bit (CC-01).]] - rationale - gateway/soc/services.py
- [[Return ServiceDescriptor for each known container plus internal gateway services]] - rationale - gateway/soc/services.py
- [[Return the container engine from app_state if not injected.]] - rationale - gateway/soc/services.py
- [[Return the gateway's own container plus each configured bot's real     container]] - rationale - gateway/soc/services.py
- [[STANDBY = binary installed but cannot run in this environment; should be healthy]] - rationale - gateway/tests/test_soc_services.py
- [[ServiceDescriptor]] - code - gateway/soc/services.py
- [[ServiceDescriptor_1]] - code - gateway/soc/models.py
- [[ServiceManager]] - code - gateway/soc/services.py
- [[ServiceStatus]] - code - gateway/soc/services.py
- [[ServiceStatus_1]] - code - gateway/soc/models.py
- [[TestDescribeService]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestGetEngine]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestGetLogs]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestLifecycleActions]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestListServices]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestServiceDescriptorDefaults]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerGetLogs]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerImport]] - code - gateway/tests/test_soc_services.py
- [[Thin wrapper around the container engine that produces ServiceDescriptors.]] - rationale - gateway/soc/services.py
- [[Unit tests for ServiceManager.get_logs — including module_filter behaviour.]] - rationale - gateway/tests/test_soc_services.py
- [[Validate ServiceDescriptor model defaults — no real container calls.]] - rationale - gateway/tests/test_soc_services.py
- [[Verify ServiceManager can be imported without a running container engine.]] - rationale - gateway/tests/test_soc_services.py
- [[_INTERNAL_SERVICE_ATTRS (internal gateway service table)]] - code - gateway/soc/services.py
- [[_check_clamd()]] - code - gateway/soc/services.py
- [[_check_fluent_bit()]] - code - gateway/soc/services.py
- [[_check_openscap()]] - code - gateway/soc/services.py
- [[_check_wazuh_agent()]] - code - gateway/soc/services.py
- [[_engine_health_to_health()]] - code - gateway/soc/services.py
- [[_engine_status_to_service_status()]] - code - gateway/soc/services.py
- [[_full_inspect_info()]] - code - gateway/tests/test_soc_services_coverage.py
- [[_inspect_via_socket()]] - code - gateway/soc/services.py
- [[_known_services()]] - code - gateway/soc/services.py
- [[services.py]] - code - gateway/soc/services.py
- [[test_soc_services.py]] - code - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceManager
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_ServiceManager]]
- 25 edges to [[_COMMUNITY__FakeRBAC]]
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 9 edges to [[_COMMUNITY__FakeRBAC_1]]
- 4 edges to [[_COMMUNITY_test_soc_bots.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_start-agentshroud.sh]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_soc.js]]
- 1 edge to [[_COMMUNITY_get_engine]]

## Top bridge nodes
- [[ServiceStatus_1]] - degree 13, connects to 5 communities
- [[ServiceDescriptor_1]] - degree 20, connects to 4 communities
- [[HealthStatus_1]] - degree 12, connects to 4 communities
- [[ServiceManager]] - degree 106, connects to 3 communities
- [[services.py]] - degree 16, connects to 3 communities
