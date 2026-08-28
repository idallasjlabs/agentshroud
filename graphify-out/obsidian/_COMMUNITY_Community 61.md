---
type: community
cohesion: 0.03
members: 77
---

# Community 61

**Cohesion:** 0.03 - loosely connected
**Members:** 77 nodes

## Members
- [[._apply_path_rewriting()]] - code - gateway/security/path_isolation.py
- [[._check_cross_user_access()]] - code - gateway/security/path_isolation.py
- [[._cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[._ensure_user_directory()]] - code - gateway/security/path_isolation.py
- [[._get_user_temp_dir()]] - code - gateway/security/path_isolation.py
- [[._is_base_directory_access()]] - code - gateway/security/path_isolation.py
- [[._sanitize_user_id()]] - code - gateway/security/path_isolation.py
- [[.cleanup_abandoned_directories()]] - code - gateway/security/path_isolation.py
- [[.config()_4]] - code - gateway/tests/test_path_isolation.py
- [[.end_user_session()]] - code - gateway/security/path_isolation.py
- [[.get_user_temp_path()]] - code - gateway/security/path_isolation.py
- [[.manager()_1]] - code - gateway/tests/test_path_isolation.py
- [[.register_user_session()]] - code - gateway/security/path_isolation.py
- [[.rewrite_path()]] - code - gateway/security/path_isolation.py
- [[.temp_dir()]] - code - gateway/tests/test_path_isolation.py
- [[.test_allow_own_namespace_access()]] - code - gateway/tests/test_path_isolation.py
- [[.test_already_isolated_paths_not_rewritten()]] - code - gateway/tests/test_path_isolation.py
- [[.test_basic_result()]] - code - gateway/tests/test_path_isolation.py
- [[.test_block_base_directory_access()]] - code - gateway/tests/test_path_isolation.py
- [[.test_block_cross_user_access()]] - code - gateway/tests/test_path_isolation.py
- [[.test_blocked_result()]] - code - gateway/tests/test_path_isolation.py
- [[.test_cleanup_abandoned_directories()]] - code - gateway/tests/test_path_isolation.py
- [[.test_custom_config()_2]] - code - gateway/tests/test_path_isolation.py
- [[.test_default_config()_5]] - code - gateway/tests/test_path_isolation.py
- [[.test_dont_cleanup_active_user_directories()]] - code - gateway/tests/test_path_isolation.py
- [[.test_end_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[.test_get_active_users()]] - code - gateway/tests/test_path_isolation.py
- [[.test_get_user_temp_path()]] - code - gateway/tests/test_path_isolation.py
- [[.test_initialization()_2]] - code - gateway/tests/test_path_isolation.py
- [[.test_path_rewriting_nested_paths()]] - code - gateway/tests/test_path_isolation.py
- [[.test_path_rewriting_no_rewrite_needed()]] - code - gateway/tests/test_path_isolation.py
- [[.test_path_rewriting_temp_files()]] - code - gateway/tests/test_path_isolation.py
- [[.test_register_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[.test_user_id_sanitization()]] - code - gateway/tests/test_path_isolation.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace.          Re]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Create path isolation manager for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create temporary directory for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create test configuration._1]] - rationale - gateway/tests/test_path_isolation.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Ensure user's isolated directory exists.]] - rationale - gateway/security/path_isolation.py
- [[Get a path within the user's isolated temp directory.]] - rationale - gateway/security/path_isolation.py
- [[Get the isolated temp directory path for a user.]] - rationale - gateway/security/path_isolation.py
- [[PathRewriteResult]] - code - gateway/security/path_isolation.py
- [[Register a new user session and create their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Result of path rewriting operation.]] - rationale - gateway/security/path_isolation.py
- [[Rewrite a path to isolate it to the user's namespace.          Args]] - rationale - gateway/security/path_isolation.py
- [[Sanitize user ID to prevent path traversal attacks.]] - rationale - gateway/security/path_isolation.py
- [[Test PathRewriteResult dataclass.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test allowing access to own namespace.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test basic result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocked result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocking cross-user namespace access.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocking direct access to base agentshroud directory.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test cleanup of abandoned user directories.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test custom configuration values._1]] - rationale - gateway/tests/test_path_isolation.py
- [[Test default configuration values._4]] - rationale - gateway/tests/test_path_isolation.py
- [[Test ending user session.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test getting active users.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test getting user temp path.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test manager initialization.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path isolation configuration.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path isolation manager.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path rewriting for tmp files.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path rewriting for nested tmp paths.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test paths that don't need rewriting.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test that active user directories are not cleaned up.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test that already isolated paths are not double-rewritten.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test user ID sanitization.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test user session registration.]] - rationale - gateway/tests/test_path_isolation.py
- [[TestPathIsolationConfig]] - code - gateway/tests/test_path_isolation.py
- [[TestPathIsolationManager]] - code - gateway/tests/test_path_isolation.py
- [[TestPathRewriteResult]] - code - gateway/tests/test_path_isolation.py
- [[test_path_isolation.py]] - code - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_61
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Community 19]]

## Top bridge nodes
- [[TestPathIsolationManager]] - degree 24, connects to 2 communities
- [[PathRewriteResult]] - degree 9, connects to 1 community
- [[._get_user_temp_dir()]] - degree 8, connects to 1 community
- [[.rewrite_path()]] - degree 7, connects to 1 community
- [[TestPathIsolationConfig]] - degree 7, connects to 1 community