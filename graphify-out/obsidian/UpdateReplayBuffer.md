---
source_file: "gateway/proxy/telegram_replay.py"
type: "code"
community: "Community 148"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_148
---

# UpdateReplayBuffer

## Connections
- [[.__init__()_40]] - `method` [EXTRACTED]
- [[._conn_ok()]] - `method` [EXTRACTED]
- [[._init_db()]] - `method` [EXTRACTED]
- [[.cleanup_if_due()]] - `method` [EXTRACTED]
- [[.close()_8]] - `method` [EXTRACTED]
- [[.mark_delivered()]] - `method` [EXTRACTED]
- [[.pull_undelivered()]] - `method` [EXTRACTED]
- [[.record_inbound()]] - `method` [EXTRACTED]
- [[SQLite-backed Telegram update store, safe for concurrent asyncio callers.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `conceptually_related_to` [INFERRED]
- [[buf()]] - `calls` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[telegram_replay.py]] - `contains` [EXTRACTED]
- [[test_multibot_isolation()]] - `calls` [EXTRACTED]
- [[test_pull_undelivered_execute_exception_swallowed()]] - `calls` [EXTRACTED]
- [[test_sqlite_failure_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_telegram_replay.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_148