---
type: community
cohesion: 0.07
members: 42
---

# telegram_api_proxy (/telegram-api/{path})

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-_allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME]] - code - docker/bots/hermes/start.sh
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[XDG_CACHE_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_DATA_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_STATE_HOME]] - code - docker/bots/hermes/start.sh
- [[_build_telegram_token_registry]] - code - gateway/ingest_api/main.py
- [[_email_owner]] - code - docker/bots/hermes/start.sh
- [[_release_telegram_lock]] - code - docker/bots/hermes/start.sh
- [[_telegram_bot_token]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready]] - code - docker/bots/hermes/start.sh
- [[_telegram_send]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo]] - code - docker/bots/hermes/start.sh
- [[start.sh (Hermes s6 main program  startup wrapper)]] - code - docker/bots/hermes/start.sh
- [[start.sh script]] - code - docker/bots/hermes/start.sh
- [[telegram_api_proxy (telegram-api{path})]] - code - gateway/ingest_api/main.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_api_proxy_/telegram-api/path
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 2 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)_1]]
- 2 edges to [[_COMMUNITY_AsyncMock_1]]
- 2 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)_1]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_Data Validation (DATA-VAL)]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_AgentTarget_3]]

## Top bridge nodes
- [[telegram_api_proxy (telegram-api{path})]] - degree 21, connects to 6 communities
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 5 communities
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 17, connects to 3 communities
- [[TestTelegramTokenRegistryRebuildOnMiss]] - degree 10, connects to 2 communities
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 2 communities
