---
type: community
cohesion: 0.07
members: 62
---

# MCPServerConfig

**Cohesion:** 0.07 - loosely connected
**Members:** 62 nodes

## Members
- [[.__init__()_29]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_96]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_30]] - code - gateway/proxy/mcp_proxy.py
- [[._record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_permission()_1]] - code - gateway/proxy/mcp_permissions.py
- [[.from_dict()_9]] - code - gateway/proxy/mcp_config.py
- [[.get_stats()_15]] - code - gateway/proxy/mcp_proxy.py
- [[.get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[.highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[.infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_77]] - code - gateway/proxy/mcp_config.py
- [[Any_34]] - code - gateway/proxy/mcp_proxy.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[EnhancedApprovalQueue]] - code - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[MCPAuditTrail]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector]] - code - gateway/proxy/mcp_proxy.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_3]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig_2]] - code - gateway/proxy/mcp_config.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Parse config from a dictionary (e.g. loaded from YAML).]] - rationale - gateway/proxy/mcp_config.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[config()]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPServerConfig
SORT file.name ASC
```

## Connections to other communities
- 75 edges to [[_COMMUNITY_MCPToolCall]]
- 64 edges to [[_COMMUNITY_StdioConnection]]
- 36 edges to [[_COMMUNITY_PermissionLevel]]
- 25 edges to [[_COMMUNITY_MCPPermissionManager]]
- 20 edges to [[_COMMUNITY_MCPInspector]]
- 17 edges to [[_COMMUNITY_MCPAuditTrail]]
- 15 edges to [[_COMMUNITY_MCPToolResult]]
- 14 edges to [[_COMMUNITY_FakeProcess]]
- 8 edges to [[_COMMUNITY_RBACConfig]]
- 7 edges to [[_COMMUNITY_.process_tool_call()]]
- 6 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 6 edges to [[_COMMUNITY_SSHProxy]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_Enum]]
- 3 edges to [[_COMMUNITY_TestAuditTrail]]
- 3 edges to [[_COMMUNITY_TestInjectionDetection]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_make_event()]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]
- 1 edge to [[_COMMUNITY_cls]]

## Top bridge nodes
- [[MCPProxyConfig_2]] - degree 88, connects to 13 communities
- [[MCPServerConfig_2]] - degree 90, connects to 11 communities
- [[MCPTransport]] - degree 63, connects to 11 communities
- [[mcp_proxy.py]] - degree 27, connects to 11 communities
- [[proxy__init__.py]] - degree 24, connects to 7 communities