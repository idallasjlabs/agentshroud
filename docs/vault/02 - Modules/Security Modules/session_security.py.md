---
title: session_security.py
type: module
file_path: gateway/security/session_security.py
tags: [security, session-management, session-hijacking, event-injection, rate-limiting, mcp]
related: [[oauth_security.py]], [[token_validation.py]], [[subagent_monitor.py]]
status: documented
---

# session_security.py

## Purpose
Provides cryptographically secure session lifecycle management for the MCP gateway: generates random session identifiers, binds sessions to client IP and User-Agent fingerprints, enforces session expiry and rotation, validates event sources to prevent event injection, and applies per-IP session creation rate limiting.

## Threat Model
Addresses session hijacking (Chen et al. 2026, arXiv:2602.14364) and event injection attacks (Wang et al. 2026, arXiv:2602.08412) against agent frameworks. A session is bound to the exact IP and User-Agent that created it; any deviation raises `SessionBindingError`. Events are only accepted from pre-registered sources; unregistered source names raise `EventInjectionError`.

## Responsibilities
- Generate 32-byte URL-safe random session IDs via `secrets.token_urlsafe`
- Bind each session to an IP + User-Agent fingerprint (SHA-256 hash)
- Enforce a configurable maximum session age (default 1 hour)
- Enforce per-IP session creation rate limits (default 10 sessions per 60-second window)
- Limit total concurrent sessions globally (hard cap of 10,000)
- Support secure session rotation (issue new ID while preserving binding and event sources)
- Register trusted event sources per session; reject events from unregistered sources
- Provide expiry cleanup for both sessions and IP rate-limit tracking data

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `SessionManager` | Class | Core session lifecycle manager |
| `Session` | Dataclass | Session record: ID, IP, user-agent, fingerprint, creation time, event sources |
| `SessionError` | Exception | Base exception for all session failures |
| `SessionExpired` | Exception | Raised when a session has exceeded `max_session_age` |
| `SessionBindingError` | Exception | Raised when IP or User-Agent does not match the session fingerprint |
| `EventInjectionError` | Exception | Raised when an event arrives from an unregistered source |
| `RateLimitExceeded` | Exception | Raised when an IP exceeds the session creation rate limit |

## Function Details

### SessionManager.__init__(max_session_age, max_sessions_per_ip, rate_limit_window)
**Purpose:** Configures session lifetime, per-IP creation limit, and the rolling window duration for rate limiting.
**Parameters:** `max_session_age` (int, default 3600 s), `max_sessions_per_ip` (int, default 10), `rate_limit_window` (int, default 60 s)

### SessionManager.create_session(ip, user_agent)
**Purpose:** Validates rate limit for `ip`, evicts expired sessions if at global capacity, generates a new session ID, computes the fingerprint, stores the session, and returns the `Session` object.
**Parameters:** `ip` (str), `user_agent` (str)
**Returns:** `Session`; raises `RateLimitExceeded` if rate limit exceeded

### SessionManager.validate_session(session_id, ip, user_agent)
**Purpose:** Verifies the session exists, has not expired, and the IP + User-Agent fingerprint matches the stored value. Deletes the session and raises `SessionExpired` if expired.
**Parameters:** `session_id` (str), `ip` (str), `user_agent` (str)
**Returns:** `True`; raises `SessionError`, `SessionExpired`, or `SessionBindingError`

### SessionManager.rotate_session(old_session_id, ip, user_agent)
**Purpose:** Validates the existing session, removes it, issues a new random session ID, and creates a replacement session preserving the fingerprint and event sources. Used to limit session lifetime while maintaining continuity.
**Parameters:** `old_session_id` (str), `ip` (str), `user_agent` (str)
**Returns:** New `Session`

### SessionManager.destroy_session(session_id)
**Purpose:** Removes a session from the store. No-op if the session does not exist. Called on agent logout or termination.
**Parameters:** `session_id` (str)

### SessionManager.register_event_source(session_id, source)
**Purpose:** Adds `source` to the session's trusted event source set. Only sources registered here will be accepted by `validate_event`.
**Parameters:** `session_id` (str), `source` (str)

### SessionManager.validate_event(session_id, source, event)
**Purpose:** Verifies that `source` is in the session's registered event sources before allowing the event to be processed. Raises `EventInjectionError` for unregistered sources.
**Parameters:** `session_id` (str), `source` (str), `event` (Any)
**Returns:** `True`; raises `EventInjectionError`

### SessionManager.cleanup_expired()
**Purpose:** Removes all expired sessions and purges stale IP rate-limit records. Returns the count of sessions removed. Should be called periodically.
**Returns:** `int`

## Configuration / Environment Variables
- All configuration is passed via constructor arguments; no environment variables
- `MAX_TOTAL_SESSIONS = 10000` — class-level hard cap on total simultaneous sessions

## Related
- [[oauth_security.py]]
- [[token_validation.py]]
- [[subagent_monitor.py]]
