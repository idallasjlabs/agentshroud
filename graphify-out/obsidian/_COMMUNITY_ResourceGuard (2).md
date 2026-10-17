---
type: community
members: 23
---

# ResourceGuard (2)

**Members:** 23 nodes

## Members
- [[dot-setup_method()_23]] - code - gateway/tests/test_resource_guard.py
- [[dot-teardown_method()_5]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_brief_spike_below_debounce_does_not_alert()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_resource_over_limit_blocked()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_resource_temp_files_limit()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_check_resource_under_limit_passes()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_invalid_resource_type()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_multiple_agents_isolated()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_request_count_limiting()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_resource_guard_config()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_system_resource_monitoring_alerts_after_debounce()]] - code - gateway/tests/test_resource_guard.py
- [[dot-test_window_expiry_resets_usage()]] - code - gateway/tests/test_resource_guard.py
- [[A single over-threshold sample followed by an under-threshold sample is suppress]] - rationale - gateway/tests/test_resource_guard.py
- [[Sustained high CPU fires the alert after debounce samples are crossed.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test ResourceGuardConfig dataclass.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test handling of invalid resource types.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test request count per minute limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test temp file count limiting.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that different agents have isolated resource tracking.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage over limits is blocked.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage resets after time window.]] - rationale - gateway/tests/test_resource_guard.py
- [[Test that resource usage under limits passes.]] - rationale - gateway/tests/test_resource_guard.py
- [[TestResourceGuard]] - code - gateway/tests/test_resource_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard_2
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_AlertDispatcher (2)]]

## Top bridge nodes
- [[TestResourceGuard]] - degree 16, connects to 1 community
- [[dot-setup_method()_23]] - degree 3, connects to 1 community
- [[dot-test_resource_guard_config()]] - degree 3, connects to 1 community
