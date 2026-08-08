---
type: community
cohesion: 0.16
members: 18
---

# scripts/canary-deploy.sh

**Cohesion:** 0.16 - loosely connected
**Members:** 18 nodes

## Members
- [[Container runtime auto-detection contract (SCRUM-92)]] - rationale - docker/README.md
- [[_cr_plugin_works()]] - code - scripts/lib/container-runtime.sh
- [[canary-deploy.sh]] - code - scripts/canary-deploy.sh
- [[canary-deploy.sh script]] - code - scripts/canary-deploy.sh
- [[check()]] - code - scripts/post-deploy-check.sh
- [[container-runtime.sh]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh script]] - code - scripts/lib/container-runtime.sh
- [[container_runtime_engine()]] - code - scripts/lib/container-runtime.sh
- [[deploy_ref()]] - code - scripts/canary-deploy.sh
- [[detect_container_runtime()]] - code - scripts/lib/container-runtime.sh
- [[die()]] - code - scripts/canary-deploy.sh
- [[dockerversions.env (Pinned Vendor Versions)]] - code - docker/versions.env
- [[log()_5]] - code - scripts/canary-deploy.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[run()_4]] - code - scripts/canary-deploy.sh
- [[run_in_repo()]] - code - scripts/canary-deploy.sh
- [[scriptsasb (builddeploy helper, secret extraction)]] - code - scripts/asb

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/canary-deploysh
SORT file.name ASC
```
