---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Sanitizer & Resource Guard"
location: "L714"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# Same plaintext encrypted twice should produce different ciphertext (random IV).

## Connections
- [[.test_different_plaintexts_different_ciphertexts()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard
