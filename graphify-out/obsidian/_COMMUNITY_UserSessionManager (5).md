---
type: community
members: 9
---

# UserSessionManager (5)

**Members:** 9 nodes

## Members
- [[dot-test_beta_rc_alpha_are_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_downstream_rebuild_counter_is_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_empty_is_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_plain_releases_are_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2' is a real published OpenClaw release, not a prerelease marker — the…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Pre-release builds must never be shipped to production automatically.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[TestIsStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[True when ``version`` is a shippable release rather than a pre-release.]] - rationale - scripts/discover_upstream_versions.py
- [[is_stable()]] - code - scripts/discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_5
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_pick_latest_stable]]

## Top bridge nodes
- [[is_stable()]] - degree 7, connects to 2 communities
- [[TestIsStable]] - degree 6, connects to 1 community
