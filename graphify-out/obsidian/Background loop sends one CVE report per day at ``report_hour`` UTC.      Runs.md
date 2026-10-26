---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Community 736"
location: "L402"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_736
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC.      Runs

## Connections
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_736