---
source_file: "gateway/security/cron_state_monitor.py"
type: "rationale"
community: "Cron State Monitor"
location: "L292"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Cron_State_Monitor
---

# Start the poll loop as an asyncio task (idempotent).

## Connections
- [[.start()_2]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Cron_State_Monitor