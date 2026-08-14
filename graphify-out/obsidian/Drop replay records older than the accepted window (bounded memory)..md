---
source_file: "gateway/security/mfa_guard.py"
type: "rationale"
community: "Enforce-Mode Auto-Revert"
location: "L296"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enforce-Mode_Auto-Revert
---

# Drop replay records older than the accepted window (bounded memory).

## Connections
- [[._prune_used()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enforce-Mode_Auto-Revert