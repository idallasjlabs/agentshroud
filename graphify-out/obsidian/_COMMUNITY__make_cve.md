---
type: community
members: 29
---

# _make_cve

**Members:** 29 nodes

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
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME_1]] - code - docker/bots/hermes/start.sh
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - rationale - docker/bots/hermes/start.sh
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
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
- [[telegram_api_proxy()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_cve
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 3 edges to [[_COMMUNITY_SecureBrowser (2)]]
- 2 edges to [[_COMMUNITY_api.py (2)]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_GroupConfig]]
- 2 edges to [[_COMMUNITY_TestFabricatedSecurityNotice (2)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 1 edge to [[_COMMUNITY__make_cve (2)]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_make_event]]

## Top bridge nodes
- [[telegram_api_proxy()]] - degree 21, connects to 6 communities
- [[TestTelegramTokenRegistryRebuildOnMiss]] - degree 10, connects to 3 communities
- [[start.sh (Hermes s6 main program  startup wrapper)]] - degree 17, connects to 2 communities
- [[_telegram_send]] - degree 6, connects to 2 communities
- [[dot-_mock_request()]] - degree 5, connects to 1 community
