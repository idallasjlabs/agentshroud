---
source_file: "gateway/tests/test_approval_queue.py"
type: "rationale"
community: "SCRUM-154 Fix: submit()/decide() held the approv"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SCRUM-154_Fix_submit/decide_held_the_approv
---

# SCRUM-154 Fix: submit()/decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout

#graphify/rationale #graphify/EXTRACTED #community/SCRUM-154_Fix_submit/decide_held_the_approv