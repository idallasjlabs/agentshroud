---
source_file: "gateway/tests/test_security_toolchain.py"
type: "rationale"
community: "run_trivy_scan"
location: "L235"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/run_trivy_scan
---

# returncode 0 = clean, 1 = vulns found (both expected); anything         else mea

## Connections
- [[dot-test_run_nonzero_exit_code_is_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/run_trivy_scan
