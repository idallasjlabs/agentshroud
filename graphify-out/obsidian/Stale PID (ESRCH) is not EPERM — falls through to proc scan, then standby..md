---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "SOC Service Manager (Container Engine)"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_Service_Manager_Container_Engine
---

# Stale PID (ESRCH) is not EPERM — falls through to /proc scan, then standby.

## Connections
- [[dot-test_esrch_falls_through_to_proc_scan()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_Service_Manager_Container_Engine