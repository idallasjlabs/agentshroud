---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "SSHProxy"
location: "L281"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SSHProxy
---

# A host not present in the SSH allowlist is rejected with 404.

## Connections
- [[.test_write_file_disallowed_host_rejected()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SSHProxy