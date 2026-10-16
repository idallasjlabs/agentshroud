---
type: community
cohesion: 0.02
members: 162
---

# ResourceGuard

**Cohesion:** 0.02 - loosely connected
**Members:** 162 nodes

## Members
- [[dot-__del__()]] - code - gateway/security/resource_guard.py
- [[dot-__init__()_66]] - code - gateway/security/resource_guard.py
- [[dot-_alert_high_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_build_bridge()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-_check_system_resources()]] - code - gateway/security/resource_guard.py
- [[dot-_cleanup_expired_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_get_disk_io_stats()]] - code - gateway/security/resource_guard.py
- [[dot-_monitor_resources()]] - code - gateway/security/resource_guard.py
- [[dot-_start_monitoring_task()]] - code - gateway/security/resource_guard.py
- [[dot-add_alert_callback()_1]] - code - gateway/security/resource_guard.py
- [[dot-check_cpu_limit()]] - code - gateway/security/resource_guard.py
- [[dot-check_disk_write_limit()]] - code - gateway/security/resource_guard.py
- [[dot-check_memory_limit()]] - code - gateway/security/resource_guard.py
- [[dot-check_resource()]] - code - gateway/security/resource_guard.py
- [[dot-check_vram_headroom()]] - code - gateway/security/resource_guard.py
- [[dot-cleanup_temp_files()]] - code - gateway/security/resource_guard.py
- [[dot-get_usage_stats()]] - code - gateway/security/resource_guard.py
- [[dot-register_temp_file()]] - code - gateway/security/resource_guard.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_resource_guard.py
- [[dot-start_request_tracking()]] - code - gateway/security/resource_guard.py
- [[dot-stop()_6]] - code - gateway/security/resource_guard.py
- [[dot-stop_monitoring()]] - code - gateway/security/resource_guard.py
- [[dot-teardown_method()_6]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_bridge_registered_via_add_alert_callback_fires_through()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_brief_spike_below_debounce_does_not_alert()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_cpu_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_check_disk_write_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_check_memory_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_check_resource_over_limit_blocked()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_resource_temp_files_limit()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_resource_under_limit_passes()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_cleanup_keeps_fresh_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cleanup_removes_stale_agents()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cleanup_tolerates_missing_file()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cleanup_unlinks_existing_and_clears_registry()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cpu_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_cpu_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cpu_limit_fails_closed_on_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cpu_limit_ok_when_under()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_default_mode_is_enforce()_5]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_disabled_when_threshold_zero()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_disk_write_limit_allows_when_no_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit_under_threshold()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_from_environment_defaults_to_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_get_resource_guard_is_lazy_singleton()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_get_usage_stats_for_agent()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_get_usage_stats_system_wide()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_invalid_resource_type()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_keyvault_instantiated_and_seeded_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_memory_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_memory_limit_fails_closed_on_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_memory_limit_ok_and_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_missing_timestamp_falls_back_to_zero()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_multiple_agents_isolated()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_natural_language_question_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_no_hardcoded_owner_id_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_non_spike_alert_dispatched_with_medium_severity()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_passes_with_sufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_pipeline_scans_outbound_for_key_leaks()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_register_blocks_over_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_register_under_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_rejects_insufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_request_count_limiting()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_resource_guard_config()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_resource_guard_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_sanitize_reason_preserves_simple_text()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_file_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_module_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_setup_resource_guard_returns_real_guard_with_default_limits()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_setup_with_custom_limits_overrides_defaults()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_spike_alert_dispatched_with_high_severity()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_start_request_tracking_records_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_start_request_tracking_survives_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_stop_cancels_monitor_task()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_stop_cancels_monitor_task_and_idempotent()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_system_resource_monitoring_alerts_after_debounce()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_unparseable_text_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_usage_stats()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_window_expiry_resets_usage()]] - code - gateway/tests/test_resource_guard.py
- [[A single over-threshold sample followed by an under-threshold sample is suppress]] - rationale - gateway/tests/test_resource_guard.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_22]] - code - gateway/security/resource_guard.py
- [[Any_23]] - code - gateway/tests/test_resource_guard_wiring.py
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Best-effort cleanup for test contexts that don't call stop().]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded CPU time limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded disk write limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded memory limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if resource usage is allowed for an agent.          Args             agen]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Clean up temporary files for an agent.]] - rationale - gateway/security/resource_guard.py
- [[Configuration for resource limits.]] - rationale - gateway/security/resource_guard.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[End-to-end register the bridge on a real ResourceGuard, trigger         its ale]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[Get current disk IO statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get the global resource guard instance, creating it lazily on first call.]] - rationale - gateway/security/resource_guard.py
- [[Monitor and limit resource usage per agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Pre-flight VRAM headroom check before dispatching a long-context local-model cal]] - rationale - gateway/security/resource_guard.py
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[Raised when a local-model call is rejected because estimated VRAM usage     woul]] - rationale - gateway/security/resource_guard.py
- [[Recreate the lifespan bridge closure verbatim from gatewayingest_apilifespan.p]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[Register a temporary file for tracking.]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard]] - code - gateway/security/resource_guard.py
- [[ResourceGuard is instantiated at startup and reachable on app_state.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[ResourceLimits]] - code - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[Setup resource guard with custom limits.]] - rationale - gateway/security/resource_guard.py
- [[Start background monitoring task.]] - rationale - gateway/security/resource_guard.py
- [[Start tracking resources for a specific agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring task cleanly.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring.]] - rationale - gateway/security/resource_guard.py
- [[Sustained high CPU fires the alert after debounce samples are crossed.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test ResourceGuardConfig dataclass.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test handling of invalid resource types.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test request count per minute limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test temp file count limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that different agents have isolated resource tracking.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage over limits is blocked.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage resets after time window.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage under limits passes.]] - rationale - gateway/tests/test_resource_guard.py
- [[TestCpuMemoryDiskLimits]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestDRYOwnerChatID]] - code - gateway/tests/test_round2_hardening.py
- [[TestEgressConfigDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestEnvGuardFailOpen]] - code - gateway/tests/test_round2_hardening.py
- [[TestExpiredUsageCleanup]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestFileSandboxDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestGlobalAccessor]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestKeyVaultWired]] - code - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[TestNotifyUserBlockedSanitization]] - code - gateway/tests/test_round2_hardening.py
- [[TestResourceGuard]] - code - gateway/tests/test_resource_guard.py
- [[TestResourceGuardAlertBridge]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceGuardFailClosed]] - code - gateway/tests/test_round2_hardening.py
- [[TestResourceGuardLifecycle]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceGuardWiring]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestTempFiles]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestUsageStatsAndTracking]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestVramHeadroom]] - code - gateway/tests/test_resource_guard_limits.py
- [[Tests for Round 2 hardening — 9 fixes.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py
- [[The lifespan bridges ResourceGuard's native callback payload to AlertDispatcher.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[The lifespan must stop the background monitor task on shutdown.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py
- [[VRAMHeadroomError]] - code - gateway/security/resource_guard.py
- [[Verify resource check methods return False (deny) on exception.]] - rationale - gateway/tests/test_round2_hardening.py
- [[get_resource_guard()]] - code - gateway/security/resource_guard.py
- [[guard()_2]] - code - gateway/tests/test_resource_guard_limits.py
- [[resource_guard.py]] - code - gateway/security/resource_guard.py
- [[setup_resource_guard()]] - code - gateway/security/resource_guard.py
- [[stop() should cancel background monitor cleanly.]] - rationale - gateway/tests/test_resource_guard.py
- [[test_resource_guard.py]] - code - gateway/tests/test_resource_guard.py
- [[test_resource_guard_limits.py]] - code - gateway/tests/test_resource_guard_limits.py
- [[test_resource_guard_wiring.py]] - code - gateway/tests/test_resource_guard_wiring.py
- [[test_round2_hardening.py]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_AlertDispatcher]]
- 14 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY_GitGuard]]
- 9 edges to [[_COMMUNITY_EgressFilterConfig]]
- 9 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[test_round2_hardening.py]] - degree 17, connects to 4 communities
- [[TestResourceGuardFailClosed]] - degree 11, connects to 4 communities
- [[TestLLMProxyEndpoints]] - degree 10, connects to 4 communities
- [[TestNotifyUserBlockedSanitization]] - degree 10, connects to 4 communities
- [[TestEnvGuardFailOpen]] - degree 9, connects to 4 communities
