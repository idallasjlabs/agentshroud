---
type: community
members: 37
---

# BotConfig

**Members:** 37 nodes

## Members
- [[dot-_allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-_mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[dot-test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the rebuild path…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry once its…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[BaseModel_4]] - code
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Declaration for a single bot encapsulated by AgentShroud. Required bot HTTP…]] - rationale - gateway/ingest_api/bot_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —…]] - rationale - gateway/tests/test_config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Repeated misses within the debounce window must not re-read secrets on every…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Tests for multi-bot Telegram token registry in the gateway route handler. Phase…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[The token registry is built lazily on the first telegram-api{path} request…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[_build_telegram_token_registry()]] - code - gateway/ingest_api/main.py
- [[_fake_read_secret()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[_fake_read_secret()_1]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
- [[telegram_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_bot_config_base_url()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_defaults_to_agentshroud_id()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_uses_explicit_override()]] - code - gateway/tests/test_config.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BotConfig
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TestTelegramTokenRegistry]]
- 1 edge to [[_COMMUNITY_TestTelegramProxyRouteMultiBot]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_TestMultiBotContextvarRouting]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_asyncio_5]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[test_telegram_proxy_multibot.py]] - degree 10, connects to 5 communities
- [[telegram_api_proxy()]] - degree 11, connects to 3 communities
- [[BotConfig]] - degree 18, connects to 2 communities
- [[bot_config.py]] - degree 3, connects to 2 communities
- [[dot-_mock_request()]] - degree 5, connects to 1 community
