---
type: community
members: 14
---

# TestInfoLeakage

**Members:** 14 nodes

## Members
- [[dot-test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_log_sanitizer_covers_stack_traces()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_token_error_no_secret_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Stack traces containing secrets should be sanitized.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test that errors don't leak sensitive information.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestInfoLeakage]] - code - gateway/tests/test_security_audit_advanced.py
- [[Token validation errors shouldn't expose signing keys.]] - rationale - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInfoLeakage
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 1 edge to [[_COMMUNITY_PIIConfig]]

## Top bridge nodes
- [[TestInfoLeakage]] - degree 14, connects to 7 communities
- [[dot-test_encrypted_store_error_no_key_leak()]] - degree 3, connects to 1 community
- [[dot-test_env_guard_scrubs_output()]] - degree 3, connects to 1 community
- [[dot-test_git_guard_no_path_leak()]] - degree 3, connects to 1 community
- [[dot-test_log_sanitizer_covers_stack_traces()]] - degree 3, connects to 1 community
