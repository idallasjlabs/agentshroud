---
source_file: "gateway/tests/test_approval_queue.py"
type: "rationale"
community: "Approval Queue"
location: "L471"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue
---

# SCRUM-110: writes go through a temp file + os.replace so a crash     mid-write c

## Connections
- [[test_persist_pending_store_writes_atomically()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue