---
type: community
cohesion: 0.04
members: 93
---

# Mcp Permissions

**Cohesion:** 0.04 - loosely connected
**Members:** 93 nodes

## Members
- [[.__ge__()]] - code - gateway/proxy/mcp_config.py
- [[.__gt__()]] - code - gateway/proxy/mcp_config.py
- [[.__le__()]] - code - gateway/proxy/mcp_config.py
- [[.__lt__()]] - code - gateway/proxy/mcp_config.py
- [[._record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_permission()]] - code - gateway/proxy/mcp_permissions.py
- [[.from_dict()]] - code - gateway/proxy/mcp_config.py
- [[.get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.level_value()]] - code - gateway/proxy/mcp_config.py
- [[.test_admin_ge_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_all_pass()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_allowed_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_high()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_low()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_combined_blocks_private_data_parameter()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_trust_is_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_denied_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_disabled_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_execute_lt_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_explicit_config()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_full_access()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_level_values()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_not_in_allowlist()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_delete()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_list()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pattern_sensitive()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_permission_denied()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_per_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_le_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_read_lt_write()]] - code - gateway/tests/test_mcp_permissions.py
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
- [[Any_16]] - code - gateway/proxy/mcp_config.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_config.py
- [[Parse config from a dictionary (e.g. loaded from YAML).]] - rationale - gateway/proxy/mcp_config.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel]] - code - gateway/proxy/mcp_config.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestCheckAll]] - code - gateway/tests/test_mcp_permissions.py
- [[TestInferPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[TestPermissionLevel]] - code - gateway/tests/test_mcp_permissions.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_mcp_permissions.py
- [[TestServerAccess]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustLevels]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustMapping]] - code - gateway/tests/test_mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[__init__.py_7]] - code - gateway/proxy/__init__.py
- [[config()_2]] - code - gateway/tests/test_mcp_permissions.py
- [[config()_3]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[test_mcp_permissions.py]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mcp_Permissions
SORT file.name ASC
```

## Connections to other communities
- 102 edges to [[_COMMUNITY_Mcp Proxy]]
- 44 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 33 edges to [[_COMMUNITY_Mcp Permissions (proxy)]]
- 25 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 16 edges to [[_COMMUNITY_Mcp Proxy]]
- 14 edges to [[_COMMUNITY_Mcp Inspector (proxy)]]
- 10 edges to [[_COMMUNITY_Mcp Audit (proxy)]]
- 8 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 5 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 5 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 4 edges to [[_COMMUNITY_Mcp Proxy (proxy)]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 3 edges to [[_COMMUNITY_Mcp Proxy]]
- 2 edges to [[_COMMUNITY_Enhanced Approval]]
- 2 edges to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 2 edges to [[_COMMUNITY_Mcp Proxy Endpoint]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]
- 1 edge to [[_COMMUNITY_Soc Egress Endpoints]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Llm Proxy]]
- 1 edge to [[_COMMUNITY_Mcp Result Endpoint]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Collaborator Greeter]]

## Top bridge nodes
- [[mcp_proxy.py]] - degree 27, connects to 12 communities
- [[MCPProxyConfig]] - degree 88, connects to 11 communities
- [[MCPServerConfig]] - degree 90, connects to 9 communities
- [[PermissionLevel]] - degree 71, connects to 8 communities
- [[ProxyResult]] - degree 18, connects to 8 communities