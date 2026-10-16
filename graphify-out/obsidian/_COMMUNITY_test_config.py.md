---
type: community
cohesion: 0.09
members: 27
---

# test_config.py

**Cohesion:** 0.09 - loosely connected
**Members:** 27 nodes

## Members
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —     regres]] - rationale - gateway/tests/test_config.py
- [[Load the real agentshroud.yaml when present (deployment host), else the     comm]] - rationale - gateway/tests/test_config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[Return real container names for all configured bots (e.g.     'agentshroud-open]] - rationale - gateway/web/api.py
- [[RouterConfig must accept the Hermes Docker service hostname.]] - rationale - gateway/tests/test_config.py
- [[RouterConfig should accept single-label Docker service hostnames.]] - rationale - gateway/tests/test_config.py
- [[Test PII entity type mapping]] - rationale - gateway/tests/test_config.py
- [[Test loading configuration from agentshroud.yaml (or the committed example).]] - rationale - gateway/tests/test_config.py
- [[Test that configuration has sensible defaults]] - rationale - gateway/tests/test_config.py
- [[Test that load_config() populates bots — from YAML or backward-compat default.]] - rationale - gateway/tests/test_config.py
- [[When agentshroud.yaml declares hermes, load_config() populates it in bots.]] - rationale - gateway/tests/test_config.py
- [[_bot_service_names()]] - code - gateway/web/api.py
- [[_bot_service_names() must use each bot's real container name, not a     hardcode]] - rationale - gateway/tests/test_config.py
- [[_load_config()]] - code - gateway/tests/test_config.py
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
TABLE source_file, type FROM #community/test_configpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_load_config]]
- 5 edges to [[_COMMUNITY_DataLedger]]
- 4 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY__get_engine]]
- 2 edges to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[test_config.py]] - degree 18, connects to 3 communities
- [[_bot_service_names()]] - degree 8, connects to 3 communities
- [[_load_config()]] - degree 6, connects to 1 community
- [[test_bot_config_base_url()]] - degree 3, connects to 1 community
- [[test_bot_config_resolved_container_name_defaults_to_agentshroud_id()]] - degree 3, connects to 1 community
