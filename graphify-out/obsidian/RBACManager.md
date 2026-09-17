---
source_file: "gateway/security/rbac.py"
type: "code"
community: "ingest_api/main.py"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# RBACManager

## Connections
- [[.__init__()_9]] - `method` [EXTRACTED]
- [[._build_permission_matrix()]] - `method` [EXTRACTED]
- [[._build_tool_permissions()]] - `method` [EXTRACTED]
- [[.audit_privilege_change()]] - `method` [EXTRACTED]
- [[.can_user_manage_user()]] - `method` [EXTRACTED]
- [[.check_group_permission()]] - `method` [EXTRACTED]
- [[.check_permission()]] - `method` [EXTRACTED]
- [[.check_tool_permission()]] - `method` [EXTRACTED]
- [[.get_role_hierarchy()]] - `method` [EXTRACTED]
- [[.get_user_permissions_summary()]] - `method` [EXTRACTED]
- [[.get_user_role()_1]] - `method` [EXTRACTED]
- [[.is_privilege_escalation()]] - `method` [EXTRACTED]
- [[.list_users_and_roles()]] - `method` [EXTRACTED]
- [[.set_user_role()_1]] - `method` [EXTRACTED]
- [[.setup_method()_1]] - `calls` [EXTRACTED]
- [[.test_invalid_action_resource_combinations()]] - `calls` [EXTRACTED]
- [[.test_invalid_user_id()]] - `calls` [EXTRACTED]
- [[.test_permission_check_with_context()]] - `calls` [EXTRACTED]
- [[.test_rbac_manager_without_config()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PUT users{user_id}role endpoint]] - `calls` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[Role-Based Access Control Manager.]] - `rationale_for` [EXTRACTED]
- [[TestCollaboratorPersistence]] - `uses` [INFERRED]
- [[TestGroupRegistry]] - `uses` [INFERRED]
- [[TestRBACConfig]] - `uses` [INFERRED]
- [[TestRBACErrorHandling]] - `uses` [INFERRED]
- [[TestRBACIntegration]] - `uses` [INFERRED]
- [[TestRBACManager]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[_get_rbac_manager()]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[set_user_role()_1]] - `calls` [EXTRACTED]
- [[socauth.py]] - `imports` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_rbac.py]] - `tests` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ingest_api/mainpy