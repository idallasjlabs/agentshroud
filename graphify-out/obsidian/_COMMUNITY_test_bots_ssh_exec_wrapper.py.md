---
type: community
cohesion: 0.10
members: 51
---

# test_bots_ssh_exec_wrapper.py

**Cohesion:** 0.10 - loosely connected
**Members:** 51 nodes

## Members
- [[dot-__init__()_48]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_49]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_item()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-remove()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-submit_tool_request()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_approved_decision_allows()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_async_egress_filter_deny_uses_rule_as_reason()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_denied_decision_blocks_with_item_status()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_denied_decision_with_missing_item_defaults_denied()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_egress_filter_allow_passes_through()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_emit_swallows_bus_errors()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_emits_event_to_bus()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_execution_redacts_admin_private_content()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_execution_with_none_content_skips_result_inspection()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_generic_exception()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_get_or_create_by_transport_and_caching()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_get_stats_after_allowed_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_get_stats_zero_and_after_calls()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_no_patterns_returns_unchanged()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_no_queue_allows_by_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_owner_bypasses_redaction()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_process_tool_call_blocks_on_denial()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_process_tool_result_handles_none_content()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_process_tool_result_redacts_private_data()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_redacts_nested_dict_list_tuple()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_sanitized_params_preferred_over_originals()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_server_error_response()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_server_error_response_without_message()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_shutdown_stops_all_connections()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_stop_all_clears_pool()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_successful_execution_with_result_inspection()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_sync_egress_filter_deny_blocks()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_timeout_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_tool_not_requiring_approval_allowed()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_unknown_server_returns_error_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-wait_for_decision()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[ConnectionPool]] - code - gateway/proxy/mcp_proxy.py
- [[FakeApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeConn]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Pool of connections to MCP servers.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in connection injected into the proxy's pool.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[TestApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestConnectionPool]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEgressFilterPaths]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEmitPrivacyEvent]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExecuteToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestResultProcessingAndLifecycle]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestSanitizeAdminPrivateData]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_proxy()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[test_mcp_proxy_coverage.py]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_bots_ssh_exec_wrapperpy
SORT file.name ASC
```

## Connections to other communities
- 53 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 34 edges to [[_COMMUNITY_StdioConnection]]
- 25 edges to [[_COMMUNITY_MCPInspector]]
- 22 edges to [[_COMMUNITY_MCPToolCall]]
- 16 edges to [[_COMMUNITY_MCPToolResult]]
- 13 edges to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 12 edges to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 3 edges to [[_COMMUNITY_api.py (2)]]
- 3 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition]]

## Top bridge nodes
- [[test_mcp_proxy_coverage.py]] - degree 34, connects to 8 communities
- [[FakeApprovalQueue]] - degree 27, connects to 8 communities
- [[FakeConn]] - degree 30, connects to 7 communities
- [[TestExecuteToolCall]] - degree 24, connects to 7 communities
- [[TestApprovalQueue]] - degree 21, connects to 7 communities
