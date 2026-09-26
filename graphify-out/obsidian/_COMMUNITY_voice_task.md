---
type: community
cohesion: 0.10
members: 26
---

# voice_task

**Cohesion:** 0.10 - loosely connected
**Members:** 26 nodes

## Members
- [[.test_cpu_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_disk_write_limit()]] - code - gateway/tests/test_security_audit.py
- [[.test_memory_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_resource_guard_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_setup_resource_guard_returns_real_guard_with_default_limits()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[.test_setup_with_custom_limits_overrides_defaults()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[.test_stop_cancels_monitor_task_and_idempotent()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[.test_usage_stats()]] - code - gateway/tests/test_security_audit.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB headr]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Configuration for resource limits.]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard is instantiated at startup and reachable on app_state.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[ResourceLimits]] - code - gateway/security/resource_guard.py
- [[Setup resource guard with custom limits.]] - rationale - gateway/security/resource_guard.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[TestResourceGuardLifecycle]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceGuardWiring]] - code - gateway/tests/test_resource_guard_wiring.py
- [[The lifespan must stop the background monitor task on shutdown.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[setup_resource_guard()]] - code - gateway/security/resource_guard.py
- [[test_resource_guard.py]] - code - gateway/tests/test_resource_guard.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_wiring.py]] - code - gateway/tests/test_resource_guard_wiring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/voice_task
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_rbac_config.py]]
- 16 edges to [[_COMMUNITY_lifespan.py]]
- 10 edges to [[_COMMUNITY_SlackSocketClient]]
- 6 edges to [[_COMMUNITY_asyncio]]
- 5 edges to [[_COMMUNITY_Quick Reference Commands]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_REPORT STRUCTURE]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_Mode B — Comprehensive review sweep]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]

## Top bridge nodes
- [[ResourceLimits]] - degree 49, connects to 10 communities
- [[setup_resource_guard()]] - degree 9, connects to 3 communities
- [[test_resource_guard_wiring.py]] - degree 8, connects to 3 communities
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - degree 4, connects to 2 communities
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - degree 4, connects to 2 communities