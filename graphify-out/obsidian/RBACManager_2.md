---
source_file: "gateway/security/rbac.py"
type: "code"
community: "Action"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Action
---

# RBACManager

## Connections
- [[dot-__init__()_88]] - `method` [EXTRACTED]
- [[dot-_build_permission_matrix()]] - `method` [EXTRACTED]
- [[dot-_build_tool_permissions()]] - `method` [EXTRACTED]
- [[dot-audit_privilege_change()]] - `method` [EXTRACTED]
- [[dot-can_user_manage_user()]] - `method` [EXTRACTED]
- [[dot-check_group_permission()]] - `method` [EXTRACTED]
- [[dot-check_permission()_1]] - `method` [EXTRACTED]
- [[dot-check_tool_permission()]] - `method` [EXTRACTED]
- [[dot-get_role_hierarchy()]] - `method` [EXTRACTED]
- [[dot-get_user_permissions_summary()]] - `method` [EXTRACTED]
- [[dot-get_user_role()]] - `method` [EXTRACTED]
- [[dot-is_privilege_escalation()]] - `method` [EXTRACTED]
- [[dot-list_users_and_roles()]] - `method` [EXTRACTED]
- [[dot-set_user_role()]] - `method` [EXTRACTED]
- [[dot-setup_method()_18]] - `calls` [EXTRACTED]
- [[dot-test_invalid_action_resource_combinations()]] - `calls` [EXTRACTED]
- [[dot-test_invalid_user_id()]] - `calls` [EXTRACTED]
- [[dot-test_permission_check_with_context()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_manager_without_config()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACConfig_4]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Role_91]] - `uses` [INFERRED]
- [[Role-Based Access Control Manager.]] - `rationale_for` [EXTRACTED]
- [[TestCollaboratorPersistence]] - `uses` [INFERRED]
- [[TestGroupRegistry]] - `uses` [INFERRED]
- [[TestRBACConfig]] - `uses` [INFERRED]
- [[TestRBACErrorHandling]] - `uses` [INFERRED]
- [[TestRBACIntegration]] - `uses` [INFERRED]
- [[TestRBACManager]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[_get_rbac_manager()]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[set_user_role()_1]] - `calls` [EXTRACTED]
- [[socauth.py]] - `imports` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_rbac.py]] - `tests` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Action
