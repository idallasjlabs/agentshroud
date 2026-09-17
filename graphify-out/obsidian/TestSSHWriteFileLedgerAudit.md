---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "SSHProxy"
location: "L681"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SSHProxy
---

# TestSSHWriteFileLedgerAudit

## Connections
- [[.test_write_file_success_and_denial_both_create_distinct_ledger_entries()]] - `method` [EXTRACTED]
- [[.test_write_file_success_creates_matching_ledger_entry()]] - `method` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[Gap coverage confirm a real audit-ledger row is created for BOTH a     successf]] - `rationale_for` [EXTRACTED]
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
- [[test_ssh_write_file_endpoint.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SSHProxy