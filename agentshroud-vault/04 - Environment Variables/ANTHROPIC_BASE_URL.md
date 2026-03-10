---
title: ANTHROPIC_BASE_URL
type: env-var
tags: [#type/env-var, #status/critical]
required: true
default: "none"
related: ["[[llm_proxy]]", "[[agentshroud-bot]]", "[[patch-telegram-sdk.sh]]"]
status: active
last_reviewed: 2026-03-09
---

# ANTHROPIC_BASE_URL

## What It Controls

Routes all Anthropic SDK API calls from the bot through the gateway's LLM proxy at `/v1/`. This enables inspection, filtering, and audit of all LLM requests and responses.

## Expected Format

URL string (no trailing slash, no `/v1` suffix — the SDK appends that itself)

```
http://gateway:8080
```

## Effect If Missing

The Anthropic SDK uses `https://api.anthropic.com` directly. On the isolated network, this times out — the bot cannot make LLM calls.

## Effect If Wrong Format

- Wrong host — connection refused
- With `/v1` suffix — double `/v1/v1/` in request path, API calls fail

## Where It Is Set

`docker/docker-compose.yml` bot service:
```yaml
environment:
  - ANTHROPIC_BASE_URL=http://gateway:8080
```

Also patched directly into the Anthropic SDK by [[patch-telegram-sdk.sh]] (the `patch-anthropic-sdk.sh` component). The SDK's base URL is overridden at the source level as a belt-and-suspenders approach.

## Used In

| File | How |
|------|-----|
| Anthropic SDK (OpenClaw) | Used as API base URL for all Claude calls |
| `docker/bots/openclaw/patch-anthropic-sdk.sh` | Source-level URL override in SDK |
| [[llm_proxy]] | Receives requests routed here, forwards to `api.anthropic.com` |

> [!DANGER] Critical — if this is not set, the bot cannot call Claude. The bot and gateway are both broken.
