---
type: community
cohesion: 0.07
members: 52
---

# Module Group 78

**Cohesion:** 0.07 - loosely connected
**Members:** 52 nodes

## Members
- [[.__post_init__()]] - code - gateway/proxy/mcp_proxy.py
- [[.mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.set_event_bus()]] - code - gateway/proxy/mcp_proxy.py
- [[.test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_chain_includes_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_chain_valid_after_calls()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_elevated_agent_can_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_data_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_mixed_allowed_blocked_chain()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_owner_bypass()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_passthrough_allows_everything()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_passthrough_still_audits()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_tool_violation_emits_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_read_only_agent_can_read()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_read_only_agent_denied_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_session_store_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_stats_blocked_counted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_stats_tracking()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_unknown_server_default_allow()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_workspace_contributor_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[MCPProxy]] - code - gateway/proxy/mcp_proxy.py
- [[MCPToolCall]] - code - gateway/proxy/mcp_proxy.py
- [[Main MCP proxy that intercepts tool calls and routes through security.      Tran]] - rationale - gateway/proxy/mcp_proxy.py
- [[Mix of allowed, blocked, and result entries all in one chain.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Represents an MCP tool_use request.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestAllowDenyList]] - code - gateway/tests/test_mcp_proxy.py
- [[TestChainIntegrityMultiple]] - code - gateway/tests/test_mcp_proxy.py
- [[TestHashChainIntegration]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPassthroughMode]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPrivacyPolicyEvents]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyInterception]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyPermissions]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyRateLimiting]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyStats]] - code - gateway/tests/test_mcp_proxy.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[passthrough_proxy()]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_78
SORT file.name ASC
```

## Connections to other communities
- 97 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 36 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 19 edges to [[_COMMUNITY_Module Group 139]]
- 18 edges to [[_COMMUNITY_Module Group 266]]
- 16 edges to [[_COMMUNITY_Module Group 154]]
- 15 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 13 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 12 edges to [[_COMMUNITY_Module Group 124]]
- 10 edges to [[_COMMUNITY_Module Group 205]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 3 edges to [[_COMMUNITY_Module Group 387]]
- 3 edges to [[_COMMUNITY_Module Group 442]]
- 3 edges to [[_COMMUNITY_Module Group 468]]
- 1 edge to [[_COMMUNITY_Module Group 546]]

## Top bridge nodes
- [[MCPProxy]] - degree 78, connects to 15 communities
- [[MCPToolCall]] - degree 89, connects to 13 communities
- [[test_mcp_proxy.py]] - degree 40, connects to 9 communities
- [[TestProxyInterception]] - degree 20, connects to 6 communities
- [[TestPrivacyPolicyEvents]] - degree 19, connects to 6 communities
