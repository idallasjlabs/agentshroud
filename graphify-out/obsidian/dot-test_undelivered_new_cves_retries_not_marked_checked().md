---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 156"
location: "L1771"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_156
---

# .test_undelivered_new_cves_retries_not_marked_checked()

## Connections
- [[TestUpstreamCveCheckSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_all_agents()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_5]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[datetime]] - `calls` [INFERRED]
- [[now()_5]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_156