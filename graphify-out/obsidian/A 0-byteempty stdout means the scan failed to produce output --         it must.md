---
source_file: "gateway/tests/test_security_toolchain.py"
type: "rationale"
community: "parse_trivy_output (2)"
location: "L217"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_trivy_output_2
---

# A 0-byte/empty stdout means the scan failed to produce output --         it must

## Connections
- [[dot-test_run_empty_stdout_is_error_not_clean()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_trivy_output_2
