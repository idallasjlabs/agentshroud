---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "test_telegram_replay.py"
location: "L43"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_replaypy
---

# SQLite-backed Telegram update store, safe for concurrent asyncio callers.

## Connections
- [[UpdateReplayBuffer]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_replaypy