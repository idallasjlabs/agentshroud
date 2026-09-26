---
source_file: "gateway/security/mfa_guard.py"
type: "rationale"
community: "TestAuth"
location: "L296"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestAuth
---

# Drop replay records older than the accepted window (bounded memory).

## Connections
- [[._prune_used()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestAuth