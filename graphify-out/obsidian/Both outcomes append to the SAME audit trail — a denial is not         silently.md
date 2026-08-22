---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "Security Fixes & SSH Write Endpoint"
location: "L735"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Fixes__SSH_Write_Endpoint
---

# Both outcomes append to the SAME audit trail — a denial is not         silently

## Connections
- [[.test_write_file_success_and_denial_both_create_distinct_ledger_entries()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Fixes__SSH_Write_Endpoint