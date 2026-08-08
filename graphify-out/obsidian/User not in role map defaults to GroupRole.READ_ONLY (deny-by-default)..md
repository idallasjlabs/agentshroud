---
source_file: "gateway/tests/test_group_rbac.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L127"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# User not in role map defaults to GroupRole.READ_ONLY (deny-by-default).

## Connections
- [[.test_non_member_defaults_to_readonly()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles