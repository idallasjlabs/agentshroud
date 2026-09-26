---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "lifespan.py"
location: "L68"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/lifespanpy
---

# Same plaintext should produce different blobs (random salt/nonce).

## Connections
- [[.test_different_encryptions_differ()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/lifespanpy