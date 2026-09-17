---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Session Manager & PII/Context Guard"
location: "L45"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# Encryption/decryption time should not leak plaintext length.

## Connections
- [[dot-test_encrypted_store_constant_time()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard