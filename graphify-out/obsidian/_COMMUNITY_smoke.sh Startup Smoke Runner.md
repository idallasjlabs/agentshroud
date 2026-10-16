---
type: community
cohesion: 0.33
members: 7
---

# smoke.sh Startup Smoke Runner

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[check()_2]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh
- [[extract_default()]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[smoke.sh Startup Smoke Runner]] - code - scripts/smoke.sh
- [[test_openclaw_model_provider_consistency.sh]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[test_openclaw_model_provider_consistency.sh script]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[test_openclaw_readiness_retry.sh]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh
- [[test_openclaw_readiness_retry.sh script]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/smokesh_Startup_Smoke_Runner
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test-sunday-upgrade-scan.sh]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]

## Top bridge nodes
- [[smoke.sh Startup Smoke Runner]] - degree 4, connects to 2 communities
