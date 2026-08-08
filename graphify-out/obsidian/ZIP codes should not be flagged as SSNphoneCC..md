---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L166"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# ZIP codes should not be flagged as SSN/phone/CC.

## Connections
- [[.test_no_false_positive_on_zip()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures