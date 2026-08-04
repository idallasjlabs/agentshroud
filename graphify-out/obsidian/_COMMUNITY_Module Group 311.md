---
type: community
cohesion: 0.15
members: 13
---

# Module Group 311

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[._get_client()]] - code - gateway/proxy/collaborator_greeter.py
- [[._persist_state()]] - code - gateway/proxy/collaborator_greeter.py
- [[.maybe_greet()]] - code - gateway/proxy/collaborator_greeter.py
- [[AsyncClient]] - code - gateway/proxy/collaborator_greeter.py
- [[Greet user if cooldown has expired. Returns True when greeting was sent.]] - rationale - gateway/proxy/collaborator_greeter.py
- [[client()_2]] - code - gateway/tests/test_dashboard.py
- [[client()_3]] - code - gateway/tests/test_dashboard_endpoints.py
- [[client()_6]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[client()_7]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[client()_10]] - code - gateway/tests/test_security_fixes.py
- [[client()_11]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[client()_12]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_311
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 136]]
- 1 edge to [[_COMMUNITY_Module Group 272]]
- 1 edge to [[_COMMUNITY_MCP Inspector & Audit]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_Module Group 166]]
- 1 edge to [[_COMMUNITY_Module Group 232]]
- 1 edge to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 1 edge to [[_COMMUNITY_Module Group 132]]
- 1 edge to [[_COMMUNITY_Module Group 171]]
- 1 edge to [[_COMMUNITY_SOC Router Tests]]

## Top bridge nodes
- [[AsyncClient]] - degree 10, connects to 2 communities
- [[test_mcp_proxy_endpoint.py]] - degree 3, connects to 2 communities
- [[.maybe_greet()]] - degree 4, connects to 1 community
- [[._get_client()]] - degree 3, connects to 1 community
- [[._persist_state()]] - degree 2, connects to 1 community
