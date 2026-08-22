---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report (security)"
location: "L909"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# Background loop: pull the GHSA feed as source of truth once per day.      This i

## Connections
- [[ghsa_ingest_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report_security