---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "test_mfa_guard.py"
location: "L655"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# Return True if a non-zombie falco process is running inside this container.

## Connections
- [[_is_falco_running()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_mfa_guardpy
