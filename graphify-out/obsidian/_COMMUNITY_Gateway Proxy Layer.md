---
type: community
cohesion: 0.50
members: 4
---

# Gateway Proxy Layer

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[.stop()_3]] - code - gateway/proxy/mcp_proxy.py
- [[.stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Proxy_Layer
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[.stop_all()]] - degree 3, connects to 1 community
- [[.shutdown()]] - degree 3, connects to 1 community
- [[.stop()_3]] - degree 2, connects to 1 community