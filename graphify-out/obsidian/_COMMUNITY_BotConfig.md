---
type: community
members: 22
---

# BotConfig

**Members:** 22 nodes

## Members
- [[dot-base_url()]] - code - gateway/ingest_api/bot_config.py
- [[dot-resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[dot-test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[BaseModel_4]] - code
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Declaration for a single bot encapsulated by AgentShroud. Required bot HTTP…]] - rationale - gateway/ingest_api/bot_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —…]] - rationale - gateway/tests/test_config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Tests for multi-bot Telegram token registry in the gateway route handler. Phase…]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
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
- 6 edges to [[_COMMUNITY_GatewayConfig]]
- 2 edges to [[_COMMUNITY_TestMultiBotContextvarRouting]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestTelegramTokenRegistry]]
- 1 edge to [[_COMMUNITY_TestTelegramTokenRegistryRebuildOnMiss]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[test_telegram_proxy_multibot.py]] - degree 10, connects to 6 communities
- [[BotConfig]] - degree 18, connects to 3 communities
- [[dot-base_url()]] - degree 4, connects to 2 communities
- [[dot-resolved_container_name()]] - degree 3, connects to 1 community
- [[test_bot_config_base_url()]] - degree 3, connects to 1 community
