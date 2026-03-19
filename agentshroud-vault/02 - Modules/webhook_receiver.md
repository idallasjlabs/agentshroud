---
title: webhook_receiver.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/proxy/webhook_receiver.py
tags: [#type/module, #status/active]
related: ["[[telegram_proxy]]", "[[pipeline]]", "[[main]]"]
status: active
last_reviewed: 2026-03-09
---

# webhook_receiver.py — Inbound Telegram Webhook Processing

## Purpose

Handles incoming Telegram webhooks — validates signatures, processes update objects, and forwards sanitized messages to the bot's webhook endpoint.

## Responsibilities

- Validate Telegram webhook signatures (`validate_signature()`)
- Parse incoming update objects
- Extract user IDs and message content
- Apply pipeline inbound scan
- Forward sanitized update to bot at `BotConfig.webhook_path` (`/webhook`)

## `validate_signature()`

Validates the `X-Telegram-Bot-Api-Secret-Token` header against a configured secret token. This prevents unauthorized parties from injecting fake webhook updates.

> [!WARNING] UNCERTAIN
> The `owner_user_id` is read from config. Verify that `RBACConfig` and the webhook receiver use the same source of truth for owner identification.

## Webhook vs Long-Poll

AgentShroud can operate in two modes:

| Mode | Description |
|------|-------------|
| **Long-poll** (current) | Gateway polls `getUpdates` directly, processes updates inline |
| **Webhook** | Telegram pushes updates to gateway's webhook endpoint |

The current production setup uses long-poll. The `WebhookReceiver` is available for webhook mode.

## Related

- [[telegram_proxy]] — long-poll processing (current mode)
- [[pipeline]] — inbound scan applied to webhook messages
- [[main]] — mounts webhook receiver if configured
