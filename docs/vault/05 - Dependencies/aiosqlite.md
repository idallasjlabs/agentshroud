---
title: aiosqlite
type: dependency
tags: [database, sqlite, async, python]
related: [Gateway Core/ledger.py, Dependencies/All Dependencies]
status: documented
---

# aiosqlite

**Package:** `aiosqlite`
**Version:** ≥0.20.0,<1.0.0
**Used in:** Audit ledger, approval queue store

## Purpose

Async wrapper around Python's standard `sqlite3` module. Enables non-blocking SQLite operations within FastAPI's async request handlers. Without async I/O, SQLite writes would block the event loop during high-traffic periods.

## Where Used

| Module | Usage |
|--------|-------|
| `gateway/ingest_api/ledger.py` | Async SQLite for audit ledger (all request records) |
| `gateway/approval_queue/store.py` | Async persistence for approval queue |
| `gateway/security/audit_store.py` | Audit event storage |

## Database Files

| Database | Volume Path | Size |
|----------|------------|------|
| Ledger | `gateway-data:/app/data/ledger.db` | Grows with usage; 90-day retention |

## WAL Mode

The ledger uses Write-Ahead Logging (WAL) for crash safety:
```python
await conn.execute("PRAGMA journal_mode=WAL")
```

This ensures database consistency on unclean shutdown.

## Related Notes

- [[Gateway Core/ledger.py|ledger.py]] — Primary user of aiosqlite
- [[Containers & Services/volumes]] — `gateway-data` volume stores the database
- [[Dependencies/All Dependencies]] — Full dependency list
