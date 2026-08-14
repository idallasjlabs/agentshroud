---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "rationale"
community: "Tool Chain Analyzer"
location: "L85"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Chain_Analyzer
---

# Intercept builtins.open for specific paths; delegate everything else.

## Connections
- [[_patch_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Chain_Analyzer