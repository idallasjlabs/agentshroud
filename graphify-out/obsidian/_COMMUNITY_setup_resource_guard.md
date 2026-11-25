---
type: community
members: 12
---

# setup_resource_guard

**Members:** 12 nodes

## Members
- [[dot-test_setup_resource_guard_returns_real_guard_with_default_limits()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_setup_with_custom_limits_overrides_defaults()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[dot-test_stop_cancels_monitor_task_and_idempotent()]] - code - gateway/tests/test_resource_guard_wiring.py
- [[ResourceGuard is instantiated at startup and reachable on app_state.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[ResourceGuard ↔ AlertDispatcher wiring tests. Covers the post-review fix where…]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[Setup resource guard with custom limits.]] - rationale - gateway/security/resource_guard.py
- [[TestResourceGuardLifecycle]] - code - gateway/tests/test_resource_guard_wiring.py
- [[TestResourceGuardWiring]] - code - gateway/tests/test_resource_guard_wiring.py
- [[The lifespan must stop the background monitor task on shutdown.]] - rationale - gateway/tests/test_resource_guard_wiring.py
- [[asyncio_12]] - code
- [[setup_resource_guard()]] - code - gateway/security/resource_guard.py
- [[test_resource_guard_wiring.py]] - code - gateway/tests/test_resource_guard_wiring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/setup_resource_guard
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_TestResourceGuardAlertBridge]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[setup_resource_guard()]] - degree 9, connects to 3 communities
- [[test_resource_guard_wiring.py]] - degree 7, connects to 2 communities
- [[TestResourceGuardWiring]] - degree 6, connects to 1 community
- [[TestResourceGuardLifecycle]] - degree 5, connects to 1 community
- [[dot-test_setup_with_custom_limits_overrides_defaults()]] - degree 3, connects to 1 community
