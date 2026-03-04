---
title: alert_dispatcher.py
type: module
file_path: gateway/security/alert_dispatcher.py
tags: [security, alerting, notifications, rate-limiting, deduplication, audit]
related: ["[[Security Modules/canary.py|canary.py]]", "[[Security Modules/drift_detector.py|drift_detector.py]]", "[[Data Flow]]"]
status: documented
---

# alert_dispatcher.py

## Purpose
Routes security findings to the appropriate notification channel based on severity, with deduplication and rate limiting to prevent alert fatigue. All alerts are persisted to a JSONL log file regardless of routing outcome.

## Threat Model
Alert fatigue and notification failure — high volumes of duplicate or low-priority alerts flooding notification channels, causing operators to miss critical security events. Also covers the failure mode where an alert fire-and-forget to the gateway API silently fails while the underlying event goes unrecorded.

## Responsibilities
- Persist every alert to a JSONL file at `/var/log/security/alerts/alerts.jsonl` before any routing decision
- Deduplicate alerts by `id` within a 24-hour window (configurable)
- Route CRITICAL and HIGH severity alerts to the gateway notification API immediately
- Rate-limit immediate notifications to 10 per hour (configurable); overflow alerts go to the digest buffer
- Buffer MEDIUM and LOW severity alerts for a daily digest
- Provide `get_digest()` to drain the buffer for scheduled digest delivery
- Provide `get_stats()` for observability into dispatcher health
- Provide `cleanup_seen()` to evict expired deduplication entries

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `AlertDispatcher` | Class | Main dispatcher with dedup, rate limiting, and routing |
| `AlertDispatcher.dispatch()` | Method | Entry point; returns action taken |
| `AlertDispatcher.get_digest()` | Method | Drain buffered MEDIUM/LOW alerts |
| `AlertDispatcher.get_stats()` | Method | Observability stats |
| `AlertDispatcher.cleanup_seen()` | Method | Remove expired dedup entries |
| `AlertDispatcher._is_duplicate()` | Method | Check dedup window by alert ID |
| `AlertDispatcher._is_rate_limited()` | Method | Check 1-hour sliding window counter |
| `AlertDispatcher._log_alert()` | Method | Append to JSONL log |
| `AlertDispatcher._send_notification()` | Method | POST to gateway `/api/alerts` |
| `AlertDispatcher._format_alert_message()` | Method | Human-readable alert string |

## Function Details

### AlertDispatcher.dispatch(alert)
**Purpose:** Main routing pipeline — log, dedup check, severity routing, rate-limit check, notify or buffer.
**Parameters:** `alert` (dict) — must contain at minimum `id` (str) and `severity` (str). Recognized severity values: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
**Returns:** `dict[str, str]` with key `action`:
  - `"notified"` — CRITICAL/HIGH, notification sent successfully
  - `"notify_failed"` — CRITICAL/HIGH, notification POST failed
  - `"rate_limited"` — CRITICAL/HIGH but rate limit reached; added to digest buffer
  - `"buffered"` — MEDIUM/LOW; added to digest buffer
  - `"deduped"` — duplicate within dedup window; no further action
**Side effects:** Writes to JSONL log; may POST to gateway API; mutates in-memory dedup and rate-limit state.

### AlertDispatcher._send_notification(alert)
**Purpose:** HTTP POST to `{gateway_url}/api/alerts` with JSON payload including type, severity, tool, message, alert_id, and timestamp. Uses `urllib.request` (no external dependencies).
**Returns:** bool — True on HTTP 2xx, False on any exception.
**Side effects:** Network I/O; logs success or failure.

### AlertDispatcher.get_digest(clear)
**Purpose:** Retrieve all buffered MEDIUM/LOW alerts, optionally clearing the buffer.
**Parameters:** `clear` (bool, default True)
**Returns:** `list[dict]`

### AlertDispatcher.cleanup_seen()
**Purpose:** Remove deduplication entries older than `dedup_window` seconds from `_seen_ids`.
**Returns:** int — number of entries removed.

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `alert_log` | `/var/log/security/alerts/alerts.jsonl` | JSONL log path |
| `gateway_url` | `http://localhost:8080` | Gateway API base URL |
| `max_per_hour` | 10 | Max immediate notifications per hour |
| `dedup_window` | 86400 (24h) | Seconds before same alert ID can re-notify |

## Module-Level Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `MAX_ALERTS_PER_HOUR` | 10 | Default rate limit |
| `RATE_WINDOW_SECONDS` | 3600 | Sliding window size |
| `DEDUP_WINDOW_SECONDS` | 86400 | 24-hour dedup window |

## Mode: Enforce vs Monitor
Not applicable. All alerts are dispatched regardless of mode. Routing is driven by severity, not by a global mode flag.

## Environment Variables
None directly. The `gateway_url` and log path are set at instantiation.

## Alert JSONL Format
Each line written to `alerts.jsonl` is a JSON object of the original alert dict merged with a `logged_at` ISO 8601 timestamp (UTC).

## Operational Notes
- The log directory is created on `__init__` if it does not exist.
- `_sent_times` is a `collections.deque` used as a sliding-window counter. Stale entries are pruned on each rate-limit check.
- If the gateway API is unreachable, `notify_failed` is returned but the alert is still persisted to JSONL — no alert data is lost.

## Related
- [[Data Flow]]
- [[Security Modules/canary.py|canary.py]]
- [[Security Modules/drift_detector.py|drift_detector.py]]
- [[Security Modules/clamav_scanner.py|clamav_scanner.py]]
