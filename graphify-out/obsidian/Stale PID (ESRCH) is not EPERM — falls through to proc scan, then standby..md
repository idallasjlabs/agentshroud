---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "Community 486"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_486
---

# Stale PID (ESRCH) is not EPERM — falls through to /proc scan, then standby.

## Connections
- [[.test_esrch_falls_through_to_proc_scan()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_486