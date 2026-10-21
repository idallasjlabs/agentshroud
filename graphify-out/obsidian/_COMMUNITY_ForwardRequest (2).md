---
type: community
members: 10
---

# ForwardRequest (2)

**Members:** 10 nodes

## Members
- [[AsyncClient]] - code - gateway/proxy/collaborator_greeter.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[client()_13]] - code - gateway/tests/test_dashboard.py
- [[client()_14]] - code - gateway/tests/test_dashboard_endpoints.py
- [[client()_15]] - code - gateway/tests/test_e2e.py
- [[client()_16]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[client()_17]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[client()_18]] - code - gateway/tests/test_security_fixes.py
- [[client()_19]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[client()_20]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ForwardRequest_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_collaborator_greeter.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[AsyncClient]] - degree 10, connects to 1 community
- [[client()_15]] - degree 3, connects to 1 community
- [[client()_13]] - degree 2, connects to 1 community
- [[client()_14]] - degree 2, connects to 1 community
- [[client()_16]] - degree 2, connects to 1 community
