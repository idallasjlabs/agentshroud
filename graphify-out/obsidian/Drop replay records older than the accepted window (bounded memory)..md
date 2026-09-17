---
source_file: "gateway/security/mfa_guard.py"
type: "rationale"
community: "test_mfa_guard.py"
location: "L296"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# Drop replay records older than the accepted window (bounded memory).

## Connections
- [[._prune_used()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_mfa_guardpy