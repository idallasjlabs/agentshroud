---
title: web_proxy.py
type: module
file_path: gateway/proxy/web_proxy.py
tags: [proxy, web, ssrf, dns-filter, egress-monitor, rate-limiting, audit]
related: [[url_analyzer.py]], [[web_content_scanner.py]], [[web_config.py]], [[http_proxy.py]]
status: documented
---

# web_proxy.py

## Purpose
Intercepts and audits all outbound HTTP traffic from the OpenClaw agent. Applies a layered security policy: SSRF is always a hard block; domain policy (allowlist or denylist), DNS filtering, and rate limiting are hard blocks; prompt injection, PII findings, and browser/OAuth flags are soft flags that annotate the result without blocking.

## Responsibilities
- Pre-flight check all outbound requests via `check_request()` before the HTTP call is made
- Apply DNS security filtering (fail-closed on error) for every request
- Hard-block SSRF attempts (private/reserved IPs, localhost variants) via `URLAnalyzer`
- Apply domain policy: allowlist mode (default-deny) or denylist mode (default-allow)
- Apply per-domain rate limiting using a sliding-window `RateLimiter`
- Flag browser security and OAuth concerns without blocking
- Post-response scan via `scan_response()` for prompt injection, PII, suspicious content types, and response size violations
- Record all traffic to the hash chain audit log
- Record egress events to `EgressMonitor`
- Track per-category statistics for all block and flag outcomes

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ProxyAction` | Enum | ALLOW, FLAG, BLOCK |
| `WebProxyResult` | Dataclass | Full result: URL, action, block reason, URL findings, content findings, injection score, audit info, security headers |
| `RateLimiter` | Class | In-memory sliding-window per-domain rate limiter (max 10,000 tracked domains) |
| `WebProxy` | Class | Main web traffic proxy; wires together URL analysis, DNS filter, content scanner, egress monitor |

## Function Details

### WebProxy.check_request(url, method, headers)
**Purpose:** Pre-flight security check for an outbound HTTP request. Hard-blocks SSRF and denied domains; soft-flags everything else. Returns immediately after the first hard block.
**Parameters:** `url` (str), `method` (str, default "GET"), `headers` (dict).
**Returns:** `WebProxyResult` — check `.blocked` before proceeding with the actual request.

### WebProxy.scan_response(url, body, content_type, status_code, response_size)
**Purpose:** Post-response content security scan. Flags suspicious content types, oversized responses, prompt injection, hidden content, and PII. Never blocks — always returns the content for the agent to use.
**Parameters:** `url` (str), `body` (str), `content_type` (str), `status_code` (int), `response_size` (int).
**Returns:** `WebProxyResult` with content findings.

### WebProxy._audit(event_type, url, metadata)
**Purpose:** Append an event to the hash chain audit log.
**Returns:** Entry ID string, or None if no audit chain is configured.

### RateLimiter.check(domain, rpm_limit)
**Purpose:** Check if a domain is within its per-minute request budget. Evicts stale domains when the tracked-domain cap is reached.
**Returns:** `bool` — True if allowed.

## Security Check Order (check_request)
1. Passthrough mode check (skip all if enabled)
2. URL analysis via `URLAnalyzer`
3. DNS security filter (fail-closed)
4. SSRF hard block
5. Domain policy (allowlist or denylist)
6. Rate limit check
7. URL findings (flag only)
8. Browser security check (fail-closed for HIGH/CRITICAL; flag for MEDIUM)
9. OAuth/auth header flag

## Configuration / Environment Variables
- Config injected via `WebProxyConfig` (see [[web_config.py]])
- `passthrough_mode` — bypass all checks; still logs
- DNS filter, network validator, egress monitor, browser security, OAuth validator all initialized with defaults at construction

## Related
- [[url_analyzer.py]]
- [[web_content_scanner.py]]
- [[web_config.py]]
- [[http_proxy.py]]
- [[pipeline.py]]
