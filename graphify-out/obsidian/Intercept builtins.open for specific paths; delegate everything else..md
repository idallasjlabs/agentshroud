---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "MiddlewareManager (2)"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MiddlewareManager_2
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MiddlewareManager_2
