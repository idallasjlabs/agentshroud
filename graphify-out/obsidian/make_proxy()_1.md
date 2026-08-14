---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Collaborator Prompt Safety"
location: "L68"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_Prompt_Safety
---

# make_proxy()

## Connections
- [[.test_approved_decision_allows()]] - `calls` [EXTRACTED]
- [[.test_async_egress_filter_deny_uses_rule_as_reason()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_blocks_with_item_status()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_with_missing_item_defaults_denied()]] - `calls` [EXTRACTED]
- [[.test_egress_filter_allow_passes_through()]] - `calls` [EXTRACTED]
- [[.test_emit_swallows_bus_errors()]] - `calls` [EXTRACTED]
- [[.test_emits_event_to_bus()]] - `calls` [EXTRACTED]
- [[.test_execution_redacts_admin_private_content()]] - `calls` [EXTRACTED]
- [[.test_execution_with_none_content_skips_result_inspection()]] - `calls` [EXTRACTED]
- [[.test_generic_exception()]] - `calls` [EXTRACTED]
- [[.test_get_stats_after_allowed_call()]] - `calls` [EXTRACTED]
- [[.test_get_stats_zero_and_after_calls()]] - `calls` [EXTRACTED]
- [[.test_no_patterns_returns_unchanged()]] - `calls` [EXTRACTED]
- [[.test_no_queue_allows_by_default()]] - `calls` [EXTRACTED]
- [[.test_owner_bypasses_redaction()]] - `calls` [EXTRACTED]
- [[.test_process_tool_call_blocks_on_denial()]] - `calls` [EXTRACTED]
- [[.test_process_tool_result_handles_none_content()]] - `calls` [EXTRACTED]
- [[.test_process_tool_result_redacts_private_data()]] - `calls` [EXTRACTED]
- [[.test_redacts_nested_dict_list_tuple()]] - `calls` [EXTRACTED]
- [[.test_sanitized_params_preferred_over_originals()]] - `calls` [EXTRACTED]
- [[.test_server_error_response()]] - `calls` [EXTRACTED]
- [[.test_server_error_response_without_message()]] - `calls` [EXTRACTED]
- [[.test_shutdown_stops_all_connections()]] - `calls` [EXTRACTED]
- [[.test_successful_execution_with_result_inspection()]] - `calls` [EXTRACTED]
- [[.test_sync_egress_filter_deny_blocks()]] - `calls` [EXTRACTED]
- [[.test_timeout_error()]] - `calls` [EXTRACTED]
- [[.test_tool_not_requiring_approval_allowed()]] - `calls` [EXTRACTED]
- [[.test_unknown_server_returns_error_result()]] - `calls` [EXTRACTED]
- [[MCPAuditTrail]] - `calls` [EXTRACTED]
- [[MCPInspector]] - `calls` [EXTRACTED]
- [[MCPPermissionManager]] - `calls` [EXTRACTED]
- [[MCPProxy]] - `calls` [EXTRACTED]
- [[MCPProxy_1]] - `references` [EXTRACTED]
- [[make_config()]] - `calls` [EXTRACTED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_Prompt_Safety