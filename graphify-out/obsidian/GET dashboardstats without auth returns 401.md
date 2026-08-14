---
source_file: "gateway/tests/test_dashboard.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# GET /dashboard/stats without auth returns 401

## Connections
- [[test_dashboard_stats_requires_auth()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline