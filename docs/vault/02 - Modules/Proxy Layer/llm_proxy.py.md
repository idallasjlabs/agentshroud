---
title: llm_proxy.py
type: module
file_path: gateway/proxy/llm_proxy.py
tags: [proxy, llm, anthropic, pii, prompt-injection, outbound-filter, api-proxy]
related: [[telegram_proxy.py]], [[pipeline.py]], [[forwarder.py]]
status: documented
---

# llm_proxy.py

## Purpose
Implements a reverse proxy between the AI agent client (OpenClaw) and the Anthropic API. The agent connects to `http://gateway:8080/v1/messages` (via `ANTHROPIC_BASE_URL` env var) instead of `https://api.anthropic.com`. Inbound user messages are scanned for PII and injection; outbound LLM responses are filtered for XML artifacts and credential leaks.

## Responsibilities
- Accept Anthropic-format `/v1/messages` requests and scan all user message content for PII and injection threats before forwarding
- Support multi-part message content (text blocks within structured content arrays)
- Forward requests to `https://api.anthropic.com` with only safe headers passed through
- For non-streaming responses: apply XML block stripping and credential blocking to LLM output text before returning it to the agent
- Streaming responses pass through without outbound filtering (content filtering only on non-stream)
- Track statistics: total requests, messages scanned, PII redacted count, injections blocked, responses filtered

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `LLMProxy` | Class | Main proxy class for Anthropic API intermediation |

## Function Details

### LLMProxy.proxy_messages(path, body, headers)
**Purpose:** Full request lifecycle: parse body → scan user messages (inbound) → forward to Anthropic → filter response (outbound, non-streaming).
**Parameters:** `path` (str), `body` (bytes), `headers` (dict[str, str]) — raw request headers.
**Returns:** `(status_code, response_headers, response_body)` tuple.

### LLMProxy._scan_inbound(text)
**Purpose:** Apply PII sanitization and middleware checks (injection detection, context guard) to a single user message text string.
**Parameters:** `text` (str).
**Returns:** Sanitized or blocked text. Blocked messages are replaced with `[MESSAGE BLOCKED BY AGENTSHROUD: reason]`.

### LLMProxy._filter_outbound(resp_body)
**Purpose:** Parse the Anthropic response JSON, iterate over text content blocks, apply XML block stripping and credential blocking to each.
**Parameters:** `resp_body` (bytes).
**Returns:** Potentially modified `resp_body` (bytes). Returns original on parse error.

### LLMProxy._forward_to_anthropic(url, body, headers)
**Purpose:** Forward the request to the real Anthropic API. Passes only safe headers: `authorization`, `x-api-key`, `anthropic-version`, `anthropic-beta`, `content-type`, `accept`.
**Parameters:** `url` (str), `body` (bytes), `headers` (dict).
**Returns:** `(status_code, response_headers, response_body)`. HTTPError responses are returned with their original status code rather than raised.

### LLMProxy.get_stats()
**Purpose:** Return cumulative proxy statistics.
**Returns:** Dict with total_requests, messages_scanned, pii_redacted, injections_blocked, responses_filtered.

## Configuration / Environment Variables
- `ANTHROPIC_API_BASE` constant = `https://api.anthropic.com` (not configurable at runtime)
- `ANTHROPIC_BASE_URL` — environment variable on the OpenClaw/agent side, set to `http://gateway:8080` to route through the proxy
- `pipeline`, `middleware_manager`, `sanitizer` injected at construction time
- HTTP request timeout: 120 seconds

## Header Pass-Through Policy
Only these headers are forwarded to Anthropic:
- `authorization`
- `x-api-key`
- `anthropic-version`
- `anthropic-beta`
- `content-type`
- `accept`

All other headers (e.g. host, internal tracing) are stripped.

## Related
- [[telegram_proxy.py]]
- [[pipeline.py]]
- [[forwarder.py]]
