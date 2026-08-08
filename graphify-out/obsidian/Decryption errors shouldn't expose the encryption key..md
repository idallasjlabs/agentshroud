---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L387"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Decryption errors shouldn't expose the encryption key.

## Connections
- [[.test_encrypted_store_error_no_key_leak()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures