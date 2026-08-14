---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L196"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Agent can write to /tmp for temporary files.

## Connections
- [[.test_tmp_write_allowed()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core