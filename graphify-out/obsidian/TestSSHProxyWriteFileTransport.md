---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L430"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SSHProxy
---

# TestSSHProxyWriteFileTransport

## Connections
- [[.test_write_file_non_numeric_stdout_falls_back_to_zero_bytes()]] - `method` [EXTRACTED]
- [[.test_write_file_oserror_from_subprocess()]] - `method` [EXTRACTED]
- [[.test_write_file_remote_command_is_identical_across_calls()]] - `method` [EXTRACTED]
- [[.test_write_file_sends_path_and_content_via_stdin()]] - `method` [EXTRACTED]
- [[.test_write_file_timeout()]] - `method` [EXTRACTED]
- [[.test_write_file_unknown_host_raises()]] - `method` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[GatewayConfig_4]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[SSHConfig_2]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy_1]] - `uses` [INFERRED]
- [[SSHWriteResult]] - `uses` [INFERRED]
- [[Unit tests for SSHProxy.write_file() — verifies pathcontent travel as     DATA]] - `rationale_for` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SSHProxy