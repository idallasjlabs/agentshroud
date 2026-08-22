---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "Security Hardening"
location: "L710"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Hardening
---

# Same plaintext encrypted twice should produce different ciphertext (random IV).

## Connections
- [[.test_different_plaintexts_different_ciphertexts()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Hardening