---
source_file: "gateway/tests/test_agent_cve_registry.py"
type: "rationale"
community: "Community 933"
location: "L132"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_933
---

# A real CVE always came from a GHSA advisory, so cve_id implies ghsa_id.

## Connections
- [[test_entry_with_cve_id_also_has_ghsa_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_933