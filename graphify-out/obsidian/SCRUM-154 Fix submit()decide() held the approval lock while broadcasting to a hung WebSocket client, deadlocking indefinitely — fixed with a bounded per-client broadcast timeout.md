---
source_file: "gateway/tests/test_approval_queue.py"
type: "rationale"
community: "Community 1572"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_1572
---

# SCRUM-154 Fix: submit()/decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout

#graphify/rationale #graphify/EXTRACTED #community/Community_1572