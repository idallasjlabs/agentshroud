---
title: telegram_proxy.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/proxy/telegram_proxy.py
tags: [#type/module, #status/critical]
related: ["[[main]]", "[[pipeline]]", "[[patch-telegram-sdk.sh]]", "[[Photo Download Failure]]", "[[TELEGRAM_API_BASE_URL]]"]
status: active
last_reviewed: 2026-03-09
---

# telegram_proxy.py — Telegram Bot API Reverse Proxy

## Purpose

Acts as a man-in-the-middle between OpenClaw and Telegram's Bot API. Every Telegram API call (inbound getUpdates, outbound sendMessage, file downloads) routes through this class.

## Architecture

```
Bot (grammY SDK)
    │  TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
    ▼
Gateway /telegram-api/bot<token>/<method>
    │
    ├── Inbound (getUpdates)
    │       ├── RBAC check (owner vs collaborator)
    │       ├── Collaborator: rate limit, command filter, disclosure notice
    │       ├── process_inbound() — PromptGuard + PII scan
    │       └── Forward to bot /webhook
    │
    └── Outbound (sendMessage, sendPhoto, etc.)
            ├── is_system=True → skip filtering (startup/shutdown msgs)
            ├── process_outbound() — PII + PromptProtection scan
            └── Forward to api.telegram.org
```

## Class: `TelegramAPIProxy`

### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `pipeline` | `SecurityPipeline` | Security pipeline for scanning |
| `middleware_manager` | `MiddlewareManager` | Tool result scanner |
| `sanitizer` | `PIISanitizer` | PII redaction |

### Method: `proxy_request(bot_token, method, body, content_type, is_system, path_prefix)`

The core proxy method. Called for every Telegram API request.

| Parameter | Type | Description |
|-----------|------|-------------|
| `bot_token` | `str` | Telegram bot token from URL |
| `method` | `str` | API method name (e.g., `sendMessage`, `getUpdates`) |
| `body` | `bytes` | Request body |
| `content_type` | `str` | Content-Type header |
| `is_system` | `bool` | If True, skip outbound filtering |
| `path_prefix` | `str` | `""` for methods, `"file/"` for file downloads |

**File download routing:**
```python
url = f"{TELEGRAM_API_BASE}/file/bot{bot_token}/{method}"
# vs. regular API:
url = f"{TELEGRAM_API_BASE}/bot{bot_token}/{method}"
```

The `path_prefix` parameter selects which URL pattern is used. This is how `/telegram-api/file/bot<token>/<path>` correctly routes to `api.telegram.org/file/bot<token>/<path>`.

### Method: `_sanitize_reason(reason) → str`

Strips internal Python module paths and file paths from block reasons before they are shown to users. Prevents infrastructure disclosure.

```python
# Removes: "gateway.security.module_name" → "[internal]"
# Removes: "/app/gateway/security/module.py line 42" → ""
```

## RBAC Logic

```python
is_owner = str(user_id) == str(self._rbac.owner_user_id)
is_collaborator = str(user_id) in [str(x) for x in self._rbac.collaborator_user_ids]
```

- **Owner:** full access, no rate limits, no command filtering
- **Collaborator:** 200 msg/hr rate limit, `_COLLABORATOR_BLOCKED_COMMANDS` filtered, disclosure notice on first message
- **Unknown:** treated as collaborator (fail-open for usability; access still filtered)

## Blocked Commands (Collaborators)

```python
_COLLABORATOR_BLOCKED_COMMANDS = {
    "/skill", "/1password", "/op", "/exec", "/run", "/cron",
    "/ssh", "/admin", "/config", "/secret", "/key", "/token",
    "/memory", "/reset", "/kill", "/restart", "/update",
}
```

Collaborators attempting these commands receive the disclosure message instead.

## System Notification Bypass

The bot's `start.sh` sends startup/shutdown notifications via:
```sh
curl -H "X-AgentShroud-System: 1" http://gateway:8080/telegram-api/...
```

In `main.py`, this header sets `is_system=True`, which causes `proxy_request()` to skip all outbound content filtering. This is appropriate because these are shell-script admin messages, not LLM output.

## Known Issues / Recent Fixes

> [!NOTE] Photo Download Fix (2026-03-09)
> OpenClaw's `downloadAndSaveTelegramFile()` used a hardcoded `https://api.telegram.org/file/...` URL — this bypassed the proxy and timed out on the isolated network. Fixed by [[patch-telegram-sdk.sh]] which rewrites all dist files to use `${TELEGRAM_API_BASE_URL}`. The `path_prefix="file/"` parameter in this class handles the correct URL routing.

## Environment Variables Used

- `TELEGRAM_BOT_TOKEN` — used as fallback if not available via Docker secret
- Reads `RBACConfig` (from `gateway/security/rbac_config.py`) for owner/collaborator IDs

## Related

- [[patch-telegram-sdk.sh]] — ensures bot actually sends file downloads to gateway
- [[Photo Download Failure]] — error and fix documentation
- [[TELEGRAM_API_BASE_URL]] — env var that routes bot to gateway
- [[pipeline]] — security pipeline called for every message
