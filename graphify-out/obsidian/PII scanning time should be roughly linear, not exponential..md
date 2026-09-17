---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Session Manager & PII/Context Guard"
location: "L81"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# PII scanning time should be roughly linear, not exponential.

## Connections
- [[dot-test_pii_scan_time_independent_of_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard