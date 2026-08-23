---
source_file: "gateway/tests/test_approval_queue.py"
type: "rationale"
community: "Approval Queue"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue
---

# SCRUM-154 Fix: submit()/decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue