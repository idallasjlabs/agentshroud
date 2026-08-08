---
source_file: "gateway/tests/test_group_rbac.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L425"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# get_all_roles with an invalid role string falls back to READ_ONLY per entry.

## Connections
- [[.test_get_all_roles_invalid_string_defaults_to_readonly()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles