---
source_file: "gateway/security/report_store.py"
type: "rationale"
community: "ReportStore"
location: "L164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ReportStore
---

# Prune oldest reports so the shared volume can't be filled.

## Connections
- [[._enforce_count_cap()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ReportStore