---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "_wrap_response()"
location: "L1173"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Security modules should not *call* eval() or exec().          Uses AST analysis

## Connections
- [[dot-test_no_eval_or_exec_in_security()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
