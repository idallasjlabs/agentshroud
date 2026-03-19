---
title: httpx
type: dependency
tags: [#type/dependency, #status/active]
related: ["[[llm_proxy]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# httpx

**Version:** `>=0.28.0,<1.0.0`
**Type:** Async HTTP client

## What It Does

Modern async HTTP client for Python. Used by the gateway to make outbound HTTP requests to the Anthropic API, Telegram API, and other services.

## Where It's Used

- [[llm_proxy]] — forwards requests to `api.anthropic.com`
- `telegram_egress_notify.py` — sends Telegram alerts on egress events
- `approval_queue/enhanced_queue.py` — Telegram notifications for approval requests

## Key Usage Pattern

```python
async with httpx.AsyncClient() as client:
    response = await client.post(
        "https://api.anthropic.com/v1/messages",
        headers=request.headers,
        content=await request.body(),
    )
```

## What Breaks If Missing

LLM proxy cannot forward requests. Gateway starts but LLM calls fail.
