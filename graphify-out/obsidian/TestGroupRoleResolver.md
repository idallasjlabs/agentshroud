---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "Group RBAC Roles"
location: "L108"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# TestGroupRoleResolver

## Connections
- [[.test_is_high_risk_false_for_web_search()]] - `method` [EXTRACTED]
- [[.test_is_high_risk_true_for_email_sending()]] - `method` [EXTRACTED]
- [[.test_is_high_risk_true_for_external_api_calls()]] - `method` [EXTRACTED]
- [[.test_is_high_risk_true_for_file_deletion()]] - `method` [EXTRACTED]
- [[.test_is_high_risk_true_for_skill_installation()]] - `method` [EXTRACTED]
- [[.test_member_resolves_to_member_role()]] - `method` [EXTRACTED]
- [[.test_non_member_defaults_to_readonly()]] - `method` [EXTRACTED]
- [[.test_owner_resolves_to_owner_role()]] - `method` [EXTRACTED]
- [[.test_readonly_user_resolves_to_readonly_role()]] - `method` [EXTRACTED]
- [[.test_unknown_group_defaults_to_readonly()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[GroupRoleResolver correctly maps Telegram user IDs to per-group roles.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_RBAC_Roles