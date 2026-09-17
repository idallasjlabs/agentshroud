---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "ToolACLEnforcer"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# ToolACLConfig

## Connections
- [[.__init__()_206]] - `references` [EXTRACTED]
- [[.effective_admin()_1]] - `method` [EXTRACTED]
- [[.effective_collaborator_allowed()_1]] - `method` [EXTRACTED]
- [[.effective_private()_1]] - `method` [EXTRACTED]
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()_1]] - `calls` [EXTRACTED]
- [[.test_group_allowlist_grants_extra_tool()_1]] - `calls` [EXTRACTED]
- [[.test_no_rbac_allows_read()_1]] - `calls` [EXTRACTED]
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()_1]] - `calls` [EXTRACTED]
- [[.test_project_allowed_tools_grant_access()_1]] - `calls` [EXTRACTED]
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_3]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[TestAdminAccess_1]] - `uses` [INFERRED]
- [[TestCVE2026_9367TerminalToolDenied_1]] - `uses` [INFERRED]
- [[TestClassificationSets_1]] - `uses` [INFERRED]
- [[TestCollaboratorAccess_1]] - `uses` [INFERRED]
- [[TestDenyUnknownFalse_1]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist_1]] - `uses` [INFERRED]
- [[TestNoRBACConfig_1]] - `uses` [INFERRED]
- [[TestOriginAwareAuthorization_1]] - `uses` [INFERRED]
- [[TestOwnerAccess_1]] - `uses` [INFERRED]
- [[TestToolRateLimiting_1]] - `uses` [INFERRED]
- [[TestViewerAccess_1]] - `uses` [INFERRED]
- [[ToolACLEnforcer_1]] - `shares_data_with` [EXTRACTED]
- [[enforcer()_4]] - `calls` [EXTRACTED]
- [[test_tool_acl.py_1]] - `references` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolACLEnforcer