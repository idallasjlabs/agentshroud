---
type: community
members: 57
---

# Community 96

**Members:** 57 nodes

## Members
- [[.__init__()_91]] - code - gateway/security/encrypted_store.py
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
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
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
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_96
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Community 0]]
- 14 edges to [[_COMMUNITY_Community 22]]
- 4 edges to [[_COMMUNITY_Community 151]]
- 4 edges to [[_COMMUNITY_Community 52]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 3 edges to [[_COMMUNITY_Community 24]]
- 3 edges to [[_COMMUNITY_Community 11]]
- 2 edges to [[_COMMUNITY_Community 684]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 21]]
- 1 edge to [[_COMMUNITY_Community 45]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 941]]
- 1 edge to [[_COMMUNITY_Community 577]]
- 1 edge to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 1105]]
- 1 edge to [[_COMMUNITY_Community 84]]
- 1 edge to [[_COMMUNITY_Community 626]]
- 1 edge to [[_COMMUNITY_Community 393]]
- 1 edge to [[_COMMUNITY_Community 466]]

## Top bridge nodes
- [[EncryptedStore]] - degree 65, connects to 10 communities
- [[TestEncryptedStore]] - degree 35, connects to 7 communities
- [[outbound_filter.py]] - degree 8, connects to 6 communities
- [[FR4 Data Confidentiality]] - degree 8, connects to 5 communities
- [[encrypted_store.py]] - degree 6, connects to 2 communities