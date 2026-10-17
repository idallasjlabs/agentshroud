---
source_file: "gateway/tests/test_security_toolchain.py"
type: "rationale"
community: "parse_trivy_output"
location: "L235"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_trivy_output
---

# returncode 0 = clean, 1 = vulns found (both expected); anything         else mea

## Connections
- [[dot-test_run_nonzero_exit_code_is_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_trivy_output
