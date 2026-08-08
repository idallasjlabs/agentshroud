---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L56"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Prompt guard should scan full input, not short-circuit on first match.

## Connections
- [[.test_prompt_guard_no_early_exit_leak()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures