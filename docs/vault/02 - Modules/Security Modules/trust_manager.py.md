---
title: trust_manager.py
type: module
file_path: gateway/security/trust_manager.py
tags: [security, trust, authorization, progressive-trust, sqlite, rate-limiting]
related: ["[[Security Modules/agent_isolation.py|agent_isolation.py]]", "[[Security Modules/egress_filter.py|egress_filter.py]]", "[[Data Flow]]"]
status: documented
---

# trust_manager.py

## Purpose
Implements a progressive trust system where agents earn autonomy over time through successful operations and lose trust through failures and violations. Actions are gated by minimum required trust levels, and trust scores decay during inactivity.

## Threat Model
Privilege escalation and unconstrained agent autonomy — a newly registered or compromised agent attempting high-risk actions (executing commands, accessing secrets, modifying config) before it has established a track record of safe behavior.

## Responsibilities
- Register agents with an initial trust level and score
- Gate actions against minimum required trust levels via `is_action_allowed()`
- Increment trust score on `record_success()`, decrement on `record_failure()`, sharply decrement on `record_violation()`
- Apply time-based decay to scores so inactive agents lose trust gradually
- Rate-limit trust gains: cap successes credited per hour to `max_successes_per_hour` (anti-escalation)
- Persist all trust scores and full event history to SQLite (supports `:memory:` for tests)
- Enable WAL journal mode on file-backed databases for concurrent read safety
- Provide `get_history()` for audit trail retrieval per agent

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `TrustLevel` | IntEnum | UNTRUSTED(0) / BASIC(1) / STANDARD(2) / ELEVATED(3) / FULL(4) |
| `TrustConfig` | Dataclass | All tunable parameters: thresholds, points, decay, rate limits |
| `DEFAULT_ACTION_LEVELS` | Module dict | Default action → minimum `TrustLevel` mapping |
| `TrustManager` | Class | Main trust manager |
| `TrustManager.register_agent()` | Method | Add agent to the DB with initial score/level |
| `TrustManager.get_trust()` | Method | Get current (decay-adjusted) level and score |
| `TrustManager.is_action_allowed()` | Method | Authorization check for a named action |
| `TrustManager.record_success()` | Method | +5 points (default), rate-limited |
| `TrustManager.record_failure()` | Method | -20 points (default) |
| `TrustManager.record_violation()` | Method | -50 points (default) |
| `TrustManager.get_history()` | Method | Audit log for an agent |

## Function Details

### TrustManager.is_action_allowed(agent_id, action)
**Purpose:** Check if an agent's current trust level meets the minimum required for the action.
**Parameters:**
- `agent_id` (str) — agent identifier
- `action` (str) — action key from `action_levels` dict
**Returns:** bool — False if agent not registered or trust level insufficient
**Side effects:** None; reads decay-adjusted score.

### TrustManager.get_trust(agent_id)
**Purpose:** Return current trust state with decay applied (does not persist decay to DB).
**Returns:** `tuple[TrustLevel, float]` or None if agent not registered.

### TrustManager._apply_decay(score, last_action_time)
**Purpose:** Reduce score based on hours of inactivity. Default: 0.5 points per 24-hour decay period.
**Returns:** float, floor 0.0.

### TrustManager._update_score(agent_id, delta, event_type, details)
**Purpose:** Core score mutation. Applies decay first, then delta, then rate-limits positive deltas. Writes updated score and a history row atomically.
**Side effects:** Writes to `trust_scores` and `trust_history` tables.

### TrustManager.get_history(agent_id, limit)
**Purpose:** Return the most recent `limit` trust events for an agent, newest first.
**Returns:** `list[dict]` with keys: timestamp, event_type, score_delta, new_score, new_level, details.

## Default Action Trust Requirements

| Action | Minimum Level |
|--------|---------------|
| `read_file` | BASIC |
| `send_message` | STANDARD |
| `write_file` | STANDARD |
| `network_request` | STANDARD |
| `execute_command` | ELEVATED |
| `install_package` | ELEVATED |
| `modify_config` | ELEVATED |
| `delete_file` | ELEVATED |
| `admin_action` | FULL |
| `access_secrets` | FULL |

## Configuration (TrustConfig)

| Field | Default | Description |
|-------|---------|-------------|
| `initial_level` | BASIC | Starting trust level for new agents |
| `initial_score` | 100.0 | Starting trust score |
| `thresholds` | {0:0, 1:50, 2:150, 3:300, 4:500} | Score thresholds per level |
| `success_points` | 5.0 | Points added per success |
| `failure_points` | -20.0 | Points deducted per failure |
| `violation_points` | -50.0 | Points deducted per violation |
| `max_successes_per_hour` | 10 | Cap on credited successes per hour |
| `decay_rate` | 0.5 | Points lost per decay interval |
| `decay_interval_hours` | 24.0 | Decay interval in hours |

## Mode: Enforce vs Monitor
This module does not have a separate mode toggle. Trust gates are always enforced: `is_action_allowed()` returns False when trust is insufficient. Monitoring happens through the SQLite history tables and the Python logger.

## Environment Variables
None. DB path and config are passed at instantiation.

## Database Schema
Two SQLite tables:
- `trust_scores` — one row per agent: score, level, timestamps, counters
- `trust_history` — append-only event log: event_type, score_delta, new_score, new_level, details

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/agent_isolation.py|agent_isolation.py]]
- [[Security Modules/egress_filter.py|egress_filter.py]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
