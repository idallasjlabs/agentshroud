---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "Group RBAC & Tool ACL"
location: "L159"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Group_RBAC__Tool_ACL
---

# TestReadOnlyMemberGroupContext

## Connections
- [[.test_readonly_allowed_read_in_group()]] - `method` [EXTRACTED]
- [[.test_readonly_allowed_web_search_in_group()]] - `method` [EXTRACTED]
- [[.test_readonly_denied_email_sending_in_group()]] - `method` [EXTRACTED]
- [[.test_readonly_denied_external_api_calls_in_group()]] - `method` [EXTRACTED]
- [[.test_readonly_denied_file_deletion_in_group()]] - `method` [EXTRACTED]
- [[.test_readonly_denied_skill_installation_in_group()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Read-only members must be denied high-risk tools in any group context.]] - `rationale_for` [EXTRACTED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Group_RBAC__Tool_ACL