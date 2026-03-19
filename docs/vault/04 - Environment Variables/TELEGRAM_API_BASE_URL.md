---
title: TELEGRAM_API_BASE_URL
type: env-var
tags: [telegram, proxy, routing]
related: [Proxy Layer/telegram_proxy.py, Configuration/All Environment Variables, ANTHROPIC_BASE_URL]
status: documented
---

# TELEGRAM_API_BASE_URL

## Description

Overrides the base URL for all Telegram Bot API calls from the OpenClaw bot. Routes them through the gateway for security scanning and PII redaction.

## Value

```
http://gateway:8080/telegram-api
```

## Effect

All Telegram API calls go to `http://gateway:8080/telegram-api/bot<token>/sendMessage` instead of `https://api.telegram.org/bot<token>/sendMessage`.

The gateway's Telegram proxy handler (`/telegram-api/*`) receives the request, scans it for PII, logs it to the audit ledger, and forwards to the real Telegram API.

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
```

## SDK Patch

`docker/scripts/patch-telegram-sdk.sh` patches the Telegram SDK at build time to use `$TELEGRAM_API_BASE_URL`.

## Related Notes

- [[Proxy Layer/telegram_proxy.py|telegram_proxy.py]] — Gateway handler
- [[TELEGRAM_BOT_TOKEN]] — The bot token used with this URL
- [[Configuration/All Environment Variables]] — All env vars
