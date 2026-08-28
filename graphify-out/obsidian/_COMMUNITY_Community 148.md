---
type: community
cohesion: 0.07
members: 43
---

# Community 148

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[.__init__()_40]] - code - gateway/proxy/telegram_replay.py
- [[._conn_ok()]] - code - gateway/proxy/telegram_replay.py
- [[._init_db()]] - code - gateway/proxy/telegram_replay.py
- [[.cleanup_if_due()]] - code - gateway/proxy/telegram_replay.py
- [[.close()_8]] - code - gateway/proxy/telegram_replay.py
- [[.mark_delivered()]] - code - gateway/proxy/telegram_replay.py
- [[.pull_undelivered()]] - code - gateway/proxy/telegram_replay.py
- [[.record_inbound()]] - code - gateway/proxy/telegram_replay.py
- [[Any_22]] - code - gateway/proxy/telegram_replay.py
- [[Close the SQLite connection (idempotent).]] - rationale - gateway/proxy/telegram_replay.py
- [[Exception during cleanup execute must be swallowed.]] - rationale - gateway/tests/test_telegram_replay.py
- [[Exception during execute in mark_delivered must be swallowed.]] - rationale - gateway/tests/test_telegram_replay.py
- [[Exception during execute in pull_undelivered must return empty list.]] - rationale - gateway/tests/test_telegram_replay.py
- [[Exception during executemany (valid conn, SQL error) must be swallowed.]] - rationale - gateway/tests/test_telegram_replay.py
- [[Mark all updates with update_id  offset as delivered (normal getUpdates ack).]] - rationale - gateway/proxy/telegram_replay.py
- [[Periodically prune rows older than retention window.]] - rationale - gateway/proxy/telegram_replay.py
- [[Persist inbound updates so they can be replayed after a crash.]] - rationale - gateway/proxy/telegram_replay.py
- [[Return undelivered updates older than grace window (avoids replay storms).]] - rationale - gateway/proxy/telegram_replay.py
- [[SQLite-backed Telegram update store, safe for concurrent asyncio callers.]] - rationale - gateway/proxy/telegram_replay.py
- [[UpdateReplayBuffer]] - code - gateway/proxy/telegram_replay.py
- [[_cleanup_call_count_for_next_cleanup()]] - code - gateway/tests/test_telegram_replay.py
- [[_update()]] - code - gateway/tests/test_telegram_replay.py
- [[buf()]] - code - gateway/tests/test_telegram_replay.py
- [[telegram_replay.py]] - code - gateway/proxy/telegram_replay.py
- [[test_cleanup_db_error_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_cleanup_drops_old_rows()]] - code - gateway/tests/test_telegram_replay.py
- [[test_cleanup_execute_exception_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_cleanup_interval_guard()]] - code - gateway/tests/test_telegram_replay.py
- [[test_duplicate_record_is_ignored()]] - code - gateway/tests/test_telegram_replay.py
- [[test_grace_window_excludes_recent()]] - code - gateway/tests/test_telegram_replay.py
- [[test_mark_delivered_db_error_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_mark_delivered_excludes_from_pull()]] - code - gateway/tests/test_telegram_replay.py
- [[test_mark_delivered_execute_exception_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_multibot_isolation()]] - code - gateway/tests/test_telegram_replay.py
- [[test_pull_undelivered_db_error_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_pull_undelivered_execute_exception_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_pull_undelivered_handles_corrupt_payload()]] - code - gateway/tests/test_telegram_replay.py
- [[test_record_inbound_db_error_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_record_inbound_executemany_exception_swallowed()]] - code - gateway/tests/test_telegram_replay.py
- [[test_record_inbound_skips_updates_without_update_id()]] - code - gateway/tests/test_telegram_replay.py
- [[test_record_then_pull_returns_undelivered()]] - code - gateway/tests/test_telegram_replay.py
- [[test_sqlite_failure_does_not_raise()]] - code - gateway/tests/test_telegram_replay.py
- [[test_telegram_replay.py]] - code - gateway/tests/test_telegram_replay.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_148
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Ingest API & Approval Routes]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]

## Top bridge nodes
- [[UpdateReplayBuffer]] - degree 17, connects to 2 communities
- [[telegram_replay.py]] - degree 2, connects to 1 community