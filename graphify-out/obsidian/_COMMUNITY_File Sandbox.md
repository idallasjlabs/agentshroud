---
type: community
members: 129
---

# File Sandbox

**Members:** 129 nodes

## Members
- [[.__init__()_117]] - code - gateway/security/tool_acl.py
- [[._can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[._get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[._get_role()]] - code - gateway/security/tool_acl.py
- [[.can_use_high_risk()]] - code - gateway/security/group_rbac.py
- [[.can_use_tool()]] - code - gateway/security/tool_acl.py
- [[.can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[.check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[.effective_admin()]] - code - gateway/security/tool_acl.py
- [[.effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[.effective_private()]] - code - gateway/security/tool_acl.py
- [[.enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[.get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[.get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[.get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[.rank()]] - code - gateway/security/group_rbac.py
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
- [[.test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_member_allowed_read_write_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_gmail_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_high_risk_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_ssh_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_allowed_all_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_unrestricted_matches_dm_behavior()]] - code - gateway/tests/test_group_rbac.py
- [[.test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[.test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[.test_readonly_allowed_read_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_email_sending_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_external_api_calls_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_file_deletion_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_skill_installation_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.]] - rationale - gateway/security/tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[GET socv1tool-acl{entity_id}]] - code - gateway/soc/router.py
- [[GroupRole]] - code - gateway/security/group_rbac.py
- [[Numeric rank for comparison — higher is more privileged.]] - rationale - gateway/security/group_rbac.py
- [[Owner group-context check must match standard can_use_tool result.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner is allowed ALL tools in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner must have unrestricted access even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Per-group roles for Telegram group workspace members.      Hierarchy (highest to]] - rationale - gateway/security/group_rbac.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Read-only member IS allowed read tool in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member IS allowed web_search (low-risk) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied email_sending even when called from group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied external_api_calls in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied file_deletion in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied skill_installation in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only members must be denied high-risk tools in any group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member (non-owner group role) is denied high-risk tools that require app]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed readwrite in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed web_search in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied gmail (private tool) even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied ssh (private tool) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - rationale - gateway/tests/test_group_rbac.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[Return True if this role is permitted to REQUEST high-risk tools.          OWNER]] - rationale - gateway/security/group_rbac.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestReadOnlyMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[acl_config()]] - code - gateway/tests/test_group_rbac.py
- [[enforcer()]] - code - gateway/tests/test_group_rbac.py
- [[enforcer()_3]] - code - gateway/tests/test_tool_acl.py
- [[group_rbac.py (GroupRoleResolver)]] - code - gateway/security/group_rbac.py
- [[group_role_resolver()]] - code - gateway/tests/test_group_rbac.py
- [[rbac()_1]] - code - gateway/tests/test_group_rbac.py
- [[rbac()_6]] - code - gateway/tests/test_tool_acl.py
- [[teams()_3]] - code - gateway/tests/test_group_rbac.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_group_rbac.py]] - code - gateway/tests/test_group_rbac.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py
- [[tool_acl.py (ToolACLEnforcer)]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/File_Sandbox
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 20 edges to [[_COMMUNITY_Gateway Test Suite]]
- 17 edges to [[_COMMUNITY_Group Workspace Isolation]]
- 15 edges to [[_COMMUNITY_Gateway Test Suite]]
- 5 edges to [[_COMMUNITY_Custom Skills]]
- 4 edges to [[_COMMUNITY_docsvault]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Slack API Proxy]]
- 1 edge to [[_COMMUNITY_Gateway Proxy Layer]]
- 1 edge to [[_COMMUNITY_Approval Queue Tests]]

## Top bridge nodes
- [[ToolACLEnforcer]] - degree 72, connects to 7 communities
- [[test_group_rbac.py]] - degree 19, connects to 5 communities
- [[GroupRole]] - degree 19, connects to 4 communities
- [[ToolACLConfig]] - degree 36, connects to 3 communities
- [[TestReadOnlyMemberGroupContext]] - degree 14, connects to 3 communities