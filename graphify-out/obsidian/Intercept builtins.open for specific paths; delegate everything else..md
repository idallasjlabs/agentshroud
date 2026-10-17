---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "ServiceManager (3)"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ServiceManager_3
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ServiceManager_3
