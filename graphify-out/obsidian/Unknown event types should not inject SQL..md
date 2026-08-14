---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "Audit Export Pipeline"
location: "L909"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# Unknown event types should not inject SQL.

## Connections
- [[.test_event_type_validation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Export_Pipeline