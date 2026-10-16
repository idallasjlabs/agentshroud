---
type: community
cohesion: 0.03
members: 114
---

# MiddlewareManager

**Cohesion:** 0.03 - loosely connected
**Members:** 114 nodes

## Members
- [[dot-__init__()_166]] - code - gateway/security/path_isolation.py
- [[dot-_apply_path_rewriting()]] - code - gateway/security/path_isolation.py
- [[dot-_check_cross_user_access()]] - code - gateway/security/path_isolation.py
- [[dot-_cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_base_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_ensure_user_directory()]] - code - gateway/security/path_isolation.py
- [[dot-_get_user_temp_dir()]] - code - gateway/security/path_isolation.py
- [[dot-_is_base_directory_access()]] - code - gateway/security/path_isolation.py
- [[dot-_sanitize_user_id()]] - code - gateway/security/path_isolation.py
- [[dot-cleanup_abandoned_directories()]] - code - gateway/security/path_isolation.py
- [[dot-config()_4]] - code - gateway/tests/test_path_isolation.py
- [[dot-end_user_session()]] - code - gateway/security/path_isolation.py
- [[dot-get_active_users()]] - code - gateway/security/path_isolation.py
- [[dot-get_stats()_15]] - code - gateway/security/path_isolation.py
- [[dot-get_user_temp_path()]] - code - gateway/security/path_isolation.py
- [[dot-manager()_2]] - code - gateway/tests/test_path_isolation.py
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
- [[dot-test_context_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_custom_config()_3]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_default_config()_7]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_dns_filter_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_dont_cleanup_active_user_directories()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_egress_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_end_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_file_sandbox_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_get_active_users()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_get_user_temp_path()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_initialization()_4]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_multi_turn_tracker_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_output_canary_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_path_isolation_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_path_rewriting_nested_paths()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_path_rewriting_no_rewrite_needed()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_path_rewriting_temp_files()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_register_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_subagent_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_tool_chain_analyzer_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_user_id_sanitization()]] - code - gateway/tests/test_path_isolation.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace.          Re]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Configuration for path isolation system.]] - rationale - gateway/security/path_isolation.py
- [[Create base agentshroud temp directory if it doesn't exist.]] - rationale - gateway/security/path_isolation.py
- [[Create path isolation manager for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create temporary directory for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create test configuration._1]] - rationale - gateway/tests/test_path_isolation.py
- [[EgressFilterConfig_1]] - code - gateway/security/egress_filter.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Ensure user's isolated directory exists.]] - rationale - gateway/security/path_isolation.py
- [[Get a path within the user's isolated temp directory.]] - rationale - gateway/security/path_isolation.py
- [[Get set of currently active users.]] - rationale - gateway/security/path_isolation.py
- [[Get statistics about path isolation manager.]] - rationale - gateway/security/path_isolation.py
- [[Get the isolated temp directory path for a user.]] - rationale - gateway/security/path_isolation.py
- [[Manages per-user path isolation for temporary files and directories.]] - rationale - gateway/security/path_isolation.py
- [[Path Isolation Manager Tests]] - code - gateway/tests/test_path_isolation.py
- [[PathIsolationConfig]] - code - gateway/security/path_isolation.py
- [[PathIsolationManager]] - code - gateway/security/path_isolation.py
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
- [[Test default configuration values._5]] - rationale - gateway/tests/test_path_isolation.py
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
- [[TestGetModuleModeEnforceDefault]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestModuleConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestModuleInstantiationInEnforceMode]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestPathIsolationConfig]] - code - gateway/tests/test_path_isolation.py
- [[TestPathIsolationManager]] - code - gateway/tests/test_path_isolation.py
- [[TestPathRewriteResult]] - code - gateway/tests/test_path_isolation.py
- [[Verify get_module_mode returns enforce when no override is set.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Verify individual module configs default to enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Verify modules can instantiate and operate in enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[any_62]] - code - gateway/security/path_isolation.py
- [[enforcement-audit-script.py]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[fail()_2]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[ok()]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[path_isolation.py]] - code - gateway/security/path_isolation.py
- [[run()_4]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[test_all_modules_enforce.py]] - code - gateway/tests/test_all_modules_enforce.py
- [[test_path_isolation.py]] - code - gateway/tests/test_path_isolation.py
- [[warn()_4]] - code - docs/planning/reviews/enforcement-audit-script.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_MiddlewareManager]]
- 14 edges to [[_COMMUNITY_AlertDispatcher]]
- 14 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 10 edges to [[_COMMUNITY_EgressFilterConfig]]
- 9 edges to [[_COMMUNITY_MiddlewareManager_1]]
- 7 edges to [[_COMMUNITY_ResourceGuard_1]]
- 7 edges to [[_COMMUNITY_ContextSegment]]
- 7 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 6 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 5 edges to [[_COMMUNITY_TrustConfig_1]]
- 5 edges to [[_COMMUNITY_ConsentFramework_1]]
- 5 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 5 edges to [[_COMMUNITY_MultiTurnTracker_1]]
- 5 edges to [[_COMMUNITY_DNSFilterConfig]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 4 edges to [[_COMMUNITY_InjectionAction]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_1]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_2]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_ApprovalHardening_1]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 2 edges to [[_COMMUNITY_UserSessionManager_3]]
- 2 edges to [[_COMMUNITY_ApprovalHardening_2]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_4]]
- 1 edge to [[_COMMUNITY_UserSessionManager_4]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_9]]

## Top bridge nodes
- [[enforcement-audit-script.py]] - degree 34, connects to 20 communities
- [[run()_4]] - degree 29, connects to 19 communities
- [[TestModuleInstantiationInEnforceMode]] - degree 31, connects to 15 communities
- [[TestModuleConfigDefaults]] - degree 25, connects to 15 communities
- [[test_all_modules_enforce.py]] - degree 24, connects to 15 communities
