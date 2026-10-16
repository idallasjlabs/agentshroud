---
type: community
cohesion: 0.33
members: 6
---

# TestGoogleAPIProxy

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestGoogleAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]

## Top bridge nodes
- [[TestGoogleAPIProxy]] - degree 4, connects to 1 community
