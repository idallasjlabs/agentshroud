---
type: community
cohesion: 0.04
members: 53
---

# Community 109

**Cohesion:** 0.04 - loosely connected
**Members:** 53 nodes

## Members
- [[.__init__()_27]] - code - gateway/proxy/mcp_permissions.py
- [[._load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[._recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[.get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[.record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[.set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.test_admin_allowed_at_trust_3()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_denied_at_trust_2()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_private_tool_allowed_for_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_admin_private_tool_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_exec_denied_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_memory_dot_search_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_memory_get_denied_for_non_owner()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
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
- [[.test_read_tool_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_tool_allowed_at_trust_1()]] - code - gateway/tests/test_mcp_permissions.py
- [[.test_write_tool_denied_at_trust_0()]] - code - gateway/tests/test_mcp_permissions.py
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
- [[TestProxyInterception]] - code - gateway/tests/test_mcp_proxy.py
- [[TestToolPermission]] - code - gateway/tests/test_mcp_permissions.py
- [[mgr()_1]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_109
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_Community 44]]
- 33 edges to [[_COMMUNITY_Community 39]]
- 14 edges to [[_COMMUNITY_Community 103]]
- 7 edges to [[_COMMUNITY_Community 154]]
- 6 edges to [[_COMMUNITY_Community 261]]
- 5 edges to [[_COMMUNITY_Community 206]]
- 5 edges to [[_COMMUNITY_Community 324]]
- 2 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 1 edge to [[_COMMUNITY_Community 616]]
- 1 edge to [[_COMMUNITY_Community 473]]
- 1 edge to [[_COMMUNITY_Community 917]]
- 1 edge to [[_COMMUNITY_Community 992]]

## Top bridge nodes
- [[MCPPermissionManager]] - degree 102, connects to 12 communities
- [[TestProxyInterception]] - degree 20, connects to 4 communities
- [[TestToolPermission]] - degree 27, connects to 2 communities
- [[.test_egress_allows_non_url_tool_call()]] - degree 6, connects to 2 communities
- [[.test_egress_denied_blocks_url_tool_call()]] - degree 6, connects to 2 communities