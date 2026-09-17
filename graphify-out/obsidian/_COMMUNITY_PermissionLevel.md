---
type: community
cohesion: 0.05
members: 56
---

# PermissionLevel

**Cohesion:** 0.05 - loosely connected
**Members:** 56 nodes

## Members
- [[.__ge__()]] - code - gateway/proxy/mcp_config.py
- [[.__gt__()]] - code - gateway/proxy/mcp_config.py
- [[.__le__()]] - code - gateway/proxy/mcp_config.py
- [[.__lt__()]] - code - gateway/proxy/mcp_config.py
- [[.level_value()]] - code - gateway/proxy/mcp_config.py
- [[.test_admin_ge_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_all_pass()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_allowed_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_high()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_low()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_combined_blocks_private_data_parameter()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_trust_is_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_denied_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_disabled_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_execute_lt_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_explicit_config()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_full_access()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_level_values()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_no_patterns_returns_unchanged()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_not_in_allowlist()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_owner_bypasses_redaction()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_pattern_delete()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_list()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_sensitive()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_permission_denied()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_enforced()_2]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_per_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_le_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_lt_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_redacts_nested_dict_list_tuple()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_server_denied_stops_early()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_set_and_get()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_0_read_only()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_1_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_2_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_3_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_sufficient_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_too_low_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_unknown_server_default_allow()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_lt_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[Configuration for a specific MCP tool.]] - rationale - gateway/proxy/mcp_config.py
- [[MCPToolConfig]] - code - gateway/proxy/mcp_config.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_config.py
- [[TestCheckAll]] - code - gateway/tests/test_mcp_permissions.py
- [[TestInferPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[TestPermissionLevel]] - code - gateway/tests/test_mcp_permissions.py
- [[TestRateLimiting_4]] - code - gateway/tests/test_mcp_permissions.py
- [[TestSanitizeAdminPrivateData]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestServerAccess]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustMapping]] - code - gateway/tests/test_mcp_permissions.py
- [[config()_4]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_permissions.py]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PermissionLevel
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_StdioConnection]]
- 36 edges to [[_COMMUNITY_MCPServerConfig]]
- 34 edges to [[_COMMUNITY_MCPToolCall]]
- 14 edges to [[_COMMUNITY_MCPPermissionManager]]
- 7 edges to [[_COMMUNITY_MCPToolResult]]
- 6 edges to [[_COMMUNITY_FakeProcess]]
- 4 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 3 edges to [[_COMMUNITY_MCPAuditTrail]]
- 3 edges to [[_COMMUNITY_MCPInspector]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_TestAuditTrail]]
- 2 edges to [[_COMMUNITY_TestInjectionDetection]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]

## Top bridge nodes
- [[PermissionLevel_1]] - degree 71, connects to 12 communities
- [[MCPToolConfig]] - degree 59, connects to 11 communities
- [[TestSanitizeAdminPrivateData]] - degree 18, connects to 7 communities
- [[test_mcp_permissions.py]] - degree 17, connects to 4 communities
- [[TestServerAccess]] - degree 13, connects to 2 communities