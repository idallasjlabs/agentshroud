---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Gateway Security Module"
location: "L383"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# Check if a Trivy report was already sent today (disk-based, secondary to _sent_d

## Connections
- [[_already_checked_upstream_today()]] - `rationale_for` [EXTRACTED]
- [[_already_sent_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module