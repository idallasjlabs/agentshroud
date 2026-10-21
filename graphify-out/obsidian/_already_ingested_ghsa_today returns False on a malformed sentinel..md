---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1625"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# _already_ingested_ghsa_today returns False on a malformed sentinel.

## Connections
- [[dot-test_already_ingested_helper_swallows_read_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
