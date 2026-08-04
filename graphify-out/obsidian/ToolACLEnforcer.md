---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "Progressive Trust Levels"
location: "L205"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Progressive_Trust_Levels
---

# ToolACLEnforcer

## Connections
- [[.__init__()_95]] - `method` [EXTRACTED]
- [[._get_group_tool_allowlist()]] - `method` [EXTRACTED]
- [[._get_role()]] - `method` [EXTRACTED]
- [[.can_use_tool()]] - `method` [EXTRACTED]
- [[.check_tool_rate_limit()]] - `method` [EXTRACTED]
- [[.enforcer()]] - `calls` [EXTRACTED]
- [[.get_allowed_tools()]] - `method` [EXTRACTED]
- [[.get_denial_counts()]] - `method` [EXTRACTED]
- [[.get_denied_tools()]] - `method` [EXTRACTED]
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[.test_enforcer_without_trust_manager_unchanged()]] - `calls` [EXTRACTED]
- [[.test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[.test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[.test_no_rbac_defaults_to_viewer()]] - `calls` [EXTRACTED]
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[.test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[.test_trust_deny_wins_over_acl()]] - `calls` [EXTRACTED]
- [[.test_unknown_tool_falls_through_to_acl()]] - `calls` [EXTRACTED]
- [[Enforces tool-level access control based on user role and group membership.]] - `rationale_for` [EXTRACTED]
- [[ProgressiveTrustConfig_2]] - `uses` [INFERRED]
- [[RBACConfig_4]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[TeamsConfig_2]] - `uses` [INFERRED]
- [[TestAdminAccess]] - `uses` [INFERRED]
- [[TestBackwardCompat]] - `uses` [INFERRED]
- [[TestCVE2026_9367TerminalToolDenied]] - `uses` [INFERRED]
- [[TestClassificationSets]] - `uses` [INFERRED]
- [[TestCollaboratorAccess]] - `uses` [INFERRED]
- [[TestDenyUnknownFalse]] - `uses` [INFERRED]
- [[TestEnumMapping]] - `uses` [INFERRED]
- [[TestGatedPromotion]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist]] - `uses` [INFERRED]
- [[TestNoRBACConfig]] - `uses` [INFERRED]
- [[TestOwnerAccess]] - `uses` [INFERRED]
- [[TestProgressiveTrustConfigUnit]] - `uses` [INFERRED]
- [[TestToolACLComposition]] - `uses` [INFERRED]
- [[TestToolGating]] - `uses` [INFERRED]
- [[TestToolRateLimiting]] - `uses` [INFERRED]
- [[TestTypedViolations]] - `uses` [INFERRED]
- [[TestViewerAccess]] - `uses` [INFERRED]
- [[TrustLevel_2]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[enforcer()_2]] - `calls` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_progressive_trust_integration.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `imports` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Progressive_Trust_Levels
