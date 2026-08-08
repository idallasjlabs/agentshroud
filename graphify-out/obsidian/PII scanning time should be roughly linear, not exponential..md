---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L81"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# PII scanning time should be roughly linear, not exponential.

## Connections
- [[.test_pii_scan_time_independent_of_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline