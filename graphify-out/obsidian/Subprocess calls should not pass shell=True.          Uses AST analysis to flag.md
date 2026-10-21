---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "_wrap_response() (2)"
location: "L657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response_2
---

# Subprocess calls should not pass shell=True.          Uses AST analysis to flag

## Connections
- [[dot-test_no_shell_true_in_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response_2
