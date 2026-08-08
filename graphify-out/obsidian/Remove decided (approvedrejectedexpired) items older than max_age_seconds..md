---
source_file: "gateway/approval_queue/queue.py"
type: "rationale"
community: "Approval Queue Tests"
location: "L259"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue_Tests
---

# Remove decided (approved/rejected/expired) items older than max_age_seconds.

## Connections
- [[.cleanup_decided()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue_Tests