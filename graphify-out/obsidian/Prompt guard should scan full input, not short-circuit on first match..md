---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Module Middleware"
location: "L56"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# Prompt guard should scan full input, not short-circuit on first match.

## Connections
- [[.test_prompt_guard_no_early_exit_leak()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Module_Middleware