---
source_file: "gateway/security/mfa_guard.py"
type: "rationale"
community: "Mfa Guard"
location: "L296"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Mfa_Guard
---

# Drop replay records older than the accepted window (bounded memory).

## Connections
- [[._prune_used()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Mfa_Guard