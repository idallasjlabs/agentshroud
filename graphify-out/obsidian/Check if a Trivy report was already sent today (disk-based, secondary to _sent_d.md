---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L488"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Check if a Trivy report was already sent today (disk-based, secondary to _sent_d

## Connections
- [[_already_sent_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy