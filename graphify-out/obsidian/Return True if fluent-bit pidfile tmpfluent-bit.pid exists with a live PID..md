---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "IEC 62443 Scorecard"
location: "L400"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/IEC_62443_Scorecard
---

# Return True if fluent-bit pidfile /tmp/fluent-bit.pid exists with a live PID.

## Connections
- [[_is_fluent_bit_running()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/IEC_62443_Scorecard