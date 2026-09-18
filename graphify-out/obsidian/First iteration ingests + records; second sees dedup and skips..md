---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_sleep()"
location: "L1329"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# First iteration ingests + records; second sees dedup and skips.

## Connections
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - `rationale_for` [EXTRACTED]
- [[.test_runs_ingest_records_then_skips_next_iteration()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep