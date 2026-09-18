---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "GroupRoleResolver"
location: "L298"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/GroupRoleResolver
---

# TestOwnerGroupContext

## Connections
- [[.test_owner_allowed_all_tools_in_group()]] - `method` [EXTRACTED]
- [[.test_owner_unrestricted_matches_dm_behavior()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[Owner must have unrestricted access even in group context.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/GroupRoleResolver