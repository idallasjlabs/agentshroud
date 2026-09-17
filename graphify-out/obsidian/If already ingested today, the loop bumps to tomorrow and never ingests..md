---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_sleep()"
location: "L1391"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# If already ingested today, the loop bumps to tomorrow and never ingests.

## Connections
- [[.test_skips_when_already_ingested_today()]] - `rationale_for` [EXTRACTED]
- [[.test_skips_when_already_ingested_today()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep