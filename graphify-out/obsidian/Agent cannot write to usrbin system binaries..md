---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Security Audit & Drift Detection"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Drift_Detection
---

# Agent cannot write to /usr/bin/ system binaries.

## Connections
- [[.test_usr_bin_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Drift_Detection