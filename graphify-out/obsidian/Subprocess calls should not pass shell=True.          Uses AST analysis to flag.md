---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "ContextGuard"
location: "L657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ContextGuard
---

# Subprocess calls should not pass shell=True.          Uses AST analysis to flag

## Connections
- [[dot-test_no_shell_true_in_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ContextGuard
