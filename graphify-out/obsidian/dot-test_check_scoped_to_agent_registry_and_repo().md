---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 82"
location: "L634"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_82
---

# .test_check_scoped_to_agent_registry_and_repo()

## Connections
- [[TestPerAgentUpstreamChecks]] - `method` [EXTRACTED]
- [[_fake_check()]] - `indirect_call` [INFERRED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_82