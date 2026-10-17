---
type: community
members: 103
---

# AgentTarget (2)

**Members:** 103 nodes

## Members
- [[dot-__init__()_122]] - code - gateway/ingest_api/router.py
- [[dot-_build_forward_payload()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent_stream()]] - code - gateway/ingest_api/router.py
- [[dot-health_check()_2]] - code - gateway/ingest_api/router.py
- [[dot-list_targets()]] - code - gateway/ingest_api/router.py
- [[dot-process_inbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[dot-register_bots()]] - code - gateway/ingest_api/router.py
- [[dot-resolve_target()]] - code - gateway/ingest_api/router.py
- [[dot-test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[AgentShroud Secure Chat Interface (static HTMLJS)]] - code - gateway/ingest_api/static/chat.html
- [[AgentTarget_1]] - code - gateway/ingest_api/router.py
- [[AgentTarget_2]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Any_45]] - code - gateway/ingest_api/router.py
- [[Both bots must be reachable via the same router without conflict.]] - rationale - gateway/tests/test_router.py
- [[Build a fake httpx.Response whose .json() returns body.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Build the outbound payload for `target`, shared by the blocking and         stre]] - rationale - gateway/ingest_api/router.py
- [[Check health of one or all agent targets          Args             target Spec]] - rationale - gateway/ingest_api/router.py
- [[Create a router configuration for testing]] - rationale - gateway/tests/test_router.py
- [[Create a router instance for testing]] - rationale - gateway/tests/test_router.py
- [[Determine which agent should receive this content          Args             req]] - rationale - gateway/ingest_api/router.py
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Forward sanitized content to agent via HTTP POST          Args             targ]] - rationale - gateway/ingest_api/router.py
- [[ForwardError]] - code - gateway/ingest_api/router.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/router.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Initialize router          Args             config Router configuration]] - rationale - gateway/ingest_api/router.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover     (Anthropic cr]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[MultiAgentRouter]] - code - gateway/ingest_api/router.py
- [[Populate routing targets from the bots registry.          Iterates all BotConfig]] - rationale - gateway/ingest_api/router.py
- [[Raised when forwarding to agent fails]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Regression forward returned out_result.sanitized_message without checking]] - rationale - gateway/tests/test_forward_routing.py
- [[Return all configured agent targets          Returns             List of AgentT]] - rationale - gateway/ingest_api/router.py
- [[RouterConfig]] - code - gateway/ingest_api/router.py
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[Routes content to appropriate agent containers      Routing priority     1. Exp]] - rationale - gateway/ingest_api/router.py
- [[Stream sanitized content to an OpenAI-compatible agent, yielding text         de]] - rationale - gateway/ingest_api/router.py
- [[Test forwarding handles HTTP error responses]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles timeout exception]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles unexpected exceptions]] - rationale - gateway/tests/test_router.py
- [[Test forwarding to offline agent raises ForwardError]] - rationale - gateway/tests/test_router.py
- [[Test health check for offline agent]] - rationale - gateway/tests/test_router.py
- [[Test health check for single target]] - rationale - gateway/tests/test_router.py
- [[Test health check with healthy agent]] - rationale - gateway/tests/test_router.py
- [[Test listing all configured targets]] - rationale - gateway/tests/test_router.py
- [[TestOutboundBlockedNotDelivered]] - code - gateway/tests/test_forward_routing.py
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[_BlockedOutboundPipeline]] - code - gateway/tests/test_forward_routing.py
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
- [[route_to='hermes' must resolve to the Hermes AgentTarget.]] - rationale - gateway/tests/test_router.py
- [[router()_1]] - code - gateway/tests/test_router_openai_translation.py
- [[router()_2]] - code - gateway/tests/test_router.py
- [[router()_3]] - code - gateway/tests/test_router_streaming.py
- [[router_config()]] - code - gateway/tests/test_router.py
- [[sendMessage() JS — POST forward from browser chat UI]] - code - gateway/ingest_api/static/chat.html
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
- [[test_hermes_and_openclaw_coexist()]] - code - gateway/tests/test_router.py
- [[test_list_targets()]] - code - gateway/tests/test_router.py
- [[test_openai_empty_choices_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_malformed_response_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_payload_includes_model()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_returns_content_string()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_sends_messages_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_resolves_hermes_target()]] - code - gateway/tests/test_router.py
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
TABLE source_file, type FROM #community/AgentTarget_2
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 15 edges to [[_COMMUNITY_AgentTarget]]
- 13 edges to [[_COMMUNITY_AgentTarget (3)]]
- 11 edges to [[_COMMUNITY_create_auth_dependency]]
- 10 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py (2)]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[MultiAgentRouter]] - degree 47, connects to 8 communities
- [[ForwardError]] - degree 16, connects to 5 communities
- [[AgentTarget_2]] - degree 58, connects to 4 communities
- [[RouterError]] - degree 7, connects to 4 communities
- [[test_router.py]] - degree 28, connects to 3 communities
