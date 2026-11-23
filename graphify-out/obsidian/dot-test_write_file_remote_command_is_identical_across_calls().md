---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L483"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SSHProxy
---

# .test_write_file_remote_command_is_identical_across_calls()

## Connections
- [[SSHProxy]] - `calls` [EXTRACTED]
- [[TestSSHProxyWriteFileTransport]] - `method` [EXTRACTED]
- [[The remote command string must not vary with request content — proving it…]] - `rationale_for` [EXTRACTED]
- [[_b64()]] - `calls` [EXTRACTED]
- [[asyncio_36]] - `references` [EXTRACTED]
- [[communicate()_1]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()_2]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()_3]] - `indirect_call` [INFERRED]
- [[kill()_1]] - `contains` [EXTRACTED]
- [[wait()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SSHProxy
