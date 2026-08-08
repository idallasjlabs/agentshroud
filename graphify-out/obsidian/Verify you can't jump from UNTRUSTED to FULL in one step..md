---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L370"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Verify you can't jump from UNTRUSTED to FULL in one step.

## Connections
- [[.test_trust_escalation_attack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection