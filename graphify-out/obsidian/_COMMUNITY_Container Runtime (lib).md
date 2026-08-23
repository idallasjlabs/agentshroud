---
type: community
cohesion: 0.40
members: 6
---

# Container Runtime (lib)

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[Container runtime auto-detection contract (SCRUM-92)]] - rationale - docker/README.md
- [[_cr_plugin_works()]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh script]] - code - scripts/lib/container-runtime.sh
- [[container_runtime_engine()]] - code - scripts/lib/container-runtime.sh
- [[detect_container_runtime()]] - code - scripts/lib/container-runtime.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Container_Runtime_lib
SORT file.name ASC
```
