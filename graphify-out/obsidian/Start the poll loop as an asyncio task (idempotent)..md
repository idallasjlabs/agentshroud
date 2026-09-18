---
source_file: "gateway/security/cron_state_monitor.py"
type: "rationale"
community: "CronStateMonitor"
location: "L292"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CronStateMonitor
---

# Start the poll loop as an asyncio task (idempotent).

## Connections
- [[.start()_2]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CronStateMonitor