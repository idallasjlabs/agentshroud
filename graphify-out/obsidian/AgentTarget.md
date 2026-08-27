---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Community 38"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_38
---

# AgentTarget

## Connections
- [[.test_agent_id_propagated_for_hermes()]] - `calls` [EXTRACTED]
- [[.test_agent_id_propagated_for_openclaw()]] - `calls` [EXTRACTED]
- [[.test_blocked_outbound_replaced_with_policy_notice()]] - `calls` [EXTRACTED]
- [[.test_default_not_used_in_pipeline()]] - `calls` [EXTRACTED]
- [[AgentTarget_1]] - `uses` [INFERRED]
- [[Any_9]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Downstream agent target]] - `rationale_for` [EXTRACTED]
- [[ForwardError]] - `uses` [INFERRED]
- [[ForwardRequest_1]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[RouterError]] - `uses` [INFERRED]
- [[TestAgentIdPropagatedFromTarget]] - `uses` [INFERRED]
- [[TestOutboundBlockedNotDelivered]] - `uses` [INFERRED]
- [[TestOwnerSpoofingViaForwardBody]] - `uses` [INFERRED]
- [[TestOwnerTrustElevation]] - `uses` [INFERRED]
- [[_BlockedOutboundPipeline]] - `uses` [INFERRED]
- [[_BlockingPipeline]] - `uses` [INFERRED]
- [[_PassthroughPipeline]] - `uses` [INFERRED]
- [[_PipelineCaptor]] - `uses` [INFERRED]
- [[_TrustCaptor]] - `uses` [INFERRED]
- [[_make_mock_app_state()]] - `calls` [EXTRACTED]
- [[_make_stream_app_state()]] - `calls` [EXTRACTED]
- [[_make_trust_app_state()]] - `calls` [EXTRACTED]
- [[_target()]] - `calls` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[router.py]] - `imports` [EXTRACTED]
- [[test_agent_target_custom_paths()]] - `calls` [EXTRACTED]
- [[test_agent_target_default_paths()]] - `calls` [EXTRACTED]
- [[test_forward_routing.py]] - `references` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_forward_stream_rejects_non_openai_compat_target()]] - `calls` [EXTRACTED]
- [[test_forward_to_agent_http_error()]] - `calls` [EXTRACTED]
- [[test_forward_to_agent_offline()]] - `calls` [EXTRACTED]
- [[test_forward_to_agent_timeout()]] - `calls` [EXTRACTED]
- [[test_forward_to_agent_unexpected_error()]] - `calls` [EXTRACTED]
- [[test_forward_uses_chat_path()]] - `calls` [EXTRACTED]
- [[test_generic_target_returns_json_as_is()]] - `calls` [EXTRACTED]
- [[test_generic_target_sends_content_body()]] - `calls` [EXTRACTED]
- [[test_health_check_uses_health_path()]] - `calls` [EXTRACTED]
- [[test_openai_empty_choices_raises_forward_error()]] - `calls` [EXTRACTED]
- [[test_openai_malformed_response_raises_forward_error()]] - `calls` [EXTRACTED]
- [[test_openai_payload_includes_model()]] - `calls` [EXTRACTED]
- [[test_openai_target_returns_content_string()]] - `calls` [EXTRACTED]
- [[test_openai_target_sends_messages_body()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_router_openai_translation.py]] - `imports` [EXTRACTED]
- [[test_router_streaming.py]] - `imports` [EXTRACTED]
- [[test_stream_ignores_lines_without_data_prefix()]] - `calls` [EXTRACTED]
- [[test_stream_payload_sets_stream_true()]] - `calls` [EXTRACTED]
- [[test_stream_raises_forward_error_on_connect_failure()]] - `calls` [EXTRACTED]
- [[test_stream_raises_forward_error_on_http_status_error()]] - `calls` [EXTRACTED]
- [[test_stream_raises_forward_error_on_malformed_json()]] - `calls` [EXTRACTED]
- [[test_stream_rejects_non_openai_compat_target()]] - `calls` [EXTRACTED]
- [[test_stream_skips_chunk_missing_choices_key_and_continues()]] - `calls` [EXTRACTED]
- [[test_stream_yields_content_deltas_in_order()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_38