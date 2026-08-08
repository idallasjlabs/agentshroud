---
type: community
cohesion: 0.02
members: 107
---

# Group RBAC Roles

**Cohesion:** 0.02 - loosely connected
**Members:** 107 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/group_rbac.py
- [[.can_use_high_risk()]] - code - gateway/security/group_rbac.py
- [[.get_all_roles()]] - code - gateway/security/group_rbac.py
- [[.get_role()]] - code - gateway/security/group_rbac.py
- [[.is_high_risk_tool()]] - code - gateway/security/group_rbac.py
- [[.is_member_or_higher()]] - code - gateway/security/group_rbac.py
- [[.is_owner()]] - code - gateway/security/group_rbac.py
- [[.rank()]] - code - gateway/security/group_rbac.py
- [[.remove_role()]] - code - gateway/security/group_rbac.py
- [[.set_role()]] - code - gateway/security/group_rbac.py
- [[.test_can_use_high_risk_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_can_use_high_risk_owner()]] - code - gateway/tests/test_group_rbac.py
- [[.test_can_use_high_risk_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_all_roles_empty_for_unknown_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_all_roles_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_all_roles_returns_all_entries()]] - code - gateway/tests/test_group_rbac.py
- [[.test_get_role_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
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
- [[.test_non_member_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_allowed_all_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_resolves_to_owner_role()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_unrestricted_matches_dm_behavior()]] - code - gateway/tests/test_group_rbac.py
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
- [[.test_unknown_group_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[An invalid role string in the map falls back to READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[GroupRole]] - code - gateway/security/group_rbac.py
- [[GroupRoleResolver]] - code - gateway/security/group_rbac.py
- [[GroupRoleResolver correctly maps Telegram user IDs to per-group roles.]] - rationale - gateway/tests/test_group_rbac.py
- [[Numeric rank for comparison — higher is more privileged.]] - rationale - gateway/security/group_rbac.py
- [[Owner group-context check must match standard can_use_tool result.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner is allowed ALL tools in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner must have unrestricted access even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Per-group roles for Telegram group workspace members.      Hierarchy (highest to]] - rationale - gateway/security/group_rbac.py
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
- [[Return True if this role is permitted to REQUEST high-risk tools.          OWNER]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is at least a member (member or owner).]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is the owner in group_chat_id.]] - rationale - gateway/security/group_rbac.py
- [[Return all user→role mappings for a group.]] - rationale - gateway/security/group_rbac.py
- [[Return the GroupRole for user_id in group_chat_id.          Returns GroupRole.RE]] - rationale - gateway/security/group_rbac.py
- [[Set or update the role for a user in a specific group.]] - rationale - gateway/security/group_rbac.py
- [[Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestGroupRoleProperties]] - code - gateway/tests/test_group_rbac.py
- [[TestGroupRoleResolver]] - code - gateway/tests/test_group_rbac.py
- [[TestMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestOwnerGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[TestReadOnlyMemberGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[Unknown group_chat_id defaults to GroupRole.READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[User not in role map defaults to GroupRole.READ_ONLY (deny-by-default).]] - rationale - gateway/tests/test_group_rbac.py
- [[acl_config()]] - code - gateway/tests/test_group_rbac.py
- [[email_sending is recognized as a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py
- [[enforcer()]] - code - gateway/tests/test_group_rbac.py
- [[get_all_roles with an invalid role string falls back to READ_ONLY per entry.]] - rationale - gateway/tests/test_group_rbac.py
- [[group_rbac.py]] - code - gateway/security/group_rbac.py
- [[group_rbac.py (GroupRoleResolver)]] - code - gateway/security/group_rbac.py
- [[group_role_resolver()]] - code - gateway/tests/test_group_rbac.py
- [[owner_in_group resolves to GroupRole.OWNER.]] - rationale - gateway/tests/test_group_rbac.py
- [[rbac()_1]] - code - gateway/tests/test_group_rbac.py
- [[remove_role on a user not in map is a no-op (no exception).]] - rationale - gateway/tests/test_group_rbac.py
- [[teams()_3]] - code - gateway/tests/test_group_rbac.py
- [[test_group_rbac.py]] - code - gateway/tests/test_group_rbac.py
- [[tool_acl.py (ToolACLEnforcer)]] - code - gateway/security/tool_acl.py
- [[web_search is NOT a high-risk tool.]] - rationale - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Group_RBAC_Roles
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Auth & Exception Types]]
- 9 edges to [[_COMMUNITY_Gateway Test Suite]]
- 9 edges to [[_COMMUNITY_Progressive Trust Config]]
- 7 edges to [[_COMMUNITY_Collaborator Response Templates]]
- 1 edge to [[_COMMUNITY_SOC Dashboard]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_MCP Policy Engine]]
- 1 edge to [[_COMMUNITY_Group Workspace Isolation]]

## Top bridge nodes
- [[GroupRoleResolver]] - degree 36, connects to 5 communities
- [[test_group_rbac.py]] - degree 19, connects to 5 communities
- [[TestGroupRoleProperties]] - degree 27, connects to 4 communities
- [[GroupRole]] - degree 19, connects to 4 communities
- [[TestGroupRoleResolver]] - degree 18, connects to 4 communities