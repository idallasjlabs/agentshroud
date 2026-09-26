---
source_file: "gateway/tests/test_main_endpoints.py"
type: "rationale"
community: "InjectionSeverity"
location: "L497"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# /api/alerts must reject non-localhost callers (S1 fix).

## Connections
- [[TestAlertsLocalhostEnforcement]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/InjectionSeverity