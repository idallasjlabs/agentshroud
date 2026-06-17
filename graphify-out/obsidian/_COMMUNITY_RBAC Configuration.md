---
type: community
cohesion: 0.03
members: 127
---

# RBAC Configuration

**Cohesion:** 0.03 - loosely connected
**Members:** 127 nodes

## Members
- [[.__init__()_89]] - code - gateway/security/rbac.py
- [[._build_permission_matrix()]] - code - gateway/security/rbac.py
- [[._build_tool_permissions()]] - code - gateway/security/rbac.py
- [[.audit_privilege_change()]] - code - gateway/security/rbac.py
- [[.can_user_manage_user()]] - code - gateway/security/rbac.py
- [[.check_group_permission()]] - code - gateway/security/rbac.py
- [[.check_permission()]] - code - gateway/security/rbac.py
- [[.check_tool_permission()_1]] - code - gateway/security/rbac.py
- [[.create_group()]] - code - gateway/security/rbac_config.py
- [[.get_role_hierarchy()]] - code - gateway/security/rbac.py
- [[.get_user_permissions_summary()]] - code - gateway/security/rbac.py
- [[.get_user_role()]] - code - gateway/security/rbac.py
- [[.init_auto_groups()]] - code - gateway/security/rbac_config.py
- [[.is_privilege_escalation()]] - code - gateway/security/rbac.py
- [[.list_users_and_roles()]] - code - gateway/security/rbac.py
- [[.set_user_role()]] - code - gateway/security/rbac.py
- [[.setup_method()_18]] - code - gateway/tests/test_rbac.py
- [[.setup_method()_17]] - code - gateway/tests/test_rbac.py
- [[.teardown_method()_3]] - code - gateway/tests/test_rbac.py
- [[.test_conversion_error_path()_4]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_default_config_initialization()]] - code - gateway/tests/test_rbac.py
- [[.test_full_dict()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_get_users_by_role()]] - code - gateway/tests/test_rbac.py
- [[.test_invalid_action_resource_combinations()]] - code - gateway/tests/test_rbac.py
- [[.test_invalid_user_id()]] - code - gateway/tests/test_rbac.py
- [[.test_list_users_and_roles()]] - code - gateway/tests/test_rbac.py
- [[.test_minimal_dict_uses_fallbacks()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_owner_and_collaborators_can_be_overridden_from_env()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_check_with_context()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_admin()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_collaborator()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_owner()]] - code - gateway/tests/test_rbac.py
- [[.test_permission_matrix_viewer()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_allows_authorized_access()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_blocks_unauthorized_access()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_handles_missing_user_id()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_initialization_in_middleware()]] - code - gateway/tests/test_rbac.py
- [[.test_rbac_manager_without_config()]] - code - gateway/tests/test_rbac.py
- [[.test_role_assignment()]] - code - gateway/tests/test_rbac.py
- [[.test_role_hierarchy_checks()]] - code - gateway/tests/test_rbac.py
- [[.test_role_hierarchy_levels()]] - code - gateway/tests/test_rbac.py
- [[.test_set_user_role()]] - code - gateway/tests/test_rbac.py
- [[.test_severity_enum_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_string_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_tool_tier_permissions()]] - code - gateway/tests/test_rbac.py
- [[.test_user_management_hierarchy()]] - code - gateway/tests/test_rbac.py
- [[.test_user_permissions_summary()]] - code - gateway/tests/test_rbac.py
- [[A named group of users.]] - rationale - gateway/security/rbac_config.py
- [[Action_1]] - code - gateway/security/rbac.py
- [[Actions that can be performed in the system.]] - rationale - gateway/security/rbac.py
- [[Any_49]] - code - gateway/security/rbac.py
- [[Any_65]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Build the permission matrix for all roles.]] - rationale - gateway/security/rbac.py
- [[Build tool tier permissions for each role.]] - rationale - gateway/security/rbac.py
- [[Check if a user can perform an action on a group.          Permission matrix]] - rationale - gateway/security/rbac.py
- [[Check if a user can use tools of a specific tier.]] - rationale - gateway/security/rbac.py
- [[Check if a user has permission to perform an action on a resource.]] - rationale - gateway/security/rbac.py
- [[Check if one user can manage another user.]] - rationale - gateway/security/rbac.py
- [[Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t]] - rationale - gateway/tests/test_rbac.py
- [[Create or replace a custom group and persist it.]] - rationale - gateway/security/rbac_config.py
- [[Derive and reset auto-groups from current RBAC user list, then load custom group]] - rationale - gateway/security/rbac_config.py
- [[Env overrides should drive runtime ownercollaborator identity.]] - rationale - gateway/tests/test_rbac.py
- [[Get a summary of permissions for a user.]] - rationale - gateway/security/rbac.py
- [[Get role hierarchy levels (higher number = more privileges).]] - rationale - gateway/security/rbac.py
- [[Get the role for a user.]] - rationale - gateway/security/rbac.py
- [[Group]] - code - gateway/security/rbac_config.py
- [[Initialize RBAC manager with configuration.]] - rationale - gateway/security/rbac.py
- [[List all users and their roles (admin+ only)._1]] - rationale - gateway/security/rbac.py
- [[Log privilege changes; emit WARNING for escalations (unusual patterns).]] - rationale - gateway/security/rbac.py
- [[PermissionResult]] - code - gateway/security/rbac.py
- [[RBACConfig]] - code - gateway/security/rbac.py
- [[RBACConfig_3]] - code - gateway/tests/test_rbac.py
- [[RBACManager_1]] - code - gateway/security/rbac.py
- [[Read custom groups from disk.]] - rationale - gateway/security/rbac_config.py
- [[Resource_1]] - code - gateway/security/rbac.py
- [[Resources that can be accessed in the system.]] - rationale - gateway/security/rbac.py
- [[Result of permission check.]] - rationale - gateway/security/rbac.py
- [[Return True if changing from_role → to_role represents an escalation.]] - rationale - gateway/security/rbac.py
- [[Role]] - code - gateway/security/rbac.py
- [[Role_1]] - code - gateway/security/rbac_config.py
- [[Role-Based Access Control Manager.]] - rationale - gateway/security/rbac.py
- [[Set a user's role (owner-only operation).]] - rationale - gateway/security/rbac.py
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
- [[TestFromDict]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestMapSeverity]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestRBACConfig]] - code - gateway/tests/test_rbac.py
- [[TestRBACErrorHandling]] - code - gateway/tests/test_rbac.py
- [[TestRBACIntegration]] - code - gateway/tests/test_rbac.py
- [[TestRBACManager]] - code - gateway/tests/test_rbac.py
- [[Tool security tiers for RBAC permissions.]] - rationale - gateway/security/rbac_config.py
- [[ToolTier_1]] - code - gateway/security/rbac.py
- [[ToolTier_2]] - code - gateway/security/rbac_config.py
- [[User roles in AgentShroud RBAC system.      Hierarchy (highest to lowest)]] - rationale - gateway/security/rbac_config.py
- [[Write only custom groups to disk (auto-groups are derived at runtime).]] - rationale - gateway/security/rbac_config.py
- [[_load_persisted_groups()]] - code - gateway/security/rbac_config.py
- [[_persist_groups()]] - code - gateway/security/rbac_config.py
- [[auth.py_1]] - code - gateway/soc/auth.py
- [[rbac.py]] - code - gateway/security/rbac.py
- [[rbac_config.py]] - code - gateway/security/rbac_config.py
- [[test_rbac.py]] - code - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBAC_Configuration
SORT file.name ASC
```

## Connections to other communities
- 47 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 39 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 34 edges to [[_COMMUNITY_SOC Authentication]]
- 30 edges to [[_COMMUNITY_Module Group 120]]
- 29 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 23 edges to [[_COMMUNITY_Module Group 186]]
- 21 edges to [[_COMMUNITY_Module Group 207]]
- 14 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 10 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 9 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 8 edges to [[_COMMUNITY_Module Group 296]]
- 6 edges to [[_COMMUNITY_Privacy Policy]]
- 5 edges to [[_COMMUNITY_Webhook Receiver]]
- 5 edges to [[_COMMUNITY_SOC Router Tests]]
- 4 edges to [[_COMMUNITY_Group Config & Teams]]
- 4 edges to [[_COMMUNITY_Module Group 270]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Module Group 554]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_Module Group 272]]
- 1 edge to [[_COMMUNITY_Module Group 213]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_SOC Services & Health Status]]

## Top bridge nodes
- [[Role_1]] - degree 110, connects to 19 communities
- [[Action_1]] - degree 61, connects to 11 communities
- [[Resource_1]] - degree 60, connects to 11 communities
- [[rbac_config.py]] - degree 15, connects to 8 communities
- [[PermissionResult]] - degree 41, connects to 7 communities