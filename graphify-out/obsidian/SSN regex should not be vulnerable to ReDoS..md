---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L299"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# SSN regex should not be vulnerable to ReDoS.

## Connections
- [[.test_regex_redos_ssn()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline