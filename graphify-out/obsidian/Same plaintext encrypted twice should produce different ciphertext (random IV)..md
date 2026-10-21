---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "_wrap_response()"
location: "L710"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Same plaintext encrypted twice should produce different ciphertext (random IV).

## Connections
- [[dot-test_different_plaintexts_different_ciphertexts()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
