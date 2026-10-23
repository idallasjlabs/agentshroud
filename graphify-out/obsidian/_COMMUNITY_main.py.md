---
type: community
cohesion: 0.18
members: 13
---

# main.py

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[Attach BufferHandler to the root agentshroud logger.]] - rationale - gateway/web/dashboard_endpoints.py
- [[BufferHandler]] - code - gateway/web/dashboard_endpoints.py
- [[Live Dashboard Module Badge Icon]] - image - branding/icons/modules/live-dashboard-256x256.png
- [[Logging handler that pushes records into the LogBuffer.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Proxy statistics (requests allowedblockedflagged).]] - rationale - gateway/web/dashboard_endpoints.py
- [[SSH host connectivity status.]] - rationale - gateway/web/dashboard_endpoints.py
- [[TCP connect to port 22 to check if host is reachable.]] - rationale - gateway/web/dashboard_endpoints.py
- [[_check_host()]] - code - gateway/web/dashboard_endpoints.py
- [[_tcp_check()]] - code - gateway/web/dashboard_endpoints.py
- [[dashboard_endpoints.py]] - code - gateway/web/dashboard_endpoints.py
- [[install_log_handler()]] - code - gateway/web/dashboard_endpoints.py
- [[proxy_status()_1]] - code - gateway/web/dashboard_endpoints.py
- [[ssh_hosts()_1]] - code - gateway/web/dashboard_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mainpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_main.py (2)]]
- 2 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle) (2)]]
- 2 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle) (3)]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle) (4)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]

## Top bridge nodes
- [[dashboard_endpoints.py]] - degree 14, connects to 6 communities
- [[BufferHandler]] - degree 4, connects to 1 community
- [[_check_host()]] - degree 4, connects to 1 community
- [[ssh_hosts()_1]] - degree 4, connects to 1 community
- [[Live Dashboard Module Badge Icon]] - degree 2, connects to 1 community
