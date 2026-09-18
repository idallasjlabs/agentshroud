---
source_file: "gateway/tests/test_discover_upstream_versions.py"
type: "rationale"
community: "pick_latest_hermes_tag()"
location: "L114"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/pick_latest_hermes_tag
---

# latest'/'main' float and would defeat the whole point of pinning.

## Connections
- [[.test_rejects_floating_tags()]] - `rationale_for` [EXTRACTED]
- [[.test_rejects_floating_tags()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/pick_latest_hermes_tag