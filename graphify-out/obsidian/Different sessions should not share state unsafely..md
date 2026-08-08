---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L344"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Different sessions should not share state unsafely.

## Connections
- [[.test_session_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures