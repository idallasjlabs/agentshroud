---
type: community
members: 64
---

# Community 33

**Members:** 64 nodes

## Members
- [[.__init__()_83]] - code - gateway/security/group_rbac.py
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
- [[.test_is_member_or_higher_false_for_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_member_or_higher_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_member_or_higher_for_owner()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_owner_false_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[.test_is_owner_true()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_allowed_all_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[.test_owner_unrestricted_matches_dm_behavior()]] - code - gateway/tests/test_group_rbac.py
- [[.test_rank_member_middle()]] - code - gateway/tests/test_group_rbac.py
- [[.test_rank_owner_highest()]] - code - gateway/tests/test_group_rbac.py
- [[.test_rank_readonly_lowest()]] - code - gateway/tests/test_group_rbac.py
- [[.test_remove_role_falls_back_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[.test_remove_role_noop_for_missing_user()]] - code - gateway/tests/test_group_rbac.py
- [[.test_set_role_creates_new_entry()]] - code - gateway/tests/test_group_rbac.py
- [[.test_set_role_updates_existing_entry()]] - code - gateway/tests/test_group_rbac.py
- [[An invalid role string in the map falls back to READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[GroupRole]] - code - gateway/security/group_rbac.py
- [[GroupRoleResolver]] - code - gateway/security/group_rbac.py
- [[Numeric rank for comparison — higher is more privileged.]] - rationale - gateway/security/group_rbac.py
- [[Owner group-context check must match standard can_use_tool result.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner is allowed ALL tools in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner must have unrestricted access even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Per-group roles for Telegram group workspace members.      Hierarchy (highest to]] - rationale - gateway/security/group_rbac.py
- [[Per-tool call rate limit configuration.]] - rationale - gateway/security/tool_acl.py
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
- [[TestOwnerGroupContext]] - code - gateway/tests/test_group_rbac.py
- [[ToolRateLimit]] - code - gateway/security/tool_acl.py
- [[acl_config()]] - code - gateway/tests/test_group_rbac.py
- [[enforcer()]] - code - gateway/tests/test_group_rbac.py
- [[get_all_roles with an invalid role string falls back to READ_ONLY per entry.]] - rationale - gateway/tests/test_group_rbac.py
- [[group_rbac.py]] - code - gateway/security/group_rbac.py
- [[group_rbac.py (GroupRoleResolver)]] - code - gateway/security/group_rbac.py
- [[group_role_resolver()]] - code - gateway/tests/test_group_rbac.py
- [[rbac()_1]] - code - gateway/tests/test_group_rbac.py
- [[remove_role on a user not in map is a no-op (no exception).]] - rationale - gateway/tests/test_group_rbac.py
- [[teams()_3]] - code - gateway/tests/test_group_rbac.py
- [[test_group_rbac.py]] - code - gateway/tests/test_group_rbac.py
- [[tool_acl.py]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_33
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 6]]
- 7 edges to [[_COMMUNITY_Community 194]]
- 7 edges to [[_COMMUNITY_Community 11]]
- 4 edges to [[_COMMUNITY_Community 196]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 884]]
- 3 edges to [[_COMMUNITY_Community 1284]]
- 3 edges to [[_COMMUNITY_Community 1070]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 300]]
- 1 edge to [[_COMMUNITY_Community 141]]

## Top bridge nodes
- [[GroupRoleResolver]] - degree 36, connects to 7 communities
- [[test_group_rbac.py]] - degree 17, connects to 7 communities
- [[GroupRole]] - degree 19, connects to 6 communities
- [[tool_acl.py]] - degree 9, connects to 5 communities
- [[TestGroupRoleProperties]] - degree 27, connects to 4 communities