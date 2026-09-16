---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Community 124"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_124
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC. Runs…

## Connections
- [[cve_report_scheduler]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_124