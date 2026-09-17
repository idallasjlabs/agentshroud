---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L965"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Background loop: pull the GHSA feed as source of truth once per day.      This i

## Connections
- [[ghsa_ingest_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy