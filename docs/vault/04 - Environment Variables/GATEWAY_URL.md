---
title: GATEWAY_URL
type: env-var
tags: [gateway, routing, configuration]
related: [Configuration/All Environment Variables, ANTHROPIC_BASE_URL, GATEWAY_AUTH_TOKEN]
status: documented
---

# GATEWAY_URL

## Description

General-purpose gateway URL used by external clients (iOS Shortcuts, browser extension, management tools) to reach the gateway API. Distinct from `ANTHROPIC_BASE_URL` which is the bot-to-gateway routing.

## Typical Value

```
# Local access
http://localhost:8080

# Tailscale access (from iOS Shortcuts)
http://agentshroud.tail240ea8.ts.net:8080
```

## Usage Contexts

| Client | URL used |
|--------|---------|
| iOS Shortcuts | Tailscale URL (set in `agentshroud.yaml` `shortcuts.endpoint`) |
| Browser extension | Direct localhost URL |
| Management scripts | Localhost URL |
| Bot container | `http://gateway:8080` (internal Docker DNS) |

## Configuration

Set in `agentshroud.yaml`:
```yaml
shortcuts:
  endpoint: ""   # Set to Tailscale URL during setup
```

## Related Notes

- [[ANTHROPIC_BASE_URL]] — Bot-specific routing URL
- [[GATEWAY_AUTH_TOKEN]] — Auth token required for all requests
- [[Configuration/All Environment Variables]] — All env vars
- [[Runbooks/First Time Setup]] — Setting up Tailscale endpoint
