---
source_file: "gateway/security/group_rbac.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L147"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# Remove a user's role entry from a group (falls back to READ_ONLY).

## Connections
- [[.remove_role()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles