---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L436"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SSHProxy
---

# .test_write_file_sends_path_and_content_via_stdin()

## Connections
- [[SSHProxy]] - `calls` [EXTRACTED]
- [[TestSSHProxyWriteFileTransport]] - `method` [EXTRACTED]
- [[_b64()]] - `calls` [EXTRACTED]
- [[asyncio_33]] - `references` [EXTRACTED]
- [[communicate()_2]] - `contains` [EXTRACTED]
- [[fake_create_subprocess_exec()_3]] - `indirect_call` [INFERRED]
- [[kill()_2]] - `contains` [EXTRACTED]
- [[wait()_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SSHProxy
