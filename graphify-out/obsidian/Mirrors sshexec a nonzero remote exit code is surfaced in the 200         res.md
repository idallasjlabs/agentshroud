---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "SSHProxy"
location: "L168"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SSHProxy
---

# Mirrors /ssh/exec: a nonzero remote exit code is surfaced in the 200         res

## Connections
- [[.test_write_file_remote_failure_returns_200_with_success_false()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SSHProxy