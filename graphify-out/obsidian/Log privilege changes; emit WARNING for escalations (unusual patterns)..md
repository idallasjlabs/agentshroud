---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "MiddlewareManager"
location: "L360"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MiddlewareManager
---

# Log privilege changes; emit WARNING for escalations (unusual patterns).

## Connections
- [[.audit_privilege_change()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MiddlewareManager