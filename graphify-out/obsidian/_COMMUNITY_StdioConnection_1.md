---
type: community
cohesion: 0.50
members: 4
---

# StdioConnection

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_3]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-stop_all()]] - degree 3, connects to 1 community
- [[dot-shutdown()]] - degree 3, connects to 1 community
- [[dot-stop()_3]] - degree 2, connects to 1 community
