---
source_file: "gateway/security/rbac.py"
type: "code"
community: "Auth & Exception Types"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Auth__Exception_Types
---

# RBACManager

## Connections
- [[.__init__()_109]] - `method` [EXTRACTED]
- [[._build_permission_matrix()]] - `method` [EXTRACTED]
- [[._build_tool_permissions()]] - `method` [EXTRACTED]
- [[.audit_privilege_change()]] - `method` [EXTRACTED]
- [[.can_user_manage_user()]] - `method` [EXTRACTED]
- [[.check_group_permission()]] - `method` [EXTRACTED]
- [[.check_permission()]] - `method` [EXTRACTED]
- [[.check_tool_permission()_1]] - `method` [EXTRACTED]
- [[.get_role_hierarchy()]] - `method` [EXTRACTED]
- [[.get_user_permissions_summary()]] - `method` [EXTRACTED]
- [[.get_user_role()]] - `method` [EXTRACTED]
- [[.is_privilege_escalation()]] - `method` [EXTRACTED]
- [[.list_users_and_roles()]] - `method` [EXTRACTED]
- [[.set_user_role()]] - `method` [EXTRACTED]
- [[.setup_method()_20]] - `calls` [EXTRACTED]
- [[.test_invalid_action_resource_combinations()]] - `calls` [EXTRACTED]
- [[.test_invalid_user_id()]] - `calls` [EXTRACTED]
- [[.test_permission_check_with_context()]] - `calls` [EXTRACTED]
- [[.test_rbac_manager_without_config()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_10]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACConfig_3]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[Role-Based Access Control Manager.]] - `rationale_for` [EXTRACTED]
- [[TestGroupRegistry]] - `uses` [INFERRED]
- [[TestRBACConfig]] - `uses` [INFERRED]
- [[TestRBACErrorHandling]] - `uses` [INFERRED]
- [[TestRBACIntegration]] - `uses` [INFERRED]
- [[TestRBACManager]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[_get_rbac_manager()]] - `calls` [EXTRACTED]
- [[auth.py_1]] - `imports` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[set_user_role()_1]] - `calls` [EXTRACTED]
- [[test_rbac.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Auth__Exception_Types