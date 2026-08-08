---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "Group RBAC Roles"
location: "L298"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Group_RBAC_Roles
---

# TestOwnerGroupContext

## Connections
- [[.test_owner_allowed_all_tools_in_group()]] - `method` [EXTRACTED]
- [[.test_owner_unrestricted_matches_dm_behavior()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[Owner must have unrestricted access even in group context.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Group_RBAC_Roles