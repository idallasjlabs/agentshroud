---
type: community
members: 37
---

# GroupRoleResolver

**Members:** 37 nodes

## Members
- [[dot-__init__()_128]] - code - gateway/security/group_rbac.py
- [[dot-get_role()]] - code - gateway/security/group_rbac.py
- [[dot-is_high_risk_tool()]] - code - gateway/security/group_rbac.py
- [[dot-is_member_or_higher()]] - code - gateway/security/group_rbac.py
- [[dot-is_owner()_4]] - code - gateway/security/group_rbac.py
- [[dot-remove_role()]] - code - gateway/security/group_rbac.py
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
- [[dot-test_rank_member_middle()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_rank_owner_highest()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_rank_readonly_lowest()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_remove_role_falls_back_to_readonly()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_remove_role_noop_for_missing_user()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_set_role_creates_new_entry()]] - code - gateway/tests/test_group_rbac.py
- [[dot-test_set_role_updates_existing_entry()]] - code - gateway/tests/test_group_rbac.py
- [[An invalid role string in the map falls back to READ_ONLY.]] - rationale - gateway/tests/test_group_rbac.py
- [[GroupRoleResolver]] - code - gateway/security/group_rbac.py
- [[Remove a user's role entry from a group (falls back to READ_ONLY).]] - rationale - gateway/security/group_rbac.py
- [[Resolve per-group roles for Telegram group workspace members. Args…]] - rationale - gateway/security/group_rbac.py
- [[Return True if the tool is classified as high-risk. High-risk tools require…]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is at least a member (member or owner).]] - rationale - gateway/security/group_rbac.py
- [[Return True if user_id is the owner in group_chat_id.]] - rationale - gateway/security/group_rbac.py
- [[Return the GroupRole for user_id in group_chat_id. Returns GroupRole.READ_ONLY…]] - rationale - gateway/security/group_rbac.py
- [[Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers.]] - rationale - gateway/tests/test_group_rbac.py
- [[TestGroupRoleProperties]] - code - gateway/tests/test_group_rbac.py
- [[get_all_roles with an invalid role string falls back to READ_ONLY per entry.]] - rationale - gateway/tests/test_group_rbac.py
- [[remove_role on a user not in map is a no-op (no exception).]] - rationale - gateway/tests/test_group_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupRoleResolver
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_GroupRole]]
- 3 edges to [[_COMMUNITY_test_group_rbac.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[GroupRoleResolver]] - degree 27, connects to 3 communities
- [[TestGroupRoleProperties]] - degree 23, connects to 2 communities
- [[dot-get_role()]] - degree 5, connects to 1 community
