---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "Security Hardening"
location: "L68"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Hardening
---

# Same plaintext should produce different blobs (random salt/nonce).

## Connections
- [[.test_different_encryptions_differ()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Hardening