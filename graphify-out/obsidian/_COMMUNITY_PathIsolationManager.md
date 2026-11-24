---
type: community
members: 62
---

# PathIsolationManager

**Members:** 62 nodes

## Members
- [[dot-__init__()_103]] - code - gateway/security/path_isolation.py
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
- [[dot-test_basic_result()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_blocked_result()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_context_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_custom_config()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_default_config()_1]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_file_sandbox_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_multi_turn_tracker_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_path_isolation_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_tool_chain_analyzer_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace. Returns…]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Configuration for path isolation system.]] - rationale - gateway/security/path_isolation.py
- [[Create base agentshroud temp directory if it doesn't exist.]] - rationale - gateway/security/path_isolation.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Ensure user's isolated directory exists.]] - rationale - gateway/security/path_isolation.py
- [[Get a path within the user's isolated temp directory.]] - rationale - gateway/security/path_isolation.py
- [[Get set of currently active users.]] - rationale - gateway/security/path_isolation.py
- [[Get statistics about path isolation manager.]] - rationale - gateway/security/path_isolation.py
- [[Get the isolated temp directory path for a user.]] - rationale - gateway/security/path_isolation.py
- [[Manages per-user path isolation for temporary files and directories.]] - rationale - gateway/security/path_isolation.py
- [[PathIsolationConfig]] - code - gateway/security/path_isolation.py
- [[PathIsolationManager]] - code - gateway/security/path_isolation.py
- [[PathRewriteResult]] - code - gateway/security/path_isolation.py
- [[Register a new user session and create their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Result of path rewriting operation.]] - rationale - gateway/security/path_isolation.py
- [[Rewrite a path to isolate it to the user's namespace. Args path Original file…]] - rationale - gateway/security/path_isolation.py
- [[Sanitize user ID to prevent path traversal attacks.]] - rationale - gateway/security/path_isolation.py
- [[Test PathRewriteResult dataclass.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test basic result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test blocked result creation.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test custom configuration values.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test default configuration values.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test path isolation configuration.]] - rationale - gateway/tests/test_path_isolation.py
- [[TestModuleInstantiationInEnforceMode]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestPathIsolationConfig]] - code - gateway/tests/test_path_isolation.py
- [[TestPathRewriteResult]] - code - gateway/tests/test_path_isolation.py
- [[Verify modules can instantiate and operate in enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[any_36]] - code
- [[path_isolation.py]] - code - gateway/security/path_isolation.py
- [[test_path_isolation.py]] - code - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 4 edges to [[_COMMUNITY_run]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_BrowserSecurityGuard]]
- 2 edges to [[_COMMUNITY_OutputCanary]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_MultiTurnTracker]]
- 2 edges to [[_COMMUNITY_ToolChainAnalyzer]]

## Top bridge nodes
- [[TestModuleInstantiationInEnforceMode]] - degree 24, connects to 9 communities
- [[PathIsolationManager]] - degree 29, connects to 5 communities
- [[PathIsolationConfig]] - degree 17, connects to 5 communities
- [[path_isolation.py]] - degree 6, connects to 2 communities
- [[test_path_isolation.py]] - degree 7, connects to 1 community
