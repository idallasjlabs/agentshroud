---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "rationale"
community: "PII Sanitizer & E2E Tests"
location: "L340"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__E2E_Tests
---

# PII redacted for agent A does not leak into agent B's audit trail.

## Connections
- [[.test_pii_from_agent_a_not_in_agent_b_audit()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__E2E_Tests