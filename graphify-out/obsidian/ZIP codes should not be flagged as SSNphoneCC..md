---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Sanitizer & Resource Guard"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# ZIP codes should not be flagged as SSN/phone/CC.

## Connections
- [[.test_no_false_positive_on_zip()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard
