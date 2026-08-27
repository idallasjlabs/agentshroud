---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "Community 486"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_486
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_486