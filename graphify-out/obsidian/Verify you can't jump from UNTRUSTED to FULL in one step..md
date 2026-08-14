---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "Audit Export Pipeline"
location: "L370"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# Verify you can't jump from UNTRUSTED to FULL in one step.

## Connections
- [[.test_trust_escalation_attack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Export_Pipeline