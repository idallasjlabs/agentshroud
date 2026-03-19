---
title: TELEGRAM_API_BASE_URL
type: env-var
tags: [#type/env-var, #status/critical]
required: true
default: "none"
related: ["[[telegram_proxy]]", "[[patch-telegram-sdk.sh]]", "[[agentshroud-bot]]", "[[Photo Download Failure]]"]
status: active
last_reviewed: 2026-03-09
---

# TELEGRAM_API_BASE_URL

## What It Controls

Routes all Telegram Bot API calls from the bot through the gateway instead of directly to `api.telegram.org`. This enables the gateway to inspect, log, and filter all Telegram traffic — both API method calls and file downloads.

## Expected Format

URL string (no trailing slash)

```
http://gateway:8080/telegram-api
```

## Effect If Missing

The grammY SDK falls back to `https://api.telegram.org` directly. On the isolated network, this times out — the bot cannot send or receive Telegram messages.

## Effect If Wrong Format

- Wrong host (e.g., `http://localhost:8080/telegram-api`) — connection refused (bot is not on loopback network)
- Missing `/telegram-api` suffix — requests route to wrong gateway endpoint, 404

## Where It Is Set

`docker/docker-compose.yml` bot service:
```yaml
environment:
  - TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
```

## Used In

| File | How |
|------|-----|
| [[patch-telegram-sdk.sh]] | Injected into grammY `apiRoot` and OpenClaw dist file download URL |
| OpenClaw dist (post-patch) | `${process.env.TELEGRAM_API_BASE_URL}/file/bot<token>/<path>` |
| grammY SDK (post-patch) | `process.env.TELEGRAM_API_BASE_URL \|\| "https://api.telegram.org"` |

## Why Both Patches Are Needed

1. **grammY patch** — covers API method calls (sendMessage, getUpdates, etc.)
2. **OpenClaw dist patch** — covers `downloadAndSaveTelegramFile()` which has a separate hardcoded URL

Node.js native `fetch()` does NOT respect `HTTPS_PROXY`, so proxy-level interception is insufficient — source-level patching is required.

> [!DANGER] Critical — without this env var AND both SDK patches applied, photo uploads will fail with "Failed to download media" and Telegram connectivity may be broken.

See [[Photo Download Failure]] for the full error and fix.
