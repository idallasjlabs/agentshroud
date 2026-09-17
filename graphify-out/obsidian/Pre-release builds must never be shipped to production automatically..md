---
source_file: "gateway/tests/test_discover_upstream_versions.py"
type: "rationale"
community: "discover_upstream_versions.py"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/discover_upstream_versionspy
---

# Pre-release builds must never be shipped to production automatically.

## Connections
- [[TestIsStable]] - `rationale_for` [EXTRACTED]
- [[TestIsStable_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/discover_upstream_versionspy