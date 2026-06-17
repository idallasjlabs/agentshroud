---
type: community
cohesion: 0.12
members: 38
---

# Module Group 124

**Cohesion:** 0.12 - loosely connected
**Members:** 38 nodes

## Members
- [[.__init__()_128]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_127]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.get_item()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.submit_tool_request()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_approved_decision_allows()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_async_egress_filter_deny_uses_rule_as_reason()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_denied_decision_blocks_with_item_status()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_denied_decision_with_missing_item_defaults_denied()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_egress_filter_allow_passes_through()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_emit_swallows_bus_errors()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_emits_event_to_bus()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_execution_redacts_admin_private_content()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_execution_with_none_content_skips_result_inspection()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_generic_exception()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_get_stats_after_allowed_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_get_stats_zero_and_after_calls()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_no_queue_allows_by_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_process_tool_call_blocks_on_denial()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_process_tool_result_handles_none_content()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_process_tool_result_redacts_private_data()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_sanitized_params_preferred_over_originals()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_server_error_response()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_server_error_response_without_message()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_shutdown_stops_all_connections()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_successful_execution_with_result_inspection()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_sync_egress_filter_deny_blocks()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_timeout_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_tool_not_requiring_approval_allowed()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_unknown_server_returns_error_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.wait_for_decision()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeConn]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Stand-in connection injected into the proxy's pool.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[TestApprovalQueue]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExecuteToolCall]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestResultProcessingAndLifecycle]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_call()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_proxy()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_124
SORT file.name ASC
```

## Connections to other communities
- 65 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 12 edges to [[_COMMUNITY_Module Group 78]]
- 7 edges to [[_COMMUNITY_Module Group 266]]
- 6 edges to [[_COMMUNITY_Module Group 139]]
- 6 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 5 edges to [[_COMMUNITY_Module Group 154]]
- 3 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 3 edges to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[FakeApprovalQueue]] - degree 27, connects to 7 communities
- [[FakeConn]] - degree 30, connects to 6 communities
- [[TestExecuteToolCall]] - degree 24, connects to 6 communities
- [[TestApprovalQueue]] - degree 21, connects to 6 communities
- [[TestResultProcessingAndLifecycle]] - degree 20, connects to 6 communities