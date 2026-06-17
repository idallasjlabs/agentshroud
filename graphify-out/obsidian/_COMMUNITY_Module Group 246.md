---
type: community
cohesion: 0.12
members: 19
---

# Module Group 246

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Load the real agentshroud.yaml when present (deployment host), else the     comm]] - rationale - gateway/tests/test_config.py
- [[RouterConfig must accept the Hermes Docker service hostname.]] - rationale - gateway/tests/test_config.py
- [[RouterConfig should accept single-label Docker service hostnames.]] - rationale - gateway/tests/test_config.py
- [[Test PII entity type mapping]] - rationale - gateway/tests/test_config.py
- [[Test loading configuration from agentshroud.yaml (or the committed example).]] - rationale - gateway/tests/test_config.py
- [[Test that configuration has sensible defaults]] - rationale - gateway/tests/test_config.py
- [[Test that load_config() populates bots — from YAML or backward-compat default.]] - rationale - gateway/tests/test_config.py
- [[When agentshroud.yaml declares hermes, load_config() populates it in bots.]] - rationale - gateway/tests/test_config.py
- [[_load_config()]] - code - gateway/tests/test_config.py
- [[test_bot_config_base_url()]] - code - gateway/tests/test_config.py
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
TABLE source_file, type FROM #community/Module_Group_246
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 4 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 127]]

## Top bridge nodes
- [[test_config.py]] - degree 14, connects to 3 communities
- [[_load_config()]] - degree 6, connects to 1 community
- [[test_bot_config_base_url()]] - degree 3, connects to 1 community
- [[test_config_defaults()]] - degree 3, connects to 1 community
- [[test_entity_type_mapping()]] - degree 3, connects to 1 community