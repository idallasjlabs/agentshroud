---
type: community
cohesion: 0.07
members: 42
---

# _seed_cron

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[.test_beta_rc_alpha_are_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_downstream_counter_sorts_above_its_base_release()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_downstream_rebuild_counter_is_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_empty_is_not_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_empty_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_ignores_prereleases_even_when_numerically_highest()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_no_stable_versions_returns_none()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_numeric_ordering_not_lexicographic()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_picks_the_highest_stable_version()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_plain_releases_are_stable()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_real_openclaw_tail_picks_2026_9_4()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[.test_unparseable_entries_are_skipped_not_crashed_on()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[2026.10.1' must beat '2026.9.4' — string compare gets this wrong.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2 is a patch published after 2026.7.1, so it must win.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[2026.7.1-2' is a real published OpenClaw release, not a prerelease         marke]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[All published versions of an npm package (via the npm CLI).]] - rationale - scripts/discover_upstream_versions.py
- [[Any_76]] - code - scripts/discover_upstream_versions.py
- [[Newest stable release from an npm version list, or None.]] - rationale - scripts/discover_upstream_versions.py
- [[No-Op Upgrade Gate (7-week silent no-op)]] - concept - scripts/sunday-upgrade-apply.sh
- [[Pre-release builds must never be shipped to production automatically.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Resolve the latest stable release of each wrapped tool.      Each entry is indep]] - rationale - scripts/discover_upstream_versions.py
- [[Selecting the newest shippable npm release.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Tag records for a Docker Hub repository, newest first.]] - rationale - scripts/discover_upstream_versions.py
- [[TestIsStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[TestPickLatestStable]] - code - gateway/tests/test_discover_upstream_versions.py
- [[Tests for scriptsdiscover_upstream_versions.py — latest-release discovery.  Cop]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[The actual npm tail as of 2026-09-15.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[True when ``version`` is a shippable release rather than a pre-release.]] - rationale - scripts/discover_upstream_versions.py
- [[Version - comparable int tuple, or None if not numeric.      A trailing ``-N``]] - rationale - scripts/discover_upstream_versions.py
- [[_digest_for_tag()]] - code - scripts/discover_upstream_versions.py
- [[_sortable()]] - code - scripts/discover_upstream_versions.py
- [[discover()]] - code - scripts/discover_upstream_versions.py
- [[discover_upstream_versions.py]] - code - scripts/discover_upstream_versions.py
- [[fetch_dockerhub_tags()]] - code - scripts/discover_upstream_versions.py
- [[fetch_npm_versions()]] - code - scripts/discover_upstream_versions.py
- [[is_stable]] - code - scripts/discover_upstream_versions.py
- [[is_stable()]] - code - scripts/discover_upstream_versions.py
- [[main()_17]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_hermes_tag]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable()]] - code - scripts/discover_upstream_versions.py
- [[test_discover_upstream_versions.py]] - code - gateway/tests/test_discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_seed_cron
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_run-standalone.sh]]
- 3 edges to [[_COMMUNITY_DraftEntry]]
- 2 edges to [[_COMMUNITY_OutputSchemaEnforcer]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.7.0 Enforcement Audit Results]]

## Top bridge nodes
- [[discover_upstream_versions.py]] - degree 12, connects to 3 communities
- [[test_discover_upstream_versions.py]] - degree 8, connects to 2 communities
- [[No-Op Upgrade Gate (7-week silent no-op)]] - degree 3, connects to 2 communities
- [[discover()]] - degree 9, connects to 1 community
- [[main()_17]] - degree 3, connects to 1 community