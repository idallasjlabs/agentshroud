---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "Community 12"
location: "L565"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_12
---

# If the remote script exits 0 but its stdout isn't a parseable         integer, b

## Connections
- [[.test_write_file_non_numeric_stdout_falls_back_to_zero_bytes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_12