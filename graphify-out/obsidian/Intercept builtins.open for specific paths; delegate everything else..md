---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "SOC Service Manager (Container Engine)"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_Service_Manager_Container_Engine
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_Service_Manager_Container_Engine