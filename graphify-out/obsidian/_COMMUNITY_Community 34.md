---
type: community
members: 68
---

# Community 34

**Members:** 68 nodes

## Members
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Build a fake httpx.Response whose .json() returns body.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Create a router configuration for testing]] - rationale - gateway/tests/test_router.py
- [[Create a router instance for testing]] - rationale - gateway/tests/test_router.py
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover     (Anthropic cr]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Test forwarding handles HTTP error responses]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles timeout exception]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles unexpected exceptions]] - rationale - gateway/tests/test_router.py
- [[Test forwarding to offline agent raises ForwardError]] - rationale - gateway/tests/test_router.py
- [[Test health check for offline agent]] - rationale - gateway/tests/test_router.py
- [[Test health check for single target]] - rationale - gateway/tests/test_router.py
- [[Test health check with healthy agent]] - rationale - gateway/tests/test_router.py
- [[Test listing all configured targets]] - rationale - gateway/tests/test_router.py
- [[Test routing to default target]] - rationale - gateway/tests/test_router.py
- [[Test routing with explicit route_to]] - rationale - gateway/tests/test_router.py
- [[Test routing with invalid explicit target falls back to default]] - rationale - gateway/tests/test_router.py
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[_mock_response()]] - code - gateway/tests/test_router_openai_translation.py
- [[_mock_stream_response()]] - code - gateway/tests/test_router_streaming.py
- [[_sse_lines()]] - code - gateway/tests/test_router_streaming.py
- [[forward_to_agent builds URL from target.chat_path.]] - rationale - gateway/tests/test_router.py
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent passes response.json() through unchanged for chat targets.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends the generic {content, ledger_id, ...} body for chat targ]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends {model, messages} when chat_path ends v1chatcompleti]] - rationale - gateway/tests/test_router_openai_translation.py
- [[health_check builds URL from target.health_path.]] - rationale - gateway/tests/test_router.py
- [[load_config computes CORS origins from the configured port.]] - rationale - gateway/tests/test_router.py
- [[router()_1]] - code - gateway/tests/test_router.py
- [[router_config()]] - code - gateway/tests/test_router.py
- [[test_agent_target_custom_paths()]] - code - gateway/tests/test_router.py
- [[test_agent_target_default_paths()]] - code - gateway/tests/test_router.py
- [[test_cors_origins_include_configured_port()]] - code - gateway/tests/test_router.py
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
- [[test_list_targets()]] - code - gateway/tests/test_router.py
- [[test_openai_empty_choices_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_malformed_response_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_payload_includes_model()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_returns_content_string()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_sends_messages_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_resolve_target_default()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_invalid_explicit()]] - code - gateway/tests/test_router.py
- [[test_router.py]] - code - gateway/tests/test_router.py
- [[test_router_openai_translation.py]] - code - gateway/tests/test_router_openai_translation.py
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
TABLE source_file, type FROM #community/Community_34
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 7]]
- 10 edges to [[_COMMUNITY_Community 47]]
- 7 edges to [[_COMMUNITY_Community 368]]
- 7 edges to [[_COMMUNITY_Community 325]]
- 4 edges to [[_COMMUNITY_Community 92]]
- 4 edges to [[_COMMUNITY_Community 861]]
- 3 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 254]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 2154]]
- 1 edge to [[_COMMUNITY_Community 251]]
- 1 edge to [[_COMMUNITY_Community 312]]

## Top bridge nodes
- [[AgentTarget]] - degree 58, connects to 9 communities
- [[test_router.py]] - degree 28, connects to 4 communities
- [[test_router_openai_translation.py]] - degree 16, connects to 4 communities
- [[test_router_streaming.py]] - degree 17, connects to 3 communities
- [[router_config()]] - degree 3, connects to 1 community