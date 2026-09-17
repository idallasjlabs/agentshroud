---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L948"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Check if the GHSA ingest already ran today (disk-based, secondary guard).

## Connections
- [[_already_ingested_ghsa_today]] - `rationale_for` [EXTRACTED]
- [[_already_ingested_ghsa_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy