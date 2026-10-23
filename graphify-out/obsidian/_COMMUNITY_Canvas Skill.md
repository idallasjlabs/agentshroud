---
type: community
cohesion: 0.09
members: 37
---

# Canvas Skill

**Cohesion:** 0.09 - loosely connected
**Members:** 37 nodes

## Members
- [[dot-_store_path()]] - code - gateway/tests/test_rbac.py
- [[dot-test_default_config_initialization()]] - code - gateway/tests/test_rbac.py
- [[dot-test_get_users_by_role()]] - code - gateway/tests/test_rbac.py
- [[dot-test_load_collab_store_returns_empty_on_corrupt_json()]] - code - gateway/tests/test_rbac.py
- [[dot-test_load_removed_and_paused_ids_empty_when_no_file()]] - code - gateway/tests/test_rbac.py
- [[dot-test_owner_and_collaborators_can_be_overridden_from_env()]] - code - gateway/tests/test_rbac.py
- [[dot-test_pause_and_unpause_collaborator()]] - code - gateway/tests/test_rbac.py
- [[dot-test_pause_does_not_remove_from_collaborator_role()]] - code - gateway/tests/test_rbac.py
- [[dot-test_pause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_pause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_persist_and_load_collaborator()]] - code - gateway/tests/test_rbac.py
- [[dot-test_persist_is_idempotent()]] - code - gateway/tests/test_rbac.py
- [[dot-test_persist_returns_none_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_persist_returns_none_on_mkdir_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_removed_and_paused_ids_coexist_independently()]] - code - gateway/tests/test_rbac.py
- [[dot-test_removed_dynamic_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[dot-test_removed_hardcoded_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[dot-test_revoke_hardcoded_collaborator_records_removal_even_though_never_persisted()]] - code - gateway/tests/test_rbac.py
- [[dot-test_revoke_removes_dynamic_collaborator_and_records_removal()]] - code - gateway/tests/test_rbac.py
- [[dot-test_revoke_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_revoke_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_role_assignment()]] - code - gateway/tests/test_rbac.py
- [[dot-test_role_hierarchy_checks()]] - code - gateway/tests/test_rbac.py
- [[dot-test_unpause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_unpause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[Bug 1 RBACConfig.__post_init__ must exclude persisted-removed IDs from the]] - rationale - gateway/tests/test_rbac.py
- [[Bug 1 revoking a hardcoded default (never in approved_collaborators.json)]] - rationale - gateway/tests/test_rbac.py
- [[Env overrides should drive runtime ownercollaborator identity.]] - rationale - gateway/tests/test_rbac.py
- [[Pausing is access-gating only, not a roleremoval change (constraint check).]] - rationale - gateway/tests/test_rbac.py
- [[RBACConfig]] - code - gateway/tests/test_rbac.py
- [[Test default RBAC configuration initialization.]] - rationale - gateway/tests/test_rbac.py
- [[Test dynamic role assignment.]] - rationale - gateway/tests/test_rbac.py
- [[Test getting users by role.]] - rationale - gateway/tests/test_rbac.py
- [[Test role hierarchy helper methods.]] - rationale - gateway/tests/test_rbac.py
- [[TestCollaboratorPersistence]] - code - gateway/tests/test_rbac.py
- [[Writes to one exclusion set must not clobber the other persisted keys.]] - rationale - gateway/tests/test_rbac.py
- [[removed_collaborator_ids  paused_collaborator_ids share approved_collaborators.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Canvas_Skill
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 3 edges to [[_COMMUNITY_Function Details]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestCollaboratorPersistence]] - degree 30, connects to 3 communities
- [[RBACConfig]] - degree 18, connects to 3 communities
- [[dot-test_default_config_initialization()]] - degree 3, connects to 1 community
- [[dot-test_get_users_by_role()]] - degree 3, connects to 1 community
- [[dot-test_owner_and_collaborators_can_be_overridden_from_env()]] - degree 3, connects to 1 community
