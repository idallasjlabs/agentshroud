---
type: community
cohesion: 0.05
members: 58
---

# Module Group 66

**Cohesion:** 0.05 - loosely connected
**Members:** 58 nodes

## Members
- [[.__init__()_62]] - code - gateway/security/encrypted_store.py
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[._resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
- [[.setup_method()_23]] - code - gateway/tests/test_security_hardening.py
- [[.test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_hmac_comparison_for_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[.test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[.test_pii_scan_time_independent_of_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_prompt_guard_no_early_exit_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[.test_token_validation_rejects_fast()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Invalid tokens should be rejected quickly (no expensive operations).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[PII scanning time should be roughly linear, not exponential.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard should scan full input, not short-circuit on first match.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Test for timing side-channels in security-critical comparisons.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[TestTimingAttacks]] - code - gateway/tests/test_security_audit_advanced.py
- [[Verify hmac.compare_digest is available for constant-time comparison.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_66
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Module Group 79]]
- 14 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 9 edges to [[_COMMUNITY_Alert Dispatcher]]
- 8 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 4 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 4 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 4 edges to [[_COMMUNITY_Module Group 110]]
- 4 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 3 edges to [[_COMMUNITY_Module Group 189]]
- 3 edges to [[_COMMUNITY_Module Group 88]]
- 3 edges to [[_COMMUNITY_Subagent Monitor]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 216]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Module Group 102]]
- 1 edge to [[_COMMUNITY_DNS Filter & Tunneling Detection]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 71]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Module Group 137]]
- 1 edge to [[_COMMUNITY_Module Group 323]]
- 1 edge to [[_COMMUNITY_Module Group 285]]
- 1 edge to [[_COMMUNITY_Module Group 80]]

## Top bridge nodes
- [[EncryptedStore]] - degree 65, connects to 16 communities
- [[TestTimingAttacks]] - degree 30, connects to 13 communities
- [[TestEncryptedStore]] - degree 35, connects to 9 communities
- [[.decrypt()]] - degree 9, connects to 1 community
- [[_secure_zero()]] - degree 9, connects to 1 community