---
source_file: "gateway/tests/test_security_toolchain.py"
type: "code"
community: "parse_trivy_output (2)"
location: "L234"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/parse_trivy_output_2
---

# .test_run_nonzero_exit_code_is_error()

## Connections
- [[TestTrivyRun]] - `method` [EXTRACTED]
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - `rationale_for` [EXTRACTED]
- [[run_trivy_scan()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/parse_trivy_output_2
