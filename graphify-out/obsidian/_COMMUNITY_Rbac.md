---
type: community
cohesion: 0.06
members: 59
---

# Rbac

**Cohesion:** 0.06 - loosely connected
**Members:** 59 nodes

## Members
- [[._make_rbac()]] - code - gateway/tests/test_rbac.py
- [[._store_path()]] - code - gateway/tests/test_rbac.py
- [[.is_member()_1]] - code - gateway/security/rbac_config.py
- [[.list_groups()]] - code - gateway/security/rbac_config.py
- [[.setup_method()_20]] - code - gateway/tests/test_rbac.py
- [[.test_add_remove_member()]] - code - gateway/tests/test_rbac.py
- [[.test_auto_groups_created()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_create_reserved_group_id()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_delete_auto_group()]] - code - gateway/tests/test_rbac.py
- [[.test_create_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_default_config_initialization()]] - code - gateway/tests/test_rbac.py
- [[.test_delete_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_everyone_group_contains_all_users()]] - code - gateway/tests/test_rbac.py
- [[.test_get_users_by_role()]] - code - gateway/tests/test_rbac.py
- [[.test_is_member_unknown_group_returns_false()]] - code - gateway/tests/test_rbac.py
- [[.test_load_collab_store_returns_empty_on_corrupt_json()]] - code - gateway/tests/test_rbac.py
- [[.test_load_removed_and_paused_ids_empty_when_no_file()]] - code - gateway/tests/test_rbac.py
- [[.test_owner_and_collaborators_can_be_overridden_from_env()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_and_unpause_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_does_not_remove_from_collaborator_role()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_and_load_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_is_idempotent()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_returns_none_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_returns_none_on_mkdir_error()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_and_paused_ids_coexist_independently()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_dynamic_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_hardcoded_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_hardcoded_collaborator_records_removal_even_though_never_persisted()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_removes_dynamic_collaborator_and_records_removal()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[.test_role_assignment()]] - code - gateway/tests/test_rbac.py
- [[.test_role_hierarchy_checks()]] - code - gateway/tests/test_rbac.py
- [[.test_slack_group_contains_slack_ids()]] - code - gateway/tests/test_rbac.py
- [[.test_telegram_group_contains_numeric_ids()]] - code - gateway/tests/test_rbac.py
- [[.test_unpause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_unpause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[Bug 1 RBACConfig.__post_init__ must exclude persisted-removed IDs from the]] - rationale - gateway/tests/test_rbac.py
- [[Bug 1 revoking a hardcoded default (never in approved_collaborators.json)]] - rationale - gateway/tests/test_rbac.py
- [[Env overrides should drive runtime ownercollaborator identity.]] - rationale - gateway/tests/test_rbac.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[LogRecord_3]] - code - gateway/ingest_api/lifespan.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Pausing is access-gating only, not a roleremoval change (constraint check).]] - rationale - gateway/tests/test_rbac.py
- [[RBACConfig_3]] - code - gateway/tests/test_rbac.py
- [[RBACConfig_5]] - code - gateway/tests/test_rbac.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[Set up test environment._1]] - rationale - gateway/tests/test_rbac.py
- [[Test default RBAC configuration initialization.]] - rationale - gateway/tests/test_rbac.py
- [[Test dynamic role assignment.]] - rationale - gateway/tests/test_rbac.py
- [[Test getting users by role.]] - rationale - gateway/tests/test_rbac.py
- [[Test role hierarchy helper methods.]] - rationale - gateway/tests/test_rbac.py
- [[TestCollaboratorPersistence]] - code - gateway/tests/test_rbac.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py
- [[Writes to one exclusion set must not clobber the other persisted keys.]] - rationale - gateway/tests/test_rbac.py
- [[removed_collaborator_ids  paused_collaborator_ids share approved_collaborators.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Rbac
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 8 edges to [[_COMMUNITY_Rbac Config (security)]]
- 6 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 5 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 1 edge to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 1 edge to [[_COMMUNITY_SOC Router Coverage]]

## Top bridge nodes
- [[GroupRegistry]] - degree 37, connects to 5 communities
- [[TestCollaboratorPersistence]] - degree 30, connects to 2 communities
- [[TestGroupRegistry]] - degree 21, connects to 2 communities
- [[RBACConfig_3]] - degree 18, connects to 2 communities
- [[RBACConfig_5]] - degree 13, connects to 2 communities