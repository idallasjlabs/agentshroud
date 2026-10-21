---
type: community
members: 73
---

# PortManager

**Members:** 73 nodes

## Members
- [[dot-__init__()_178]] - code - gateway/security/encrypted_store.py
- [[dot-_derive_key()]] - code - gateway/security/encrypted_store.py
- [[dot-_resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[dot-decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt()]] - code - gateway/security/encrypted_store.py
- [[dot-encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[dot-get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[dot-rotate()]] - code - gateway/security/encrypted_store.py
- [[dot-setup_method()_33]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_hmac_comparison_for_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_log_sanitizer_covers_stack_traces()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_pii_scan_time_independent_of_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_prompt_guard_no_early_exit_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_token_error_no_secret_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_token_validation_rejects_fast()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_wrong_key_fails()]] - code - gateway/tests/test_security_hardening.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Invalid tokens should be rejected quickly (no expensive operations).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[PII scanning time should be roughly linear, not exponential.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard should scan full input, not short-circuit on first match.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Stack traces containing secrets should be sanitized.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test for timing side-channels in security-critical comparisons.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test that errors don't leak sensitive information.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[TestInfoLeakage]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestTimingAttacks]] - code - gateway/tests/test_security_audit_advanced.py
- [[Token validation errors shouldn't expose signing keys.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Verify hmac.compare_digest is available for constant-time comparison.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PortManager
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 14 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 13 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_test_playback_state.c]]
- 6 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 5 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 3 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 3 edges to [[_COMMUNITY__wrap_response() (4)]]
- 3 edges to [[_COMMUNITY_SessionManager]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_SecureBrowser (3)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy()]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_socrouter.py (2)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)_1]]

## Top bridge nodes
- [[EncryptedStore]] - degree 63, connects to 16 communities
- [[TestInfoLeakage]] - degree 30, connects to 16 communities
- [[TestTimingAttacks]] - degree 29, connects to 16 communities
- [[TestEncryptedStore]] - degree 35, connects to 7 communities
- [[_secure_zero()]] - degree 9, connects to 2 communities
