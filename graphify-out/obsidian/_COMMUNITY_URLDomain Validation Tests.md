---
type: community
members: 45
---

# URL/Domain Validation Tests

**Members:** 45 nodes

## Members
- [[._check()]] - code - gateway/security/file_sandbox.py
- [[._detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[._is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[._match_pattern()]] - code - gateway/security/file_sandbox.py
- [[._matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[._matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[.check_read()]] - code - gateway/security/file_sandbox.py
- [[.check_write()]] - code - gateway/security/file_sandbox.py
- [[.detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[.get_audit_log()_3]] - code - gateway/security/file_sandbox.py
- [[.get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[.scan()_3]] - code - gateway/security/file_sandbox.py
- [[.test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_credit_card_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[.test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
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
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/URL/Domain_Validation_Tests
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 1 edge to [[_COMMUNITY_gatewayruntime]]
- 1 edge to [[_COMMUNITY_SOC RBAC & Auth]]

## Top bridge nodes
- [[PIIScanner]] - degree 16, connects to 2 communities
- [[file_sandbox.py]] - degree 9, connects to 2 communities
- [[TestSensitivePathBlocking]] - degree 11, connects to 1 community
- [[TestPIIScanning]] - degree 10, connects to 1 community
- [[._check()]] - degree 9, connects to 1 community