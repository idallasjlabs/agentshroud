---
type: community
members: 87
---

# PathIsolationManager

**Members:** 87 nodes

## Members
- [[dot-__init__()_95]] - code - gateway/security/path_isolation.py
- [[dot-_apply_path_rewriting()]] - code - gateway/security/path_isolation.py
- [[dot-_check_cross_user_access()]] - code - gateway/security/path_isolation.py
- [[dot-_cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_base_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_get_user_temp_dir()]] - code - gateway/security/path_isolation.py
- [[dot-_is_base_directory_access()]] - code - gateway/security/path_isolation.py
- [[dot-_sanitize_user_id()]] - code - gateway/security/path_isolation.py
- [[dot-cleanup_abandoned_directories()]] - code - gateway/security/path_isolation.py
- [[dot-config()]] - code - gateway/tests/test_path_isolation.py
- [[dot-end_user_session()]] - code - gateway/security/path_isolation.py
- [[dot-get_active_users()]] - code - gateway/security/path_isolation.py
- [[dot-get_stats()_6]] - code - gateway/security/path_isolation.py
- [[dot-get_user_temp_path()]] - code - gateway/security/path_isolation.py
- [[dot-manager()]] - code - gateway/tests/test_path_isolation.py
- [[dot-register_user_session()]] - code - gateway/security/path_isolation.py
- [[dot-rewrite_path()]] - code - gateway/security/path_isolation.py
- [[dot-temp_dir()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_allow_own_namespace_access()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_already_isolated_paths_not_rewritten()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_basic_result()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_block_base_directory_access()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_block_cross_user_access()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_blocked_result()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_cleanup_abandoned_directories()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_dont_cleanup_active_user_directories()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_end_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_get_active_users()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_get_stats()_1]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_get_user_temp_path()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_initialization()_2]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_path_isolation_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_path_rewriting_nested_paths()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_path_rewriting_no_rewrite_needed()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_path_rewriting_temp_files()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_register_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_user_id_sanitization()]] - code - gateway/tests/test_path_isolation.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace. Returns…]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Create base agentshroud temp directory if it doesn't exist.]] - rationale - gateway/security/path_isolation.py
- [[Create path isolation manager for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create temporary directory for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create test configuration.]] - rationale - gateway/tests/test_path_isolation.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Ensure user's isolated directory exists.]] - rationale - gateway/security/path_isolation.py
- [[Get a path within the user's isolated temp directory.]] - rationale - gateway/security/path_isolation.py
- [[Get set of currently active users.]] - rationale - gateway/security/path_isolation.py
- [[Get statistics about path isolation manager.]] - rationale - gateway/security/path_isolation.py
- [[Get the isolated temp directory path for a user.]] - rationale - gateway/security/path_isolation.py
- [[Manages per-user path isolation for temporary files and directories.]] - rationale - gateway/security/path_isolation.py
- [[PathIsolationManager]] - code - gateway/security/path_isolation.py
- [[PathRewriteResult]] - code - gateway/security/path_isolation.py
- [[Register a new user session and create their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Result of path rewriting operation.]] - rationale - gateway/security/path_isolation.py
- [[Rewrite a path to isolate it to the user's namespace. Args path Original file…]] - rationale - gateway/security/path_isolation.py
- [[Sanitize user ID to prevent path traversal attacks.]] - rationale - gateway/security/path_isolation.py
- [[Test PathRewriteResult dataclass.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test allowing access to own namespace.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test basic result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocked result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocking cross-user namespace access.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocking direct access to base agentshroud directory.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test cleanup of abandoned user directories.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test ending user session.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test getting active users.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test getting statistics.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test getting user temp path.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test manager initialization.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path isolation manager.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path rewriting for tmp files.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path rewriting for nested tmp paths.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test paths that don't need rewriting.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test that active user directories are not cleaned up.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test that already isolated paths are not double-rewritten.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test user ID sanitization.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test user session registration.]] - rationale - gateway/tests/test_path_isolation.py
- [[TestPathIsolationManager]] - code - gateway/tests/test_path_isolation.py
- [[TestPathRewriteResult]] - code - gateway/tests/test_path_isolation.py
- [[any_37]] - code
- [[fixture_79]] - code
- [[patch_4]] - code
- [[path_isolation.py]] - code - gateway/security/path_isolation.py
- [[test_path_isolation.py]] - code - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_TestModuleInstantiationInEnforceMode]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[PathIsolationManager]] - degree 29, connects to 5 communities
- [[path_isolation.py]] - degree 6, connects to 3 communities
- [[dot-test_path_isolation_instantiates()]] - degree 3, connects to 2 communities
- [[TestPathIsolationManager]] - degree 23, connects to 1 community
- [[test_path_isolation.py]] - degree 7, connects to 1 community
