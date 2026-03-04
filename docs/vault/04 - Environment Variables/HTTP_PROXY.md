---
title: HTTP_PROXY / HTTPS_PROXY
type: env-var
tags: [proxy, egress, networking]
related: [Proxy Layer/http_proxy.py, Configuration/All Environment Variables, Configuration/agentshroud.yaml]
status: documented
---

# HTTP_PROXY / HTTPS_PROXY

## Description

When set, routes all HTTP and HTTPS traffic from the bot container through the gateway's HTTP CONNECT proxy (port 8181). This is the network-layer enforcement of the egress allowlist.

## Value

```
HTTP_PROXY=http://gateway:8181
HTTPS_PROXY=http://gateway:8181
```

## Current Status

**Currently disabled** in `docker/docker-compose.yml` (commented out):
```yaml
# - HTTP_PROXY=http://gateway:8181   # DISABLED: enable in FINAL phase
# - HTTPS_PROXY=http://gateway:8181  # DISABLED: enable in FINAL phase
```

Egress control is currently enforced at the application layer via `ANTHROPIC_BASE_URL` and `TELEGRAM_API_BASE_URL` routing. Full network-layer enforcement via HTTP_PROXY is planned for the final production phase.

## When Enabled

With `HTTP_PROXY=http://gateway:8181`:
- All bot container HTTP/HTTPS traffic routes through `http_proxy.py`
- Gateway's domain allowlist (`proxy.allowed_domains`) enforced at network level
- Bot cannot make any direct internet connections
- Provides defense-in-depth alongside application-layer routing

## Gateway Proxy Port

Port 8181 — configured in `agentshroud.yaml`:
```yaml
proxy:
  mode: allowlist
  listen_port: 8181
```

## Related Notes

- [[Proxy Layer/http_proxy.py|http_proxy.py]] — HTTP CONNECT proxy implementation
- [[Configuration/agentshroud.yaml]] — `proxy.allowed_domains` list
- [[Security Modules/egress_filter.py|egress_filter.py]] — Application-layer egress enforcement
- [[Configuration/All Environment Variables]] — All env vars
