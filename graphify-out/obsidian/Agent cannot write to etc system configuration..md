---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Security Audit & Drift Detection"
location: "L164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Drift_Detection
---

# Agent cannot write to /etc/ system configuration.

## Connections
- [[.test_etc_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Drift_Detection