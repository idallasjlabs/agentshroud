---
type: community
members: 105
---

# AgentTarget

**Members:** 105 nodes

## Members
- [[dot-_build_forward_payload()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent_stream()]] - code - gateway/ingest_api/router.py
- [[dot-health_check()_5]] - code - gateway/ingest_api/router.py
- [[dot-list_targets()]] - code - gateway/ingest_api/router.py
- [[dot-resolve_target()]] - code - gateway/ingest_api/router.py
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Any_60]] - code
- [[Build a fake httpx.Response whose .json() returns body.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Build the outbound payload for `target`, shared by the blocking and streaming…]] - rationale - gateway/ingest_api/router.py
- [[Check health of one or all agent targets Args target Specific target to…]] - rationale - gateway/ingest_api/router.py
- [[Determine which agent should receive this content Args request Forward…]] - rationale - gateway/ingest_api/router.py
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Exception_15]] - code
- [[Forward sanitized content to agent via HTTP POST Args target Agent target to…]] - rationale - gateway/ingest_api/router.py
- [[ForwardError]] - code - gateway/ingest_api/router.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover (Anthropic…]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Raised when forwarding to agent fails]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Return all configured agent targets Returns List of AgentTarget objects]] - rationale - gateway/ingest_api/router.py
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[Stream sanitized content to an OpenAI-compatible agent, yielding text deltas as…]] - rationale - gateway/ingest_api/router.py
- [[Test forwarding handles HTTP error responses]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles timeout exception]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles unexpected exceptions]] - rationale - gateway/tests/test_router.py
- [[Test forwarding to offline agent raises ForwardError]] - rationale - gateway/tests/test_router.py
- [[Test health check for offline agent]] - rationale - gateway/tests/test_router.py
- [[Test health check for single target]] - rationale - gateway/tests/test_router.py
- [[Test health check with healthy agent]] - rationale - gateway/tests/test_router.py
- [[Test routing to default target]] - rationale - gateway/tests/test_router.py
- [[Test routing with explicit route_to]] - rationale - gateway/tests/test_router.py
- [[Test routing with invalid explicit target falls back to default]] - rationale - gateway/tests/test_router.py
- [[Tests for MultiAgentRouter.forward_to_agent_stream — SSE relay to an OpenAI-…]] - rationale - gateway/tests/test_router_streaming.py
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[_aiter_lines()_1]] - code - gateway/tests/test_router_streaming.py
- [[_mock_response()]] - code - gateway/tests/test_router_openai_translation.py
- [[_mock_stream_response()]] - code - gateway/tests/test_router_streaming.py
- [[_raise_connect()]] - code - gateway/tests/test_router.py
- [[_sse_lines()]] - code - gateway/tests/test_router_streaming.py
- [[asyncio_58]] - code
- [[asyncio_59]] - code
- [[asyncio_60]] - code
- [[forward_to_agent builds URL from target.chat_path.]] - rationale - gateway/tests/test_router.py
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent passes response.json() through unchanged for chat targets.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends the generic {content, ledger_id, ...} body for chat…]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends {model, messages} when chat_path ends…]] - rationale - gateway/tests/test_router_openai_translation.py
- [[health_check builds URL from target.health_path.]] - rationale - gateway/tests/test_router.py
- [[json()_2]] - code - gateway/tests/test_router.py
- [[mock_get()]] - code - gateway/tests/test_router.py
- [[mock_get()_1]] - code - gateway/tests/test_router.py
- [[mock_post()]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_1]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_2]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_3]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_4]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_5]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_6]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_7]] - code - gateway/tests/test_router.py
- [[mock_post()_8]] - code - gateway/tests/test_router.py
- [[mock_post()_9]] - code - gateway/tests/test_router.py
- [[mock_post()_10]] - code - gateway/tests/test_router.py
- [[mock_stream()_12]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_13]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_14]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_15]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_16]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_17]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_18]] - code - gateway/tests/test_router_streaming.py
- [[raise_for_status()]] - code - gateway/tests/test_router.py
- [[raise_for_status()_1]] - code - gateway/tests/test_router.py
- [[test_agent_target_custom_paths()]] - code - gateway/tests/test_router.py
- [[test_agent_target_default_paths()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_http_error()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_offline()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_timeout()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_unexpected_error()]] - code - gateway/tests/test_router.py
- [[test_forward_uses_chat_path()]] - code - gateway/tests/test_router.py
- [[test_generic_target_returns_json_as_is()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_generic_target_sends_content_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_health_check_healthy_agent()]] - code - gateway/tests/test_router.py
- [[test_health_check_offline_agent()]] - code - gateway/tests/test_router.py
- [[test_health_check_single_target()]] - code - gateway/tests/test_router.py
- [[test_health_check_uses_health_path()]] - code - gateway/tests/test_router.py
- [[test_openai_empty_choices_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_malformed_response_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_payload_includes_model()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_returns_content_string()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_sends_messages_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_resolve_target_default()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_invalid_explicit()]] - code - gateway/tests/test_router.py
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
TABLE source_file, type FROM #community/AgentTarget
SORT file.name ASC
```

## Connections to other communities
- 44 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 8 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 8 edges to [[_COMMUNITY_test_forward_routing.py]]
- 8 edges to [[_COMMUNITY_test_forward_stream.py]]
- 4 edges to [[_COMMUNITY_TestConfigValidation]]
- 1 edge to [[_COMMUNITY__TrustCaptor]]

## Top bridge nodes
- [[AgentTarget]] - degree 53, connects to 5 communities
- [[ForwardError]] - degree 24, connects to 3 communities
- [[test_router_streaming.py]] - degree 20, connects to 2 communities
- [[dot-resolve_target()]] - degree 5, connects to 2 communities
- [[test_resolve_target_default()]] - degree 4, connects to 2 communities
