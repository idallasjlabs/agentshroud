---
source_file: "gateway/security/scanner_integration.py"
type: "rationale"
community: "get_trivy_summary"
location: "L322"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_trivy_summary
---

# Return True if the most recent report file was written within max_age_hours.

## Connections
- [[_is_fresh()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_trivy_summary
