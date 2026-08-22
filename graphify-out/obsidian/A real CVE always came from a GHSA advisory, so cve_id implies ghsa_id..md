---
source_file: "gateway/tests/test_agent_cve_registry.py"
type: "rationale"
community: "Agent Cve Registry"
location: "L132"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_Cve_Registry
---

# A real CVE always came from a GHSA advisory, so cve_id implies ghsa_id.

## Connections
- [[test_entry_with_cve_id_also_has_ghsa_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_Cve_Registry