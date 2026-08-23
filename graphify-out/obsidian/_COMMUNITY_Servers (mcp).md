---
type: community
cohesion: 1.00
members: 2
---

# Servers (mcp)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Rationale agentshroud-gateway MCP server disabled (no mcp route, crash-loop correlation)]] - rationale - docker/config/openclaw/mcp/servers.json
- [[openclaw mcpservers.json (MCP server definitions)]] - document - docker/config/openclaw/mcp/servers.json

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Servers_mcp
SORT file.name ASC
```
