---
source_file: "gateway/security/path_isolation.py"
type: "code"
community: "PathIsolationManager"
location: "L62"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PathIsolationManager
---

# PathIsolationManager

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_103]] - `method` [EXTRACTED]
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
- [[dot-get_stats()_5]] - `method` [EXTRACTED]
- [[dot-get_user_temp_path()]] - `method` [EXTRACTED]
- [[dot-manager()_1]] - `calls` [EXTRACTED]
- [[dot-register_user_session()]] - `method` [EXTRACTED]
- [[dot-rewrite_path()]] - `method` [EXTRACTED]
- [[dot-test_path_isolation_instantiates()]] - `calls` [EXTRACTED]
- [[Manages per-user path isolation for temporary files and directories.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestPathIsolationManager]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[path_isolation.py]] - `contains` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_path_isolation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PathIsolationManager
