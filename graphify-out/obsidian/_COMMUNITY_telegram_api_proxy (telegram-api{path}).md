---
type: community
cohesion: 0.10
members: 36
---

# telegram_api_proxy (/telegram-api/{path})

**Cohesion:** 0.10 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-_allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Crash backoff escalation (rolling 10-minute start window)]] - rationale - docker/bots/hermes/start.sh
- [[Dev Hermes polling prod's Hermes Telegram bot]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME_1]] - code - docker/bots/hermes/start.sh
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[XDG_CACHE_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_DATA_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_STATE_HOME]] - code - docker/bots/hermes/start.sh
- [[_build_telegram_token_registry]] - code - gateway/ingest_api/main.py
- [[_count_recent_restarts()]] - code - docker/bots/hermes/crashwatch.sh
- [[_email_owner]] - code - docker/bots/hermes/start.sh
- [[_log()_1]] - code - docker/bots/hermes/crashwatch.sh
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_api_proxy_/telegram-api/path
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 5 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]

## Top bridge nodes
- [[telegram_api_proxy (telegram-api{path})]] - degree 21, connects to 5 communities
- [[TestTelegramTokenRegistryRebuildOnMiss]] - degree 10, connects to 3 communities
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 18, connects to 2 communities
- [[_telegram_send]] - degree 6, connects to 1 community
- [[dot-_mock_request()]] - degree 5, connects to 1 community
