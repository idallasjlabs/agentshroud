---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "RBACConfig"
location: "L170"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBACConfig
---

# ToolACLConfig

## Connections
- [[dot-__init__()_90]] - `references` [EXTRACTED]
- [[dot-effective_admin()]] - `method` [EXTRACTED]
- [[dot-effective_collaborator_allowed()]] - `method` [EXTRACTED]
- [[dot-effective_private()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[dot-test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[dot-test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[GroupRole]] - `uses` [INFERRED]
- [[GroupRoleResolver]] - `uses` [INFERRED]
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[RBACConfig_3]] - `uses` [INFERRED]
- [[Role_23]] - `uses` [INFERRED]
- [[TeamsConfig_1]] - `uses` [INFERRED]
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
- [[TestOriginAwareAuthorization]] - `uses` [INFERRED]
- [[TestOwnerAccess]] - `uses` [INFERRED]
- [[TestOwnerGroupContext]] - `uses` [INFERRED]
- [[TestReadOnlyMemberGroupContext]] - `uses` [INFERRED]
- [[TestToolRateLimiting]] - `uses` [INFERRED]
- [[TestViewerAccess]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `shares_data_with` [EXTRACTED]
- [[acl_config()]] - `calls` [EXTRACTED]
- [[enforcer()]] - `calls` [EXTRACTED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `references` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBACConfig
