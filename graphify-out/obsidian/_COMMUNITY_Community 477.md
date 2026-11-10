---
type: community
members: 25
---

# Community 477

**Members:** 25 nodes

## Members
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_477
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 0]]
- 6 edges to [[_COMMUNITY_Community 52]]
- 3 edges to [[_COMMUNITY_Community 11]]
- 2 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[TestSecureZero]] - degree 23, connects to 6 communities
- [[_secure_zero()]] - degree 9, connects to 2 communities
- [[.decrypt()]] - degree 8, connects to 1 community
- [[.encrypt()]] - degree 6, connects to 1 community
- [[._derive_key()]] - degree 5, connects to 1 community