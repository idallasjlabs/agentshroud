---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Community 779"
location: "L767"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_779
---

# Background loop: checks for new upstream agent CVEs once per day at report_hour

## Connections
- [[upstream_cve_check_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_779