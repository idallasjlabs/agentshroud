---
type: community
members: 34
---

# PathIsolationManager

**Members:** 34 nodes

## Members
- [[dot-__init__()_100]] - code - gateway/security/path_isolation.py
- [[dot-_apply_path_rewriting()]] - code - gateway/security/path_isolation.py
- [[dot-_check_cross_user_access()]] - code - gateway/security/path_isolation.py
- [[dot-_cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_base_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_get_user_temp_dir()]] - code - gateway/security/path_isolation.py
- [[dot-_is_base_directory_access()]] - code - gateway/security/path_isolation.py
- [[dot-_sanitize_user_id()]] - code - gateway/security/path_isolation.py
- [[dot-cleanup_abandoned_directories()]] - code - gateway/security/path_isolation.py
- [[dot-end_user_session()]] - code - gateway/security/path_isolation.py
- [[dot-get_active_users()]] - code - gateway/security/path_isolation.py
- [[dot-get_stats()_5]] - code - gateway/security/path_isolation.py
- [[dot-get_user_temp_path()]] - code - gateway/security/path_isolation.py
- [[dot-register_user_session()]] - code - gateway/security/path_isolation.py
- [[dot-rewrite_path()]] - code - gateway/security/path_isolation.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace. Returns…]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Create base agentshroud temp directory if it doesn't exist.]] - rationale - gateway/security/path_isolation.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Ensure user's isolated directory exists.]] - rationale - gateway/security/path_isolation.py
- [[Get a path within the user's isolated temp directory.]] - rationale - gateway/security/path_isolation.py
- [[Get set of currently active users.]] - rationale - gateway/security/path_isolation.py
- [[Get statistics about path isolation manager.]] - rationale - gateway/security/path_isolation.py
- [[Get the isolated temp directory path for a user.]] - rationale - gateway/security/path_isolation.py
- [[Manages per-user path isolation for temporary files and directories.]] - rationale - gateway/security/path_isolation.py
- [[PathIsolationManager]] - code - gateway/security/path_isolation.py
- [[Register a new user session and create their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Rewrite a path to isolate it to the user's namespace. Args path Original file…]] - rationale - gateway/security/path_isolation.py
- [[Sanitize user ID to prevent path traversal attacks.]] - rationale - gateway/security/path_isolation.py
- [[any_36]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 4 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_PathRewriteResult]]
- 2 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[PathIsolationManager]] - degree 29, connects to 5 communities
- [[dot-rewrite_path()]] - degree 7, connects to 1 community
- [[dot-__init__()_100]] - degree 3, connects to 1 community
