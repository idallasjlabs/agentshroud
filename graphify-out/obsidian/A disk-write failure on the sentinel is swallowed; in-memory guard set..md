---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_sleep()"
location: "L1542"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# A disk-write failure on the sentinel is swallowed; in-memory guard set.

## Connections
- [[.test_ingest_records_even_when_disk_write_fails()]] - `rationale_for` [EXTRACTED]
- [[.test_ingest_records_even_when_disk_write_fails()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep