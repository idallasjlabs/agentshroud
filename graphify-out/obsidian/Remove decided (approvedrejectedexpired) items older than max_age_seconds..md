---
source_file: "gateway/approval_queue/queue.py"
type: "rationale"
community: "Community 413"
location: "L265"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_413
---

# Remove decided (approved/rejected/expired) items older than max_age_seconds.

## Connections
- [[.cleanup_decided()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_413