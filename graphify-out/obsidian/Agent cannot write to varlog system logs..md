---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Security Audit & Drift Detection"
location: "L178"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Drift_Detection
---

# Agent cannot write to /var/log/ system logs.

## Connections
- [[.test_var_log_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Drift_Detection