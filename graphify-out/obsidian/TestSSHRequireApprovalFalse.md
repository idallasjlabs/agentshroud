---
source_file: "gateway/tests/test_ssh_endpoints.py"
type: "code"
community: "ApprovalQueueConfig"
location: "L354"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalQueueConfig
---

# TestSSHRequireApprovalFalse

## Connections
- [[dot-no_approval_client()]] - `method` [EXTRACTED]
- [[dot-test_non_auto_approved_executes_directly()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_1]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[GatewayConfig_4]] - `uses` [INFERRED]
- [[LedgerConfig_1]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[SSHConfig_2]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy_1]] - `uses` [INFERRED]
- [[SSHResult]] - `uses` [INFERRED]
- [[Test require_approval=false executes directly (Finding 5)]] - `rationale_for` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ApprovalQueueConfig
