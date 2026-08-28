---
type: community
cohesion: 0.14
members: 26
---

# Community 335

**Cohesion:** 0.14 - loosely connected
**Members:** 26 nodes

## Members
- [[._store_path()]] - code - gateway/tests/test_rbac.py
- [[.test_load_collab_store_returns_empty_on_corrupt_json()]] - code - gateway/tests/test_rbac.py
- [[.test_load_removed_and_paused_ids_empty_when_no_file()]] - code - gateway/tests/test_rbac.py
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
- [[.test_unpause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_unpause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[Bug 1 RBACConfig.__post_init__ must exclude persisted-removed IDs from the]] - rationale - gateway/tests/test_rbac.py
- [[Bug 1 revoking a hardcoded default (never in approved_collaborators.json)]] - rationale - gateway/tests/test_rbac.py
- [[Pausing is access-gating only, not a roleremoval change (constraint check).]] - rationale - gateway/tests/test_rbac.py
- [[TestCollaboratorPersistence]] - code - gateway/tests/test_rbac.py
- [[Writes to one exclusion set must not clobber the other persisted keys.]] - rationale - gateway/tests/test_rbac.py
- [[removed_collaborator_ids  paused_collaborator_ids share approved_collaborators.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_335
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Community 200]]

## Top bridge nodes
- [[TestCollaboratorPersistence]] - degree 30, connects to 3 communities
- [[.test_pause_does_not_remove_from_collaborator_role()]] - degree 4, connects to 1 community
- [[.test_removed_hardcoded_collaborator_excluded_from_effective_set()]] - degree 4, connects to 1 community
- [[.test_removed_dynamic_collaborator_excluded_from_effective_set()]] - degree 3, connects to 1 community