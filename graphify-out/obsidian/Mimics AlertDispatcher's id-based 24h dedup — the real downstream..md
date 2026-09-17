---
source_file: "gateway/tests/test_cron_state_monitor.py"
type: "rationale"
community: "CronStateMonitor"
location: "L191"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CronStateMonitor
---

# Mimics AlertDispatcher's id-based 24h dedup — the real downstream.

## Connections
- [[_DedupDispatchFake]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CronStateMonitor