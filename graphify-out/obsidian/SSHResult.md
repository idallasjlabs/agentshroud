---
source_file: "gateway/ssh_proxy/proxy.py"
type: "code"
community: "Approval Queue (WebSocket)"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Approval_Queue_WebSocket
---

# SSHResult

## Connections
- [[dot-execute()]] - `references` [EXTRACTED]
- [[dot-test_non_auto_approved_executes_directly()]] - `calls` [EXTRACTED]
- [[dot-test_ssh_exec_auto_approved()]] - `calls` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_accepted_and_forwarded()]] - `calls` [EXTRACTED]
- [[dot-test_ssh_exec_cwd_none_forwards_none()]] - `calls` [EXTRACTED]
- [[dot-test_ssh_history()]] - `calls` [EXTRACTED]
- [[Result of an SSH command execution]] - `rationale_for` [EXTRACTED]
- [[SSHConfig_1]] - `uses` [INFERRED]
- [[SSHConfig_2]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[TestExecute]] - `uses` [INFERRED]
- [[TestInjectionNewline]] - `uses` [INFERRED]
- [[TestIsAutoApproved]] - `uses` [INFERRED]
- [[TestSSHDisabled]] - `uses` [INFERRED]
- [[TestSSHDisabledEndpoint]] - `uses` [INFERRED]
- [[TestSSHExec]] - `uses` [INFERRED]
- [[TestSSHHistory]] - `uses` [INFERRED]
- [[TestSSHHosts]] - `uses` [INFERRED]
- [[TestSSHRequireApprovalFalse]] - `uses` [INFERRED]
- [[TestSSHValidateCwd]] - `uses` [INFERRED]
- [[TestValidateCommand]] - `uses` [INFERRED]
- [[proxy.py]] - `contains` [EXTRACTED]
- [[ssh_proxy__init__.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Approval_Queue_WebSocket