---
type: community
cohesion: 0.05
members: 45
---

# BotConfig

**Cohesion:** 0.05 - loosely connected
**Members:** 45 nodes

## Members
- [[dot-_make_proxy()_1]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_bot_id_falls_back_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_bot_id_returns_contextvar_when_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_send_token_returns_contextvar_inside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_active_send_token_returns_default_outside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
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
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[After proxy_request returns, _inbound_bot_token is reset to its prior value.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Cross-bot reply misrouting fix via contextvar-scoped send token]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_bot_id() returns 'openclaw'.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_send_token() returns self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestMultiBotContextvarRouting]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Tests for per-request bot token routing via contextvars.      Regression suite f]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The contextvar set by proxy_request is visible throughout _proxy_request_impl.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_id is set, _active_bot_id() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_token is set, _active_send_token() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Without contextvar, _send_telegram_text uses self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[_send_telegram_text uses the inbound contextvar token, not self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BotConfig
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 3 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 4 communities
- [[TestTelegramTokenRegistry]] - degree 13, connects to 3 communities
- [[TestMultiBotContextvarRouting]] - degree 14, connects to 2 communities
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 2 communities
