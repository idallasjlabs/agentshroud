---
type: community
cohesion: 0.04
members: 83
---

# Tool ACL & RBAC Config

**Cohesion:** 0.04 - loosely connected
**Members:** 83 nodes

## Members
- [[.effective_admin()]] - code - gateway/security/tool_acl.py
- [[.effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[.effective_private()]] - code - gateway/security/tool_acl.py
- [[.get_user_groups_by_id()]] - code - gateway/security/rbac_config.py
- [[.get_user_role()_1]] - code - gateway/security/rbac_config.py
- [[.get_users_by_role()]] - code - gateway/security/rbac_config.py
- [[.is_admin_or_higher()]] - code - gateway/security/rbac_config.py
- [[.is_collaborator_or_higher()]] - code - gateway/security/rbac_config.py
- [[.is_operator_or_higher()]] - code - gateway/security/rbac_config.py
- [[.is_owner()]] - code - gateway/security/rbac_config.py
- [[.set_user_role()_1]] - code - gateway/security/rbac_config.py
- [[.test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[.test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[.test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.wire_teams_config()]] - code - gateway/security/rbac_config.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Check if user has admin privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Check if user has collaborator privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Check if user has operator privileges or higher (admin, operator, owner).]] - rationale - gateway/security/rbac_config.py
- [[Check if user is the owner (any platform).]] - rationale - gateway/security/rbac_config.py
- [[Configuration for Role-Based Access Control.]] - rationale - gateway/security/rbac_config.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Get all users with a specific role.]] - rationale - gateway/security/rbac_config.py
- [[Get role for a user ID.]] - rationale - gateway/security/rbac_config.py
- [[Merge group membership and admin IDs from TeamsConfig into RBAC.          Called]] - rationale - gateway/security/rbac_config.py
- [[Per-tool call rate limit configuration.]] - rationale - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[RBACConfig_4]] - code - gateway/tests/test_tool_acl.py
- [[RBACConfig_1]] - code - gateway/security/rbac_config.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Return member IDs of a group, or empty list if no teams config.]] - rationale - gateway/security/rbac_config.py
- [[Set role for a user ID (owner-only operation).]] - rationale - gateway/security/rbac_config.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[ToolRateLimit]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[enforcer()_2]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_2]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py
- [[tool_acl.py]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tool_ACL__RBAC_Config
SORT file.name ASC
```

## Connections to other communities
- 39 edges to [[_COMMUNITY_RBAC Configuration]]
- 24 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 14 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 14 edges to [[_COMMUNITY_Group Config & Teams]]
- 14 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 12 edges to [[_COMMUNITY_Privacy Policy]]
- 9 edges to [[_COMMUNITY_Module Group 75]]
- 8 edges to [[_COMMUNITY_SOC Authentication]]
- 7 edges to [[_COMMUNITY_Module Group 120]]
- 6 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 5 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 5 edges to [[_COMMUNITY_Module Group 207]]
- 4 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 3 edges to [[_COMMUNITY_Module Group 154]]
- 3 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 3 edges to [[_COMMUNITY_SOC Services & Health Status]]
- 3 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 2 edges to [[_COMMUNITY_Webhook Receiver]]
- 2 edges to [[_COMMUNITY_Module Group 196]]
- 2 edges to [[_COMMUNITY_Module Group 296]]
- 1 edge to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 1 edge to [[_COMMUNITY_Module Group 177]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Module Group 60]]
- 1 edge to [[_COMMUNITY_Session Manager & Webhook]]
- 1 edge to [[_COMMUNITY_Module Group 554]]
- 1 edge to [[_COMMUNITY_Module Group 186]]
- 1 edge to [[_COMMUNITY_Module Group 213]]
- 1 edge to [[_COMMUNITY_Module Group 270]]

## Top bridge nodes
- [[RBACConfig_1]] - degree 166, connects to 32 communities
- [[test_tool_acl.py]] - degree 18, connects to 3 communities
- [[TestCVE2026_9367TerminalToolDenied]] - degree 14, connects to 3 communities
- [[TestCollaboratorAccess]] - degree 12, connects to 3 communities
- [[TestToolRateLimiting]] - degree 11, connects to 3 communities