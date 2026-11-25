---
type: community
members: 23
---

# PermissionCheck

**Members:** 23 nodes

## Members
- [[dot-_record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_permission()_2]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call. Returns allowed=True and…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool. Default-allow only blocks if trust…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name. Checks explicit…]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of a permission check.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[_walk()]] - code - gateway/proxy/mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PermissionCheck
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_MCPServerConfig]]

## Top bridge nodes
- [[dot-infer_permission_level()]] - degree 5, connects to 3 communities
- [[PermissionCheck]] - degree 9, connects to 2 communities
- [[dot-check_all()]] - degree 7, connects to 1 community
- [[dot-check_tool_parameters()]] - degree 7, connects to 1 community
- [[dot-check_tool_permission()_2]] - degree 7, connects to 1 community
