---
type: community
cohesion: 0.05
members: 69
---

# RBACConfig

**Cohesion:** 0.05 - loosely connected
**Members:** 69 nodes

## Members
- [[dot-__init__()_97]] - code - gateway/security/tool_acl.py
- [[dot-_can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[dot-_get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[dot-_get_role()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool()_1]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_from_origin()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[dot-check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[dot-effective_admin()]] - code - gateway/security/tool_acl.py
- [[dot-effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[dot-effective_private()]] - code - gateway/security/tool_acl.py
- [[dot-get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[dot-get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin.]] - rationale - gateway/security/tool_acl.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.]] - rationale - gateway/security/tool_acl.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/tool_acl.py
- [[RBACConfig_4]] - code - gateway/tests/test_tool_acl.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[TeamsConfig_1]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[_make_rbac()]] - code - gateway/tests/test_tool_acl.py
- [[enforcer()_1]] - code - gateway/tests/test_tool_acl.py
- [[rbac()]] - code - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_MiddlewareManager]]
- 19 edges to [[_COMMUNITY_TrustConfig]]
- 12 edges to [[_COMMUNITY_GroupRoleResolver]]
- 11 edges to [[_COMMUNITY_telegram_proxy.py]]
- 8 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 4 edges to [[_COMMUNITY_hermesSOUL_1]]
- 3 edges to [[_COMMUNITY_ProxyAction_1]]
- 3 edges to [[_COMMUNITY_export_bot]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection_3]]
- 2 edges to [[_COMMUNITY_test_runtime_engines.py_1]]
- 2 edges to [[_COMMUNITY_test_prompt_guard.py_3]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[ToolACLEnforcer]] - degree 77, connects to 13 communities
- [[ToolACLConfig]] - degree 38, connects to 8 communities
- [[test_tool_acl.py]] - degree 23, connects to 6 communities
- [[TestCollaboratorAccess]] - degree 12, connects to 2 communities
- [[TestAdminAccess]] - degree 10, connects to 2 communities
