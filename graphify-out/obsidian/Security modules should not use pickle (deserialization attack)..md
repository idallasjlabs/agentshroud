---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L637"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# Security modules should not use pickle (deserialization attack).

## Connections
- [[.test_no_pickle_in_security_modules()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection