---
source_file: "gateway/security/path_isolation.py"
type: "code"
community: "Community 6"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_6
---

# PathIsolationManager

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[.__init__()_106]] - `method` [EXTRACTED]
- [[._apply_path_rewriting()]] - `method` [EXTRACTED]
- [[._check_cross_user_access()]] - `method` [EXTRACTED]
- [[._cleanup_user_directory()]] - `method` [EXTRACTED]
- [[._ensure_base_directory()]] - `method` [EXTRACTED]
- [[._ensure_user_directory()]] - `method` [EXTRACTED]
- [[._get_user_temp_dir()]] - `method` [EXTRACTED]
- [[._is_base_directory_access()]] - `method` [EXTRACTED]
- [[._sanitize_user_id()]] - `method` [EXTRACTED]
- [[.cleanup_abandoned_directories()]] - `method` [EXTRACTED]
- [[.end_user_session()]] - `method` [EXTRACTED]
- [[.get_active_users()]] - `method` [EXTRACTED]
- [[.get_stats()_18]] - `method` [EXTRACTED]
- [[.get_user_temp_path()]] - `method` [EXTRACTED]
- [[.manager()_1]] - `calls` [EXTRACTED]
- [[.register_user_session()]] - `method` [EXTRACTED]
- [[.rewrite_path()]] - `method` [EXTRACTED]
- [[.test_path_isolation_instantiates()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Manages per-user path isolation for temporary files and directories.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Path Isolation Manager Tests]] - `references` [EXTRACTED]
- [[PathIsolationConfig]] - `references` [EXTRACTED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestPathIsolationConfig]] - `uses` [INFERRED]
- [[TestPathIsolationManager]] - `uses` [INFERRED]
- [[TestPathRewriteResult]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[path_isolation.py]] - `contains` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_path_isolation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_6