---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Auth & Exception Types"
location: "L387"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Auth__Exception_Types
---

# Decryption errors shouldn't expose the encryption key.

## Connections
- [[.test_encrypted_store_error_no_key_leak()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Auth__Exception_Types