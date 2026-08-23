---
type: community
cohesion: 0.18
members: 11
---

# Telegram Proxy Multibot

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[._mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Proxy_Multibot
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]

## Top bridge nodes
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 2 communities