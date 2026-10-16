---
type: community
cohesion: 0.04
members: 75
---

# BotConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 75 nodes

## Members
- [[dot-_allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_make_proxy()_4]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-base_url()]] - code - gateway/ingest_api/bot_config.py
- [[dot-resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[dot-test_active_bot_id_falls_back_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_bot_id_returns_contextvar_when_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_send_token_returns_contextvar_inside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_send_token_returns_default_outside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_proxy_request_contextvar_visible_inside_impl()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_proxy_request_resets_contextvar_after_return()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_send_telegram_text_falls_back_to_default_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_send_telegram_text_uses_inbound_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[After proxy_request returns, _inbound_bot_token is reset to its prior value.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Cross-bot reply misrouting fix via contextvar-scoped send token]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - rationale - gateway/ingest_api/bot_config.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_bot_id() returns 'openclaw'.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_send_token() returns self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestMultiBotContextvarRouting]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Tests for per-request bot token routing via contextvars.      Regression suite f]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The contextvar set by proxy_request is visible throughout _proxy_request_impl.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_id is set, _active_bot_id() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_token is set, _active_send_token() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[Without contextvar, _send_telegram_text uses self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[_build_telegram_token_registry()]] - code - gateway/ingest_api/main.py
- [[_send_telegram_text uses the inbound contextvar token, not self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
- [[telegram_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BotConfig
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 6 edges to [[_COMMUNITY_load_config]]
- 4 edges to [[_COMMUNITY_test_config.py]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_DataLedger]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_test_security_fixes.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[BotConfig]] - degree 34, connects to 7 communities
- [[telegram_api_proxy()]] - degree 14, connects to 3 communities
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 2 communities
- [[dot-test_client_disconnect_returns_499()]] - degree 4, connects to 2 communities
- [[TestMultiBotContextvarRouting]] - degree 14, connects to 1 community
