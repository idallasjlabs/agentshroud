---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L643"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# No yaml.load() without Loader (arbitrary code execution).

## Connections
- [[.test_no_yaml_unsafe_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures