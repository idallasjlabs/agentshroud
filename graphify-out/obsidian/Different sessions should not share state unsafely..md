---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Sanitizer & Resource Guard"
location: "L348"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# Different sessions should not share state unsafely.

## Connections
- [[.test_session_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard
