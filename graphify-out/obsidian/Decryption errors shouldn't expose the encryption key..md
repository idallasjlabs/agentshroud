---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Session Manager & PII/Context Guard"
location: "L387"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# Decryption errors shouldn't expose the encryption key.

## Connections
- [[dot-test_encrypted_store_error_no_key_leak()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard