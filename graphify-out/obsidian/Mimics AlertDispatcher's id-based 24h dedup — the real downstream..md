---
source_file: "gateway/tests/test_cron_state_monitor.py"
type: "rationale"
community: "Cron State Monitor"
location: "L191"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Cron_State_Monitor
---

# Mimics AlertDispatcher's id-based 24h dedup — the real downstream.

## Connections
- [[_DedupDispatchFake]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Cron_State_Monitor