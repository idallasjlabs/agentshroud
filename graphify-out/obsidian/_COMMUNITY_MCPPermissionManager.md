---
type: community
members: 71
---

# MCPPermissionManager

**Members:** 71 nodes

## Members
- [[dot-__init__()_6]] - code - gateway/proxy/mcp_permissions.py
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
- [[dot-get_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
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
- [[Audit signal for blocked admin-private tool access attempts.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Block non-owner tool calls that reference admin-private data pathscontent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check and update rate limits for a tool call. Returns allowed=True and…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can access a server at all.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Check if an agent can call a specific tool. Default-allow only blocks if trust…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Get trust level, defaulting to 1 (write) for unknown agents.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name. Checks explicit…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[Manages permissions for MCP tool calls. Default-allow philosophy tools work…]] - rationale - gateway/proxy/mcp_permissions.py
- [[PermissionCheck]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateAccessAttempt]] - code - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[RateLimitEntry]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Record blocked private-tool access attempts for SOCaudit views.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Result of a permission check.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Run all permission checks in order. Returns first failure or final success.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestToolPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[Track rate limit state for a tool+agent combo.]] - rationale - gateway/proxy/mcp_permissions.py
- [[_walk()]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_permissions.py_2]] - code - gateway/proxy/mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 5 edges to [[_COMMUNITY_MCPProxy]]
- 3 edges to [[_COMMUNITY_MCPToolCall]]
- 3 edges to [[_COMMUNITY_test_mcp_proxy_coverage.py]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_MCPServerConfig]]
- 2 edges to [[_COMMUNITY_mcp_proxy.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 41, connects to 8 communities
- [[mcp_permissions.py_2]] - degree 16, connects to 8 communities
- [[PermissionCheck]] - degree 9, connects to 2 communities
- [[dot-infer_permission_level()]] - degree 5, connects to 2 communities
- [[dot-__init__()_6]] - degree 5, connects to 2 communities
