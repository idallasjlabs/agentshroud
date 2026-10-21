---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "_wrap_response()"
location: "L56"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# SSN without dashes: 123456789 — Presidio+spaCy only (regex needs dashes).

## Connections
- [[dot-test_ssn_no_dashes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
