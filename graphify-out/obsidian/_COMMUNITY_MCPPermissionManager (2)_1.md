---
type: community
cohesion: 0.08
members: 38
---

# MCPPermissionManager (2)

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_86]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-check_tool_permission()_1]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager_2
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 22 edges to [[_COMMUNITY_MCPToolCall]]
- 12 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 8 edges to [[_COMMUNITY_StdioConnection]]
- 7 edges to [[_COMMUNITY_MCPInspector]]
- 5 edges to [[_COMMUNITY_MCPToolResult]]
- 4 edges to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 4 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 3 edges to [[_COMMUNITY_ConsentFramework (2)]]
- 1 edge to [[_COMMUNITY_TestInspectorEdgeCases]]
- 1 edge to [[_COMMUNITY_TestPIIDetection]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 1 edge to [[_COMMUNITY_Egress Filter Errors]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 101, connects to 13 communities
- [[PermissionCheck]] - degree 12, connects to 3 communities
- [[dot-__init__()_86]] - degree 5, connects to 2 communities
- [[dot-check_tool_permission()_1]] - degree 7, connects to 1 community
- [[dot-check_rate_limit()]] - degree 5, connects to 1 community
