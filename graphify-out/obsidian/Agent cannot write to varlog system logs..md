---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L178"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Agent cannot write to /var/log/ system logs.

## Connections
- [[.test_var_log_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core