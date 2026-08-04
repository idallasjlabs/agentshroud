---
source_file: "gateway/approval_queue/queue.py"
type: "rationale"
community: "Approval Queue Core"
location: "L219"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue_Core
---

# Remove decided (approved/rejected/expired) items older than max_age_seconds.

## Connections
- [[.cleanup_decided()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue_Core
