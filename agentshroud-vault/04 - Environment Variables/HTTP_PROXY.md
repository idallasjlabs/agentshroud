---
title: HTTP_PROXY / HTTPS_PROXY
type: env-var
tags: [#type/env-var, #status/critical]
required: true
default: "none"
related: ["[[agentshroud-bot]]", "[[egress_filter]]", "[[patch-telegram-sdk.sh]]", "[[Architecture Overview]]"]
status: active
last_reviewed: 2026-03-09
---

# HTTP_PROXY / HTTPS_PROXY

## What They Control

Routes all outbound HTTP/HTTPS traffic from the bot through the gateway's HTTP CONNECT proxy on port 8181. This gives the gateway visibility and control over all bot egress.

## Expected Format

```
http://gateway:8181
```

## Effect If Missing

The bot attempts direct HTTP connections. Since `agentshroud-isolated` has no internet routing, connections to external services time out.

## Important Limitation

> [!WARNING] Node.js native `fetch()` does NOT respect `HTTP_PROXY` / `HTTPS_PROXY`.
> Only Node.js code that uses proxy-aware HTTP clients (e.g., `node-fetch` with a proxy agent, `axios` with proxy config, or the `undici` client with proxy settings) will honor these variables.
>
> OpenClaw's Telegram file download code uses native `fetch()` — it ignores these variables. This is why [[patch-telegram-sdk.sh]] was needed to patch the URL at the source level.

## What DOES Respect These Variables

- `curl` and `wget` (used in shell scripts, including `start.sh` Telegram notifications)
- Python `httpx` and `requests` (gateway uses these internally)
- Most npm packages that use `node-fetch` or `got` with proper proxy config

## Where They Are Set

`docker/docker-compose.yml` bot service:
```yaml
environment:
  - HTTP_PROXY=http://gateway:8181
  - HTTPS_PROXY=http://gateway:8181
  - NO_PROXY=gateway,localhost,127.0.0.1
```

## `NO_PROXY`

Bypasses proxy for direct connections to the gateway itself (e.g., bot calling `/chat` on the gateway). Prevents infinite proxy loops.

## Used In

- All proxy-aware HTTP clients in the bot container
- Gateway validates origin IPs: only `_PROXY_ALLOWED_NETWORKS` may connect
