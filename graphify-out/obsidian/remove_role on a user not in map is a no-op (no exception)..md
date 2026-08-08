---
source_file: "gateway/tests/test_group_rbac.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L392"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# remove_role on a user not in map is a no-op (no exception).

## Connections
- [[.test_remove_role_noop_for_missing_user()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles