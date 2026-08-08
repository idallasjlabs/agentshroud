---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Unicode tricks shouldn't bypass PII detection.

## Connections
- [[.test_unicode_normalization_bypass()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline