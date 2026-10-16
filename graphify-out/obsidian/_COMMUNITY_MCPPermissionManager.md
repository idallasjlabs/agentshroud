---
type: community
cohesion: 0.06
members: 78
---

# MCPPermissionManager

**Cohesion:** 0.06 - loosely connected
**Members:** 78 nodes

## Members
- [[dot-__init__()_149]] - code - gateway/proxy/mcp_permissions.py
- [[dot-__init__()_150]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_151]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_152]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_permission()_2]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_stats()_16]] - code - gateway/proxy/mcp_proxy.py
- [[dot-get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Any_61]] - code - gateway/proxy/mcp_proxy.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[EnhancedApprovalQueue_2]] - code - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/mcp_proxy.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionResult_1]] - code - gateway/proxy/mcp_inspector.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_proxy.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_3]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig_2]] - code - gateway/proxy/mcp_config.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[config()_4]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 111 edges to [[_COMMUNITY_MCPToolCall]]
- 83 edges to [[_COMMUNITY_StdioConnection]]
- 44 edges to [[_COMMUNITY_PermissionLevel]]
- 23 edges to [[_COMMUNITY_MCPToolResult]]
- 18 edges to [[_COMMUNITY_MCPAuditTrail]]
- 17 edges to [[_COMMUNITY_FakeProcess]]
- 10 edges to [[_COMMUNITY_RBACConfig]]
- 6 edges to [[_COMMUNITY_dot-process_tool_call]]
- 6 edges to [[_COMMUNITY_DataLedger]]
- 5 edges to [[_COMMUNITY_TestToolPermission]]
- 4 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 4 edges to [[_COMMUNITY_TestPIIDetection]]
- 4 edges to [[_COMMUNITY_TestExtractEgressTargets]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_TestAuditTrail]]
- 3 edges to [[_COMMUNITY_Enum]]
- 3 edges to [[_COMMUNITY_dot-inspect_tool_call]]
- 2 edges to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_AGENTSHROUD_MODE]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_agentshroud.yaml]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]

## Top bridge nodes
- [[MCPProxyConfig_3]] - degree 88, connects to 13 communities
- [[MCPPermissionManager_1]] - degree 101, connects to 12 communities
- [[MCPServerConfig_2]] - degree 90, connects to 11 communities
- [[MCPTransport]] - degree 63, connects to 11 communities
- [[mcp_proxy.py]] - degree 26, connects to 8 communities
