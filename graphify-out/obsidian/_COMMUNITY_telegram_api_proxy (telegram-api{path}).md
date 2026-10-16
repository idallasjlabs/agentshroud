---
type: community
cohesion: 0.06
members: 51
---

# telegram_api_proxy (/telegram-api/{path})

**Cohesion:** 0.06 - loosely connected
**Members:** 51 nodes

## Members
- [[dot-_allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME_1]] - code - docker/bots/hermes/start.sh
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[XDG_CACHE_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_DATA_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_STATE_HOME]] - code - docker/bots/hermes/start.sh
- [[_build_telegram_token_registry]] - code - gateway/ingest_api/main.py
- [[_count_recent_restarts()]] - code - docker/bots/hermes/crashwatch.sh
- [[_email_owner]] - code - docker/bots/hermes/start.sh
- [[_log()]] - code - docker/bots/hermes/crashwatch.sh
- [[_read_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[_release_telegram_lock]] - code - docker/bots/hermes/start.sh
- [[_telegram_alert()]] - code - docker/bots/hermes/crashwatch.sh
- [[_telegram_bot_token]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready]] - code - docker/bots/hermes/start.sh
- [[_telegram_send]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo]] - code - docker/bots/hermes/start.sh
- [[_write_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh script]] - code - docker/bots/hermes/crashwatch.sh
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
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_BotConfig_1]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]

## Top bridge nodes
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 5 communities
- [[telegram_api_proxy (telegram-api{path})]] - degree 21, connects to 4 communities
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 17, connects to 3 communities
- [[TestTelegramTokenRegistry]] - degree 13, connects to 2 communities
- [[TestTelegramTokenRegistryRebuildOnMiss]] - degree 10, connects to 2 communities
