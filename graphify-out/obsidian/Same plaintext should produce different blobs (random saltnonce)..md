---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "TestEncryptedStore"
location: "L68"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestEncryptedStore
---

# Same plaintext should produce different blobs (random salt/nonce).

## Connections
- [[dot-test_different_encryptions_differ()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestEncryptedStore
