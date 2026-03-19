---
title: http_proxy.py
type: module
file_path: gateway/proxy/http_proxy.py
tags: [proxy, http-connect, egress, allowlist, tcp-tunnel, network-security]
related: [[web_proxy.py]], [[web_config.py]], [[forwarder.py]]
status: documented
---

# http_proxy.py

## Purpose
Implements an asyncio HTTP CONNECT proxy server that intercepts all outbound TCP connections from the AI agent. By setting `HTTP_PROXY` / `HTTPS_PROXY` environment variables on the agent container to point at this server (port 8181), every outbound connection must be validated against a domain allowlist before a TCP tunnel is established.

## Responsibilities
- Listen on `0.0.0.0:8181` for HTTP CONNECT tunnel requests
- Parse the `CONNECT host:port HTTP/1.1` request line and consume all request headers
- Validate the target domain+port against the `WebProxy` allowlist before tunneling
- Return `403 Forbidden` for blocked domains, `502 Bad Gateway` on connection failure
- Relay raw bytes bidirectionally between the client and the target once a tunnel is established
- Track statistics: total, allowed, and blocked tunnel attempts with a rolling recent-connection log (100 entries)

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `HTTPConnectProxy` | Class | Asyncio TCP server implementing HTTP CONNECT with domain allowlist enforcement |
| `ALLOWED_DOMAINS` | List | Default domain allowlist used when no `WebProxy` is injected |

## Function Details

### HTTPConnectProxy.start()
**Purpose:** Start the asyncio TCP server on the configured host/port.
**Returns:** None. Server runs until `stop()` is called.

### HTTPConnectProxy.stop()
**Purpose:** Close the server socket and wait for it to drain.

### HTTPConnectProxy._handle_client(reader, writer)
**Purpose:** Top-level connection handler; wraps `_process_connect()` with error handling and ensures writer is closed.

### HTTPConnectProxy._process_connect(reader, writer)
**Purpose:** Full CONNECT request processing: parse request line, drain headers, validate method, parse host:port, check domain against allowlist, establish TCP tunnel or return error response.

### HTTPConnectProxy._relay(reader, writer)
**Purpose:** Static coroutine; copies bytes from one stream to another in 64KB chunks until EOF. Used in both directions simultaneously via `asyncio.gather()`.
**Parameters:** `reader` (StreamReader), `writer` (StreamWriter).

### HTTPConnectProxy.get_stats()
**Purpose:** Return traffic statistics.
**Returns:** Dict with total, allowed, blocked counts, and a list of up to 20 recent connection records.

## Default Allowlist
```
api.openai.com
api.anthropic.com
api.telegram.org
oauth2.googleapis.com
www.googleapis.com
gmail.googleapis.com
*.github.com
*.githubusercontent.com
```

## Configuration / Environment Variables
- `host` (default: `0.0.0.0`), `port` (default: 8181) — set at construction
- `HTTP_PROXY` / `HTTPS_PROXY` — must be set on the agent container to `http://gateway:8181`
- Domain allowlist configured via `WebProxyConfig.allowed_domains` injected through `WebProxy`
- Request header read timeout: 10 seconds; tunnel connect timeout: 10 seconds

## Related
- [[web_proxy.py]]
- [[web_config.py]]
- [[forwarder.py]]
