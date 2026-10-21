---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "sync-cve-registry.py"
location: "L998"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# Check if the GHSA ingest already ran today (disk-based, secondary guard).

## Connections
- [[_already_ingested_ghsa_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/sync-cve-registrypy
