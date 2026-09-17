---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "test_security_audit.py"
location: "L56"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# SSN without dashes: 123456789 — Presidio+spaCy only (regex needs dashes).

## Connections
- [[.test_ssn_no_dashes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy