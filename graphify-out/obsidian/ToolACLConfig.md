---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "Community 75"
location: "L170"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_75
---

# ToolACLConfig

## Connections
- [[.__init__()_121]] - `references` [EXTRACTED]
- [[.effective_admin()]] - `method` [EXTRACTED]
- [[.effective_collaborator_allowed()]] - `method` [EXTRACTED]
- [[.effective_private()]] - `method` [EXTRACTED]
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[.test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[.test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[.test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACConfig_4]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[TestAdminAccess]] - `uses` [INFERRED]
- [[TestCVE2026_9367TerminalToolDenied]] - `uses` [INFERRED]
- [[TestClassificationSets]] - `uses` [INFERRED]
- [[TestCollaboratorAccess]] - `uses` [INFERRED]
- [[TestDenyUnknownFalse]] - `uses` [INFERRED]
- [[TestGroupRoleProperties]] - `uses` [INFERRED]
- [[TestGroupRoleResolver]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist]] - `uses` [INFERRED]
- [[TestMemberGroupContext]] - `uses` [INFERRED]
- [[TestNoRBACConfig]] - `uses` [INFERRED]
- [[TestOwnerAccess]] - `uses` [INFERRED]
- [[TestOwnerGroupContext]] - `uses` [INFERRED]
- [[TestReadOnlyMemberGroupContext]] - `uses` [INFERRED]
- [[TestToolRateLimiting]] - `uses` [INFERRED]
- [[TestViewerAccess]] - `uses` [INFERRED]
- [[acl_config()]] - `calls` [EXTRACTED]
- [[enforcer()_3]] - `calls` [EXTRACTED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `imports` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_75