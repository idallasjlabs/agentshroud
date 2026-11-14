---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Community 368"
location: "L395"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_368
---

# The gateway never writes the registry, so the alert must not say it did.

## Connections
- [[.test_alert_does_not_claim_registration()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_368