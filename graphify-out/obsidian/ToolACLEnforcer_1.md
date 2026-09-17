---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "ToolACLEnforcer"
location: "L206"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# ToolACLEnforcer

## Connections
- [[.__init__()_206]] - `method` [EXTRACTED]
- [[._can_use_tool_impl()_1]] - `method` [EXTRACTED]
- [[._get_group_tool_allowlist()_1]] - `method` [EXTRACTED]
- [[._get_role()_1]] - `method` [EXTRACTED]
- [[.can_use_tool()_2]] - `method` [EXTRACTED]
- [[.can_use_tool_from_origin()_1]] - `method` [EXTRACTED]
- [[.can_use_tool_in_group_context()_1]] - `method` [EXTRACTED]
- [[.check_tool_rate_limit()_1]] - `method` [EXTRACTED]
- [[.enforcer()_1]] - `calls` [EXTRACTED]
- [[.get_allowed_tools()_1]] - `method` [EXTRACTED]
- [[.get_denial_counts()_1]] - `method` [EXTRACTED]
- [[.get_denied_tools()_1]] - `method` [EXTRACTED]
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()_1]] - `calls` [EXTRACTED]
- [[.test_group_allowlist_grants_extra_tool()_1]] - `calls` [EXTRACTED]
- [[.test_no_rbac_allows_read()_1]] - `calls` [EXTRACTED]
- [[.test_no_rbac_defaults_to_viewer()_1]] - `calls` [EXTRACTED]
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()_1]] - `calls` [EXTRACTED]
- [[.test_project_allowed_tools_grant_access()_1]] - `calls` [EXTRACTED]
- [[A2AGovernanceProxy_1]] - `semantically_similar_to` [INFERRED]
- [[ADMIN_TOOLS]] - `shares_data_with` [EXTRACTED]
- [[COLLABORATOR_ALLOWED_TOOLS]] - `shares_data_with` [EXTRACTED]
- [[Enforces tool-level access control based on user role and group membership.]] - `rationale_for` [EXTRACTED]
- [[PRIVATE_TOOLS]] - `shares_data_with` [EXTRACTED]
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
- [[ToolACLConfig_1]] - `shares_data_with` [EXTRACTED]
- [[can_use_tool_from_origin]] - `conceptually_related_to` [EXTRACTED]
- [[enforcer()_4]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py_1]] - `conceptually_related_to` [INFERRED]
- [[test_tool_acl.py_1]] - `references` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolACLEnforcer