---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_sleep()"
location: "L1476"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# _already_ingested_ghsa_today returns False on a malformed sentinel.

## Connections
- [[.test_already_ingested_helper_swallows_read_error()]] - `rationale_for` [EXTRACTED]
- [[.test_already_ingested_helper_swallows_read_error()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep