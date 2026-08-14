---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Agent cannot write to /usr/bin/ system binaries.

## Connections
- [[.test_usr_bin_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core