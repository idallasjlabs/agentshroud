---
title: httpx
type: dependency
tags: [http, networking, async, python]
related: [Dependencies/All Dependencies, Proxy Layer/llm_proxy.py, Proxy Layer/telegram_proxy.py]
status: documented
---

# httpx

**Package:** `httpx`
**Version:** ≥0.28.0,<1.0.0
**Used in:** All proxy modules that make outbound HTTP requests

## Purpose

Async HTTP client library. Used throughout the proxy layer to forward requests to external APIs. `httpx` is preferred over `requests` because it supports async/await, enabling non-blocking proxy operations inside FastAPI.

## Where Used

| Module | Usage |
|--------|-------|
| `gateway/proxy/llm_proxy.py` | Forward LLM API requests to Anthropic/OpenAI |
| `gateway/proxy/telegram_proxy.py` | Forward Telegram Bot API calls |
| `gateway/proxy/http_proxy.py` | HTTP CONNECT proxy forwarding |
| `gateway/proxy/web_proxy.py` | Web content fetching |
| `gateway/ingest_api/main.py` | Forwarding requests to OpenClaw agent |

## Key Features Used

| Feature | Usage |
|---------|-------|
| `AsyncClient` | Non-blocking HTTP client for proxy forwarding |
| `follow_redirects=True` | Following API redirects transparently |
| `timeout=httpx.Timeout(...)` | Per-request timeouts to prevent hanging |
| Custom headers | Injecting/removing authentication headers |

## Security Note

Outgoing requests from the gateway are filtered by `egress_filter.py` before `httpx` executes them. The allowlist check happens at the request routing layer, not inside httpx itself.

## Related Notes

- [[Proxy Layer/llm_proxy.py|llm_proxy.py]] — Primary usage for LLM forwarding
- [[Security Modules/egress_filter.py|egress_filter.py]] — Validates destinations before httpx makes the request
- [[Dependencies/All Dependencies]] — Full dependency list
