---
title: "Error: Failed to download media"
type: error
tags: [#type/error, #status/critical]
severity: high
related: ["[[telegram_proxy]]", "[[patch-telegram-sdk.sh]]", "[[TELEGRAM_API_BASE_URL]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# Error: Failed to download media

## Exact Error Message

Seen in Telegram when the bot processes a photo:
```
Failed to download media. Please try again.
```

Bot log:
```
Error: The operation was aborted due to timeout
    at fetch (...)
```

## What It Means

OpenClaw's `downloadAndSaveTelegramFile()` function tried to download a photo using a hardcoded `https://api.telegram.org/file/bot<token>/<path>` URL. The bot is on the `agentshroud-isolated` network with no direct internet access. The connection timed out.

## Root Cause

**Two separate patches are required for full Telegram routing:**

1. **grammY SDK patch** (covered by `patch-telegram-sdk.sh` Patch 1) — routes API method calls (sendMessage, getUpdates) through gateway. ✓
2. **OpenClaw dist patch** (covered by `patch-telegram-sdk.sh` Patch 2 — added 2026-03-09) — routes `downloadAndSaveTelegramFile()` through gateway. This was missing prior to the fix.

Node.js native `fetch()` (used by OpenClaw's file download) does NOT respect `HTTPS_PROXY`. Only source-level URL patching works.

## Which Module Throws It

`downloadAndSaveTelegramFile()` inside OpenClaw compiled dist files:
- `pi-embedded-CtM2Mrrj.js`
- `pi-embedded-DgYXShcG.js`
- `reply-DhtejUNZ.js`
- `subagent-registry-CkqrXKq4.js`

## Diagnostic Steps

```bash
# 1. Check if patch was applied inside the running image
docker exec agentshroud-bot \
  grep -c "TELEGRAM_API_BASE_URL" \
  /usr/local/lib/node_modules/openclaw/dist/pi-embedded-CtM2Mrrj.js
# Expected: 1 or more. If 0: patch not applied, rebuild needed.

# 2. Check TELEGRAM_API_BASE_URL is set in bot
docker exec agentshroud-bot env | grep TELEGRAM_API_BASE_URL
# Expected: http://gateway:8080/telegram-api

# 3. Check gateway is routing file downloads correctly
docker logs agentshroud-gateway --since 5m | grep "file/bot"

# 4. Check bot logs for the timeout
docker logs agentshroud-bot --since 5m | grep -i "timeout\|download\|media"
```

## Fix

The fix was committed in `3243782` (2026-03-09). Requires rebuilding the bot image:

```bash
# Rebuild bot image (no cache to ensure patches run)
docker compose -f docker/docker-compose.yml build bot --no-cache

# Verify patch applied
docker run --rm agentshroud-bot:latest \
  sh -c 'grep -rl "TELEGRAM_API_BASE_URL" /usr/local/lib/node_modules/openclaw/dist/'

# Restart with new image
docker compose -f docker/docker-compose.yml up -d bot

# Test: send a photo from owner Telegram account
```

## Prevention

- Any time `openclaw` npm package is upgraded, rebuild the bot image to re-apply patches
- The glob approach in `patch-telegram-sdk.sh` is hash-suffix agnostic — will patch new dist files automatically
- Verify patch after each bot image build:
  ```bash
  docker run --rm agentshroud-bot:latest \
    grep -c "TELEGRAM_API_BASE_URL" \
    /usr/local/lib/node_modules/openclaw/dist/pi-embedded-CtM2Mrrj.js
  ```

## Related

- [[patch-telegram-sdk.sh]] — the script that applies both patches
- [[telegram_proxy]] — gateway endpoint that handles file downloads (`path_prefix="file/"`)
- [[TELEGRAM_API_BASE_URL]] — the env var that routes requests
