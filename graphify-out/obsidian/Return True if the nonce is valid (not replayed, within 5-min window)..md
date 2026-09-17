---
source_file: "gateway/security/session_security.py"
type: "rationale"
community: "SessionManager"
location: "L148"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SessionManager
---

# Return True if the nonce is valid (not replayed, within 5-min window).

## Connections
- [[.validate_nonce()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SessionManager