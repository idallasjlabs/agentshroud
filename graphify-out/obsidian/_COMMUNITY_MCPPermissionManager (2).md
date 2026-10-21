---
type: community
members: 45
---

# MCPPermissionManager (2)

**Members:** 45 nodes

## Members
- [[dot-__init__()_68]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-test_admin_allowed_at_trust_3()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_admin_denied_at_trust_2()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_admin_private_tool_allowed_for_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_admin_private_tool_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_exec_denied_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_memory_dot_search_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_memory_get_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_privacy_policy_overrides_patterns()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_privacy_policy_status_when_missing_file()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_allowed_for_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_agentshroud_memory_subpath()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_gateway_contributor_logs()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_memory_subpath()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_nested_private_reference()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_session_store_path()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_data_parameter_denied_for_workspace_contributor_logs()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_private_redaction_event_summary()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_read_tool_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_write_tool_allowed_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_write_tool_denied_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestToolPermission]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager_2
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_MCPPermissionManager]]
- 17 edges to [[_COMMUNITY_MCPPermissionManager (3)]]
- 13 edges to [[_COMMUNITY_PermissionLevel]]
- 12 edges to [[_COMMUNITY_StdioConnection]]
- 10 edges to [[_COMMUNITY_StdioConnection (2)]]
- 7 edges to [[_COMMUNITY_MCPInspector]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager (4)]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (5)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (6)]]
- 1 edge to [[_COMMUNITY_Athena — Knowledge Distiller (4)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (7)]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 101, connects to 16 communities
- [[TestToolPermission]] - degree 27, connects to 2 communities
- [[dot-__init__()_68]] - degree 5, connects to 2 communities
- [[dot-record_private_data_redaction()]] - degree 3, connects to 1 community
