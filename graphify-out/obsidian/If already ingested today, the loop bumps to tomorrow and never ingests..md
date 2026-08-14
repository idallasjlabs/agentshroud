---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L1215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# If already ingested today, the loop bumps to tomorrow and never ingests.

## Connections
- [[.test_skips_when_already_ingested_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite