---
source_file: "scripts/sync-cve-registry.py"
type: "rationale"
community: "scripts/sync-cve-registry.py"
location: "L797"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# Read a vendor version from docker/versions.env — the single source of     truth

## Connections
- [[_read_pinned_version()]] - `rationale_for` [EXTRACTED]
- [[_run_nvd_sync()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/sync-cve-registrypy