---
source_file: "scripts/migrate-cve-registry-ghsa.py"
type: "rationale"
community: "sync-cve-registry.py"
location: "L123"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# Fetch every published GitHub Security Advisory for *repo* (cursor-paginated).

## Connections
- [[fetch_advisories()]] - `rationale_for` [EXTRACTED]
- [[fetch_ghsa_advisories()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/sync-cve-registrypy