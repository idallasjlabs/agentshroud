---
type: community
cohesion: 0.18
members: 11
---

# BotConfig

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-_mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BotConfig
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_2]]

## Top bridge nodes
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 3 communities
