---
title: http_proxy.py
type: module
file_path: gateway/proxy/http_proxy.py
tags: [proxy, http-connect, egress, allowlist, tcp-tunnel, network-security, clamav, tcp-keepalive]
related: [[web_proxy.py]], [[web_config.py]], [[forwarder.py]], [[egress_filter.py]], [[clamav_scanner.py]]
status: documented
---

# http_proxy.py

## Purpose
Implements an asyncio HTTP CONNECT proxy server that intercepts all outbound TCP connections from AI agent containers. By setting `HTTP_PROXY` / `HTTPS_PROXY` environment variables on each agent container to `http://gateway:8181`, every outbound connection must be validated against a domain allowlist and the egress filter policy before a TCP tunnel is established.

## Responsibilities
- Listen on `0.0.0.0:8181` for HTTP CONNECT tunnel requests
- Parse the `CONNECT host:port HTTP/1.1` request line and consume all request headers
- Hard-block domains in `CONNECT_FORCE_BLOCK_DOMAINS` (e.g. `api.telegram.org`) regardless of any policy
- Bypass interactive egress approval for `SYSTEM_BYPASS_DOMAINS` (Slack, GitHub API) to avoid deadlocking the approval channel
- Validate all other domains through `EgressFilter` (interactive approval + policy engine), falling back to the static `WebProxy` allowlist when the filter is unavailable
- Return `403 Forbidden` for blocked domains; `502 Bad Gateway` after 3 failed connection attempts
- Enable TCP keepalive on both ends of every established tunnel to survive VPN idle-session drops
- Relay raw bytes bidirectionally: client→target via `_relay()`, target→client via `_relay_and_scan()`
- Sample the first 4 MB of every inbound download for ClamAV malware scanning (non-blocking)
- Track statistics: total, allowed, and blocked tunnel attempts with a rolling recent-connection log (100 entries) and a `clamav_infections` list

## Module-level Constants

| Constant | Type | Description |
|----------|------|-------------|
| `SYSTEM_BYPASS_DOMAINS` | `set[str]` | Domains that bypass interactive egress approval (Slack WebSocket/REST, GitHub API). **Does not** include `api.telegram.org`. |
| `CONNECT_FORCE_BLOCK_DOMAINS` | `set[str]` | Domains unconditionally blocked from direct CONNECT tunnels. Currently `{"api.telegram.org"}`. Takes priority over egress filter and system bypass. |
| `ALLOWED_DOMAINS` | `list[str]` | Default internet allowlist derived at import time from `PERMANENT_EGRESS_DOMAINS` minus `CONNECT_FORCE_BLOCK_DOMAINS`. Supplemented at startup with internal Docker/SSH targets from `agentshroud.yaml proxy.allowed_domains`. |

## Key Classes

| Name | Type | Description |
|------|------|-------------|
| `HTTPConnectProxy` | Class | Asyncio TCP server implementing HTTP CONNECT with domain allowlist enforcement, egress policy integration, ClamAV scanning, and TCP keepalive |

## Constructor Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `web_proxy` | auto-created | `WebProxy` instance using `mode="allowlist"` and `ALLOWED_DOMAINS` |
| `egress_filter` | `None` | `EgressFilter` for interactive approval + policy checks |
| `host` | `"0.0.0.0"` | Bind address |
| `port` | `8181` | Bind port |
| `ip_to_bot_registry` | `{}` | Pre-populated mapping of source IP → bot_id |
| `bot_hostnames` | `{}` | bot_id → Docker service hostname, used for lazy rDNS lookup |

## Internal State (`_stats`)

```python
{
    "total": int,               # all CONNECT requests received
    "allowed": int,             # tunnels established
    "blocked": int,             # tunnels denied
    "recent": list[dict],       # rolling window, max 100 entries
    "clamav_infections": list   # appended on ClamAV hit (key created on first hit)
}
```

Each `recent` entry: `{"timestamp": float, "host": str, "port": int, "allowed": bool, "block_reason": str}`.

Each `clamav_infections` entry: `{"host": str, "signatures": list[str], "timestamp": float}`.

## Function Details

### `HTTPConnectProxy.start()`
Start the asyncio TCP server on the configured host/port.
Returns `None`. Server runs until `stop()` is called.

### `HTTPConnectProxy.stop()`
Close the server socket and wait for it to drain.

### `HTTPConnectProxy.get_stats()`
Return traffic statistics.
**Returns:** Dict with `total`, `allowed`, `blocked` counts, and `recent` — a copy of up to **100** recent connection records.

> Note: the internal `_stats["recent"]` list stores up to 100 entries (trimmed when it exceeds 100). `get_stats()` returns `recent[:20]` as a caller-facing slice for API consumers.

### `HTTPConnectProxy._handle_client(reader, writer)`
Top-level connection handler. Wraps `_process_connect()` with `asyncio.TimeoutError` and general exception handling. Ensures `writer` is closed in a `finally` block.

### `HTTPConnectProxy._agent_id_for_peer(peer)`
Resolves a source IP address to a `bot_id` string for attribution in egress logs and stats.

**Resolution order:**
1. Direct lookup in `_ip_to_bot_registry` (pre-populated at startup)
2. Lazy reverse-DNS lookup via Docker's embedded DNS; matches against `_bot_hostnames`; caches result
3. Falls back to `"http_connect_proxy"` for unknown IPs (cache miss is also stored to avoid repeated rDNS)

### `HTTPConnectProxy._process_connect(reader, writer)`
Full CONNECT request lifecycle:

1. Identify `agent_id` from source IP via `_agent_id_for_peer()`
2. Read request line with 10 s timeout; return `408` on timeout
3. Validate method is `CONNECT`; return `405` otherwise
4. Parse `host:port` (defaults to port 443 if absent)
5. Apply domain classification:
   - `CONNECT_FORCE_BLOCK_DOMAINS` → immediate `403`, logged at `DEBUG` (expected/known)
   - `SYSTEM_BYPASS_DOMAINS` → allow, log decision to SOC egress history via `approval_queue.log_external_decision()`
   - `EgressFilter` present → call `check_async()`; if allowed, also check static allowlist as observability signal
   - `EgressFilter` absent → fall back to `WebProxy.check_request()`
6. Track stats; log unknown blocked hosts at `WARNING`, force-blocked hosts at `DEBUG`
7. Return `403` if blocked
8. Open TCP connection to target with **3 retry attempts** (back-off: 0.5 s, 1.5 s); return `502` after all attempts fail
9. Increment `allowed` counter; send `HTTP/1.1 200 Connection Established`
10. Set TCP keepalive on both tunnel sockets (see TCP Keepalive section)
11. Run `_relay()` (client→target) and `_relay_and_scan()` (target→client) concurrently via `asyncio.gather()`
12. Close target writer on completion

### `HTTPConnectProxy._relay(reader, writer, idle_timeout=120.0)` *(static)*
Copies bytes from `reader` to `writer` in 64 KB chunks until EOF.

- **Direction:** client → target
- **Idle timeout:** 120 seconds. If no data arrives within the timeout, the tunnel side is closed and a `DEBUG` log is emitted. Prevents stale connections from hanging the proxy when the remote peer stops sending without closing TCP.
- Exceptions are silently swallowed; `writer.close()` is called in `finally`.

### `HTTPConnectProxy._relay_and_scan(reader, writer, host, scan_limit=4*1024*1024)`
Copies bytes from `reader` to `writer` in 64 KB chunks until EOF, with ClamAV sampling.

- **Direction:** target → client
- **Idle timeout:** 120 seconds (same behaviour as `_relay`)
- **ClamAV sampling:** Accumulates the first `scan_limit` bytes (default 4 MB) into a buffer. Once the buffer reaches the limit, schedules `_clamav_scan_bytes()` as a background task (`asyncio.create_task`) and stops accumulating. If EOF is reached before the buffer is full, the partial buffer is still submitted for scanning.
- Scan is fire-and-forget — it does not block the relay.
- For TLS tunnels the scanner sees encrypted bytes; ClamAV returns clean (no false positives).

### `HTTPConnectProxy._clamav_scan_bytes(data: bytes, host: str)`
Writes `data` to a named temp file and runs ClamAV on it in a thread executor (`run_in_executor`) to avoid blocking the event loop.

**Behavior:**
- Imports `gateway.security.clamav_scanner.run_clamscan` at call time (avoids circular import at module load)
- If `infected_count > 0`: logs at `CRITICAL` with host and signature list; appends an entry to `self._stats["clamav_infections"]`
- If clean: logs at `DEBUG`
- If `clamscan` binary is unavailable (ClamAV sidecar not running): logs at `DEBUG` and silently degrades
- Always deletes the temp file in `finally`

## TCP Keepalive

After `200 Connection Established` is sent, keepalive is enabled on **both** the client-side and the target-side socket:

| Socket option | Value | Effect |
|---------------|-------|--------|
| `SO_KEEPALIVE` | 1 | Enable keepalive probes |
| `TCP_KEEPIDLE` | 60 s | Start probes after 60 s of idle |
| `TCP_KEEPINTVL` | 15 s | Send a probe every 15 s |
| `TCP_KEEPCNT` | 6 | Drop connection after 6 missed probes |

`TCP_KEEPIDLE`, `TCP_KEEPINTVL`, and `TCP_KEEPCNT` are set only if the platform exposes them (Linux; silently skipped on macOS). This prevents Cisco AnyConnect (and similar VPNs) from silently dropping idle TCP sessions (~10 min idle threshold), which was causing Slack Socket Mode WebSocket ping/pong timeouts.

## CONNECT Retry Logic

Before returning `502 Bad Gateway`, the proxy retries the upstream TCP connection up to **3 times**:

| Attempt | Delay before attempt |
|---------|---------------------|
| 1 | Immediate |
| 2 | 0.5 s |
| 3 | 1.5 s |

Each attempt has a 10 s connect timeout. This handles transient network hiccups (VPN reconnect, Colima networking blip) without immediately crashing OpenClaw's unhandled Bolt error path.

## Domain Policy Decision Tree

```
Incoming CONNECT host:port
        │
        ▼
Is host in CONNECT_FORCE_BLOCK_DOMAINS?  ──YES──► 403 (DEBUG log)
        │ NO
        ▼
Is host in SYSTEM_BYPASS_DOMAINS?  ──YES──► Allow + log to SOC egress history
        │ NO
        ▼
EgressFilter available?
   YES ──► check_async() ──DENY──► 403 (WARNING log)
        │               └─ALLOW─► also check WebProxy (observability only) → Allow
   NO  ──► WebProxy.check_request() ──BLOCKED──► 403 (WARNING log)
                                    └─ALLOWED─► Allow
```

## Configuration / Environment Variables

| Item | Value | Notes |
|------|-------|-------|
| Bind address | `0.0.0.0` | Configurable at construction |
| Bind port | `8181` | Configurable at construction |
| Agent env vars | `HTTP_PROXY=http://gateway:8181` | Must be set on each agent container |
| `NO_PROXY` | `gateway` | Prevents Telegram API calls from looping through the proxy |
| Request header read timeout | 10 s | Per-line timeout on CONNECT headers |
| Tunnel connect timeout | 10 s | Per retry attempt |
| Relay idle timeout | 120 s | Both `_relay` and `_relay_and_scan` |
| ClamAV scan limit | 4 MB | First 4 MB of target→client data |
| Domain allowlist | `PERMANENT_EGRESS_DOMAINS` minus `CONNECT_FORCE_BLOCK_DOMAINS` | Extended at startup from `agentshroud.yaml proxy.allowed_domains` |

## Security Notes

- `api.telegram.org` is in `CONNECT_FORCE_BLOCK_DOMAINS` and **cannot** be overridden by the egress filter or system bypass. The bot must use `TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api` to reach Telegram; this routes through the gateway's reverse proxy where the Slack bridge intercept lives. Allowing a direct tunnel would silently drop `sendMessage` responses.
- The ClamAV scan is a best-effort layer — it cannot decrypt TLS traffic. Its primary value is catching malware in cleartext (port 80) downloads.
- `clamav_infections` entries in `_stats` are in-memory only; they are lost on gateway restart.

## Related
- [[web_proxy.py]]
- [[web_config.py]]
- [[egress_filter.py]]
- [[clamav_scanner.py]]
- [[forwarder.py]]
