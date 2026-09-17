---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_sleep()"
location: "L1356"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_sleep
---

# _fake_ingest()

## Connections
- [[.test_ingest_records_even_when_disk_write_fails()]] - `indirect_call` [INFERRED]
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - `indirect_call` [INFERRED]
- [[.test_skips_ingest_when_marked_done_after_wake()]] - `indirect_call` [INFERRED]
- [[.test_skips_when_already_ingested_today()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/_sleep