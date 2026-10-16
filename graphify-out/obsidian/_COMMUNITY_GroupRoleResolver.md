---
type: community
cohesion: 0.05
members: 61
---

# GroupRoleResolver

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[dot-__init__()_123]] - code - gateway/security/group_rbac.py
- [[dot-can_use_high_risk()]] - code - gateway/security/group_rbac.py
- [[dot-get_all_roles()]] - code - gateway/security/group_rbac.py
- [[dot-get_role()]] - code - gateway/security/group_rbac.py
- [[dot-is_high_risk_tool()]] - code - gateway/security/group_rbac.py
- [[dot-is_member_or_higher()]] - code - gateway/security/group_rbac.py
- [[dot-is_owner()_2]] - code - gateway/security/group_rbac.py
- [[dot-rank()]] - code - gateway/security/group_rbac.py
- [[dot-remove_role()]] - code - gateway/security/group_rbac.py
- [[dot-set_role()]] - code - gateway/security/group_rbac.py
- [[dot-test_can_use_high_risk_member()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_can_use_high_risk_owner()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_can_use_high_risk_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_get_all_roles_empty_for_unknown_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_get_all_roles_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_get_all_roles_returns_all_entries()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_get_role_invalid_string_defaults_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_member_or_higher_false_for_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_member_or_higher_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_member_or_higher_for_owner()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_owner_false_for_member()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_is_owner_true()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_owner_allowed_all_tools_in_group()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_owner_unrestricted_matches_dm_behavior()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_rank_member_middle()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_rank_owner_highest()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_rank_readonly_lowest()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_remove_role_falls_back_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_remove_role_noop_for_missing_user()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_set_role_creates_new_entry()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_set_role_updates_existing_entry()]] - code - gateway/tests/test_group_rbac.py
- [[An invalid role string in the map falls back to READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[GroupRole]] - code - gateway/security/group_rbac.py
- [[GroupRoleResolver]] - code - gateway/security/group_rbac.py
- [[Numeric rank for comparison — higher is more privileged.]] - rationale - gateway/security/group_rbac.py
- [[Owner group-context check must match standard can_use_tool result.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner is allowed ALL tools in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Owner must have unrestricted access even in group context.]] - rationale - gateway/tests/test_group_rbac.py
- [[Per-group roles for Telegram group workspace members.      Hierarchy (highest to]] - rationale - gateway/security/group_rbac.py
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
- [[acl_config()]] - code - gateway/tests/test_group_rbac.py
- [[enforcer()_2]] - code - gateway/tests/test_group_rbac.py
- [[get_all_roles with an invalid role string falls back to READ_ONLY per entry.]] - rationale - gateway/tests/test_group_rbac.py
- [[group_rbac.py]] - code - gateway/security/group_rbac.py
- [[group_rbac.py (GroupRoleResolver)]] - code - gateway/security/group_rbac.py
- [[group_role_resolver()]] - code - gateway/tests/test_group_rbac.py
- [[rbac()_1]] - code - gateway/tests/test_group_rbac.py
- [[remove_role on a user not in map is a no-op (no exception).]] - rationale - gateway/tests/test_group_rbac.py
- [[teams()_1]] - code - gateway/tests/test_group_rbac.py
- [[test_group_rbac.py]] - code - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupRoleResolver
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_RBACConfig_1]]
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_telegram_proxy.py]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection_3]]
- 3 edges to [[_COMMUNITY_test_runtime_engines.py_1]]
- 3 edges to [[_COMMUNITY_test_prompt_guard.py_3]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[GroupRoleResolver]] - degree 36, connects to 7 communities
- [[GroupRole]] - degree 19, connects to 6 communities
- [[test_group_rbac.py]] - degree 17, connects to 6 communities
- [[TestGroupRoleProperties]] - degree 27, connects to 3 communities
- [[TestOwnerGroupContext]] - degree 10, connects to 3 communities
