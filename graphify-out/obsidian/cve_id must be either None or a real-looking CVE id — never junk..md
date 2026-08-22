---
source_file: "gateway/tests/test_agent_cve_registry.py"
type: "rationale"
community: "Agent Cve Registry"
location: "L116"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_Cve_Registry
---

# cve_id must be either None or a real-looking CVE id — never junk.

## Connections
- [[test_cve_id_field_only_holds_real_looking_cve_ids()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_Cve_Registry