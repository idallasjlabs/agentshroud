---
type: community
cohesion: 0.33
members: 10
---

# Switch Model (scripts)

**Cohesion:** 0.33 - loosely connected
**Members:** 10 nodes

## Members
- [[asb (AgentShroud bot helper)]] - code - scripts/asb
- [[ensure_local_model_available()]] - code - scripts/switch_model.sh
- [[normalize_cloud_ref()]] - code - scripts/switch_model.sh
- [[preflight_local()]] - code - scripts/switch_model.sh
- [[switch_model.sh]] - code - scripts/switch_model.sh
- [[switch_model.sh script]] - code - scripts/switch_model.sh
- [[upsert_env_value()]] - code - scripts/switch_model.sh
- [[usage()_4]] - code - scripts/switch_model.sh
- [[verify_both_bots_healthy()]] - code - scripts/switch_model.sh
- [[wait_for_local_model()]] - code - scripts/switch_model.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Switch_Model_scripts
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Hermes Model Resolver]]
- 1 edge to [[_COMMUNITY_Anthropic Openai Translator]]

## Top bridge nodes
- [[switch_model.sh]] - degree 12, connects to 2 communities