---
title: ledger.py
type: module
file_path: gateway/ingest_api/ledger.py
tags: [audit, sqlite, ledger, privacy, security, gateway-core]
related: [Gateway Core/models.py, Gateway Core/main.py, Architecture Overview]
status: documented
---

# ledger.py

## Purpose
Implements an async SQLite-backed audit trail for all content forwarded through the AgentShroud gateway. Stores only SHA-256 hashes of content — raw content is never persisted — enforcing a privacy-by-design audit model.

## Responsibilities
- Create and manage the `ledger` SQLite database with WAL mode for concurrency
- Record every forwarding event with source, target, sanitization status, and content hashes
- Support paginated queries with filtering by source, timestamp range, and target agent
- Fetch or delete individual entries (right-to-erasure support)
- Provide aggregate statistics (totals, by source, sanitized vs. not)
- Enforce configurable retention by expiring entries after `retention_days`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `DataLedger` | class | Async SQLite-backed data ledger |
| `__init__` | method | Stores config; does not open DB connection until `initialize()` |
| `initialize` | async method | Creates DB file, applies schema, runs initial retention cleanup |
| `record` | async method | Inserts a new ledger entry; hashes both sanitized and original content |
| `query` | async method | Paginated query with optional source/time/target filters |
| `get_entry` | async method | Fetches a single entry by UUID |
| `delete_entry` | async method | Permanently deletes an entry (right to erasure) |
| `get_stats` | async method | Returns aggregate counts by source and sanitization status |
| `enforce_retention` | async method | Deletes entries where `expires_at` is in the past |
| `close` | async method | Closes the aiosqlite connection |
| `_hash_content` | static method | Returns SHA-256 hex digest of a UTF-8 string |

## Function Details

### initialize()
**Purpose:** Opens the SQLite connection, enables foreign keys and WAL journal mode, creates the `ledger` and `schema_version` tables, then calls `enforce_retention()` on startup.
**Parameters:** None
**Returns:** None
**Side effects:** Creates directories if needed; logs startup cleanup count

### record(source, content, original_content, sanitized, redaction_count, redaction_types, forwarded_to, content_type, metadata)
**Purpose:** Inserts a new audit record. Both `content` and `original_content` are SHA-256 hashed before storage. `expires_at` is set to `now + retention_days`.
**Parameters:**
- `source: str` — origin identifier (shortcut, telegram, api, etc.)
- `content: str` — sanitized content (hashed, never stored as text)
- `original_content: str` — original content before sanitization (hashed)
- `sanitized: bool` — whether redactions were applied
- `redaction_count: int` — number of redactions
- `redaction_types: list[str]` — entity type names redacted
- `forwarded_to: str` — target agent name
- `content_type: str` — text, url, photo, file, ssh_command, security_event
- `metadata: Optional[dict]` — additional context
**Returns:** `LedgerEntry` with the new record's metadata
**Side effects:** Commits to SQLite; logs entry ID, source, sanitized status, size

### query(page, page_size, source, since, until, forwarded_to)
**Purpose:** Parameterized paginated query. Builds WHERE clause dynamically from non-None filters. Returns results ordered by `timestamp DESC`.
**Returns:** `LedgerQueryResponse` with entries list plus total count and pagination metadata

### enforce_retention()
**Purpose:** Deletes all entries where `expires_at < now`. Called on startup and may be called periodically.
**Returns:** `int` — count of deleted entries

## Environment Variables Used
- None directly — retention and path configuration come from `LedgerConfig` (loaded from `agentshroud.yaml`)

## Config Keys Read
- `config.path` — filesystem path to the SQLite database file (`Path` object)
- `config.retention_days` — number of days before entries expire

## Database Schema
```sql
TABLE ledger:
  id TEXT PRIMARY KEY               -- UUID
  timestamp TEXT NOT NULL           -- ISO 8601 UTC
  source TEXT NOT NULL              -- origin
  content_hash TEXT NOT NULL        -- SHA-256 of sanitized content
  original_content_hash TEXT        -- SHA-256 of original content
  sanitized INTEGER                 -- 0 or 1
  size INTEGER                      -- byte length of sanitized content
  redaction_count INTEGER
  redaction_types TEXT              -- JSON array
  forwarded_to TEXT
  content_type TEXT
  metadata TEXT                     -- JSON object
  created_at TEXT
  expires_at TEXT                   -- used for retention
```

## Imports From / Exports To
- Imports: [[Gateway Core/models.py]] (`LedgerEntry`, `LedgerQueryResponse`), `.config` (`LedgerConfig`), `aiosqlite`
- Imported by: [[Gateway Core/main.py]]

## Known Issues / Notes
- `initialize()` must be called before any other method — calls without it raise `RuntimeError("Ledger not initialized")`.
- The `delete_entry` method is commented as implementing "right to erasure" — this only removes the hash record, not any external copies.
- `redaction_types` is stored as a JSON array string; consumers must deserialize it.
- The ApprovalStore uses a separate SQLite database at `/tmp/agentshroud_approvals.db` (see TODO comment in `main.py`).
- Schema version table exists (`schema_version`) but migration logic is not yet implemented beyond initial version 1.

## Related
- [[Gateway Core/models.py]]
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
