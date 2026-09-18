---
source_file: "gateway/proxy/telegram_replay.py"
type: "code"
community: "test_telegram_replay.py"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_telegram_replaypy
---

# UpdateReplayBuffer

## Connections
- [[.__init__()_64]] - `method` [EXTRACTED]
- [[._conn_ok()]] - `method` [EXTRACTED]
- [[._init_db()_2]] - `method` [EXTRACTED]
- [[.cleanup_if_due()]] - `method` [EXTRACTED]
- [[.close()_9]] - `method` [EXTRACTED]
- [[.mark_delivered()]] - `method` [EXTRACTED]
- [[.pull_undelivered()]] - `method` [EXTRACTED]
- [[.record_inbound()]] - `method` [EXTRACTED]
- [[SQLite-backed Telegram update store, safe for concurrent asyncio callers.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_2]] - `conceptually_related_to` [INFERRED]
- [[buf()]] - `calls` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[telegram_replay.py]] - `contains` [EXTRACTED]
- [[test_multibot_isolation()]] - `calls` [EXTRACTED]
- [[test_pull_undelivered_execute_exception_swallowed()]] - `calls` [EXTRACTED]
- [[test_sqlite_failure_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_telegram_replay.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_telegram_replaypy