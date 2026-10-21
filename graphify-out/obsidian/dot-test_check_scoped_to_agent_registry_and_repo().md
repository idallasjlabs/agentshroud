---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)"
location: "L783"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
---

# .test_check_scoped_to_agent_registry_and_repo()

## Connections
- [[TestPerAgentUpstreamChecks]] - `method` [EXTRACTED]
- [[_fake_check()]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
