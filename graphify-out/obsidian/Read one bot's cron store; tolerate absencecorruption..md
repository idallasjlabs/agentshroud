---
source_file: "gateway/security/cron_state_monitor.py"
type: "rationale"
community: "CronStateMonitor"
location: "L96"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CronStateMonitor
---

# Read one bot's cron store; tolerate absence/corruption.

## Connections
- [[.parse_store()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CronStateMonitor