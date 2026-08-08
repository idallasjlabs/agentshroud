---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L310"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Email regex should not be vulnerable to ReDoS.

## Connections
- [[.test_regex_redos_email()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline