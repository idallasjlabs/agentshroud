---
type: community
cohesion: 0.06
members: 39
---

# Community 180

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-base_url()]] - code - gateway/ingest_api/bot_config.py
- [[dot-resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[dot-test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - rationale - gateway/ingest_api/bot_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —     regres]] - rationale - gateway/tests/test_config.py
- [[Load the real agentshroud.yaml when present (deployment host), else the     comm]] - rationale - gateway/tests/test_config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[RouterConfig must accept the Hermes Docker service hostname.]] - rationale - gateway/tests/test_config.py
- [[RouterConfig should accept single-label Docker service hostnames.]] - rationale - gateway/tests/test_config.py
- [[Test PII entity type mapping]] - rationale - gateway/tests/test_config.py
- [[Test loading configuration from agentshroud.yaml (or the committed example).]] - rationale - gateway/tests/test_config.py
- [[Test that configuration has sensible defaults]] - rationale - gateway/tests/test_config.py
- [[Test that load_config() populates bots — from YAML or backward-compat default.]] - rationale - gateway/tests/test_config.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When agentshroud.yaml declares hermes, load_config() populates it in bots.]] - rationale - gateway/tests/test_config.py
- [[_bot_service_names() must use each bot's real container name, not a     hardcode]] - rationale - gateway/tests/test_config.py
- [[_load_config()]] - code - gateway/tests/test_config.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_180
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 6 edges to [[_COMMUNITY_Community 161]]
- 4 edges to [[_COMMUNITY_Multi-Agent Router & Chat UI]]
- 3 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 3 edges to [[_COMMUNITY_Approval Queue (WebSocket)]]
- 2 edges to [[_COMMUNITY_Community 157]]
- 2 edges to [[_COMMUNITY_Runtime Security Comparison & Intel Report]]
- 1 edge to [[_COMMUNITY_Community 153]]
- 1 edge to [[_COMMUNITY_Gateway Config & PII Sanitizer]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 1 edge to [[_COMMUNITY_Community 461]]
- 1 edge to [[_COMMUNITY_Collaborator Activity & Telegram Proxy]]

## Top bridge nodes
- [[BotConfig]] - degree 34, connects to 10 communities
- [[test_config.py]] - degree 18, connects to 4 communities
- [[TestTelegramBotConfigTokenSecretField]] - degree 8, connects to 2 communities
- [[_load_config()]] - degree 6, connects to 1 community
- [[test_bot_service_names_uses_resolved_container_name()]] - degree 3, connects to 1 community