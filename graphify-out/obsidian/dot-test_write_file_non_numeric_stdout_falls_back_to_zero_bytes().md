---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "Approval Queue (WebSocket)"
location: "L564"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Queue_WebSocket
---

# .test_write_file_non_numeric_stdout_falls_back_to_zero_bytes()

## Connections
- [[If the remote script exits 0 but its stdout isn't a parseable         integer, b]] - `rationale_for` [EXTRACTED]
- [[SSHProxy_1]] - `calls` [EXTRACTED]
- [[TestSSHProxyWriteFileTransport]] - `method` [EXTRACTED]
- [[_b64()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Queue_WebSocket