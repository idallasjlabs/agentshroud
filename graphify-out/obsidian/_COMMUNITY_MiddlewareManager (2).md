---
type: community
members: 43
---

# MiddlewareManager (2)

**Members:** 43 nodes

## Members
- [[dot-__init__()_72]] - code - gateway/security/file_sandbox.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
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
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[Even blocked paths are allowed in monitor mode (just flagged).]] - rationale - gateway/tests/test_file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[default_config()_2]] - code - gateway/tests/test_file_sandbox.py
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_config()_1]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_2
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AlertDispatcher]]
- 11 edges to [[_COMMUNITY_AlertDispatcher (2) (2)]]

## Top bridge nodes
- [[test_file_sandbox.py]] - degree 13, connects to 2 communities
- [[TestSensitivePathBlocking]] - degree 11, connects to 2 communities
- [[TestNormalFileOperations]] - degree 10, connects to 2 communities
- [[TestPIIScanning]] - degree 10, connects to 2 communities
- [[TestFileAudit]] - degree 8, connects to 2 communities
