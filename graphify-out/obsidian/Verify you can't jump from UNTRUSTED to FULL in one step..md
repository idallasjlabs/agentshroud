---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "1Password op-proxy (POST /credentials/op-proxy; "
location: "L370"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_
---

# Verify you can't jump from UNTRUSTED to FULL in one step.

## Connections
- [[.test_trust_escalation_attack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_