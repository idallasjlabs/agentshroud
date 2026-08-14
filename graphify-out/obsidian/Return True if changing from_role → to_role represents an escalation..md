---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Return True if changing from_role → to_role represents an escalation.

## Connections
- [[.is_privilege_escalation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core