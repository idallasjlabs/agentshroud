---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Module Middleware"
location: "L657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# Subprocess calls should not pass shell=True.          Uses AST analysis to flag

## Connections
- [[.test_no_shell_true_in_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Module_Middleware