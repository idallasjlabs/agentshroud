---
type: community
cohesion: 0.12
members: 20
---

# Encrypted Store (security)

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
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
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Encrypted_Store_security
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[_secure_zero()]] - degree 9, connects to 2 communities
- [[.decrypt()]] - degree 8, connects to 1 community
- [[.encrypt()]] - degree 6, connects to 1 community
- [[._derive_key()]] - degree 5, connects to 1 community
- [[.rotate()]] - degree 5, connects to 1 community