---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# .test_encrypted_store_error_no_key_leak()

## Connections
- [[Decryption errors shouldn't expose the encryption key.]] - `rationale_for` [EXTRACTED]
- [[EncryptedStore]] - `calls` [INFERRED]
- [[TestInfoLeakage]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard