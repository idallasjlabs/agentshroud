---
title: llm_proxy.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/proxy/llm_proxy.py
tags: [#type/module, #status/critical]
related: ["[[pipeline]]", "[[lifespan]]", "[[main]]", "[[ANTHROPIC_BASE_URL]]"]
status: active
last_reviewed: 2026-03-09
---

# llm_proxy.py — Anthropic API Proxy with Streaming Filter

## Purpose

Intercepts all Anthropic API calls from the bot (`ANTHROPIC_BASE_URL=http://gateway:8080`). Forwards requests to `api.anthropic.com`, receives SSE streaming responses, buffers the full stream, runs the outbound security pipeline, and returns the (possibly sanitized/blocked) stream to the bot.

## Responsibilities

- Accept Anthropic SDK HTTP requests at `/v1/{path}`
- Forward to `api.anthropic.com` with original headers (minus Host)
- Buffer full SSE response stream before processing
- Run `pipeline.process_outbound()` on buffered content
- For BLOCK: return synthetic SSE with error message
- For REDACT: rebuild SSE stream with sanitized content in a single delta
- Propagate `X-AgentShroud-User-Id` header to middleware for user-scoped decisions

## Key Method: `handle_request(request) → StreamingResponse`

Entry point called from `main.py` for every `/v1/` request.

1. Extract `X-AgentShroud-User-Id` header → stored in `request_data` for middleware
2. Strip `Host` header (would break upstream routing)
3. Forward to `https://api.anthropic.com/v1/<path>`
4. Receive SSE stream → buffer via `_filter_outbound_streaming()`
5. Return processed stream

## Key Method: `_filter_outbound_streaming(response_bytes) → bytes`

Buffers the complete SSE event stream and runs security pipeline:

```
Buffer all SSE events
    │
    ▼
pipeline.process_outbound(full_content)
    │
    ├── FORWARD → return original buffered stream
    ├── REDACT  → extract text, sanitize, rebuild as single content_block_delta SSE
    └── BLOCK   → synthetic SSE: {"type":"content_block_delta","delta":{"type":"text_delta","text":"[BLOCKED]..."}}
```

This ensures the full LLM response is inspected before any content reaches the bot.

## Synthetic SSE Format (BLOCK)

```
event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "[Content blocked by AgentShroud security policy]"}}

event: message_stop
data: {"type": "message_stop"}
```

## Environment Variables Used

- [[ANTHROPIC_BASE_URL]] — NOT read here; the bot sets this to point to the gateway. The proxy itself always forwards to `api.anthropic.com`.
- `X-AgentShroud-User-Id` — request header, not an env var

## Related

- [[pipeline]] — `process_outbound()` is the core scan
- [[ANTHROPIC_BASE_URL]] — what routes bot traffic here
- [[main]] — mounts this at `/v1/{path}`
- [[lifespan]] — initializes `LLMProxy` with wired pipeline
