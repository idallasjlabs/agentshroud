---
source_file: "gateway/security/cron_state_monitor.py"
type: "rationale"
community: "CronStateMonitor"
location: "L156"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CronStateMonitor
---

# One poll pass over all stores.  Never raises.

## Connections
- [[.check()_5]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CronStateMonitor