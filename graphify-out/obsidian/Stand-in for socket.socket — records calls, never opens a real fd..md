---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "SOC Service Manager (Container Engine)"
location: "L43"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_Service_Manager_Container_Engine
---

# Stand-in for socket.socket — records calls, never opens a real fd.

## Connections
- [[_FakeUnixSocket]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_Service_Manager_Container_Engine