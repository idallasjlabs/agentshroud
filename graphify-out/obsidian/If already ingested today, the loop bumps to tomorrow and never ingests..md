---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1540"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# If already ingested today, the loop bumps to tomorrow and never ingests.

## Connections
- [[dot-test_skips_when_already_ingested_today()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
