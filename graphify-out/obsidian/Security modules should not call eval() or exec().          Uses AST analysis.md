---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "lifespan.py"
location: "L1173"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/lifespanpy
---

# Security modules should not *call* eval() or exec().          Uses AST analysis

## Connections
- [[.test_no_eval_or_exec_in_security()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/lifespanpy