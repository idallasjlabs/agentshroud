---
title: event_bus.py
type: module
file_path: gateway/ingest_api/event_bus.py
tags: [event-bus, pubsub, websocket, async, gateway-core]
related: [Gateway Core/main.py, Architecture Overview]
status: documented
---

# event_bus.py

## Purpose
Provides an in-process pub/sub event bus for broadcasting gateway security and operational events to WebSocket clients and internal subscribers. Used by the real-time activity dashboard and auth failure escalation logic.

## Responsibilities
- Maintain a list of async/sync subscriber callbacks
- Emit `GatewayEvent` objects to all subscribers in FIFO order (outside the lock to prevent deadlocks)
- Keep a rolling buffer of the most recent 200 events for replay on new WebSocket connections
- Track per-event-type counts for statistics
- Escalate `auth_failed` events to `severity="critical"` when 3+ failures occur within a 5-minute window

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `GatewayEvent` | dataclass | Represents a single gateway event (type, timestamp, summary, details, severity) |
| `GatewayEvent.to_dict` | method | Converts dataclass to plain dict via `asdict` for JSON serialization |
| `EventBus` | class | In-process async event bus with pub/sub and recent event buffer |
| `EventBus.subscribe` | async method | Registers a callback to receive all future events |
| `EventBus.unsubscribe` | async method | Removes a previously registered callback |
| `EventBus.emit` | async method | Dispatches an event to all subscribers; updates stats and auth failure tracker |
| `EventBus.get_stats` | async method | Returns total event count and per-type breakdown |
| `EventBus.get_recent` | async method | Returns the last N events as dicts (default 50, max 200 buffered) |
| `make_event` | function | Helper to create a `GatewayEvent` with the current UTC timestamp |

## Function Details

### EventBus.emit(event)
**Purpose:** Appends the event to the rolling buffer, increments the type counter, checks for auth failure escalation, then notifies all subscribers. Subscribers are called outside the lock; both sync and async callbacks are supported.
**Parameters:** `event: GatewayEvent`
**Returns:** None
**Side effects:**
- Truncates `_recent_events` to last 200 if overflow
- Escalates `event.severity` to `"critical"` if 3+ `auth_failed` events in 5 minutes
- Logs `WARNING` for any subscriber exception (non-fatal)

### make_event(event_type, summary, details, severity)
**Purpose:** Factory function that constructs a `GatewayEvent` with `datetime.now(timezone.utc)` as the timestamp.
**Parameters:**
- `event_type: str` — e.g., `"forward"`, `"pii_detected"`, `"auth_failed"`, `"ssh_exec"`, `"approval_submitted"`
- `summary: str` — human-readable one-line description
- `details: dict | None` — structured context
- `severity: str` — `"info"`, `"warning"`, or `"critical"`
**Returns:** `GatewayEvent`

## Environment Variables Used
- None

## Config Keys Read
- None — the event bus has no external configuration

## Event Types Emitted by main.py

| Type | Severity | Trigger |
|------|----------|---------|
| `forward` | info / warning | Content forwarded; warning if PII was sanitized |
| `pii_detected` | warning | PII entities were redacted from inbound content |
| `approval_submitted` | info | Agent submitted an action for human approval |
| `approval_decided` | info | Human approved or rejected a queued action |
| `auth_failed` | warning → critical | WebSocket authentication failed (escalates at 3+ in 5 min) |
| `ssh_denied` | warning / critical | SSH command rejected by validation; critical for injection attempts |
| `ssh_exec` | info | SSH command executed successfully |

## Imports From / Exports To
- Imports: Python stdlib only (`asyncio`, `logging`, `time`, `collections`, `dataclasses`, `datetime`)
- Imported by: [[Gateway Core/main.py]] (`EventBus`, `make_event`)

## Known Issues / Notes
- The rolling buffer is capped at 200 events. WebSocket clients that connect after events have rolled off will not see historical data beyond that window.
- `_auth_failures` is a list of floats (epoch timestamps); it is trimmed on each emit. This is O(n) per `auth_failed` event.
- Subscriber errors are caught and logged but the offending subscriber is not removed — a persistently failing subscriber will log on every event.
- The event bus is not persisted; a gateway restart clears all buffered events and subscriber state.
- Auth failure severity escalation mutates the `event` object in-place before notifying subscribers — subscribers always see the final (potentially escalated) severity.

## Related
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
