---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "_sleep()"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# Return undelivered updates older than grace window (avoids replay storms).

## Connections
- [[.pull_undelivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep