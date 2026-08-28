---
type: community
cohesion: 0.02
members: 163
---

# Group RBAC & Tool ACL

**Cohesion:** 0.02 - loosely connected
**Members:** 163 nodes

## Members
- [[.__init__()_83]] - code - gateway/security/group_rbac.py
- [[.__init__()_121]] - code - gateway/security/tool_acl.py
- [[.effective_admin()]] - code - gateway/security/tool_acl.py
- [[.effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[.effective_private()]] - code - gateway/security/tool_acl.py
- [[.enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[.get_all_roles()]] - code - gateway/security/group_rbac.py
- [[.get_role()]] - code - gateway/security/group_rbac.py
- [[.is_high_risk_tool()]] - code - gateway/security/group_rbac.py
- [[.is_member_or_higher()]] - code - gateway/security/group_rbac.py
- [[.is_owner()]] - code - gateway/security/group_rbac.py
- [[.remove_role()]] - code - gateway/security/group_rbac.py
- [[.set_role()]] - code - gateway/security/group_rbac.py
- [[.test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_can_use_high_risk_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_can_use_high_risk_owner()]] - code - gateway/tests/test_group_rbac.py
- [[.test_can_use_high_risk_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[.test_get_all_roles_empty_for_unknown_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_all_roles_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_all_roles_returns_all_entries()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_role_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_is_high_risk_false_for_web_search()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_high_risk_true_for_email_sending()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_high_risk_true_for_external_api_calls()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_high_risk_true_for_file_deletion()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_high_risk_true_for_skill_installation()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_member_or_higher_false_for_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_member_or_higher_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_member_or_higher_for_owner()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_owner_false_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_owner_true()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_allowed_read_write_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_gmail_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_high_risk_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_denied_ssh_private_tool_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_member_resolves_to_member_role()]] - code - gateway/tests/test_group_rbac.py
- [[.test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[.test_non_member_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_allowed_all_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_resolves_to_owner_role()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_unrestricted_matches_dm_behavior()]] - code - gateway/tests/test_group_rbac.py
- [[.test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[.test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[.test_rank_member_middle()]] - code - gateway/tests/test_group_rbac.py
- [[.test_rank_owner_highest()]] - code - gateway/tests/test_group_rbac.py
- [[.test_rank_readonly_lowest()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_allowed_read_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_allowed_web_search_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_email_sending_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_external_api_calls_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_file_deletion_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_denied_skill_installation_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_readonly_user_resolves_to_readonly_role()]] - code - gateway/tests/test_group_rbac.py
- [[.test_remove_role_falls_back_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_remove_role_noop_for_missing_user()]] - code - gateway/tests/test_group_rbac.py
- [[.test_set_role_creates_new_entry()]] - code - gateway/tests/test_group_rbac.py
- [[.test_set_role_updates_existing_entry()]] - code - gateway/tests/test_group_rbac.py
- [[.test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_unknown_group_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[An invalid role string in the map falls back to READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[CVE-2026-9367 terminal_tool command injection bypass fix]] - rationale - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[GroupRoleResolver]] - code - gateway/security/group_rbac.py
- [[GroupRoleResolver correctly maps Telegram user IDs to per-group roles.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner group-context check must match standard can_use_tool result.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner is allowed ALL tools in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner must have unrestricted access even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Read-only member IS allowed read tool in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member IS allowed web_search (low-risk) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied email_sending even when called from group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied external_api_calls in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied file_deletion in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only member denied skill_installation in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only members must be denied high-risk tools in any group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Read-only user resolves to GroupRole.READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member (non-owner group role) is denied high-risk tools that require app]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed readwrite in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member IS allowed web_search in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied gmail (private tool) even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member denied ssh (private tool) in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular member resolves to GroupRole.MEMBER.]] - rationale - gateway/tests/test_group_rbac.py
- [[Regular members can use medium-risk tools but not privateadmin tools.]] - rationale - gateway/tests/test_group_rbac.py
- [[Remove a user's role entry from a group (falls back to READ_ONLY).]] - rationale - gateway/security/group_rbac.py
- [[Resolve per-group roles for Telegram group workspace members.      Args]] - rationale - gateway/security/group_rbac.py
- [[Return True if the tool is classified as high-risk.          High-risk tools req]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is at least a member (member or owner).]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is the owner in group_chat_id.]] - rationale - gateway/security/group_rbac.py
- [[Return all user→role mappings for a group.]] - rationale - gateway/security/group_rbac.py
- [[Return the GroupRole for user_id in group_chat_id.          Returns GroupRole.RE]] - rationale - gateway/security/group_rbac.py
- [[Set or update the role for a user in a specific group.]] - rationale - gateway/security/group_rbac.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupRoleProperties]] - code - gateway/tests/test_group_rbac.py
- [[TestGroupRoleResolver]] - code - gateway/tests/test_group_rbac.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestReadOnlyMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Unknown group_chat_id defaults to GroupRole.READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[User not in role map defaults to GroupRole.READ_ONLY (deny-by-default).]] - rationale - gateway/tests/test_group_rbac.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[acl_config()]] - code - gateway/tests/test_group_rbac.py
- [[email_sending is recognized as a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py
- [[enforcer()]] - code - gateway/tests/test_group_rbac.py
- [[enforcer()_3]] - code - gateway/tests/test_tool_acl.py
- [[get_all_roles with an invalid role string falls back to READ_ONLY per entry.]] - rationale - gateway/tests/test_group_rbac.py
- [[group_rbac.py (GroupRoleResolver)]] - code - gateway/security/group_rbac.py
- [[group_role_resolver()]] - code - gateway/tests/test_group_rbac.py
- [[owner_in_group resolves to GroupRole.OWNER.]] - rationale - gateway/tests/test_group_rbac.py
- [[rbac()_1]] - code - gateway/tests/test_group_rbac.py
- [[rbac()_6]] - code - gateway/tests/test_tool_acl.py
- [[remove_role on a user not in map is a no-op (no exception).]] - rationale - gateway/tests/test_group_rbac.py
- [[teams()_3]] - code - gateway/tests/test_group_rbac.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_group_rbac.py]] - code - gateway/tests/test_group_rbac.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py
- [[tool_acl.py (ToolACLEnforcer)]] - code - gateway/security/tool_acl.py
- [[web_search is NOT a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Group_RBAC__Tool_ACL
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 29 edges to [[_COMMUNITY_Progressive Trust]]
- 20 edges to [[_COMMUNITY_Community 27]]
- 14 edges to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 57]]
- 1 edge to [[_COMMUNITY_Community 33]]

## Top bridge nodes
- [[GroupRoleResolver]] - degree 36, connects to 4 communities
- [[TestGroupRoleProperties]] - degree 27, connects to 4 communities
- [[test_group_rbac.py]] - degree 19, connects to 4 communities
- [[TestGroupRoleResolver]] - degree 18, connects to 4 communities
- [[TestReadOnlyMemberGroupContext]] - degree 14, connects to 4 communities