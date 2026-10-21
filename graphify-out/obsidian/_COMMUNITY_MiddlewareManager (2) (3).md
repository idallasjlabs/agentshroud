---
type: community
members: 9
---

# MiddlewareManager (2) (3)

**Members:** 9 nodes

## Members
- [[dot-mgr_with_engine()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_case_insensitive()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_empty_returns_all()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_excludes_non_matching()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_module_filter_keeps_matching_lines()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_engine_returns_empty()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_get_logs_no_filter_returns_tail()]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerGetLogs]] - code - gateway/tests/test_soc_services.py
- [[Unit tests for ServiceManager.get_logs — including module_filter behaviour.]] - rationale - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_2_3
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[TestServiceManagerGetLogs]] - degree 10, connects to 2 communities
- [[dot-mgr_with_engine()]] - degree 2, connects to 1 community
- [[dot-test_get_logs_no_engine_returns_empty()]] - degree 2, connects to 1 community
