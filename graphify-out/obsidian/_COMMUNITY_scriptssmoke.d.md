---
type: community
cohesion: 0.31
members: 9
---

# scripts/smoke.d

**Cohesion:** 0.31 - loosely connected
**Members:** 9 nodes

## Members
- [[check()_2]] - code - scripts/smoke.d/test-container-runtime.sh
- [[container-runtime.sh (detection shim)]] - code - scripts/lib/container-runtime.sh
- [[make_fake_bin()]] - code - scripts/smoke.d/test-container-runtime.sh
- [[run_detect()]] - code - scripts/smoke.d/test-container-runtime.sh
- [[run_test()]] - code - scripts/smoke.sh
- [[smoke.sh]] - code - scripts/smoke.sh
- [[smoke.sh script]] - code - scripts/smoke.sh
- [[test-container-runtime.sh]] - code - scripts/smoke.d/test-container-runtime.sh
- [[test-container-runtime.sh script]] - code - scripts/smoke.d/test-container-runtime.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/smoked
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_scriptssync-llm-settings.sh]]

## Top bridge nodes
- [[smoke.sh]] - degree 4, connects to 1 community