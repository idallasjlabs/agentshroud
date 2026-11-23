---
type: community
members: 11
---

# TestServiceManagerGetLogs

**Members:** 11 nodes

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
- [[asyncio_24]] - code
- [[fixture_30]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestServiceManagerGetLogs
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_socmodels.py]]

## Top bridge nodes
- [[TestServiceManagerGetLogs]] - degree 10, connects to 2 communities
- [[dot-mgr_with_engine()]] - degree 3, connects to 1 community
- [[dot-test_get_logs_no_engine_returns_empty()]] - degree 3, connects to 1 community
