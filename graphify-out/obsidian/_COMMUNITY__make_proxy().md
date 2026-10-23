---
type: community
cohesion: 0.03
members: 102
---

# _make_proxy()

**Cohesion:** 0.03 - loosely connected
**Members:** 102 nodes

## Members
- [[dot-__init__()_136]] - code - gateway/ingest_api/ledger.py
- [[dot-_hash_content()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_stats()_12]] - code - gateway/ingest_api/ledger.py
- [[dot-process_inbound()_5]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[dot-query()]] - code - gateway/ingest_api/ledger.py
- [[dot-record()_2]] - code - gateway/ingest_api/ledger.py
- [[dot-test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Any_48]] - code - gateway/ingest_api/ledger.py
- [[Build a fake httpx.Response whose .json() returns body.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Create a new ledger entry          Args             source Source identifier (]] - rationale - gateway/ingest_api/ledger.py
- [[Create a router configuration for testing]] - rationale - gateway/tests/test_router.py
- [[Create a router instance for testing]] - rationale - gateway/tests/test_router.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[LedgerConfig]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry]] - code - gateway/ingest_api/models.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/models.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/ledger.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover     (Anthropic cr]] - rationale - gateway/tests/test_router_streaming.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Regression forward returned out_result.sanitized_message without checking]] - rationale - gateway/tests/test_forward_routing.py
- [[Related Notes_31]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py
- [[Single entry from the data ledger]] - rationale - gateway/ingest_api/models.py
- [[Store configuration          Actual database connection created in initialize().]] - rationale - gateway/ingest_api/ledger.py
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
- [[gatewayREADME]] - document - gateway/README.md
- [[health_check builds URL from target.health_path.]] - rationale - gateway/tests/test_router.py
- [[ingest_apimodels.py]] - code - gateway/ingest_api/models.py
- [[ingest_apirouter.py]] - code - gateway/ingest_api/router.py
- [[ledger.py]] - code - gateway/ingest_api/ledger.py
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
TABLE source_file, type FROM #community/_make_proxy
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_MCPPermissionManager]]
- 17 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 13 edges to [[_COMMUNITY_TestEmailSend]]
- 9 edges to [[_COMMUNITY_ForwardRequest]]
- 7 edges to [[_COMMUNITY_ServiceManager]]
- 5 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 4 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 4 edges to [[_COMMUNITY_GroupConfig]]
- 3 edges to [[_COMMUNITY_create_auth_dependency()]]
- 2 edges to [[_COMMUNITY_Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)]]
- 2 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_pick_latest_stable]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]
- 1 edge to [[_COMMUNITY_test_fieldflare_route_strips_unsupported_fields_streaming]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (3)]]
- 1 edge to [[_COMMUNITY_dot-githubmcp.json]]
- 1 edge to [[_COMMUNITY_🛡️ AgentShroud Release Plan]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (2) (2)]]

## Top bridge nodes
- [[ingest_apimodels.py]] - degree 27, connects to 11 communities
- [[gatewayREADME]] - degree 11, connects to 7 communities
- [[AgentTarget]] - degree 58, connects to 5 communities
- [[ingest_apirouter.py]] - degree 13, connects to 5 communities
- [[test_router.py]] - degree 28, connects to 4 communities
