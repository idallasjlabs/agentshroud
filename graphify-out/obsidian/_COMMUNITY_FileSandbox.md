---
type: community
members: 102
---

# FileSandbox

**Members:** 102 nodes

## Members
- [[dot-__init__()_71]] - code - gateway/security/file_sandbox.py
- [[dot-_check()]] - code - gateway/security/file_sandbox.py
- [[dot-_detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[dot-_is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[dot-_match_pattern()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[dot-check_read()]] - code - gateway/security/file_sandbox.py
- [[dot-check_write()]] - code - gateway/security/file_sandbox.py
- [[dot-detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[dot-get_audit_log()_2]] - code - gateway/security/file_sandbox.py
- [[dot-get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[dot-get_temp_files()]] - code - gateway/security/file_sandbox.py
- [[dot-guard()_2]] - code - gateway/tests/test_security_audit.py
- [[dot-monitor_sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-record_network_activity()]] - code - gateway/security/file_sandbox.py
- [[dot-sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-sanitizer()_2]] - code - gateway/tests/test_security_audit.py
- [[dot-scan()]] - code - gateway/security/file_sandbox.py
- [[dot-store()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_3]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_file_sandbox_mcp_write()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_file_sandbox_staging_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_large_write_then_network_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_without_network_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_monitor_mode_allows_everything()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_project_files_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_small_writes_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_symlink_resolution()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_wildcard_pattern_matching()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_read_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-token_validator()]] - code - gateway/tests/test_security_audit.py
- [[Check if path is within any allowed pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if path matches any blocked pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if this is an immutable security file by name.]] - rationale - gateway/security/file_sandbox.py
- [[Detect data staging patterns (collect → compress → exfil).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect path traversal attempts in raw input before normalization.]] - rationale - gateway/security/file_sandbox.py
- [[Enhanced pattern matching for file paths.]] - rationale - gateway/security/file_sandbox.py
- [[Even blocked paths are allowed in monitor mode (just flagged).]] - rationale - gateway/tests/test_file_sandbox.py
- [[FileOperation]] - code - gateway/security/file_sandbox.py
- [[FileSandbox]] - code - gateway/security/file_sandbox.py
- [[FileSandbox in enforce mode with strict separation.]] - rationale - gateway/tests/test_privilege_separation.py
- [[FileSandboxConfig]] - code - gateway/security/file_sandbox.py
- [[FileVerdict]] - code - gateway/security/file_sandbox.py
- [[Get all flagged operations that indicate security violations.]] - rationale - gateway/security/file_sandbox.py
- [[MCP file writes should go through sandbox.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Middleware manager for request processing tests.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Monitor-mode sandbox for comparison testing.]] - rationale - gateway/tests/test_security_audit.py
- [[PIIFinding]] - code - gateway/security/file_sandbox.py
- [[PIIScanResult]] - code - gateway/security/file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[Sandbox with separation of privilege enforcement.]] - rationale - gateway/tests/test_privilege_separation.py
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[Symlinks should be resolved - symlink to blocked path must be caught.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test  wildcard patterns work correctly.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test file path pattern matching logic.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestPatternMatching]] - code - gateway/tests/test_privilege_separation.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[Tests for file IO sandboxing.]] - rationale - gateway/tests/test_file_sandbox.py
- [[default_config()_3]] - code - gateway/tests/test_file_sandbox.py
- [[enforce_config()]] - code - gateway/tests/test_privilege_separation.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py
- [[fixture_45]] - code
- [[fixture_46]] - code
- [[fixture_47]] - code
- [[middleware_manager()]] - code - gateway/tests/test_privilege_separation.py
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_config()_1]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_privilege_separation.py
- [[t_sandbox()]] - code - gateway/ingest_api/main.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py
- [[test_privilege_separation.py]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FileSandbox
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_lifespan.py]]
- 6 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_EnvironmentGuard]]
- 4 edges to [[_COMMUNITY_run]]
- 4 edges to [[_COMMUNITY_PathIsolationManager]]
- 4 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_TestFileSandbox]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_TestSecurityPolicyProtection]]
- 1 edge to [[_COMMUNITY_TestReadAccess]]
- 1 edge to [[_COMMUNITY_TestAgentShroudSourceCodeProtection]]
- 1 edge to [[_COMMUNITY_TestConfigurationProtection]]
- 1 edge to [[_COMMUNITY_TestSystemPathProtection]]
- 1 edge to [[_COMMUNITY_TestWorkspaceAccessPreserved]]
- 1 edge to [[_COMMUNITY_TestSecurityViolationLogging]]
- 1 edge to [[_COMMUNITY_TestEdgeCases]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_TestPromptGuard]]
- 1 edge to [[_COMMUNITY_LogSanitizer]]
- 1 edge to [[_COMMUNITY_TokenValidator]]
- 1 edge to [[_COMMUNITY_ContextGuard]]

## Top bridge nodes
- [[FileSandboxConfig]] - degree 31, connects to 11 communities
- [[FileSandbox]] - degree 41, connects to 10 communities
- [[test_privilege_separation.py]] - degree 17, connects to 10 communities
- [[file_sandbox.py]] - degree 12, connects to 2 communities
- [[fixture_47]] - degree 8, connects to 2 communities
