---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "Community 134"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_134
---

# ToolACLConfig

## Connections
- [[dot-__init__()_1]] - `calls` [EXTRACTED]
- [[dot-effective_admin()]] - `method` [EXTRACTED]
- [[dot-effective_collaborator_allowed()]] - `method` [EXTRACTED]
- [[dot-effective_private()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[dot-test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[dot-test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[Policy configuration for tool ACL enforcement. Loaded from agentshroud.yaml…]] - `rationale_for` [EXTRACTED]
- [[TestDenyUnknownFalse]] - `uses` [INFERRED]
- [[TestGroupRoleProperties]] - `uses` [INFERRED]
- [[TestGroupRoleResolver]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist]] - `uses` [INFERRED]
- [[TestMemberGroupContext]] - `uses` [INFERRED]
- [[TestNoRBACConfig]] - `uses` [INFERRED]
- [[TestOwnerGroupContext]] - `uses` [INFERRED]
- [[TestReadOnlyMemberGroupContext]] - `uses` [INFERRED]
- [[acl_config()]] - `calls` [EXTRACTED]
- [[enforcer()]] - `uses` [INFERRED]
- [[gateway.security.tool_acl]] - `contains` [EXTRACTED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_134