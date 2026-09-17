---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "TestPerAgentUpstreamChecks"
location: "L635"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestPerAgentUpstreamChecks
---

# check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.

## Connections
- [[.test_check_scoped_to_agent_registry_and_repo()]] - `rationale_for` [EXTRACTED]
- [[.test_check_scoped_to_agent_registry_and_repo()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestPerAgentUpstreamChecks