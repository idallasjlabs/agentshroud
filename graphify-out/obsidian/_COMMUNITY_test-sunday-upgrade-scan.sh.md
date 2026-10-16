---
type: community
cohesion: 0.21
members: 15
---

# test-sunday-upgrade-scan.sh

**Cohesion:** 0.21 - loosely connected
**Members:** 15 nodes

## Members
- [[check()_9]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[check()_10]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh
- [[extract_default()]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[make_apply_bin()]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[make_fake_repo()]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[run_apply()]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[run_gate()]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[smoke.sh Startup Smoke Runner]] - code - scripts/smoke.sh
- [[test-sunday-upgrade-scan.sh]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[test-sunday-upgrade-scan.sh script]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[test_openclaw_model_provider_consistency.sh]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[test_openclaw_model_provider_consistency.sh script]] - code - tests/startup_smoke/test_openclaw_model_provider_consistency.sh
- [[test_openclaw_readiness_retry.sh]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh
- [[test_openclaw_readiness_retry.sh script]] - code - tests/startup_smoke/test_openclaw_readiness_retry.sh
- [[write_fake()]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test-sunday-upgrade-scansh
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_AgentTarget_3]]

## Top bridge nodes
- [[test-sunday-upgrade-scan.sh]] - degree 10, connects to 1 community
- [[smoke.sh Startup Smoke Runner]] - degree 4, connects to 1 community
