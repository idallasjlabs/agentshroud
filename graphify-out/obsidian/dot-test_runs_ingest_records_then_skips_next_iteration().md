---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 156"
location: "L1328"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_156
---

# .test_runs_ingest_records_then_skips_next_iteration()

## Connections
- [[First iteration ingests + records; second sees dedup and skips.]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_fake_ingest()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[datetime]] - `calls` [INFERRED]
- [[list_cve_agents]] - `calls` [EXTRACTED]
- [[now()_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_156