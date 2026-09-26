---
source_file: "gateway/tests/test_agent_cve_registry.py"
type: "rationale"
community: "AgentRegistry"
location: "L616"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentRegistry
---

# A single shared output path makes multi-agent coverage impossible.

## Connections
- [[test_gap_reports_are_per_agent()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentRegistry