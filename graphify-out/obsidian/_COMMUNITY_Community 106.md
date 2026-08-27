---
type: community
members: 104
---

# Community 106

**Members:** 104 nodes

## Members
- [[.__init__()_27]] - code - gateway/proxy/mcp_permissions.py
- [[.__init__()_31]] - code - gateway/proxy/mcp_proxy.py
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
- [[.record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[.set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.test_all_pass()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clamp_high()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clamp_low()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_combined_blocks_private_data_parameter()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_default_trust_is_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_full_access()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_no_limit_always_allowed()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_permission_denied()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_rate_limit_per_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_server_denied_stops_early()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_set_and_get()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_0_read_only()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_1_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_2_execute()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_trust_3_admin()]] - code - gateway/tests/test_mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call.          Returns allowed=True and]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool.          Default-allow only blocks]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[EnhancedApprovalQueue_1]] - code - gateway/proxy/mcp_proxy.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPProxyConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls.      Default-allow philosophy tools wor]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[ProxyResult]] - code - gateway/proxy/mcp_proxy.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of a permission check.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of proxying an MCP tool call.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestCheckAll]] - code - gateway/tests/test_mcp_permissions.py
- [[TestProxyInterception]] - code - gateway/tests/test_mcp_proxy.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_mcp_permissions.py
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
- [[mgr()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_permissions.py]] - code - gateway/tests/test_mcp_permissions.py
- [[test_mcp_proxy_endpoint.py]] - code - gateway/tests/test_mcp_proxy_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_106
SORT file.name ASC
```

## Connections to other communities
- 130 edges to [[_COMMUNITY_Community 36]]
- 58 edges to [[_COMMUNITY_Community 1339]]
- 31 edges to [[_COMMUNITY_Community 179]]
- 21 edges to [[_COMMUNITY_Community 1540]]
- 19 edges to [[_COMMUNITY_Community 201]]
- 16 edges to [[_COMMUNITY_Community 283]]
- 11 edges to [[_COMMUNITY_Community 15]]
- 6 edges to [[_COMMUNITY_Community 447]]
- 6 edges to [[_COMMUNITY_Community 325]]
- 5 edges to [[_COMMUNITY_Community 1]]
- 4 edges to [[_COMMUNITY_Community 6]]
- 3 edges to [[_COMMUNITY_Community 67]]
- 3 edges to [[_COMMUNITY_Community 774]]
- 3 edges to [[_COMMUNITY_Community 952]]
- 3 edges to [[_COMMUNITY_Community 1012]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 251]]
- 2 edges to [[_COMMUNITY_Community 452]]
- 1 edge to [[_COMMUNITY_Community 78]]
- 1 edge to [[_COMMUNITY_Community 623]]
- 1 edge to [[_COMMUNITY_Community 374]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 79]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 487]]
- 1 edge to [[_COMMUNITY_Community 818]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 102, connects to 13 communities
- [[MCPProxyConfig]] - degree 88, connects to 13 communities
- [[MCPServerConfig]] - degree 90, connects to 11 communities
- [[mcp_proxy.py]] - degree 27, connects to 10 communities
- [[__init__.py_7]] - degree 24, connects to 6 communities