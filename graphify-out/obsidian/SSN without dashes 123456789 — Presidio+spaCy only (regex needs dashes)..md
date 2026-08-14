---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "Auth & Exception Types"
location: "L56"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Auth__Exception_Types
---

# SSN without dashes: 123456789 — Presidio+spaCy only (regex needs dashes).

## Connections
- [[.test_ssn_no_dashes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Auth__Exception_Types