---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Sanitizer & Resource Guard"
location: "L60"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# SSN without dashes: 123456789 — Presidio+spaCy only (regex needs dashes).

## Connections
- [[.test_ssn_no_dashes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard
