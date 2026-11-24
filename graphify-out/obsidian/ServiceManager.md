---
source_file: "gateway/soc/services.py"
type: "code"
community: "ServiceManager"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ServiceManager
---

# ServiceManager

## Connections
- [[dot-__init__()_162]] - `method` [EXTRACTED]
- [[dot-_describe_service()]] - `method` [EXTRACTED]
- [[dot-_get_engine()]] - `method` [EXTRACTED]
- [[dot-_logs_via_socket()]] - `method` [EXTRACTED]
- [[dot-get_logs()_1]] - `method` [EXTRACTED]
- [[dot-get_service()]] - `method` [EXTRACTED]
- [[dot-list_services()]] - `method` [EXTRACTED]
- [[dot-mgr_with_engine()]] - `calls` [EXTRACTED]
- [[dot-restart_service()_1]] - `method` [EXTRACTED]
- [[dot-start_service()]] - `method` [EXTRACTED]
- [[dot-stop_service()_1]] - `method` [EXTRACTED]
- [[dot-test_all_actions_false_without_engine()]] - `calls` [EXTRACTED]
- [[dot-test_bytes_payload_is_decoded()]] - `calls` [EXTRACTED]
- [[dot-test_empty_info_means_container_not_found()]] - `calls` [EXTRACTED]
- [[dot-test_engine_error_falls_back_to_socket()]] - `calls` [EXTRACTED]
- [[dot-test_engine_failure_falls_back_to_socket_data()]] - `calls` [EXTRACTED]
- [[dot-test_engine_failure_falls_back_to_socket_then_unknown()]] - `calls` [EXTRACTED]
- [[dot-test_exception_returns_empty()]] - `calls` [EXTRACTED]
- [[dot-test_full_running_descriptor()]] - `calls` [EXTRACTED]
- [[dot-test_get_logs_no_engine_returns_empty()]] - `calls` [EXTRACTED]
- [[dot-test_injected_engine_returned()]] - `calls` [EXTRACTED]
- [[dot-test_instantiate_without_engine()]] - `calls` [EXTRACTED]
- [[dot-test_internal_probe_failure_keeps_container_descriptors()]] - `calls` [EXTRACTED]
- [[dot-test_internal_services_status_mapping()]] - `calls` [EXTRACTED]
- [[dot-test_malformed_sections_fall_back_to_defaults()]] - `calls` [EXTRACTED]
- [[dot-test_no_engine_no_socket()]] - `calls` [EXTRACTED]
- [[dot-test_non_200_returns_empty()]] - `calls` [EXTRACTED]
- [[dot-test_parse_exception_returns_unknown()]] - `calls` [EXTRACTED]
- [[dot-test_parses_multiplexed_frames()]] - `calls` [EXTRACTED]
- [[dot-test_resolution_failure_returns_none()]] - `calls` [EXTRACTED]
- [[dot-test_resolved_from_runtime_module()]] - `calls` [EXTRACTED]
- [[dot-test_restart_success_and_failure()]] - `calls` [EXTRACTED]
- [[dot-test_socket_fallback_empty_lines()]] - `calls` [EXTRACTED]
- [[dot-test_start_success_and_failure()]] - `calls` [EXTRACTED]
- [[dot-test_stop_success_and_failure()]] - `calls` [EXTRACTED]
- [[dot-test_tail_limit_applied()]] - `calls` [EXTRACTED]
- [[dot-test_unparseable_started_at_yields_no_uptime()]] - `calls` [EXTRACTED]
- [[dot-test_update_engine_without_pull_support()]] - `calls` [EXTRACTED]
- [[dot-test_update_pull_failure_still_restarts()]] - `calls` [EXTRACTED]
- [[dot-test_update_pull_then_restart()]] - `calls` [EXTRACTED]
- [[dot-test_update_restart_failure_returns_false()]] - `calls` [EXTRACTED]
- [[dot-test_zero_started_at_skips_uptime()]] - `calls` [EXTRACTED]
- [[dot-update_service()]] - `method` [EXTRACTED]
- [[HealthStatus]] - `uses` [INFERRED]
- [[ServiceDescriptor]] - `uses` [INFERRED]
- [[ServiceStatus]] - `uses` [INFERRED]
- [[TestDescribeService]] - `uses` [INFERRED]
- [[TestGetEngine_1]] - `uses` [INFERRED]
- [[TestGetLogs]] - `uses` [INFERRED]
- [[TestLifecycleActions]] - `uses` [INFERRED]
- [[TestListServices]] - `uses` [INFERRED]
- [[TestLogsViaSocket]] - `uses` [INFERRED]
- [[TestServiceManagerGetLogs]] - `uses` [INFERRED]
- [[TestServiceManagerImport]] - `uses` [INFERRED]
- [[Thin wrapper around the container engine that produces ServiceDescriptors.]] - `rationale_for` [EXTRACTED]
- [[_local_agent_health()]] - `calls` [EXTRACTED]
- [[get_health()]] - `uses` [INFERRED]
- [[get_service_logs()]] - `uses` [INFERRED]
- [[list_services()]] - `uses` [INFERRED]
- [[restart_service()]] - `uses` [INFERRED]
- [[services.py]] - `contains` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[start_service()]] - `uses` [INFERRED]
- [[stop_service()]] - `uses` [INFERRED]
- [[test_soc_services.py]] - `imports` [EXTRACTED]
- [[test_soc_services_coverage.py]] - `imports` [EXTRACTED]
- [[update_service()]] - `uses` [INFERRED]
- [[upgrade_hermes()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ServiceManager
