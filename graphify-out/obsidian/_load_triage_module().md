---
source_file: "gateway/tests/test_agent_cve_registry.py"
type: "code"
community: "AgentRegistry"
location: "L589"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentRegistry
---

# _load_triage_module()

## Connections
- [[Import the triage script by path.      It must be registered in sys.modules befo]] - `rationale_for` [EXTRACTED]
- [[test_agent_cve_registry.py]] - `contains` [EXTRACTED]
- [[test_gap_reports_are_per_agent()]] - `calls` [EXTRACTED]
- [[test_untriageable_agents_are_refused_not_guessed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentRegistry