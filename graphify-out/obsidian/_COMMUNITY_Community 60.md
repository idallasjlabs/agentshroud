---
type: community
members: 112
---

# Community 60

**Members:** 112 nodes

## Members
- [[._make_rbac()]] - code - gateway/tests/test_rbac.py
- [[._store_path()]] - code - gateway/tests/test_rbac.py
- [[.can_user_manage_user()]] - code - gateway/security/rbac.py
- [[.get_role_hierarchy()]] - code - gateway/security/rbac.py
- [[.is_member()_1]] - code - gateway/security/rbac_config.py
- [[.setup_method()_20]] - code - gateway/tests/test_rbac.py
- [[.setup_method()_21]] - code - gateway/tests/test_rbac.py
- [[.teardown_method()_4]] - code - gateway/tests/test_rbac.py
- [[.test_add_remove_member()]] - code - gateway/tests/test_rbac.py
- [[.test_auto_groups_created()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_create_reserved_group_id()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_delete_auto_group()]] - code - gateway/tests/test_rbac.py
- [[.test_create_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_default_config_initialization()]] - code - gateway/tests/test_rbac.py
- [[.test_delete_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_everyone_group_contains_all_users()]] - code - gateway/tests/test_rbac.py
- [[.test_get_users_by_role()]] - code - gateway/tests/test_rbac.py
- [[.test_invalid_action_resource_combinations()]] - code - gateway/tests/test_rbac.py
- [[.test_invalid_user_id()]] - code - gateway/tests/test_rbac.py
- [[.test_is_member_unknown_group_returns_false()]] - code - gateway/tests/test_rbac.py
- [[.test_list_users_and_roles()]] - code - gateway/tests/test_rbac.py
- [[.test_load_collab_store_returns_empty_on_corrupt_json()]] - code - gateway/tests/test_rbac.py
- [[.test_load_removed_and_paused_ids_empty_when_no_file()]] - code - gateway/tests/test_rbac.py
- [[.test_owner_and_collaborators_can_be_overridden_from_env()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_and_unpause_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_does_not_remove_from_collaborator_role()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_pause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_check_with_context()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_admin()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_owner()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_viewer()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_and_load_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_is_idempotent()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_returns_none_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_persist_returns_none_on_mkdir_error()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_allows_authorized_access()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_blocks_unauthorized_access()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_handles_missing_user_id()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_initialization_in_middleware()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_manager_without_config()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_and_paused_ids_coexist_independently()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_dynamic_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[.test_removed_hardcoded_collaborator_excluded_from_effective_set()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_hardcoded_collaborator_records_removal_even_though_never_persisted()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_removes_dynamic_collaborator_and_records_removal()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_revoke_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[.test_role_assignment()]] - code - gateway/tests/test_rbac.py
- [[.test_role_hierarchy_checks()]] - code - gateway/tests/test_rbac.py
- [[.test_role_hierarchy_levels()]] - code - gateway/tests/test_rbac.py
- [[.test_set_user_role()]] - code - gateway/tests/test_rbac.py
- [[.test_slack_group_contains_slack_ids()]] - code - gateway/tests/test_rbac.py
- [[.test_telegram_group_contains_numeric_ids()]] - code - gateway/tests/test_rbac.py
- [[.test_tool_tier_permissions()]] - code - gateway/tests/test_rbac.py
- [[.test_unpause_returns_false_on_inner_write_error()]] - code - gateway/tests/test_rbac.py
- [[.test_unpause_returns_false_on_io_error()]] - code - gateway/tests/test_rbac.py
- [[.test_user_management_hierarchy()]] - code - gateway/tests/test_rbac.py
- [[.test_user_permissions_summary()]] - code - gateway/tests/test_rbac.py
- [[Bug 1 RBACConfig.__post_init__ must exclude persisted-removed IDs from the]] - rationale - gateway/tests/test_rbac.py
- [[Bug 1 revoking a hardcoded default (never in approved_collaborators.json)]] - rationale - gateway/tests/test_rbac.py
- [[Check if one user can manage another user.]] - rationale - gateway/security/rbac.py
- [[Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t]] - rationale - gateway/tests/test_rbac.py
- [[Env overrides should drive runtime ownercollaborator identity.]] - rationale - gateway/tests/test_rbac.py
- [[Get role hierarchy levels (higher number = more privileges).]] - rationale - gateway/security/rbac.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[LogRecord]] - code - gateway/ingest_api/lifespan.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Pausing is access-gating only, not a roleremoval change (constraint check).]] - rationale - gateway/tests/test_rbac.py
- [[RBACConfig_3]] - code - gateway/tests/test_rbac.py
- [[RBACManager_1]] - code - gateway/security/rbac.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[Role-Based Access Control Manager.]] - rationale - gateway/security/rbac.py
- [[Set up test environment._2]] - rationale - gateway/tests/test_rbac.py
- [[Set up test environment._3]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC configuration.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC error handling and edge cases.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC handling when user ID is missing.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC integration with middleware.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC manager functionality.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC manager initialization without explicit config.]] - rationale - gateway/tests/test_rbac.py
- [[Test admin role permissions.]] - rationale - gateway/tests/test_rbac.py
- [[Test collaborator role permissions.]] - rationale - gateway/tests/test_rbac.py
- [[Test default RBAC configuration initialization.]] - rationale - gateway/tests/test_rbac.py
- [[Test dynamic role assignment.]] - rationale - gateway/tests/test_rbac.py
- [[Test getting user permissions summary.]] - rationale - gateway/tests/test_rbac.py
- [[Test getting users by role.]] - rationale - gateway/tests/test_rbac.py
- [[Test handling of invalid actionresource combinations.]] - rationale - gateway/tests/test_rbac.py
- [[Test handling of invalid user IDs.]] - rationale - gateway/tests/test_rbac.py
- [[Test listing users and roles.]] - rationale - gateway/tests/test_rbac.py
- [[Test owner role permissions.]] - rationale - gateway/tests/test_rbac.py
- [[Test permission checks with additional context.]] - rationale - gateway/tests/test_rbac.py
- [[Test role hierarchy helper methods.]] - rationale - gateway/tests/test_rbac.py
- [[Test role hierarchy levels.]] - rationale - gateway/tests/test_rbac.py
- [[Test setting user roles.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC allows authorized access.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC blocks unauthorized access attempts.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC is properly initialized in middleware.]] - rationale - gateway/tests/test_rbac.py
- [[Test tool tier access permissions.]] - rationale - gateway/tests/test_rbac.py
- [[Test user management hierarchy.]] - rationale - gateway/tests/test_rbac.py
- [[Test viewer role permissions.]] - rationale - gateway/tests/test_rbac.py
- [[TestCollaboratorPersistence]] - code - gateway/tests/test_rbac.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[TestRBACConfig]] - code - gateway/tests/test_rbac.py
- [[TestRBACErrorHandling]] - code - gateway/tests/test_rbac.py
- [[TestRBACIntegration]] - code - gateway/tests/test_rbac.py
- [[TestRBACManager]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py
- [[Writes to one exclusion set must not clobber the other persisted keys.]] - rationale - gateway/tests/test_rbac.py
- [[removed_collaborator_ids  paused_collaborator_ids share approved_collaborators.]] - rationale - gateway/tests/test_rbac.py
- [[test_rbac.py]] - code - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_60
SORT file.name ASC
```

## Connections to other communities
- 53 edges to [[_COMMUNITY_Community 6]]
- 18 edges to [[_COMMUNITY_Community 72]]
- 11 edges to [[_COMMUNITY_Community 1]]
- 8 edges to [[_COMMUNITY_Community 223]]
- 5 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 2200]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 229]]
- 1 edge to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 33]]

## Top bridge nodes
- [[LogRecord]] - degree 10, connects to 8 communities
- [[RBACManager_1]] - degree 48, connects to 4 communities
- [[GroupRegistry]] - degree 34, connects to 4 communities
- [[TestCollaboratorPersistence]] - degree 30, connects to 3 communities
- [[TestRBACManager]] - degree 21, connects to 3 communities