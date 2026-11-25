---
type: community
members: 56
---

# EncryptedStore

**Members:** 56 nodes

## Members
- [[dot-__init__()_12]] - code - gateway/security/encrypted_store.py
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
- [[dot-setup_method()_5]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wrong_key_fails()]] - code - gateway/tests/test_security_hardening.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Best-effort zeroing of key material using ctypes.memset. Works on bytearray and…]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob. Args blob The encrypted blob from…]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM. Args data String, bytes, or dict (JSON-…]] - rationale - gateway/security/encrypted_store.py
- [[Encrypted Memory Store — AES-256-GCM encryption for data at rest. Provides…]] - rationale - gateway/security/encrypted_store.py
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Initialize the encrypted store. Args master_secret The master secret string.…]] - rationale - gateway/security/encrypted_store.py
- [[Re-encrypt blobs with a new master secret. Args blobs List of encrypted blobs…]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EncryptedStore
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_KeyVault]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_TestHTTPSecurity]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EncryptedStore]] - degree 37, connects to 9 communities
- [[encrypted_store.py]] - degree 5, connects to 2 communities
- [[TestEncryptedStore]] - degree 19, connects to 1 community
- [[_secure_zero()]] - degree 9, connects to 1 community
- [[TestSecureZero]] - degree 7, connects to 1 community
