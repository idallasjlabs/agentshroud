---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L549"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SSHProxy
---

# .test_write_file_oserror_from_subprocess()

## Connections
- [[SSHProxy]] - `calls` [EXTRACTED]
- [[TestSSHProxyWriteFileTransport]] - `method` [EXTRACTED]
- [[_b64()]] - `calls` [EXTRACTED]
- [[asyncio_36]] - `references` [EXTRACTED]
- [[fake_create_subprocess_exec()_1]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()_3]] - `indirect_call` [INFERRED]
- [[ssh binary missing  spawn failure surfaces as exit_code=-1 with the OSError…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SSHProxy
