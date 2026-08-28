---
type: community
cohesion: 0.03
members: 101
---

# Community 32

**Cohesion:** 0.03 - loosely connected
**Members:** 101 nodes

## Members
- [[.__init__()_15]] - code - gateway/ingest_api/router.py
- [[._build_forward_payload()]] - code - gateway/ingest_api/router.py
- [[.forward_to_agent()]] - code - gateway/ingest_api/router.py
- [[.forward_to_agent_stream()]] - code - gateway/ingest_api/router.py
- [[.health_check()]] - code - gateway/ingest_api/router.py
- [[.list_targets()]] - code - gateway/ingest_api/router.py
- [[.register_bots()]] - code - gateway/ingest_api/router.py
- [[.resolve_target()]] - code - gateway/ingest_api/router.py
- [[.validate_default_url()]] - code - gateway/ingest_api/config.py
- [[.validate_targets()]] - code - gateway/ingest_api/config.py
- [[AgentShroud Secure Chat Interface (static HTMLJS)]] - code - gateway/ingest_api/static/chat.html
- [[AgentTarget_1]] - code - gateway/ingest_api/router.py
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Any_9]] - code - gateway/ingest_api/router.py
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
- [[ForwardRequest_1]] - code - gateway/ingest_api/router.py
- [[Initialize router          Args             config Router configuration]] - rationale - gateway/ingest_api/router.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover     (Anthropic cr]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Multi-agent router configuration]] - rationale - gateway/ingest_api/config.py
- [[MultiAgentRouter]] - code - gateway/ingest_api/router.py
- [[Populate routing targets from the bots registry.          Iterates all BotConfig]] - rationale - gateway/ingest_api/router.py
- [[Raised when forwarding to agent fails]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Return all configured agent targets          Returns             List of AgentT]] - rationale - gateway/ingest_api/router.py
- [[RouterConfig]] - code - gateway/ingest_api/config.py
- [[RouterConfig_1]] - code - gateway/ingest_api/router.py
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
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Validate that default_url uses httphttps and targets an internal Docker host.]] - rationale - gateway/ingest_api/config.py
- [[Validate that each target URL uses httphttps and targets an internal Docker hos]] - rationale - gateway/ingest_api/config.py
- [[_mock_response()]] - code - gateway/tests/test_router_openai_translation.py
- [[_mock_stream_response()]] - code - gateway/tests/test_router_streaming.py
- [[_sse_lines()]] - code - gateway/tests/test_router_streaming.py
- [[forward_to_agent builds URL from target.chat_path.]] - rationale - gateway/tests/test_router.py
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent passes response.json() through unchanged for chat targets.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends the generic {content, ledger_id, ...} body for chat targ]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends {model, messages} when chat_path ends v1chatcompleti]] - rationale - gateway/tests/test_router_openai_translation.py
- [[health_check builds URL from target.health_path.]] - rationale - gateway/tests/test_router.py
- [[route_to='hermes' must resolve to the Hermes AgentTarget.]] - rationale - gateway/tests/test_router.py
- [[router()_2]] - code - gateway/tests/test_router_openai_translation.py
- [[router()_1]] - code - gateway/tests/test_router.py
- [[router()_3]] - code - gateway/tests/test_router_streaming.py
- [[router.py]] - code - gateway/ingest_api/router.py
- [[router_config()]] - code - gateway/tests/test_router.py
- [[sendMessage() JS — POST forward from browser chat UI]] - code - gateway/ingest_api/static/chat.html
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
TABLE source_file, type FROM #community/Community_32
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Community 15]]
- 25 edges to [[_COMMUNITY_Config Validation & Router]]
- 14 edges to [[_COMMUNITY_Community 104]]
- 12 edges to [[_COMMUNITY_Community 26]]
- 11 edges to [[_COMMUNITY_Community 43]]
- 10 edges to [[_COMMUNITY_Community 119]]
- 8 edges to [[_COMMUNITY_Community 64]]
- 5 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 3 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 3 edges to [[_COMMUNITY_Community 159]]
- 2 edges to [[_COMMUNITY_Community 165]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 91]]
- 1 edge to [[_COMMUNITY_Community 508]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Community 500]]
- 1 edge to [[_COMMUNITY_Community 85]]
- 1 edge to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 224]]
- 1 edge to [[_COMMUNITY_Community 288]]

## Top bridge nodes
- [[RouterConfig]] - degree 66, connects to 9 communities
- [[MultiAgentRouter]] - degree 47, connects to 8 communities
- [[router.py]] - degree 14, connects to 7 communities
- [[AgentTarget]] - degree 58, connects to 5 communities
- [[ForwardError]] - degree 16, connects to 4 communities