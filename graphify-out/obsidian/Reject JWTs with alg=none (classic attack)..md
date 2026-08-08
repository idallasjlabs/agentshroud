---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L401"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Reject JWTs with alg=none (classic attack).

## Connections
- [[.test_reject_none_algorithm()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures