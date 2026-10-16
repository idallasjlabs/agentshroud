---
type: community
cohesion: 0.04
members: 65
---

# MiddlewareManager

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[dot-_check()]] - code - gateway/security/file_sandbox.py
- [[dot-_detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[dot-_is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[dot-_match_pattern()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[dot-check_read()]] - code - gateway/security/file_sandbox.py
- [[dot-check_write()]] - code - gateway/security/file_sandbox.py
- [[dot-detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[dot-get_audit_log()_7]] - code - gateway/security/file_sandbox.py
- [[dot-get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[dot-scan()_3]] - code - gateway/security/file_sandbox.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_7]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_then_network_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_without_network_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_project_files_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_small_writes_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_read_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[Check if path is within any allowed pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if path matches any blocked pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if this is an immutable security file by name.]] - rationale - gateway/security/file_sandbox.py
- [[Detect path traversal attempts in raw input before normalization.]] - rationale - gateway/security/file_sandbox.py
- [[Enhanced pattern matching for file paths.]] - rationale - gateway/security/file_sandbox.py
- [[FileOperation]] - code - gateway/security/file_sandbox.py
- [[FileVerdict]] - code - gateway/security/file_sandbox.py
- [[Get all flagged operations that indicate security violations.]] - rationale - gateway/security/file_sandbox.py
- [[PIIFinding]] - code - gateway/security/file_sandbox.py
- [[PIIScanResult]] - code - gateway/security/file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[Rule agentshroud-path-traversal-open]] - concept - .semgrep.yml
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[default_config()_4]] - code - gateway/tests/test_file_sandbox.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_config()_3]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_file_sandbox.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[file_sandbox.py]] - degree 11, connects to 2 communities
- [[Rule agentshroud-path-traversal-open]] - degree 3, connects to 2 communities
- [[PIIScanner]] - degree 15, connects to 1 community
- [[test_file_sandbox.py]] - degree 13, connects to 1 community
- [[TestSensitivePathBlocking]] - degree 11, connects to 1 community
