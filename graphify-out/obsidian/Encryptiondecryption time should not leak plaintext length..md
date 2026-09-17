---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "EncryptedStore"
location: "L45"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EncryptedStore
---

# Encryption/decryption time should not leak plaintext length.

## Connections
- [[.test_encrypted_store_constant_time()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EncryptedStore