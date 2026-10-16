---
type: community
cohesion: 0.07
members: 76
---

# StdioConnection

**Cohesion:** 0.07 - loosely connected
**Members:** 76 nodes

## Members
- [[dot-__init__()_45]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_46]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-__init__()_47]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_item()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_or_create()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-is_running()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-remove()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_3]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_4]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-submit_tool_request()]] - code - gateway/tests/test_mcp_proxy_coverage.py
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
- [[dot-test_passthrough_process_tool_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_passthrough_with_execute()]] - code - gateway/tests/test_mcp_proxy_coverage.py
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
- [[dot-wait_for_decision()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[ConnectionPool]] - code - gateway/proxy/mcp_proxy.py
- [[Exception]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeConn]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Get existing connection or create a new one.]] - rationale - gateway/proxy/mcp_proxy.py
- [[HttpSseConnection]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPProxyConfig]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Manages a stdio connection to an MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages an HTTPSSE connection to an MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Pool of connections to MCP servers.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in connection injected into the proxy's pool.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[StdioConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestConnectionPool]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEgressFilterPaths]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEmitPrivacyEvent]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExecuteToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestPassthrough]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestResultProcessingAndLifecycle]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestSanitizeAdminPrivateData]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_config()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_proxy()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[test_mcp_proxy_coverage.py]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 83 edges to [[_COMMUNITY_MCPPermissionManager]]
- 49 edges to [[_COMMUNITY_MCPToolCall]]
- 30 edges to [[_COMMUNITY_PermissionLevel]]
- 25 edges to [[_COMMUNITY_MCPToolResult]]
- 19 edges to [[_COMMUNITY_FakeProcess]]
- 18 edges to [[_COMMUNITY_MCPAuditTrail]]
- 4 edges to [[_COMMUNITY_TestExtractEgressTargets]]
- 3 edges to [[_COMMUNITY__make_filter]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_dot-process_tool_call]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]

## Top bridge nodes
- [[test_mcp_proxy_coverage.py]] - degree 34, connects to 8 communities
- [[HttpSseConnection]] - degree 35, connects to 7 communities
- [[StdioConnection]] - degree 38, connects to 6 communities
- [[ConnectionPool]] - degree 36, connects to 6 communities
- [[FakeConn]] - degree 30, connects to 6 communities
