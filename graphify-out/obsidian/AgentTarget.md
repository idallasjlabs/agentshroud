---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "AgentTarget"
location: "L219"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# AgentTarget

## Connections
- [[dot-_build_forward_payload()]] - `references` [EXTRACTED]
- [[dot-forward_to_agent()]] - `references` [EXTRACTED]
- [[dot-forward_to_agent_stream()]] - `references` [EXTRACTED]
- [[dot-health_check()_3]] - `references` [EXTRACTED]
- [[dot-list_targets()]] - `references` [EXTRACTED]
- [[dot-resolve_target()]] - `references` [EXTRACTED]
- [[dot-test_agent_id_propagated_for_hermes()]] - `calls` [EXTRACTED]
- [[dot-test_agent_id_propagated_for_openclaw()]] - `calls` [EXTRACTED]
- [[dot-test_blocked_outbound_replaced_with_policy_notice()]] - `calls` [EXTRACTED]
- [[dot-test_default_not_used_in_pipeline()]] - `calls` [EXTRACTED]
- [[BaseModel_7]] - `inherits` [EXTRACTED]
- [[Downstream agent target]] - `rationale_for` [EXTRACTED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[TestAgentIdPropagatedFromTarget]] - `uses` [INFERRED]
- [[TestOutboundBlockedNotDelivered]] - `uses` [INFERRED]
- [[_InboundResult]] - `uses` [INFERRED]
- [[_make_mock_app_state()]] - `calls` [EXTRACTED]
- [[_make_stream_app_state()]] - `calls` [EXTRACTED]
- [[_make_trust_app_state()]] - `calls` [EXTRACTED]
- [[_resolve_user_trust_level()]] - `uses` [INFERRED]
- [[_target()]] - `calls` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[ingest_apirouter.py]] - `imports` [EXTRACTED]
- [[test_agent_target_custom_paths()]] - `calls` [EXTRACTED]
- [[test_agent_target_default_paths()]] - `calls` [EXTRACTED]
- [[test_forward_routing.py]] - `imports` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_forward_stream_rejects_non_openai_compat_target()]] - `calls` [EXTRACTED]
- [[test_forward_to_agent_http_error()]] - `uses` [INFERRED]
- [[test_forward_to_agent_offline()]] - `uses` [INFERRED]
- [[test_forward_to_agent_timeout()]] - `uses` [INFERRED]
- [[test_forward_to_agent_unexpected_error()]] - `uses` [INFERRED]
- [[test_forward_uses_chat_path()]] - `uses` [INFERRED]
- [[test_generic_target_returns_json_as_is()]] - `uses` [INFERRED]
- [[test_generic_target_sends_content_body()]] - `uses` [INFERRED]
- [[test_health_check_uses_health_path()]] - `uses` [INFERRED]
- [[test_openai_empty_choices_raises_forward_error()]] - `uses` [INFERRED]
- [[test_openai_malformed_response_raises_forward_error()]] - `uses` [INFERRED]
- [[test_openai_payload_includes_model()]] - `uses` [INFERRED]
- [[test_openai_target_returns_content_string()]] - `uses` [INFERRED]
- [[test_openai_target_sends_messages_body()]] - `uses` [INFERRED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_router_openai_translation.py]] - `imports` [EXTRACTED]
- [[test_router_streaming.py]] - `imports` [EXTRACTED]
- [[test_stream_ignores_lines_without_data_prefix()]] - `uses` [INFERRED]
- [[test_stream_payload_sets_stream_true()]] - `uses` [INFERRED]
- [[test_stream_raises_forward_error_on_connect_failure()]] - `uses` [INFERRED]
- [[test_stream_raises_forward_error_on_http_status_error()]] - `uses` [INFERRED]
- [[test_stream_raises_forward_error_on_malformed_json()]] - `uses` [INFERRED]
- [[test_stream_rejects_non_openai_compat_target()]] - `uses` [INFERRED]
- [[test_stream_skips_chunk_missing_choices_key_and_continues()]] - `uses` [INFERRED]
- [[test_stream_yields_content_deltas_in_order()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
