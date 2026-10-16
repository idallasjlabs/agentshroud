---
type: community
cohesion: 0.50
members: 4
---

# StdioConnection

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-send_request()]] - degree 4, connects to 1 community
- [[dot-start()_1]] - degree 3, connects to 1 community
