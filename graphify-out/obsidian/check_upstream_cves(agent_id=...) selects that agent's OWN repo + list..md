---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report"
location: "L635"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report
---

# check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.

## Connections
- [[.test_check_scoped_to_agent_registry_and_repo()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report