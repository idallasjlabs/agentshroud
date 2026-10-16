---
source_file: "gateway/security/path_isolation.py"
type: "code"
community: "MiddlewareManager"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MiddlewareManager
---

# PathIsolationManager

## Connections
- [[dot-__init__()_16]] - `calls` [EXTRACTED]
- [[dot-__init__()_23]] - `method` [EXTRACTED]
- [[dot-_apply_path_rewriting()]] - `method` [EXTRACTED]
- [[dot-_check_cross_user_access()]] - `method` [EXTRACTED]
- [[dot-_cleanup_user_directory()]] - `method` [EXTRACTED]
- [[dot-_ensure_base_directory()]] - `method` [EXTRACTED]
- [[dot-_ensure_user_directory()]] - `method` [EXTRACTED]
- [[dot-_get_user_temp_dir()]] - `method` [EXTRACTED]
- [[dot-_is_base_directory_access()]] - `method` [EXTRACTED]
- [[dot-_sanitize_user_id()]] - `method` [EXTRACTED]
- [[dot-cleanup_abandoned_directories()]] - `method` [EXTRACTED]
- [[dot-end_user_session()]] - `method` [EXTRACTED]
- [[dot-get_active_users()]] - `method` [EXTRACTED]
- [[dot-get_stats()_2]] - `method` [EXTRACTED]
- [[dot-get_user_temp_path()]] - `method` [EXTRACTED]
- [[dot-manager()_2]] - `calls` [EXTRACTED]
- [[dot-register_user_session()]] - `method` [EXTRACTED]
- [[dot-rewrite_path()]] - `method` [EXTRACTED]
- [[dot-test_path_isolation_instantiates()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
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
- [[run()]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_path_isolation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/MiddlewareManager
