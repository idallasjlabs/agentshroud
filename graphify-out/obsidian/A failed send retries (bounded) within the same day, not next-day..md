---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1767"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# A failed send retries (bounded) within the same day, not next-day.

## Connections
- [[dot-test_retries_on_failed_send_before_giving_up()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
