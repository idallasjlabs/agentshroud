---
title: telegram_proxy.py
type: module
file_path: gateway/proxy/telegram_proxy.py
tags: [proxy, telegram, bot-api, pii, outbound-filter, middleware]
related: [[llm_proxy.py]], [[pipeline.py]], [[http_proxy.py]]
status: documented
---

# telegram_proxy.py

## Purpose
Implements a man-in-the-middle security proxy for Telegram Bot API calls. The bot connects to the gateway at `http://gateway:8080/telegram-api/bot<token>/<method>` instead of `https://api.telegram.org/...`. Inbound messages from users are scanned for threats; outbound bot responses are filtered for credential leaks and XML artifacts.

## Responsibilities
- Forward any Telegram Bot API request to `https://api.telegram.org` after applying security checks
- Filter outbound `sendMessage`/`editMessageText`/`sendPhoto`/`sendDocument` requests: strip Claude XML internal blocks and block credential patterns
- Scan inbound `getUpdates` responses: run each message through middleware (RBAC, context guard, multi-turn tracking) and PII sanitization
- Replace blocked message text with a `[BLOCKED BY AGENTSHROUD: reason]` notice rather than dropping the update
- Add PII redaction metadata fields (`_agentshroud_pii_redacted`, `_agentshroud_redactions`) to sanitized messages
- Track statistics: total requests, messages scanned, sanitized, blocked, and outbound filtered

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `TelegramAPIProxy` | Class | Main proxy class; wraps all Telegram API calls with security scanning |

## Function Details

### TelegramAPIProxy.proxy_request(bot_token, method, body, content_type)
**Purpose:** Top-level handler for a single Telegram API call. Routes to outbound filtering if the method writes content, forwards to the real API, then routes to inbound filtering if the method reads updates.
**Parameters:** `bot_token` (str), `method` (str), `body` (bytes), `content_type` (str).
**Returns:** Parsed JSON dict from Telegram API, with message text potentially modified.

### TelegramAPIProxy._filter_outbound(body, content_type)
**Purpose:** For JSON-encoded bot send methods: strip Claude XML blocks from message text and redact credential patterns before forwarding.
**Parameters:** `body` (bytes), `content_type` (str).
**Returns:** Potentially modified `body` (bytes).

### TelegramAPIProxy._filter_inbound_updates(response_data)
**Purpose:** Iterate over each update in a `getUpdates` response, run each message text through the middleware manager and PII sanitizer, and replace text in-place with sanitized or blocked versions.
**Parameters:** `response_data` (dict) — full Telegram API response.
**Returns:** Modified `response_data` dict.

### TelegramAPIProxy._forward_to_telegram(url, body, content_type)
**Purpose:** Execute the HTTP request to the real Telegram API using `urllib.request` in a thread pool executor (non-blocking).
**Parameters:** `url` (str), `body` (bytes), `content_type` (str).
**Returns:** Parsed JSON dict.

### TelegramAPIProxy.get_stats()
**Purpose:** Return cumulative traffic statistics.
**Returns:** Dict with total_requests, messages_scanned, messages_sanitized, messages_blocked, outbound_filtered.

## Configuration / Environment Variables
- `TELEGRAM_API_BASE` constant = `https://api.telegram.org` (not configurable at runtime)
- Bot token provided per-call via `proxy_request(bot_token, ...)`
- `pipeline`, `middleware_manager`, `sanitizer` injected at construction time

## Methods Filtered (Outbound)
- `sendMessage`, `editMessageText`, `sendPhoto`, `sendDocument`, `copyMessage`, `forwardMessage`

## Methods Filtered (Inbound)
- `getUpdates` — scans all returned message texts

## Related
- [[llm_proxy.py]]
- [[pipeline.py]]
- [[http_proxy.py]]
