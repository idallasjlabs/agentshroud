---
type: community
cohesion: 0.14
members: 8
---

# MCPPermissionManager

**Cohesion:** 0.14 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-set_event_bus()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_1]] - code - gateway/proxy/mcp_proxy.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-get_privacy_policy_status()]] - degree 2, connects to 1 community
- [[dot-get_private_data_patterns()]] - degree 2, connects to 1 community
- [[dot-set_event_bus()]] - degree 2, connects to 1 community
- [[dot-stop()_1]] - degree 2, connects to 1 community
