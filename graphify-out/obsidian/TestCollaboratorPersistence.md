---
source_file: "gateway/tests/test_rbac.py"
type: "code"
community: "Community 70"
location: "L572"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_70
---

# TestCollaboratorPersistence

## Connections
- [[._store_path()]] - `method` [EXTRACTED]
- [[.test_load_collab_store_returns_empty_on_corrupt_json()]] - `method` [EXTRACTED]
- [[.test_load_removed_and_paused_ids_empty_when_no_file()]] - `method` [EXTRACTED]
- [[.test_pause_and_unpause_collaborator()]] - `method` [EXTRACTED]
- [[.test_pause_does_not_remove_from_collaborator_role()]] - `method` [EXTRACTED]
- [[.test_pause_returns_false_on_inner_write_error()]] - `method` [EXTRACTED]
- [[.test_pause_returns_false_on_io_error()]] - `method` [EXTRACTED]
- [[.test_persist_and_load_collaborator()]] - `method` [EXTRACTED]
- [[.test_persist_is_idempotent()]] - `method` [EXTRACTED]
- [[.test_persist_returns_none_on_inner_write_error()]] - `method` [EXTRACTED]
- [[.test_persist_returns_none_on_mkdir_error()]] - `method` [EXTRACTED]
- [[.test_removed_and_paused_ids_coexist_independently()]] - `method` [EXTRACTED]
- [[.test_removed_dynamic_collaborator_excluded_from_effective_set()]] - `method` [EXTRACTED]
- [[.test_removed_hardcoded_collaborator_excluded_from_effective_set()]] - `method` [EXTRACTED]
- [[.test_revoke_hardcoded_collaborator_records_removal_even_though_never_persisted()]] - `method` [EXTRACTED]
- [[.test_revoke_removes_dynamic_collaborator_and_records_removal()]] - `method` [EXTRACTED]
- [[.test_revoke_returns_false_on_inner_write_error()]] - `method` [EXTRACTED]
- [[.test_revoke_returns_false_on_io_error()]] - `method` [EXTRACTED]
- [[.test_unpause_returns_false_on_inner_write_error()]] - `method` [EXTRACTED]
- [[.test_unpause_returns_false_on_io_error()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[GroupRegistry]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[removed_collaborator_ids  paused_collaborator_ids share approved_collaborators.]] - `rationale_for` [EXTRACTED]
- [[test_rbac.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_70