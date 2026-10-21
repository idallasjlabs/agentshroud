---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "soc/router.py"
location: "L370"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/soc/routerpy
---

# Verify you can't jump from UNTRUSTED to FULL in one step.

## Connections
- [[dot-test_trust_escalation_attack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/soc/routerpy
