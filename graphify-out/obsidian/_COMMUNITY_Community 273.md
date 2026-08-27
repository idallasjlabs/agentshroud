---
type: community
members: 83
---

# Community 273

**Members:** 83 nodes

## Members
- [[._allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[._mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[._mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.base_url()]] - code - gateway/ingest_api/bot_config.py
- [[.resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[.test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[.test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - rationale - gateway/ingest_api/bot_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —     regres]] - rationale - gateway/tests/test_config.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Load the real agentshroud.yaml when present (deployment host), else the     comm]] - rationale - gateway/tests/test_config.py
- [[Map agentshroud.yaml entity names to Presidiointernal entity names]] - rationale - gateway/ingest_api/config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Return real container names for all configured bots (e.g.     'agentshroud-open]] - rationale - gateway/web/api.py
- [[RouterConfig must accept the Hermes Docker service hostname.]] - rationale - gateway/tests/test_config.py
- [[RouterConfig should accept single-label Docker service hostnames.]] - rationale - gateway/tests/test_config.py
- [[Test PII entity type mapping]] - rationale - gateway/tests/test_config.py
- [[Test loading configuration from agentshroud.yaml (or the committed example).]] - rationale - gateway/tests/test_config.py
- [[Test that configuration has sensible defaults]] - rationale - gateway/tests/test_config.py
- [[Test that load_config() populates bots — from YAML or backward-compat default.]] - rationale - gateway/tests/test_config.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When agentshroud.yaml declares hermes, load_config() populates it in bots.]] - rationale - gateway/tests/test_config.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[_bot_service_names()]] - code - gateway/web/api.py
- [[_bot_service_names() must use each bot's real container name, not a     hardcode]] - rationale - gateway/tests/test_config.py
- [[_build_telegram_token_registry()]] - code - gateway/ingest_api/main.py
- [[_entity_type_mapping()]] - code - gateway/ingest_api/config.py
- [[_load_config()]] - code - gateway/tests/test_config.py
- [[telegram_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_bot_config_base_url()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_defaults_to_agentshroud_id()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_uses_explicit_override()]] - code - gateway/tests/test_config.py
- [[test_bot_service_names_uses_resolved_container_name()]] - code - gateway/tests/test_config.py
- [[test_config.py]] - code - gateway/tests/test_config.py
- [[test_config_defaults()]] - code - gateway/tests/test_config.py
- [[test_entity_type_mapping()]] - code - gateway/tests/test_config.py
- [[test_load_config()]] - code - gateway/tests/test_config.py
- [[test_load_config_has_bots()]] - code - gateway/tests/test_config.py
- [[test_load_config_registers_hermes()]] - code - gateway/tests/test_config.py
- [[test_router_config_accepts_docker_service_hostname()]] - code - gateway/tests/test_config.py
- [[test_router_config_accepts_hermes_hostname()]] - code - gateway/tests/test_config.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_273
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 1]]
- 6 edges to [[_COMMUNITY_Community 1325]]
- 5 edges to [[_COMMUNITY_Community 34]]
- 5 edges to [[_COMMUNITY_Community 4]]
- 4 edges to [[_COMMUNITY_Community 45]]
- 3 edges to [[_COMMUNITY_Community 24]]
- 3 edges to [[_COMMUNITY_Community 9]]
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 445]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 134]]

## Top bridge nodes
- [[BotConfig]] - degree 34, connects to 7 communities
- [[telegram_api_proxy()]] - degree 14, connects to 3 communities
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 3 communities
- [[test_config.py]] - degree 18, connects to 2 communities
- [[_bot_service_names()]] - degree 8, connects to 2 communities