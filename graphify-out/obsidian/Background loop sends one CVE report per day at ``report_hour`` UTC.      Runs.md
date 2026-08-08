---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Gateway Security Module"
location: "L318"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC.      Runs

## Connections
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module