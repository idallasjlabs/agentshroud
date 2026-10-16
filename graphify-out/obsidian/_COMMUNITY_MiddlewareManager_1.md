---
type: community
cohesion: 0.02
members: 157
---

# MiddlewareManager

**Cohesion:** 0.02 - loosely connected
**Members:** 157 nodes

## Members
- [[dot-__init__()_60]] - code - gateway/security/file_sandbox.py
- [[dot-_check()]] - code - gateway/security/file_sandbox.py
- [[dot-_detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[dot-_is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[dot-_match_pattern()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[dot-check_read()]] - code - gateway/security/file_sandbox.py
- [[dot-check_write()]] - code - gateway/security/file_sandbox.py
- [[dot-detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[dot-get_audit_log()_5]] - code - gateway/security/file_sandbox.py
- [[dot-get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[dot-get_temp_files()]] - code - gateway/security/file_sandbox.py
- [[dot-record_network_activity()]] - code - gateway/security/file_sandbox.py
- [[dot-scan()_1]] - code - gateway/security/file_sandbox.py
- [[dot-test_any_python_file_in_gateway_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_case_sensitivity()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_config_yaml_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_3]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_docker_compose_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_dockerfile_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_config_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_source_read_flagged()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_large_write_then_network_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_without_network_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_modules_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_monitor_mode_allows_everything()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_multiple_violations_tracked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_normal_operations_not_violations()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_path_traversal_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_project_files_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_relative_path_resolution()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_security_module_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_sensitive_config_read_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_small_writes_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_soul_md_in_workspace_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_symlink_resolution()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_info_read_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_prompt_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_usr_bin_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_var_log_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_violation_recorded_in_audit()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_wildcard_pattern_matching()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_read_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_subdirectory_write_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[Agent can read basic system info.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can read its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can still write to its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to tmp for temporary files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to its own workspace directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to subdirectories in workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud configuration files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud's own source code.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Docker Compose configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Dockerfile.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md even in workspace path.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify gateway configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify security policies and behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system paths.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system prompt files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot read sensitive configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to etc system configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to usrbin system binaries.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to varlog system logs.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway Python source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway config directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security framework files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security module source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Any .py file in gateway directory should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Case variations should not bypass protection.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Check if path is within any allowed pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if path matches any blocked pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if this is an immutable security file by name.]] - rationale - gateway/security/file_sandbox.py
- [[Detect path traversal attempts in raw input before normalization.]] - rationale - gateway/security/file_sandbox.py
- [[Enhanced pattern matching for file paths.]] - rationale - gateway/security/file_sandbox.py
- [[Even blocked paths are allowed in monitor mode (just flagged).]] - rationale - gateway/tests/test_file_sandbox.py
- [[FileOperation]] - code - gateway/security/file_sandbox.py
- [[FileSandbox]] - code - gateway/security/file_sandbox.py
- [[FileSandbox in enforce mode with strict separation.]] - rationale - gateway/tests/test_privilege_separation.py
- [[FileVerdict]] - code - gateway/security/file_sandbox.py
- [[Get all flagged operations that indicate security violations.]] - rationale - gateway/security/file_sandbox.py
- [[Large-write-then-network-activity stagingexfiltration pattern detection]] - concept - gateway/tests/test_file_sandbox.py
- [[Middleware manager for request processing tests.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Multiple violations should all be tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Normal workspace operations should not be flagged as violations.]] - rationale - gateway/tests/test_privilege_separation.py
- [[PIIFinding]] - code - gateway/security/file_sandbox.py
- [[PIIScanResult]] - code - gateway/security/file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[Path traversal attempts should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Privilege Separation File Sandbox Tests]] - code - gateway/tests/test_privilege_separation.py
- [[Reading gateway source should be flaggedblocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Relative paths should be resolved properly.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Round 2 Security Hardening Tests]] - code - gateway/tests/test_round2_hardening.py
- [[Rule agentshroud-path-traversal-open]] - concept - .semgrep.yml
- [[Sandbox with separation of privilege enforcement.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Security violations should be recorded in audit log.]] - rationale - gateway/tests/test_privilege_separation.py
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[Symlinks should be resolved - symlink to blocked path must be caught.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test  wildcard patterns work correctly.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test edge cases and potential bypass attempts.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test file path pattern matching logic.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test read access controls.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test that security violations are properly logged and tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestAgentShroudSourceCodeProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestConfigurationProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestEdgeCases]] - code - gateway/tests/test_privilege_separation.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestPatternMatching]] - code - gateway/tests/test_privilege_separation.py
- [[TestReadAccess]] - code - gateway/tests/test_privilege_separation.py
- [[TestSecurityPolicyProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestSecurityViolationLogging]] - code - gateway/tests/test_privilege_separation.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[TestSystemPathProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestWorkspaceAccessPreserved]] - code - gateway/tests/test_privilege_separation.py
- [[default_config()_1]] - code - gateway/tests/test_file_sandbox.py
- [[enforce_config()]] - code - gateway/tests/test_privilege_separation.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py
- [[middleware_manager()]] - code - gateway/tests/test_privilege_separation.py
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_config()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_privilege_separation.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py
- [[test_privilege_separation.py]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_AlertDispatcher]]
- 21 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig_6]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_2]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[FileSandbox]] - degree 85, connects to 8 communities
- [[test_privilege_separation.py]] - degree 15, connects to 2 communities
- [[file_sandbox.py]] - degree 11, connects to 2 communities
- [[TestAgentShroudSourceCodeProtection]] - degree 9, connects to 2 communities
- [[TestReadAccess]] - degree 9, connects to 2 communities
