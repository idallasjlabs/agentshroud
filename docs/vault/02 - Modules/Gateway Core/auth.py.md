---
title: auth.py
type: module
file_path: gateway/ingest_api/auth.py
tags: [authentication, rate-limiting, bearer-token, security, gateway-core]
related: [Gateway Core/main.py, Gateway Core/models.py, Architecture Overview]
status: documented
---

# auth.py

## Purpose
Implements Bearer token authentication and token-bucket rate limiting for the AgentShroud gateway API. Uses constant-time comparison to prevent timing attacks on token validation.

## Responsibilities
- Validate `Authorization: Bearer <token>` headers on all protected endpoints
- Enforce per-client-IP rate limits using a sliding window token bucket
- Return appropriate HTTP status codes: 401 (missing/invalid token), 429 (rate limited)
- Provide a FastAPI dependency factory that injects `GatewayConfig` into the auth check

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `RateLimiter` | class | Sliding-window token-bucket rate limiter keyed by client IP |
| `RateLimiter.check` | method | Returns True if request is within limit; records the request time |
| `verify_token` | function | Constant-time Bearer token comparison using `hmac.compare_digest` |
| `get_auth_dependency` | async function | Factory that creates a FastAPI auth dependency with config injected |
| `create_auth_dependency` | function | Synchronous wrapper; returns a callable suitable for `Depends()` |
| `auth_check` | inner async function | The actual FastAPI dependency: checks rate limit, extracts and verifies Bearer token |
| `rate_limiter` | module-level instance | Global `RateLimiter(max_requests=100, window_seconds=60)` |

## Function Details

### RateLimiter.check(client_id)
**Purpose:** Slides the window by purging timestamps older than `window_seconds`, then checks if the request count would exceed `max_requests`. Appends the current timestamp on success.
**Parameters:** `client_id: str` — typically the client IP address
**Returns:** `bool` — True if allowed, False if rate limited
**Side effects:** Mutates `self.requests[client_id]` (in-memory, not persisted across restarts)

### verify_token(token, expected_token)
**Purpose:** Compares the provided Bearer token against the configured expected token using `hmac.compare_digest` to ensure fixed-time comparison regardless of string similarity.
**Parameters:** `token: str`, `expected_token: str`
**Returns:** `bool`

### get_auth_dependency(config)
**Purpose:** Returns an async closure (`auth_check`) that validates rate limits and Bearer tokens for a FastAPI `Depends()` context. The config is closed over to provide the expected token.
**Parameters:** `config: GatewayConfig`
**Returns:** async callable that raises `HTTPException` on failure

### create_auth_dependency(config)
**Purpose:** Synchronous factory wrapper for `get_auth_dependency` that is safe to pass directly to FastAPI's `Depends()` decorator at module load time (before the event loop is running).
**Parameters:** `config: GatewayConfig`
**Returns:** async callable

## Environment Variables Used
- None directly — the expected token is read from `config.auth_token` (loaded via `GatewayConfig` from `agentshroud.yaml` or environment)

## Config Keys Read
- `config.auth_token` — the expected Bearer token value for all protected endpoints

## HTTP Responses

| Code | Condition |
|------|-----------|
| 401 | Missing Authorization header or invalid Bearer token |
| 429 | Rate limit exceeded (includes `Retry-After: 60` header) |

## Imports From / Exports To
- Imports: `.config` (`GatewayConfig`)
- Imported by: [[Gateway Core/main.py]] (`create_auth_dependency`, `AuthRequired` dependency alias)

## Known Issues / Notes
- `RateLimiter` state is in-memory only. A gateway restart resets all rate limit counters.
- Because the gateway binds to `127.0.0.1`, the comment in the code notes this is "primarily a safety net" rather than a true anti-abuse measure.
- The global `rate_limiter` instance at module level means all FastAPI workers in the same process share the same counter dict. In a multi-process deployment (e.g. gunicorn), each worker has its own state.
- `security = HTTPBearer()` is created at module level but not used in the actual auth flow — the implementation manually parses the `Authorization` header. This is a minor inconsistency.
- The `auth_check` inner function re-calls `get_auth_dependency` on every request, creating a small redundant closure allocation. Functionally correct but slightly inefficient.

## Related
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
