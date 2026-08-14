---
source_file: "gateway/ssh_proxy/proxy.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/scripts/sync-cve-registrypy
---

# SSHResult

## Connections
- [[.execute()]] - `references` [EXTRACTED]
- [[.test_non_auto_approved_executes_directly()]] - `calls` [EXTRACTED]
- [[.test_ssh_exec_auto_approved()]] - `calls` [EXTRACTED]
- [[.test_ssh_exec_cwd_accepted_and_forwarded()]] - `calls` [EXTRACTED]
- [[.test_ssh_exec_cwd_none_forwards_none()]] - `calls` [EXTRACTED]
- [[.test_ssh_history()]] - `calls` [EXTRACTED]
- [[Result of an SSH command execution]] - `rationale_for` [EXTRACTED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHConfig_2]] - `uses` [INFERRED]
- [[SSHProxy_1]] - `uses` [INFERRED]
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
- [[__init__.py_12]] - `imports` [EXTRACTED]
- [[proxy.py]] - `contains` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/scripts/sync-cve-registrypy