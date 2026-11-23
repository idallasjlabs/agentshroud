---
source_file: "gateway/tests/test_security_toolchain.py"
type: "code"
community: "run_trivy_scan"
location: "L234"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run_trivy_scan
---

# .test_run_nonzero_exit_code_is_error()

## Connections
- [[TestTrivyRun]] - `method` [EXTRACTED]
- [[patch_1]] - `references` [EXTRACTED]
- [[returncode 0 = clean, 1 = vulns found (both expected); anything else means…]] - `rationale_for` [EXTRACTED]
- [[run_trivy_scan()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run_trivy_scan
