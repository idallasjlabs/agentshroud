---
type: community
members: 138
---

# ResourceGuard

**Members:** 138 nodes

## Members
- [[dot-__del__()]] - code - gateway/security/resource_guard.py
- [[dot-__init__()_160]] - code - gateway/security/resource_guard.py
- [[dot-_alert_high_usage()]] - code - gateway/security/resource_guard.py
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
- [[dot-setup_method()_27]] - code - gateway/tests/test_resource_guard.py
- [[dot-start_request_tracking()]] - code - gateway/security/resource_guard.py
- [[dot-stop()_10]] - code - gateway/security/resource_guard.py
- [[dot-stop_monitoring()]] - code - gateway/security/resource_guard.py
- [[dot-teardown_method()_4]] - code - gateway/tests/test_resource_guard.py
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
- [[dot-test_disabled_when_threshold_zero()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_get_resource_guard_is_lazy_singleton()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_invalid_resource_type()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_memory_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_multiple_agents_isolated()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_passes_with_sufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_register_blocks_over_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_register_under_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_rejects_insufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_request_count_limiting()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_resource_guard_config()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_resource_guard_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_setup_resource_guard_returns_real_guard_with_default_limits()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_setup_with_custom_limits_overrides_defaults()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_stop_cancels_monitor_task()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_stop_cancels_monitor_task_and_idempotent()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_subagent_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_system_resource_monitoring_alerts_after_debounce()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_usage_stats()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_window_expiry_resets_usage()]] - code - gateway/tests/test_resource_guard.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[A single over-threshold sample followed by an under-threshold sample is…]] - rationale - gateway/tests/test_resource_guard.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_63]] - code
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Behavior tests for ResourceGuard per-agent limit checks and VRAM pre-flight.…]] - rationale - gateway/tests/test_resource_guard_limits.py
- [[Best-effort cleanup for test contexts that don't call stop().]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded CPU time limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded disk write limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded memory limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if resource usage is allowed for an agent. Args agent_id Unique agent…]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Clean up temporary files for an agent.]] - rationale - gateway/security/resource_guard.py
- [[Configuration for resource limits.]] - rationale - gateway/security/resource_guard.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[Exception_16]] - code
- [[Get current disk IO statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get the global resource guard instance, creating it lazily on first call.]] - rationale - gateway/security/resource_guard.py
- [[Large inputs shouldn't crash prompt guard.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor and limit resource usage per agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Pre-flight VRAM headroom check before dispatching a long-context local-model…]] - rationale - gateway/security/resource_guard.py
- [[Raised when a local-model call is rejected because estimated VRAM usage would…]] - rationale - gateway/security/resource_guard.py
- [[Register a temporary file for tracking.]] - rationale - gateway/security/resource_guard.py
- [[Resource Exhaustion Guard - Security Hardening Module Monitor and limit…]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard]] - code - gateway/security/resource_guard.py
- [[ResourceGuard is instantiated at startup and reachable on app_state.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[ResourceGuard ↔ AlertDispatcher wiring tests. Covers the post-review fix where…]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[ResourceLimits]] - code - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[Setup resource guard with custom limits.]] - rationale - gateway/security/resource_guard.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Start background monitoring task.]] - rationale - gateway/security/resource_guard.py
- [[Start tracking resources for a specific agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring task cleanly.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring.]] - rationale - gateway/security/resource_guard.py
- [[Sustained high CPU fires the alert after debounce samples are crossed.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test ResourceGuardConfig dataclass.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test handling of invalid resource types.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test request count per minute limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test resource limits and DoS prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[Test temp file count limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that different agents have isolated resource tracking.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage over limits is blocked.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage resets after time window.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage under limits passes.]] - rationale - gateway/tests/test_resource_guard.py
- [[TestExpiredUsageCleanup]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestGlobalAccessor]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestResourceGuard]] - code - gateway/tests/test_resource_guard.py
- [[TestResourceGuardFailClosed]] - code - gateway/tests/test_round2_hardening.py
- [[TestResourceGuardLifecycle]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceGuardWiring]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceProtection]] - code - gateway/tests/test_security_audit.py
- [[TestTempFiles]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestVramHeadroom]] - code - gateway/tests/test_resource_guard_limits.py
- [[Tests for Resource Exhaustion Guard]] - rationale - gateway/tests/test_resource_guard.py
- [[The lifespan must stop the background monitor task on shutdown.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError]] - code - gateway/security/resource_guard.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Verify resource check methods return False (deny) on exception.]] - rationale - gateway/tests/test_round2_hardening.py
- [[asyncio_62]] - code
- [[asyncio_63]] - code
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[fixture_105]] - code
- [[get_resource_guard()]] - code - gateway/security/resource_guard.py
- [[guard()_4]] - code - gateway/tests/test_resource_guard_limits.py
- [[patch_7]] - code
- [[resource_guard.py]] - code - gateway/security/resource_guard.py
- [[setup_resource_guard()]] - code - gateway/security/resource_guard.py
- [[stop() should cancel background monitor cleanly.]] - rationale - gateway/tests/test_resource_guard.py
- [[t_resource()]] - code - gateway/ingest_api/main.py
- [[test_resource_guard.py]] - code - gateway/tests/test_resource_guard.py
- [[test_resource_guard_limits.py]] - code - gateway/tests/test_resource_guard_limits.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_wiring.py]] - code - gateway/tests/test_resource_guard_wiring.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_LLMProxy]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_TestResourceGuardAlertBridge]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_patch_1]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_TestAuth_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[ResourceGuard]] - degree 59, connects to 7 communities
- [[ResourceLimits]] - degree 29, connects to 4 communities
- [[TestResourceProtection]] - degree 16, connects to 4 communities
- [[resource_guard.py]] - degree 11, connects to 2 communities
- [[setup_resource_guard()]] - degree 9, connects to 2 communities
