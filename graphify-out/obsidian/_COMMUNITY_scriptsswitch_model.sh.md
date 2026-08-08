---
type: community
cohesion: 0.39
members: 9
---

# scripts/switch_model.sh

**Cohesion:** 0.39 - loosely connected
**Members:** 9 nodes

## Members
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
TABLE source_file, type FROM #community/scripts/switch_modelsh
SORT file.name ASC
```
