---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "Telegram Replay"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Replay
---

# Return undelivered updates older than grace window (avoids replay storms).

## Connections
- [[.pull_undelivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Replay