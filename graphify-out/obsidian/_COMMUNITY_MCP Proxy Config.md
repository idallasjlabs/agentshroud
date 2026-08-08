---
type: community
cohesion: 0.03
members: 111
---

# MCP Proxy Config

**Cohesion:** 0.03 - loosely connected
**Members:** 111 nodes

## Members
- [[.__ge__()]] - code - gateway/proxy/mcp_config.py
- [[.__gt__()]] - code - gateway/proxy/mcp_config.py
- [[.__init__()_27]] - code - gateway/proxy/mcp_permissions.py
- [[.__le__()]] - code - gateway/proxy/mcp_config.py
- [[.__lt__()]] - code - gateway/proxy/mcp_config.py
- [[._load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[._recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[._record_private_access_attempt()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_agent_server_access()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_all()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_rate_limit()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_parameters()]] - code - gateway/proxy/mcp_permissions.py
- [[.check_tool_permission()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[.highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[.infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.level_value()]] - code - gateway/proxy/mcp_config.py
- [[.record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[.set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.test_admin_ge_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_all_pass()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_high()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_low()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_combined_blocks_private_data_parameter()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_trust_is_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_execute_lt_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_explicit_config()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_full_access()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_level_values()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
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
- [[.test_write_lt_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[EnhancedApprovalQueue_1]] - code - gateway/proxy/mcp_proxy.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel]] - code - gateway/proxy/mcp_config.py
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
- [[TestCheckAll]] - code - gateway/tests/test_mcp_permissions.py
- [[TestInferPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[TestPermissionLevel]] - code - gateway/tests/test_mcp_permissions.py
- [[TestRateLimiting_1]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustLevels]] - code - gateway/tests/test_mcp_permissions.py
- [[TestTrustMapping]] - code - gateway/tests/test_mcp_permissions.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[__init__.py_7]] - code - gateway/proxy/__init__.py
- [[config()_2]] - code - gateway/tests/test_mcp_permissions.py
- [[mcp_config.py]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[mgr()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_permissions.py]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Proxy_Config
SORT file.name ASC
```

## Connections to other communities
- 102 edges to [[_COMMUNITY_Gateway Test Suite]]
- 86 edges to [[_COMMUNITY_Gateway Test Suite]]
- 16 edges to [[_COMMUNITY_Gateway Test Suite]]
- 14 edges to [[_COMMUNITY_Auth & Exception Types]]
- 14 edges to [[_COMMUNITY_Gateway Proxy Layer]]
- 11 edges to [[_COMMUNITY_Gateway Test Suite]]
- 8 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 6 edges to [[_COMMUNITY_Gateway Test Suite]]
- 5 edges to [[_COMMUNITY_Gateway Proxy Layer]]
- 5 edges to [[_COMMUNITY_Gateway Proxy Layer]]
- 5 edges to [[_COMMUNITY_Forward Routing & Approval]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Enhanced Approval Queue]]
- 1 edge to [[_COMMUNITY_Approval Queue Tests]]
- 1 edge to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 1 edge to [[_COMMUNITY_SOC Dashboard]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 100, connects to 13 communities
- [[MCPProxyConfig]] - degree 87, connects to 13 communities
- [[PermissionLevel]] - degree 71, connects to 13 communities
- [[mcp_proxy.py]] - degree 27, connects to 9 communities
- [[ProxyResult]] - degree 18, connects to 7 communities