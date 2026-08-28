---
type: community
cohesion: 0.11
members: 21
---

# Community 429

**Cohesion:** 0.11 - loosely connected
**Members:** 21 nodes

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
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_429
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 3 edges to [[_COMMUNITY_Community 30]]
- 1 edge to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 137]]
- 1 edge to [[_COMMUNITY_Community 519]]
- 1 edge to [[_COMMUNITY_Community 18]]

## Top bridge nodes
- [[encrypted_store.py]] - degree 6, connects to 5 communities
- [[_secure_zero()]] - degree 9, connects to 1 community
- [[.decrypt()]] - degree 8, connects to 1 community
- [[.encrypt()]] - degree 6, connects to 1 community
- [[._derive_key()]] - degree 5, connects to 1 community