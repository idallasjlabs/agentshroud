---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "SOC Services"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_Services
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_Services
