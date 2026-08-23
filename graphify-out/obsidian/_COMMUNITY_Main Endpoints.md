---
type: community
cohesion: 0.50
members: 4
---

# Main Endpoints

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[Test mcpproxy endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Main_Endpoints
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[TestMCPProxyEndpoint]] - degree 4, connects to 2 communities
- [[.test_mcp_proxy_endpoint()]] - degree 3, connects to 1 community