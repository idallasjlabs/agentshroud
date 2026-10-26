---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "Community 986"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_986
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_986