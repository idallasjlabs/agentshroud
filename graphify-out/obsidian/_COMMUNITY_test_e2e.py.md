---
type: community
cohesion: 0.20
members: 10
---

# test_e2e.py

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[AsyncClient]] - code - gateway/proxy/collaborator_greeter.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[client()_12]] - code - gateway/tests/test_dashboard.py
- [[client()_13]] - code - gateway/tests/test_dashboard_endpoints.py
- [[client()_14]] - code - gateway/tests/test_e2e.py
- [[client()_15]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[client()_16]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[client()_17]] - code - gateway/tests/test_security_fixes.py
- [[client()_18]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[client()_19]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2epy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_collaborator_greeter.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[AsyncClient]] - degree 10, connects to 1 community
- [[client()_14]] - degree 3, connects to 1 community
- [[client()_12]] - degree 2, connects to 1 community
- [[client()_13]] - degree 2, connects to 1 community
- [[client()_15]] - degree 2, connects to 1 community
