---
source_file: "gateway/tools/multi_host_test.py"
type: "rationale"
community: "parse_trivy_output"
location: "L149"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/parse_trivy_output
---

# 0 iff all hosts passed; 1 otherwise (incl. empty / any unreachable).

## Connections
- [[dot-exit_code()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/parse_trivy_output
