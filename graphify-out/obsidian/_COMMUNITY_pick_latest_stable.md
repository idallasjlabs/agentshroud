---
type: community
members: 17
---

# pick_latest_stable

**Members:** 17 nodes

## Members
- [[dot-test_downstream_counter_sorts_above_its_base_release()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_empty_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_ignores_prereleases_even_when_numerically_highest()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_no_stable_versions_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_numeric_ordering_not_lexicographic()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_picks_the_highest_stable_version()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_real_openclaw_tail_picks_2026_9_4()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_unparseable_entries_are_skipped_not_crashed_on()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[2026.10.1' must beat '2026.9.4' — string compare gets this wrong.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2 is a patch published after 2026.7.1, so it must win.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Newest stable release from an npm version list, or None.]] - rationale - scripts/discover_upstream_versions.py
- [[Selecting the newest shippable npm release.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[TestPickLatestStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[The actual npm tail as of 2026-09-15.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Version - comparable int tuple, or None if not numeric. A trailing ``-N``…]] - rationale - scripts/discover_upstream_versions.py
- [[_sortable()]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable()]] - code - scripts/discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pick_latest_stable
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_UserSessionManager (5)]]

## Top bridge nodes
- [[pick_latest_stable()]] - degree 13, connects to 2 communities
- [[TestPickLatestStable]] - degree 10, connects to 1 community
- [[_sortable()]] - degree 3, connects to 1 community
