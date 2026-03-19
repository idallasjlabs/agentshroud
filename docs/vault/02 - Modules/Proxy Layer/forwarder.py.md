---
title: forwarder.py
type: module
file_path: gateway/proxy/forwarder.py
tags: [proxy, forwarder, http, retry, connection-pooling, openclaw]
related: [[pipeline.py]], [[http_proxy.py]], [[llm_proxy.py]]
status: documented
---

# forwarder.py

## Purpose
Forwards sanitized requests from the gateway to the OpenClaw backend service on the internal container network. Provides connection pooling, configurable retry logic, timeout handling, health checks, and a mock handler interface for unit testing without a live OpenClaw instance.

## Responsibilities
- Forward HTTP requests to the configured OpenClaw backend URL after pipeline processing
- Retry failed requests up to `max_retries` times with configurable delay
- Support aiohttp for real HTTP forwarding; gracefully return an error when aiohttp is not installed
- Provide a mock response handler (`set_response_handler`) for test isolation without network calls
- Track health state via periodic health checks against the backend's `/health` endpoint
- Accumulate forwarding statistics: total forwarded, total errors, last forward time

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ForwarderConfig` | Dataclass | Configuration: target URL, timeout, retry count, retry delay, health check path and interval, max connections |
| `ForwardResult` | Dataclass | Result of a forward attempt: success flag, status code, body, headers, error, retry count, latency |
| `HTTPForwarder` | Class | Main forwarder with retry logic, health tracking, and optional mock handler |

## Function Details

### HTTPForwarder.forward(path, body, headers, method)
**Purpose:** Attempt to forward a request to `{target_url}{path}`. Retries on exception up to `max_retries` times. Uses mock handler when set; uses aiohttp otherwise.
**Parameters:** `path` (str), `body` (str), `headers` (dict), `method` (str, default "POST").
**Returns:** `ForwardResult`.

### HTTPForwarder.health_check()
**Purpose:** Send a GET to `health_check_path` and update `_healthy` state.
**Returns:** `bool` — True if backend responded with 2xx.

### HTTPForwarder.set_response_handler(handler)
**Purpose:** Inject a mock callable `(path, body) -> (status, response)` for testing. When set, all `forward()` calls use this handler instead of making real HTTP requests.

### HTTPForwarder.get_stats()
**Purpose:** Return operational statistics.
**Returns:** Dict with healthy flag, total_forwarded, total_errors, last_forward_time, last_health_check, target_url.

## Configuration / Environment Variables
- `ForwarderConfig.target_url` — default `http://openclaw:3000`
- `ForwarderConfig.timeout_seconds` — default 30.0
- `ForwarderConfig.max_retries` — default 3
- `ForwarderConfig.retry_delay_seconds` — default 1.0
- `ForwarderConfig.health_check_path` — default `/health`
- `ForwarderConfig.max_connections` — default 20 (informational; enforced by aiohttp session if configured)

## Related
- [[pipeline.py]]
- [[http_proxy.py]]
- [[llm_proxy.py]]
