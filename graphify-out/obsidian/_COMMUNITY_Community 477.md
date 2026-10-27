---
type: community
members: 51
---

# Community 477

**Members:** 51 nodes

## Members
- [[.__init__()_78]] - code - gateway/security/encrypted_store.py
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[._resolve_secret()]] - code - gateway/security/encrypted_store.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
- [[.setup_method()_26]] - code - gateway/tests/test_security_hardening.py
- [[.test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[.test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
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
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_477
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_Community 0]]
- 16 edges to [[_COMMUNITY_Community 52]]
- 3 edges to [[_COMMUNITY_Community 11]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 2 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Community 93]]
- 2 edges to [[_COMMUNITY_Community 420]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 509]]
- 1 edge to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 1119]]
- 1 edge to [[_COMMUNITY_Community 888]]
- 1 edge to [[_COMMUNITY_Community 792]]
- 1 edge to [[_COMMUNITY_Community 947]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 22]]

## Top bridge nodes
- [[EncryptedStore]] - degree 65, connects to 15 communities
- [[TestEncryptedStore]] - degree 35, connects to 9 communities
- [[_secure_zero()]] - degree 9, connects to 2 communities
- [[.test_encrypted_store_constant_time()]] - degree 3, connects to 1 community
- [[.test_encrypted_store_error_no_key_leak()]] - degree 3, connects to 1 community