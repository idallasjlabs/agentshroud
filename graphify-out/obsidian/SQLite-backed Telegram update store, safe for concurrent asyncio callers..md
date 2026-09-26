---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "_sleep()"
location: "L43"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# SQLite-backed Telegram update store, safe for concurrent asyncio callers.

## Connections
- [[UpdateReplayBuffer]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep