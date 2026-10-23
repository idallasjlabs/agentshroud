---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "test_soc_services_coverage.py"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_services_coveragepy
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_services_coveragepy
