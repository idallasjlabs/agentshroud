---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "_sleep()"
location: "L103"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# Mark all updates with update_id < offset as delivered (normal getUpdates ack).

## Connections
- [[.mark_delivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep