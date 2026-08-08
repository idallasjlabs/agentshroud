---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "Group RBAC Roles"
location: "L334"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# TestGroupRoleProperties

## Connections
- [[.test_can_use_high_risk_member()]] - `method` [EXTRACTED]
- [[.test_can_use_high_risk_owner()]] - `method` [EXTRACTED]
- [[.test_can_use_high_risk_readonly()]] - `method` [EXTRACTED]
- [[.test_get_all_roles_empty_for_unknown_group()]] - `method` [EXTRACTED]
- [[.test_get_all_roles_invalid_string_defaults_to_readonly()]] - `method` [EXTRACTED]
- [[.test_get_all_roles_returns_all_entries()]] - `method` [EXTRACTED]
- [[.test_get_role_invalid_string_defaults_to_readonly()]] - `method` [EXTRACTED]
- [[.test_is_member_or_higher_false_for_readonly()]] - `method` [EXTRACTED]
- [[.test_is_member_or_higher_for_member()]] - `method` [EXTRACTED]
- [[.test_is_member_or_higher_for_owner()]] - `method` [EXTRACTED]
- [[.test_is_owner_false_for_member()]] - `method` [EXTRACTED]
- [[.test_is_owner_true()]] - `method` [EXTRACTED]
- [[.test_rank_member_middle()]] - `method` [EXTRACTED]
- [[.test_rank_owner_highest()]] - `method` [EXTRACTED]
- [[.test_rank_readonly_lowest()]] - `method` [EXTRACTED]
- [[.test_remove_role_falls_back_to_readonly()]] - `method` [EXTRACTED]
- [[.test_remove_role_noop_for_missing_user()]] - `method` [EXTRACTED]
- [[.test_set_role_creates_new_entry()]] - `method` [EXTRACTED]
- [[.test_set_role_updates_existing_entry()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers.]] - `rationale_for` [EXTRACTED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_RBAC_Roles