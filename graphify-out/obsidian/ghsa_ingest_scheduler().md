---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "Gateway Security Module"
location: "L819"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# ghsa_ingest_scheduler()

## Connections
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - `rationale_for` [EXTRACTED]
- [[_already_ingested_ghsa_today()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module