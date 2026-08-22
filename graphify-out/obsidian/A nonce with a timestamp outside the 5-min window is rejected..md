---
source_file: "gateway/tests/test_session_security.py"
type: "rationale"
community: "Session Security"
location: "L172"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Security
---

# A nonce with a timestamp outside the 5-min window is rejected.

## Connections
- [[.test_nonce_expired_rejected()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Security