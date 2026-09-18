---
type: community
cohesion: 0.21
members: 16
---

# pick_latest_hermes_tag()

**Cohesion:** 0.21 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_empty_returns_none()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_empty_returns_none()_3]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_handles_four_component_tags()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_handles_four_component_tags()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_picks_newest_date_tag()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_picks_newest_date_tag()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_real_hermes_tail_picks_latest_date()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_real_hermes_tail_picks_latest_date()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_rejects_floating_tags()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_rejects_floating_tags()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[Hermes publishes date-based image tags (vYYYY.M.D).]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Newest ``vYYYY.M.D`` Docker tag, ignoring floating tags. 'latest' and 'main'…]] - rationale - scripts/discover_upstream_versions.py
- [[TestPickLatestHermesTag]] - code - gateway/tests/test_discover_upstream_versions.py
- [[TestPickLatestHermesTag_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[latest''main' float and would defeat the whole point of pinning.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[pick_latest_hermes_tag()]] - code - scripts/discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pick_latest_hermes_tag
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_sunday-upgrade]]

## Top bridge nodes
- [[pick_latest_hermes_tag()]] - degree 13, connects to 1 community
- [[TestPickLatestHermesTag]] - degree 7, connects to 1 community
- [[TestPickLatestHermesTag_1]] - degree 7, connects to 1 community