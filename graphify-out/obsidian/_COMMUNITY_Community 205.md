---
type: community
cohesion: 0.10
members: 36
---

# Community 205

**Cohesion:** 0.10 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-_make_rbac()]] - code - gateway/tests/test_rbac.py
- [[dot-add_member()]] - code - gateway/security/rbac_config.py
- [[dot-create_group()]] - code - gateway/security/rbac_config.py
- [[dot-delete_group()]] - code - gateway/security/rbac_config.py
- [[dot-get_group()]] - code - gateway/security/rbac_config.py
- [[dot-init_auto_groups()]] - code - gateway/security/rbac_config.py
- [[dot-is_member()_1]] - code - gateway/security/rbac_config.py
- [[dot-list_groups()]] - code - gateway/security/rbac_config.py
- [[dot-remove_member()]] - code - gateway/security/rbac_config.py
- [[dot-test_add_remove_member()]] - code - gateway/tests/test_rbac.py
- [[dot-test_auto_groups_created()]] - code - gateway/tests/test_rbac.py
- [[dot-test_cannot_create_reserved_group_id()]] - code - gateway/tests/test_rbac.py
- [[dot-test_cannot_delete_auto_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_create_custom_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_delete_custom_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_everyone_group_contains_all_users()]] - code - gateway/tests/test_rbac.py
- [[dot-test_is_member_unknown_group_returns_false()]] - code - gateway/tests/test_rbac.py
- [[dot-test_slack_group_contains_slack_ids()]] - code - gateway/tests/test_rbac.py
- [[dot-test_telegram_group_contains_numeric_ids()]] - code - gateway/tests/test_rbac.py
- [[A named group of users.]] - rationale - gateway/security/rbac_config.py
- [[Add a user to a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Create or replace a custom group and persist it.]] - rationale - gateway/security/rbac_config.py
- [[Delete a custom group. Returns True if deleted, False if not found.]] - rationale - gateway/security/rbac_config.py
- [[Derive and reset auto-groups from current RBAC user list, then load custom group]] - rationale - gateway/security/rbac_config.py
- [[Group]] - code - gateway/security/rbac_config.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Read custom groups from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a user from a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[Return group by ID, or None.]] - rationale - gateway/security/rbac_config.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py
- [[Write only custom groups to disk (auto-groups are derived at runtime).]] - rationale - gateway/security/rbac_config.py
- [[_load_persisted_groups()]] - code - gateway/security/rbac_config.py
- [[_persist_groups()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_205
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 5 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 3 edges to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Community 342]]
- 1 edge to [[_COMMUNITY_Ingest Middleware & File Sandbox]]

## Top bridge nodes
- [[GroupRegistry]] - degree 34, connects to 4 communities
- [[TestGroupRegistry]] - degree 21, connects to 2 communities
- [[Group]] - degree 9, connects to 2 communities
- [[_persist_groups()]] - degree 8, connects to 2 communities
- [[dot-_make_rbac()]] - degree 12, connects to 1 community