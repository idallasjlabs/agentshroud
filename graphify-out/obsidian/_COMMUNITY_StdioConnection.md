---
type: community
cohesion: 0.11
members: 44
---

# StdioConnection

**Cohesion:** 0.11 - loosely connected
**Members:** 44 nodes

## Members
- [[dot-__init__()_195]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_item()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-submit_tool_request()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
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
- [[dot-test_successful_execution_with_result_inspection()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_sync_egress_filter_deny_blocks()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_timeout_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_tool_not_requiring_approval_allowed()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_unknown_server_returns_error_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-wait_for_decision()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeConn]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Stand-in connection injected into the proxy's pool.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[TestApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEgressFilterPaths]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEmitPrivacyEvent]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExecuteToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestResultProcessingAndLifecycle]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestSanitizeAdminPrivateData]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_proxy()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[test_mcp_proxy_coverage.py]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_StdioConnection_1]]
- 20 edges to [[_COMMUNITY_MCPPermissionManager]]
- 19 edges to [[_COMMUNITY_PermissionLevel]]
- 19 edges to [[_COMMUNITY_MCPInspector]]
- 18 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 13 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 10 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 10 edges to [[_COMMUNITY_MCPAuditTrail]]
- 3 edges to [[_COMMUNITY_AsyncMock_1]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]

## Top bridge nodes
- [[test_mcp_proxy_coverage.py]] - degree 34, connects to 10 communities
- [[FakeApprovalQueue]] - degree 27, connects to 9 communities
- [[FakeConn]] - degree 30, connects to 8 communities
- [[TestExecuteToolCall]] - degree 24, connects to 8 communities
- [[TestApprovalQueue]] - degree 21, connects to 8 communities
