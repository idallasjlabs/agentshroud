---
type: community
cohesion: 0.25
members: 8
---

# TestForwardEndpoint

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_forward_middleware_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_forward_middleware_blocking()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_forward_middleware_error_handling()]] - code - gateway/tests/test_main_endpoints.py
- [[Test forward endpoint with middleware integration.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware allows requests when they pass checks.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware can block requests with HTTP 403.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware errors cause requests to be blocked.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestForwardEndpoint]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestForwardEndpoint
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[TestForwardEndpoint]] - degree 6, connects to 2 communities
- [[.test_forward_middleware_blocking()]] - degree 4, connects to 2 communities
- [[.test_forward_middleware_error_handling()]] - degree 4, connects to 2 communities