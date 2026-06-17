---
type: community
cohesion: 0.03
members: 88
---

# MCP Permissions Manager

**Cohesion:** 0.03 - loosely connected
**Members:** 88 nodes

## Members
- [[.__init__()_19]] - code - gateway/proxy/mcp_permissions.py
- [[._load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[._recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.test_admin_allowed_at_trust_3()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_denied_at_trust_2()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_ge_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_private_tool_allowed_for_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_private_tool_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_all_pass()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_allowed_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_high()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_low()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_combined_blocks_private_data_parameter()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_trust_is_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_denied_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_disabled_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_exec_denied_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_execute_lt_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_explicit_config()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_full_access()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_level_values()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_memory_dot_search_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_memory_get_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_not_in_allowlist()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_delete()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_list()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_sensitive()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_permission_denied()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_privacy_policy_overrides_patterns()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_privacy_policy_status_when_missing_file()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_allowed_for_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_agentshroud_memory_subpath()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_gateway_contributor_logs()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_memory_subpath()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_nested_private_reference()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_session_store_path()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_data_parameter_denied_for_workspace_contributor_logs()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_private_redaction_event_summary()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_enforced()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_per_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_le_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_lt_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_tool_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_server_denied_stops_early()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_set_and_get()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_0_read_only()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_1_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_2_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_3_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_sufficient_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_too_low_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_unknown_server_default_allow()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_lt_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_tool_allowed_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_tool_denied_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestCheckAll]] - code - gateway/tests/test_mcp_permissions.py
- [[TestInferPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[TestPermissionLevel]] - code - gateway/tests/test_mcp_permissions.py
- [[TestRateLimiting_1]] - code - gateway/tests/test_mcp_permissions.py
- [[TestServerAccess]] - code - gateway/tests/test_mcp_permissions.py
- [[TestToolPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustLevels]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustMapping]] - code - gateway/tests/test_mcp_permissions.py
- [[mgr()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_permissions.py]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Permissions_Manager
SORT file.name ASC
```

## Connections to other communities
- 56 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 15 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 15 edges to [[_COMMUNITY_Module Group 154]]
- 15 edges to [[_COMMUNITY_Module Group 78]]
- 6 edges to [[_COMMUNITY_Module Group 124]]
- 3 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 3 edges to [[_COMMUNITY_Module Group 266]]
- 1 edge to [[_COMMUNITY_Module Group 205]]
- 1 edge to [[_COMMUNITY_Module Group 387]]
- 1 edge to [[_COMMUNITY_Module Group 139]]
- 1 edge to [[_COMMUNITY_Module Group 442]]
- 1 edge to [[_COMMUNITY_Module Group 468]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 99, connects to 12 communities
- [[MCPProxyConfig_1]] - degree 5, connects to 3 communities
- [[TestToolPermission]] - degree 27, connects to 2 communities
- [[test_mcp_permissions.py]] - degree 15, connects to 2 communities
- [[TestServerAccess]] - degree 13, connects to 2 communities