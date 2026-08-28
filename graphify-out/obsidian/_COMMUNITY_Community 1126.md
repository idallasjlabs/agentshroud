---
type: community
cohesion: 0.33
members: 6
---

# Community 1126

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1126
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]

## Top bridge nodes
- [[TestGoogleAPIProxy]] - degree 5, connects to 2 communities
- [[.test_google_proxy_json_body_passthrough()]] - degree 3, connects to 1 community
- [[.test_google_proxy_non_json_body_passthrough()]] - degree 3, connects to 1 community