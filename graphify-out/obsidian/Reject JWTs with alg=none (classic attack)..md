---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "TestAuth"
location: "L401"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestAuth
---

# Reject JWTs with alg=none (classic attack).

## Connections
- [[.test_reject_none_algorithm()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestAuth