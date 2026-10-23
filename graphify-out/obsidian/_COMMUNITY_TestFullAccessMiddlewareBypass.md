---
type: community
cohesion: 0.11
members: 26
---

# TestFullAccessMiddlewareBypass

**Cohesion:** 0.11 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-test_beta_rc_alpha_are_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_downstream_counter_sorts_above_its_base_release()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_downstream_rebuild_counter_is_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_empty_is_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_empty_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_ignores_prereleases_even_when_numerically_highest()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_no_stable_versions_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_numeric_ordering_not_lexicographic()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_picks_the_highest_stable_version()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_plain_releases_are_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_real_openclaw_tail_picks_2026_9_4()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_unparseable_entries_are_skipped_not_crashed_on()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[2026.10.1' must beat '2026.9.4' — string compare gets this wrong.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2 is a patch published after 2026.7.1, so it must win.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2' is a real published OpenClaw release, not a prerelease marker — the…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Newest stable release from an npm version list, or None.]] - rationale - scripts/discover_upstream_versions.py
- [[Pre-release builds must never be shipped to production automatically.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Selecting the newest shippable npm release.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[TestIsStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[TestPickLatestStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[The actual npm tail as of 2026-09-15.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[True when ``version`` is a shippable release rather than a pre-release.]] - rationale - scripts/discover_upstream_versions.py
- [[Version - comparable int tuple, or None if not numeric. A trailing ``-N``…]] - rationale - scripts/discover_upstream_versions.py
- [[_sortable()]] - code - scripts/discover_upstream_versions.py
- [[is_stable()]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable()]] - code - scripts/discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestFullAccessMiddlewareBypass
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Sunday Upgrade prompt]]

## Top bridge nodes
- [[pick_latest_stable()]] - degree 13, connects to 1 community
- [[TestPickLatestStable]] - degree 10, connects to 1 community
- [[is_stable()]] - degree 7, connects to 1 community
- [[TestIsStable]] - degree 6, connects to 1 community
- [[_sortable()]] - degree 3, connects to 1 community
