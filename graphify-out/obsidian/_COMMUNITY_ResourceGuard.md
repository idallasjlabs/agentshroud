---
type: community
members: 62
---

# ResourceGuard

**Members:** 62 nodes

## Members
- [[dot-__del__()]] - code - gateway/security/resource_guard.py
- [[dot-__init__()_151]] - code - gateway/security/resource_guard.py
- [[dot-_start_monitoring_task()]] - code - gateway/security/resource_guard.py
- [[dot-check_cpu_limit()]] - code - gateway/security/resource_guard.py
- [[dot-check_memory_limit()]] - code - gateway/security/resource_guard.py
- [[dot-check_resource()]] - code - gateway/security/resource_guard.py
- [[dot-cleanup_temp_files()]] - code - gateway/security/resource_guard.py
- [[dot-register_temp_file()]] - code - gateway/security/resource_guard.py
- [[dot-setup_method()_26]] - code - gateway/tests/test_resource_guard.py
- [[dot-start_request_tracking()]] - code - gateway/security/resource_guard.py
- [[dot-stop()_8]] - code - gateway/security/resource_guard.py
- [[dot-stop_monitoring()]] - code - gateway/security/resource_guard.py
- [[dot-test_check_cpu_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_check_disk_write_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_check_memory_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_cpu_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_disk_write_limit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_get_resource_guard_is_lazy_singleton()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_memory_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_resource_guard_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_subagent_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_usage_stats()]] - code - gateway/tests/test_security_audit.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Behavior tests for ResourceGuard per-agent limit checks and VRAM pre-flight.…]] - rationale - gateway/tests/test_resource_guard_limits.py
- [[Best-effort cleanup for test contexts that don't call stop().]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded CPU time limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded memory limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if resource usage is allowed for an agent. Args agent_id Unique agent…]] - rationale - gateway/security/resource_guard.py
- [[Clean up temporary files for an agent.]] - rationale - gateway/security/resource_guard.py
- [[Configuration for resource limits.]] - rationale - gateway/security/resource_guard.py
- [[Get the global resource guard instance, creating it lazily on first call.]] - rationale - gateway/security/resource_guard.py
- [[Large inputs shouldn't crash prompt guard.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor and limit resource usage per agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Register a temporary file for tracking.]] - rationale - gateway/security/resource_guard.py
- [[Resource Exhaustion Guard - Security Hardening Module Monitor and limit…]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard]] - code - gateway/security/resource_guard.py
- [[ResourceLimits]] - code - gateway/security/resource_guard.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Start background monitoring task.]] - rationale - gateway/security/resource_guard.py
- [[Start tracking resources for a specific agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring task cleanly.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring.]] - rationale - gateway/security/resource_guard.py
- [[Test resource limits and DoS prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[TestGlobalAccessor]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestResourceGuardFailClosed]] - code - gateway/tests/test_round2_hardening.py
- [[TestResourceProtection]] - code - gateway/tests/test_security_audit.py
- [[Tests for Resource Exhaustion Guard]] - rationale - gateway/tests/test_resource_guard.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Verify resource check methods return False (deny) on exception.]] - rationale - gateway/tests/test_round2_hardening.py
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[fixture_105]] - code
- [[get_resource_guard()]] - code - gateway/security/resource_guard.py
- [[guard()_4]] - code - gateway/tests/test_resource_guard_limits.py
- [[resource_guard.py]] - code - gateway/security/resource_guard.py
- [[t_resource()]] - code - gateway/ingest_api/main.py
- [[test_resource_guard.py]] - code - gateway/tests/test_resource_guard.py
- [[test_resource_guard_limits.py]] - code - gateway/tests/test_resource_guard_limits.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_dot-_get_disk_io_stats]]
- 10 edges to [[_COMMUNITY_setup_resource_guard]]
- 7 edges to [[_COMMUNITY_TestResourceGuard]]
- 7 edges to [[_COMMUNITY_LLMProxy]]
- 6 edges to [[_COMMUNITY_VRAMHeadroomError]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_patch_1]]
- 2 edges to [[_COMMUNITY_TestResourceGuardAlertBridge]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_Session]]
- 1 edge to [[_COMMUNITY_TestTempFiles]]
- 1 edge to [[_COMMUNITY_TestExpiredUsageCleanup]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]

## Top bridge nodes
- [[ResourceGuard]] - degree 59, connects to 12 communities
- [[ResourceLimits]] - degree 29, connects to 6 communities
- [[resource_guard.py]] - degree 11, connects to 5 communities
- [[TestResourceProtection]] - degree 16, connects to 4 communities
- [[test_resource_guard_limits.py]] - degree 13, connects to 4 communities
