---
type: community
cohesion: 0.10
members: 39
---

# MCPPermissionManager

**Cohesion:** 0.10 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-_record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_permission()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig_2]] - code - gateway/proxy/mcp_config.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[config()_2]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 49 edges to [[_COMMUNITY_MCPPermissionManager]]
- 35 edges to [[_COMMUNITY_StdioConnection_1]]
- 33 edges to [[_COMMUNITY_PermissionLevel]]
- 25 edges to [[_COMMUNITY_MCPInspector]]
- 18 edges to [[_COMMUNITY_StdioConnection]]
- 17 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 12 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY_MCPAuditTrail]]
- 4 edges to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_MCPToolResult]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_5]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_6]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_7]]
- 2 edges to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_3]]

## Top bridge nodes
- [[MCPProxyConfig_2]] - degree 88, connects to 17 communities
- [[MCPServerConfig_2]] - degree 90, connects to 15 communities
- [[mcp_proxy.py]] - degree 26, connects to 12 communities
- [[proxy__init__.py]] - degree 23, connects to 7 communities
- [[mcp_config.py]] - degree 13, connects to 6 communities
