---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "Tool Chain Analyzer"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Chain_Analyzer
---

# Stale PID (ESRCH) is not EPERM — falls through to /proc scan, then standby.

## Connections
- [[.test_esrch_falls_through_to_proc_scan()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Chain_Analyzer