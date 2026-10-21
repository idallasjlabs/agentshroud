---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "rationale"
community: "ApprovalQueueConfig"
location: "L95"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig
---

# The in-memory window must be bounded; full history lives in SQLite.

## Connections
- [[TestAuditChainBounded]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalQueueConfig
