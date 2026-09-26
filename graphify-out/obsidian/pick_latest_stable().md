---
source_file: "scripts/discover_upstream_versions.py"
type: "code"
community: "_seed_cron"
location: "L94"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_seed_cron
---

# pick_latest_stable()

## Connections
- [[.test_downstream_counter_sorts_above_its_base_release()]] - `calls` [INFERRED]
- [[.test_empty_returns_none()]] - `calls` [INFERRED]
- [[.test_ignores_prereleases_even_when_numerically_highest()]] - `calls` [INFERRED]
- [[.test_no_stable_versions_returns_none()]] - `calls` [INFERRED]
- [[.test_numeric_ordering_not_lexicographic()]] - `calls` [INFERRED]
- [[.test_picks_the_highest_stable_version()]] - `calls` [INFERRED]
- [[.test_real_openclaw_tail_picks_2026_9_4()]] - `calls` [INFERRED]
- [[.test_unparseable_entries_are_skipped_not_crashed_on()]] - `calls` [INFERRED]
- [[Newest stable release from an npm version list, or None.]] - `rationale_for` [EXTRACTED]
- [[_sortable()]] - `calls` [EXTRACTED]
- [[discover()]] - `calls` [EXTRACTED]
- [[discover_upstream_versions.py]] - `contains` [EXTRACTED]
- [[is_stable()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/_seed_cron