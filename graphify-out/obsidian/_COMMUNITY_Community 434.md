---
type: community
members: 26
---

# Community 434

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
TABLE source_file, type FROM #community/Community_434
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 5]]
- 10 edges to [[_COMMUNITY_Community 2324]]
- 9 edges to [[_COMMUNITY_Community 0]]
- 6 edges to [[_COMMUNITY_Community 431]]
- 5 edges to [[_COMMUNITY_Community 208]]
- 5 edges to [[_COMMUNITY_Community 479]]
- 3 edges to [[_COMMUNITY_Community 1945]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 506]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 2049]]
- 1 edge to [[_COMMUNITY_Community 2004]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 509]]

## Top bridge nodes
- [[ResourceLimits]] - degree 51, connects to 14 communities
- [[setup_resource_guard()]] - degree 9, connects to 3 communities
- [[test_resource_guard_wiring.py]] - degree 7, connects to 2 communities
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - degree 4, connects to 2 communities
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - degree 4, connects to 2 communities