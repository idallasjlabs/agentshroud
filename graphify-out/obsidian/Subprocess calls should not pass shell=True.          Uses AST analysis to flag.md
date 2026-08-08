---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Subprocess calls should not pass shell=True.          Uses AST analysis to flag

## Connections
- [[.test_no_shell_true_in_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures