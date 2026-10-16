---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "ApprovalQueueConfig"
location: "L681"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalQueueConfig
---

# TestSSHWriteFileLedgerAudit

## Connections
- [[dot-test_write_file_success_and_denial_both_create_distinct_ledger_entries()]] - `method` [EXTRACTED]
- [[dot-test_write_file_success_creates_matching_ledger_entry()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[Gap coverage confirm a real audit-ledger row is created for BOTH a     successf]] - `rationale_for` [EXTRACTED]
- [[GatewayConfig_2]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[SSHConfig_2]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[SSHWriteResult]] - `uses` [INFERRED]
- [[test_ssh_write_file_endpoint.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ApprovalQueueConfig
