---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "P3 Infrastructure Security Modules"
location: "L1173"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/P3_Infrastructure_Security_Modules
---

# Security modules should not *call* eval() or exec().          Uses AST analysis

## Connections
- [[dot-test_no_eval_or_exec_in_security()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/P3_Infrastructure_Security_Modules