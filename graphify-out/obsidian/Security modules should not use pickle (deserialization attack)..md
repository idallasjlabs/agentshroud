---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Module Middleware"
location: "L631"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# Security modules should not use pickle (deserialization attack).

## Connections
- [[.test_no_pickle_in_security_modules()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Module_Middleware