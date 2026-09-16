---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "Approval Queue (WebSocket)"
location: "L735"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue_WebSocket
---

# Both outcomes append to the SAME audit trail — a denial is not         silently

## Connections
- [[dot-test_write_file_success_and_denial_both_create_distinct_ledger_entries()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue_WebSocket