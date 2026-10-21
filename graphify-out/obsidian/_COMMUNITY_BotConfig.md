---
type: community
members: 45
---

# BotConfig

**Members:** 45 nodes

## Members
- [[dot-_mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-base_url()]] - code - gateway/ingest_api/bot_config.py
- [[dot-resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[dot-test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - rationale - gateway/ingest_api/bot_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —     regres]] - rationale - gateway/tests/test_config.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
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
- 12 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 5 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_BotConfig (2)]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[BotConfig]] - degree 34, connects to 7 communities
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 4 communities
- [[TestTelegramTokenRegistry]] - degree 13, connects to 2 communities
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 1 community
- [[TestTelegramBotConfigTokenSecretField]] - degree 8, connects to 1 community
