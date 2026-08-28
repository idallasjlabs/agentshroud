---
type: community
cohesion: 0.33
members: 6
---

# Community 1125

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1125
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]

## Top bridge nodes
- [[TestErrorHandling]] - degree 5, connects to 2 communities