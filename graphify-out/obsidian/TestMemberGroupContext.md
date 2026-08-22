---
source_file: "gateway/tests/test_group_rbac.py"
type: "code"
community: "Tool ACL & Group RBAC"
location: "L229"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_ACL__Group_RBAC
---

# TestMemberGroupContext

## Connections
- [[.test_member_allowed_read_write_in_group()]] - `method` [EXTRACTED]
- [[.test_member_allowed_web_search_in_group()]] - `method` [EXTRACTED]
- [[.test_member_denied_gmail_private_tool_in_group()]] - `method` [EXTRACTED]
- [[.test_member_denied_high_risk_tools_in_group()]] - `method` [EXTRACTED]
- [[.test_member_denied_ssh_private_tool_in_group()]] - `method` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - `rationale_for` [EXTRACTED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_ACL__Group_RBAC