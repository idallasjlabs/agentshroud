---
source_file: "gateway/tests/test_ssh_endpoints.py"
type: "code"
community: "Approval Queue (WebSocket)"
location: "L103"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Approval_Queue_WebSocket
---

# TestSSHExec

## Connections
- [[dot-test_ssh_exec_auto_approved()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_command_not_in_allowlist()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_accepted_and_forwarded()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_invalid_rejects_400()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_none_forwards_none()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_relative_path_rejects_400()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_denied_command()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_injection_attempt()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_no_auth()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_requires_approval()]] - `method` [EXTRACTED]
- [[dot-test_ssh_exec_unknown_host()]] - `method` [EXTRACTED]
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
- [[SSHResult]] - `uses` [INFERRED]
- [[test_ssh_endpoints.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Approval_Queue_WebSocket