---
source_file: "scripts/sync-cve-registry.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L797"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Read a vendor version from docker/versions.env — the single source of     truth

## Connections
- [[_read_pinned_version()]] - `rationale_for` [EXTRACTED]
- [[_run_nvd_sync()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite