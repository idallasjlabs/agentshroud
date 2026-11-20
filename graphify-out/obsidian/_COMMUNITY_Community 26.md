---
type: community
members: 120
---

# Community 26

**Members:** 120 nodes

## Members
- [[.__init__()_119]] - code - gateway/security/path_isolation.py
- [[._apply_path_rewriting()]] - code - gateway/security/path_isolation.py
- [[._check_cross_user_access()]] - code - gateway/security/path_isolation.py
- [[._cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[._ensure_base_directory()]] - code - gateway/security/path_isolation.py
- [[._ensure_user_directory()]] - code - gateway/security/path_isolation.py
- [[._get_user_temp_dir()]] - code - gateway/security/path_isolation.py
- [[._is_base_directory_access()]] - code - gateway/security/path_isolation.py
- [[._sanitize_user_id()]] - code - gateway/security/path_isolation.py
- [[.cleanup_abandoned_directories()]] - code - gateway/security/path_isolation.py
- [[.config()_4]] - code - gateway/tests/test_path_isolation.py
- [[.end_user_session()]] - code - gateway/security/path_isolation.py
- [[.get_active_users()]] - code - gateway/security/path_isolation.py
- [[.get_stats()_18]] - code - gateway/security/path_isolation.py
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
- [[.test_context_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_custom_config()_2]] - code - gateway/tests/test_path_isolation.py
- [[.test_default_config()_5]] - code - gateway/tests/test_path_isolation.py
- [[.test_dns_filter_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_dont_cleanup_active_user_directories()]] - code - gateway/tests/test_path_isolation.py
- [[.test_egress_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_end_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[.test_file_sandbox_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_get_active_users()]] - code - gateway/tests/test_path_isolation.py
- [[.test_get_user_temp_path()]] - code - gateway/tests/test_path_isolation.py
- [[.test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_initialization()_2]] - code - gateway/tests/test_path_isolation.py
- [[.test_multi_turn_tracker_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_output_canary_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_path_isolation_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_path_rewriting_nested_paths()]] - code - gateway/tests/test_path_isolation.py
- [[.test_path_rewriting_no_rewrite_needed()]] - code - gateway/tests/test_path_isolation.py
- [[.test_path_rewriting_temp_files()]] - code - gateway/tests/test_path_isolation.py
- [[.test_register_user_session()]] - code - gateway/tests/test_path_isolation.py
- [[.test_security_config_dns_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_killswitch_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_mcp_proxy_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_pii_sanitizer_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_prompt_guard_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_subagent_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_subagent_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_tool_chain_analyzer_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_user_id_sanitization()]] - code - gateway/tests/test_path_isolation.py
- [[Apply path rewriting rules to isolate paths per user.]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access another user's isolated namespace.          Re]] - rationale - gateway/security/path_isolation.py
- [[Check if path is trying to access the base AgentShroud directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[Clean up abandoned user directories based on max age.]] - rationale - gateway/security/path_isolation.py
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[Configuration for path isolation system.]] - rationale - gateway/security/path_isolation.py
- [[Create base agentshroud temp directory if it doesn't exist.]] - rationale - gateway/security/path_isolation.py
- [[Create path isolation manager for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create temporary directory for testing.]] - rationale - gateway/tests/test_path_isolation.py
- [[Create test configuration._1]] - rationale - gateway/tests/test_path_isolation.py
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
- [[SecurityConfig_3]] - code - gateway/ingest_api/config.py
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
- [[TestGetModuleModeEnforceDefault]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestModuleConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestModuleInstantiationInEnforceMode]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestPathIsolationConfig]] - code - gateway/tests/test_path_isolation.py
- [[TestPathIsolationManager]] - code - gateway/tests/test_path_isolation.py
- [[TestPathRewriteResult]] - code - gateway/tests/test_path_isolation.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Verify get_module_mode returns enforce when no override is set.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Verify individual module configs default to enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Verify modules can instantiate and operate in enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[any]] - code - gateway/security/path_isolation.py
- [[path_isolation.py]] - code - gateway/security/path_isolation.py
- [[test_all_modules_enforce.py]] - code - gateway/tests/test_all_modules_enforce.py
- [[test_path_isolation.py]] - code - gateway/tests/test_path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_26
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_Community 0]]
- 21 edges to [[_COMMUNITY_Community 151]]
- 8 edges to [[_COMMUNITY_Community 31]]
- 7 edges to [[_COMMUNITY_Community 7]]
- 7 edges to [[_COMMUNITY_Community 1281]]
- 6 edges to [[_COMMUNITY_Community 1]]
- 6 edges to [[_COMMUNITY_Community 196]]
- 6 edges to [[_COMMUNITY_Community 72]]
- 6 edges to [[_COMMUNITY_Community 17]]
- 6 edges to [[_COMMUNITY_Community 140]]
- 6 edges to [[_COMMUNITY_Community 9]]
- 6 edges to [[_COMMUNITY_Community 233]]
- 6 edges to [[_COMMUNITY_Community 84]]
- 6 edges to [[_COMMUNITY_Community 146]]
- 6 edges to [[_COMMUNITY_Community 8]]
- 4 edges to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 890]]
- 1 edge to [[_COMMUNITY_Community 181]]
- 1 edge to [[_COMMUNITY_Community 431]]

## Top bridge nodes
- [[TestModuleInstantiationInEnforceMode]] - degree 31, connects to 14 communities
- [[TestSecurityConfigDefaults]] - degree 30, connects to 14 communities
- [[TestModuleConfigDefaults]] - degree 25, connects to 14 communities
- [[test_all_modules_enforce.py]] - degree 24, connects to 14 communities
- [[TestGetModuleModeEnforceDefault]] - degree 23, connects to 14 communities