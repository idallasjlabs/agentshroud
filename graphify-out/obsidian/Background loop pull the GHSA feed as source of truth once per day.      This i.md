---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Gateway Security Module"
location: "L826"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# Background loop: pull the GHSA feed as source of truth once per day.      This i

## Connections
- [[ghsa_ingest_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module