---
type: community
members: 72
---

# Community 477

**Members:** 72 nodes

## Members
- [[.__init__()_93]] - code - gateway/security/encrypted_store.py
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
- [[.store()_3]] - code - gateway/tests/test_security_audit.py
- [[.test_b64_roundtrip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_ciphertext_not_plaintext()]] - code - gateway/tests/test_security_audit.py
- [[.test_custom_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_encryptions_differ()]] - code - gateway/tests/test_security_hardening.py
- [[.test_different_plaintexts_different_ciphertexts()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypt_decrypt_bytes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_dict()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_roundtrip()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypt_decrypt_string()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_json()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_var_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_file_secret()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_blob_key_id()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_too_short()]] - code - gateway/tests/test_security_hardening.py
- [[.test_invalid_blob_version()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation()]] - code - gateway/tests/test_security_audit.py
- [[.test_key_rotation()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_auto_increment()]] - code - gateway/tests/test_security_hardening.py
- [[.test_large_data()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_secret_raises()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[.test_tampered_ciphertext_fails()]] - code - gateway/tests/test_security_audit.py
- [[.test_wrong_key_fails()]] - code - gateway/tests/test_security_audit.py
- [[.test_wrong_key_fails()_1]] - code - gateway/tests/test_security_hardening.py
- [[.to_dict()_6]] - code - gateway/security/canary.py
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - rationale - gateway/security/encrypted_store.py
- [[Any_43]] - code - gateway/security/canary.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[EncryptedStore]] - code - gateway/security/encrypted_store.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Initialize the encrypted store.          Args             master_secret The ma]] - rationale - gateway/security/encrypted_store.py
- [[Key rotation should re-encrypt all blobs.]] - rationale - gateway/tests/test_security_audit.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Resolve master secret from args, file, or environment.]] - rationale - gateway/security/encrypted_store.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Same plaintext encrypted twice should produce different ciphertext (random IV).]] - rationale - gateway/tests/test_security_audit.py
- [[Same plaintext should produce different blobs (random saltnonce).]] - rationale - gateway/tests/test_security_hardening.py
- [[Test encryption, key management, and secret handling.]] - rationale - gateway/tests/test_security_audit.py
- [[TestCryptography]] - code - gateway/tests/test_security_audit.py
- [[TestEncryptedStore]] - code - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[canary.py]] - code - gateway/security/canary.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_477
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 0]]
- 13 edges to [[_COMMUNITY_Community 7]]
- 12 edges to [[_COMMUNITY_Community 52]]
- 9 edges to [[_COMMUNITY_Community 162]]
- 8 edges to [[_COMMUNITY_Community 41]]
- 4 edges to [[_COMMUNITY_Community 365]]
- 4 edges to [[_COMMUNITY_Community 684]]
- 3 edges to [[_COMMUNITY_Community 72]]
- 3 edges to [[_COMMUNITY_Community 43]]
- 3 edges to [[_COMMUNITY_Community 93]]
- 3 edges to [[_COMMUNITY_Community 5]]
- 2 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Community 1119]]
- 2 edges to [[_COMMUNITY_Community 235]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 2 edges to [[_COMMUNITY_Community 904]]
- 1 edge to [[_COMMUNITY_Community 185]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 166]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 362]]
- 1 edge to [[_COMMUNITY_Community 148]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 128]]
- 1 edge to [[_COMMUNITY_Community 479]]
- 1 edge to [[_COMMUNITY_Community 888]]
- 1 edge to [[_COMMUNITY_Community 792]]
- 1 edge to [[_COMMUNITY_Community 947]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 11]]
- 1 edge to [[_COMMUNITY_Community 794]]
- 1 edge to [[_COMMUNITY_Community 393]]
- 1 edge to [[_COMMUNITY_Community 466]]

## Top bridge nodes
- [[TestCryptography]] - degree 44, connects to 18 communities
- [[EncryptedStore]] - degree 65, connects to 17 communities
- [[TestEncryptedStore]] - degree 35, connects to 9 communities
- [[FR4 Data Confidentiality]] - degree 8, connects to 5 communities
- [[canary.py]] - degree 5, connects to 2 communities