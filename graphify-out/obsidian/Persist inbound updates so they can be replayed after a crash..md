---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "_sleep()"
location: "L83"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# Persist inbound updates so they can be replayed after a crash.

## Connections
- [[.record_inbound()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep