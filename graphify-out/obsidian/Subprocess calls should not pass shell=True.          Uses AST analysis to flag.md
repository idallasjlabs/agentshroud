---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Community 809"
location: "L657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_809
---

# Subprocess calls should not pass shell=True.          Uses AST analysis to flag

## Connections
- [[.test_no_shell_true_in_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_809