---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "Gateway Proxy Layer"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Proxy_Layer
---

# Return undelivered updates older than grace window (avoids replay storms).

## Connections
- [[.pull_undelivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Proxy_Layer