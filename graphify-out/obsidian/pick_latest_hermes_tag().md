---
source_file: "scripts/discover_upstream_versions.py"
type: "code"
community: "run-standalone.sh"
location: "L109"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/run-standalonesh
---

# pick_latest_hermes_tag()

## Connections
- [[.test_empty_returns_none()_1]] - `calls` [INFERRED]
- [[.test_handles_four_component_tags()]] - `calls` [INFERRED]
- [[.test_picks_newest_date_tag()]] - `calls` [INFERRED]
- [[.test_real_hermes_tail_picks_latest_date()]] - `calls` [INFERRED]
- [[.test_rejects_floating_tags()]] - `calls` [INFERRED]
- [[Newest ``vYYYY.M.D`` Docker tag, ignoring floating tags.      'latest' and 'main]] - `rationale_for` [EXTRACTED]
- [[discover()]] - `calls` [EXTRACTED]
- [[discover_upstream_versions.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/run-standalonesh