---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "test_mfa_guard.py"
location: "L400"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# Return True if fluent-bit pidfile /tmp/fluent-bit.pid exists with a live PID.

## Connections
- [[_is_fluent_bit_running()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_mfa_guardpy
