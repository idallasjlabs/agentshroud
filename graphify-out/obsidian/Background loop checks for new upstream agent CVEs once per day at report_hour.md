---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Module Group 176"
location: "L506"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Module_Group_176
---

# Background loop: checks for new upstream agent CVEs once per day at report_hour

## Connections
- [[upstream_cve_check_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Module_Group_176
