---
type: community
members: 85
---

# Community 325

**Members:** 85 nodes

## Members
- [[.__init__()_156]] - code - gateway/tests/test_forward_routing.py
- [[.__init__()_157]] - code - gateway/tests/test_forward_routing.py
- [[._post()]] - code - gateway/tests/test_forward_routing.py
- [[._post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[._run_forward()]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_5]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_5]] - code - gateway/tests/test_forward_routing.py
- [[.test_agent_id_propagated_for_hermes()]] - code - gateway/tests/test_forward_routing.py
- [[.test_agent_id_propagated_for_openclaw()]] - code - gateway/tests/test_forward_routing.py
- [[.test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[.test_body_owner_id_with_matching_trusted_header_is_honored()]] - code - gateway/tests/test_forward_routing.py
- [[.test_body_owner_id_without_trusted_header_is_stripped()]] - code - gateway/tests/test_forward_routing.py
- [[.test_default_not_used_in_pipeline()]] - code - gateway/tests/test_forward_routing.py
- [[.test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_forward_passes_user_id_in_metadata_to_process_inbound()]] - code - gateway/tests/test_forward_routing.py
- [[.test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_non_owner_body_user_id_passes_through()]] - code - gateway/tests/test_forward_routing.py
- [[.test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[A non-owner user_id is not a spoof risk and must pass through unchanged]] - rationale - gateway/tests/test_forward_routing.py
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Build a minimal mock app_state that returns a target with the given bot name.]] - rationale - gateway/tests/test_forward_routing.py
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Legitimate voice-gateway path owner ID in body + matching trusted         heade]] - rationale - gateway/tests/test_forward_routing.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover     (Anthropic cr]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Minimal app_state for owner-trust tests.]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal pipeline mock that records which agent_id it was called with.]] - rationale - gateway/tests/test_forward_routing.py
- [[Owner ID claimed in the body with NO trusted header must not reach the         p]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'hermes' as agent_id when routed to hermes.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'openclaw' as agent_id when routed to openclaw.]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression 'default' must never appear in agent_id when a named target is resol]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression forward returned out_result.sanitized_message without checking]] - rationale - gateway/tests/test_forward_routing.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id.]] - rationale - gateway/tests/test_forward_routing.py
- [[TestAgentIdPropagatedFromTarget]] - code - gateway/tests/test_forward_routing.py
- [[TestOutboundBlockedNotDelivered]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerSpoofingViaForwardBody]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Verify that the resolved target.name is used as agent_id in pipeline calls.]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a body-supplied user_id must NOT grant owner identity     to t]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the         truste]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),         p]] - rationale - gateway/tests/test_forward_routing.py
- [[_BlockedOutboundPipeline]] - code - gateway/tests/test_forward_routing.py
- [[_PipelineCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_mock_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[_make_trust_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[_mock_stream_response()]] - code - gateway/tests/test_router_streaming.py
- [[_sse_lines()]] - code - gateway/tests/test_router_streaming.py
- [[forward-routing agent_id propagation into security pipeline]] - code - gateway/ingest_api/routes/forward.py
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent passes response.json() through unchanged for chat targets.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends the generic {content, ledger_id, ...} body for chat targ]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends {model, messages} when chat_path ends v1chatcompleti]] - rationale - gateway/tests/test_router_openai_translation.py
- [[process_inbound must receive metadata={'user_id' ...} from forward so that]] - rationale - gateway/tests/test_forward_routing.py
- [[router()_3]] - code - gateway/tests/test_router_streaming.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py
- [[test_generic_target_returns_json_as_is()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_generic_target_sends_content_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_empty_choices_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_malformed_response_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_payload_includes_model()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_returns_content_string()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_sends_messages_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_router_streaming.py]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_ignores_lines_without_data_prefix()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_payload_sets_stream_true()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_connect_failure()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_http_status_error()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_malformed_json()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_rejects_non_openai_compat_target()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_skips_chunk_missing_choices_key_and_continues()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_yields_content_deltas_in_order()]] - code - gateway/tests/test_router_streaming.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_325
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 707]]
- 10 edges to [[_COMMUNITY_Community 34]]
- 9 edges to [[_COMMUNITY_Community 92]]
- 8 edges to [[_COMMUNITY_Community 47]]
- 5 edges to [[_COMMUNITY_Community 80]]
- 5 edges to [[_COMMUNITY_Community 861]]
- 3 edges to [[_COMMUNITY_Community 1127]]
- 2 edges to [[_COMMUNITY_Community 2154]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 251]]

## Top bridge nodes
- [[AgentTarget]] - degree 58, connects to 7 communities
- [[test_router_streaming.py]] - degree 17, connects to 4 communities
- [[test_forward_routing.py]] - degree 13, connects to 2 communities
- [[_PipelineCaptor]] - degree 16, connects to 1 community
- [[_TrustCaptor]] - degree 13, connects to 1 community