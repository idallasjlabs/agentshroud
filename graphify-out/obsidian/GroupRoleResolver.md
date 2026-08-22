---
source_file: "gateway/security/group_rbac.py"
type: "code"
community: "Group Rbac"
location: "L78"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_Rbac
---

# GroupRoleResolver

## Connections
- [[.__init__()_83]] - `method` [EXTRACTED]
- [[.get_all_roles()]] - `method` [EXTRACTED]
- [[.get_role()]] - `method` [EXTRACTED]
- [[.is_high_risk_tool()]] - `method` [EXTRACTED]
- [[.is_member_or_higher()]] - `method` [EXTRACTED]
- [[.is_owner()]] - `method` [EXTRACTED]
- [[.remove_role()]] - `method` [EXTRACTED]
- [[.set_role()]] - `method` [EXTRACTED]
- [[.test_get_all_roles_empty_for_unknown_group()]] - `calls` [EXTRACTED]
- [[.test_get_all_roles_invalid_string_defaults_to_readonly()]] - `calls` [EXTRACTED]
- [[.test_get_all_roles_returns_all_entries()]] - `calls` [EXTRACTED]
- [[.test_get_role_invalid_string_defaults_to_readonly()]] - `calls` [EXTRACTED]
- [[.test_is_member_or_higher_false_for_readonly()]] - `calls` [EXTRACTED]
- [[.test_is_member_or_higher_for_member()]] - `calls` [EXTRACTED]
- [[.test_is_member_or_higher_for_owner()]] - `calls` [EXTRACTED]
- [[.test_is_owner_false_for_member()]] - `calls` [EXTRACTED]
- [[.test_is_owner_true()]] - `calls` [EXTRACTED]
- [[.test_remove_role_falls_back_to_readonly()]] - `calls` [EXTRACTED]
- [[.test_remove_role_noop_for_missing_user()]] - `calls` [EXTRACTED]
- [[.test_set_role_creates_new_entry()]] - `calls` [EXTRACTED]
- [[.test_set_role_updates_existing_entry()]] - `calls` [EXTRACTED]
- [[GroupWorkspaceManager]] - `semantically_similar_to` [INFERRED]
- [[MCPPolicyEngine]] - `semantically_similar_to` [INFERRED]
- [[Resolve per-group roles for Telegram group workspace members.      Args]] - `rationale_for` [EXTRACTED]
- [[TestGroupRoleProperties]] - `uses` [INFERRED]
- [[TestGroupRoleResolver]] - `uses` [INFERRED]
- [[TestMemberGroupContext]] - `uses` [INFERRED]
- [[TestOwnerGroupContext]] - `uses` [INFERRED]
- [[TestReadOnlyMemberGroupContext]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[ToolRateLimit]] - `uses` [INFERRED]
- [[group_rbac.py]] - `contains` [EXTRACTED]
- [[group_role_resolver()]] - `calls` [EXTRACTED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[tool_acl.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_Rbac