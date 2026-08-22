---
source_file: "gateway/security/cron_state_monitor.py"
type: "rationale"
community: "Cron State Monitor"
location: "L96"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Cron_State_Monitor
---

# Read one bot's cron store; tolerate absence/corruption.

## Connections
- [[.parse_store()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Cron_State_Monitor