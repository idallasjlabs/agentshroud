---
title: patch-telegram-sdk.sh
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/docker/scripts/patch-telegram-sdk.sh
tags: [#type/module, #status/critical]
related: ["[[telegram_proxy]]", "[[Photo Download Failure]]", "[[TELEGRAM_API_BASE_URL]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# patch-telegram-sdk.sh — OpenClaw SDK Patching

## Purpose

Patches two hardcoded URLs in the OpenClaw/Node.js Telegram SDK stack so that ALL Telegram traffic (API calls AND file downloads) routes through the gateway, not directly to `api.telegram.org`.

Runs during the bot Docker image build (`RUN sh /tmp/patch-telegram-sdk.sh`).

## Why This Is Needed

The bot container is on the `agentshroud-isolated` network — no direct internet access. Two separate code paths need patching:

1. **grammY SDK** (`grammy/out/core/client.js`) — handles all API method calls (sendMessage, getUpdates, etc.)
2. **OpenClaw dist files** — `downloadAndSaveTelegramFile()` has a separate hardcoded URL for file downloads

Node.js native `fetch()` does **not** respect `HTTPS_PROXY`. A background task confirmed this:
```
HTTPS_PROXY: http://gateway:8181
Testing native fetch to api.telegram.org...
Error: The operation was aborted due to timeout
```

Therefore source-level URL patching is the only viable approach.

## Patch 1 — grammY `apiRoot`

**Target:** `$(npm root -g)/openclaw/node_modules/grammy/out/core/client.js`

**Replaces:**
```js
const apiRoot = (_a = options.apiRoot) !== null && _a !== void 0 ? _a : "https://api.telegram.org"
```

**With:**
```js
const apiRoot = process.env.TELEGRAM_API_BASE_URL || ((_a = options.apiRoot) !== null && _a !== void 0 ? _a : "https://api.telegram.org")
```

**Effect:** All grammY API calls use `TELEGRAM_API_BASE_URL` if set.

## Patch 2 — OpenClaw Dist File Download URL

**Target:** All `.js` files in `$(npm root -g)/openclaw/dist/` containing the hardcoded URL.

**Replaces:**
```js
https://api.telegram.org/file/bot${params.token}/${params.filePath}
```

**With:**
```js
${process.env.TELEGRAM_API_BASE_URL || "https://api.telegram.org"}/file/bot${params.token}/${params.filePath}
```

**Files patched during build (v2026.3.2):**
- `pi-embedded-CtM2Mrrj.js`
- `pi-embedded-DgYXShcG.js`
- `reply-DhtejUNZ.js` (discovered during build — bonus file)
- `subagent-registry-CkqrXKq4.js`

The glob approach (`for f in dist/*.js`) is hash-suffix agnostic — works across OpenClaw version bumps.

## Runtime Value

`TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api` (set in `docker-compose.yml`)

The gateway regex at `/telegram-api/bot{token}/{method}` handles both:
- API methods: `http://gateway:8080/telegram-api/bot<token>/sendMessage`
- File downloads: `http://gateway:8080/telegram-api/file/bot<token>/path/to/file`

The `path_prefix` parameter in [[telegram_proxy]] selects the correct upstream URL format.

## Verifying the Patch Applied

```bash
# Check inside the image (after build)
docker run --rm agentshroud-bot:latest \
  sh -c 'grep -rl "TELEGRAM_API_BASE_URL" /usr/local/lib/node_modules/openclaw/dist/'

# Check inside running container
docker exec agentshroud-bot \
  grep -c "TELEGRAM_API_BASE_URL" \
  /usr/local/lib/node_modules/openclaw/dist/pi-embedded-CtM2Mrrj.js
```

Should return counts > 0.

## Related

- [[telegram_proxy]] — the gateway endpoint that receives patched requests
- [[Photo Download Failure]] — the problem this patch solves
- [[TELEGRAM_API_BASE_URL]] — the env var that controls routing
- [[agentshroud-bot]] — the container where this patch runs
