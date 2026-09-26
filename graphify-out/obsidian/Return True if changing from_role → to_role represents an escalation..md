---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "MiddlewareManager"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MiddlewareManager
---

# Return True if changing from_role → to_role represents an escalation.

## Connections
- [[.is_privilege_escalation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MiddlewareManager