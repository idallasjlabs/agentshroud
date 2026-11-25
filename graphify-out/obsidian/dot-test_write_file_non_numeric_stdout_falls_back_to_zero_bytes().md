---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L564"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SSHProxy
---

# .test_write_file_non_numeric_stdout_falls_back_to_zero_bytes()

## Connections
- [[If the remote script exits 0 but its stdout isn't a parseable integer,…]] - `rationale_for` [EXTRACTED]
- [[SSHProxy]] - `calls` [EXTRACTED]
- [[TestSSHProxyWriteFileTransport]] - `method` [EXTRACTED]
- [[_b64()]] - `calls` [EXTRACTED]
- [[asyncio_35]] - `references` [EXTRACTED]
- [[communicate()]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()_3]] - `indirect_call` [INFERRED]
- [[kill()]] - `contains` [EXTRACTED]
- [[wait()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SSHProxy
