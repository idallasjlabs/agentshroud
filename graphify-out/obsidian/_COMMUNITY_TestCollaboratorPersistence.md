---
type: community
members: 34
---

# TestCollaboratorPersistence

**Members:** 34 nodes

## Members
- [[dot-_store_path()]] - code - gateway/tests/test_rbac.py
- [[dot-test_load_collab_store_returns_empty_on_corrupt_json()]] - code - gateway/tests/test_rbac.py
- [[dot-test_load_removed_and_paused_ids_empty_when_no_file()]] - code - gateway/tests/test_rbac.py
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
- [[dot-test_unpause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[dot-test_unpause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[Bug 1 RBACConfig.__post_init__ must exclude persisted-removed IDs from the…]] - rationale - gateway/tests/test_rbac.py
- [[Bug 1 revoking a hardcoded default (never in approved_collaborators.json) must…]] - rationale - gateway/tests/test_rbac.py
- [[Pausing is access-gating only, not a roleremoval change (constraint check).]] - rationale - gateway/tests/test_rbac.py
- [[TestCollaboratorPersistence]] - code - gateway/tests/test_rbac.py
- [[Writes to one exclusion set must not clobber the other persisted keys.]] - rationale - gateway/tests/test_rbac.py
- [[boom()_7]] - code - gateway/tests/test_rbac.py
- [[boom()_8]] - code - gateway/tests/test_rbac.py
- [[boom()_9]] - code - gateway/tests/test_rbac.py
- [[boom()_10]] - code - gateway/tests/test_rbac.py
- [[boom()_11]] - code - gateway/tests/test_rbac.py
- [[boom()_12]] - code - gateway/tests/test_rbac.py
- [[boom()_13]] - code - gateway/tests/test_rbac.py
- [[boom()_14]] - code - gateway/tests/test_rbac.py
- [[removed_collaborator_ids  paused_collaborator_ids share…]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestCollaboratorPersistence
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestCollaboratorPersistence]] - degree 24, connects to 2 communities
