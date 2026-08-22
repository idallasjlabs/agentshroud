---
source_file: "gateway/tests/test_ssh_endpoints.py"
type: "code"
community: "Security Fixes & SSH Write Endpoint"
location: "L308"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Fixes__SSH_Write_Endpoint
---

# TestSSHDisabledEndpoint

## Connections
- [[.disabled_client()]] - `method` [EXTRACTED]
- [[.test_ssh_exec_disabled_returns_503()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[SSHResult]] - `uses` [INFERRED]
- [[Test that SSH disabled returns 503 (Finding 12)]] - `rationale_for` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Fixes__SSH_Write_Endpoint