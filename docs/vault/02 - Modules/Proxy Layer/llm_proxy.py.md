---
module: llm_proxy
path: gateway/proxy/llm_proxy.py
role: Multi-provider LLM reverse proxy with security pipeline, quota failover, and streaming support
dependencies:
  - gateway.proxy.anthropic_openai_sse_translator
  - gateway.proxy.anthropic_openai_translator
  - gateway.proxy.llm_quota_detector
  - httpx (streaming path)
related:
  - "[[telegram_proxy.py]]"
  - "[[pipeline.py]]"
  - "[[anthropic_openai_translator.py]]"
  - "[[anthropic_openai_sse_translator.py]]"
  - "[[llm_quota_detector.py]]"
tags: [proxy, llm, anthropic, openai, google, ollama, lmstudio, mlxlm, pii, prompt-injection, quota-failover, streaming, outbound-filter, api-proxy, tool-acl]
status: documented
---

# llm_proxy.py

## Overview

`llm_proxy.py` implements a multi-provider LLM reverse proxy that sits between the AI agent client (OpenClaw) and upstream LLM APIs. It automatically routes requests to the correct provider backend based on request path and model name, runs all inbound user messages through the security pipeline (PII redaction, injection detection), and filters all outbound LLM responses (credential blocking, XML stripping, `<think>` tag removal, Tool ACL enforcement). On cloud quota exhaustion it automatically fails over to a configured local model without dropping the request.

The proxy supports both buffered and true-streaming request paths:
- `proxy_messages` — buffered path, used for non-streaming requests and streaming requests whose responses are fully buffered before delivery.
- `proxy_messages_streaming` — true-streaming path using `httpx`, yields SSE chunks to the caller as they arrive; prevents OpenClaw's 60-second fetch timeout from triggering on slow local models.

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `LLMProxy` | Class | Main proxy class; owns the full request lifecycle for all LLM providers |
| `LLMProxy.proxy_messages` | Method | Buffered request path: route → scan inbound → forward → quota failover → filter outbound |
| `LLMProxy.proxy_messages_streaming` | Method | True-streaming path via `httpx`; yields SSE bytes as they arrive; applies same inbound scan and outbound ToolACL |
| `LLMProxy._scan_request_data` | Method | Dispatches inbound scanning across Anthropic/OpenAI, Google Gemini (`contents`), and Ollama native (`prompt`) message formats |
| `LLMProxy._scan_inbound` | Method | PII redaction (via `sanitizer`) + middleware injection check on a single text string |
| `LLMProxy._filter_outbound` | Method | Parses non-streaming response JSON; applies XML/credential filters to Anthropic and OpenAI content; strips `reasoning_content` and `<think>` tags from LM Studio / Qwen3 responses |
| `LLMProxy._filter_outbound_streaming` | Method | Parses buffered SSE lines; applies outbound filters and ToolACL to each `data:` event |
| `LLMProxy._filter_streaming_event` | Method | Per-event outbound filter; handles Anthropic `content_block_start` ToolACL (CVE-2026-9367), OpenAI delta/message content, and Anthropic content block text |
| `LLMProxy._enforce_tool_acl` | Method | Scans Anthropic non-streaming `tool_use` blocks; replaces denied tools with an informational text block |
| `LLMProxy._failover_request` | Method | Cloud→local failover: translates Anthropic→OpenAI format if needed, dispatches to Ollama, translates response back |
| `LLMProxy._emit_failover_notice` | Method | Sends a Telegram notification when failover activates; rate-limited to one notice per 30-minute window via file stamp |
| `LLMProxy._record_failover_event` | Method | Persists failover events to the AuditChain and updates `_stats` |
| `LLMProxy._forward_request` | Method | Forwards requests via `urllib`; retries up to 3× on 429/503/529 with exponential backoff + jitter; respects `Retry-After` |
| `LLMProxy._build_timeout_fallback_response` | Static method | Builds provider-compatible timeout error messages (Anthropic, OpenAI, Google, Ollama formats) |
| `LLMProxy._apply_filters` | Method | Applies XML block stripping and credential blocking to a text string |
| `LLMProxy.get_stats` | Method | Returns cumulative proxy statistics dict |

## LLM Providers

The proxy routes to six provider backends. Routing is determined by request path and model name — in that priority order.

| Provider | Base URL | Detection Logic |
|----------|----------|-----------------|
| **Anthropic** | `https://api.anthropic.com` | Default; path contains `/v1/messages` |
| **OpenAI** | `https://api.openai.com` | Path contains `/v1/chat/completions` or `/v1/completions` |
| **Google Gemini** | `https://generativelanguage.googleapis.com` | Path contains `/v1beta` or `google` in path |
| **Ollama** | `http://host.docker.internal:11434` | Model name contains `qwen`, `llama`, `mistral`, `deepseek`, `phi`, `ollama`, `lmstudio`, `mlxlm`; or native Ollama `/api/` path; or `ollama/` / `lmstudio/` prefix |
| **LM Studio** | `$LMSTUDIO_API_BASE` (default `:1234`) | Model prefix matches `qwen3`, `qwen2.5-coder`, or `gemma` in `LOCAL_MODEL_ROUTES` |
| **mlx_lm** | `$MLXLM_API_BASE` (default `:8234`) | Model prefix matches `deepseek-r1` or `mlx-community/deepseek-r1` in `LOCAL_MODEL_ROUTES` |

### Model prefix routing (`LOCAL_MODEL_ROUTES`)

`LOCAL_MODEL_ROUTES` is a dict checked before the generic Ollama fallback. Only models that do NOT run under Ollama need an entry here.

```
"mlx-community/deepseek-r1"  → MLXLM_API_BASE   # DeepSeek-R1 via mlx_lm
"deepseek-r1"                → MLXLM_API_BASE   # DeepSeek-R1 shorthand
"qwen3"                      → LMSTUDIO_API_BASE  # Qwen3 family
"qwen2.5-coder"              → LMSTUDIO_API_BASE  # Coding models
"gemma"                      → LMSTUDIO_API_BASE  # Gemma family
```

### Provider prefix normalization

OpenClaw may emit model IDs like `ollama/qwen2.5-coder:7b` or `lmstudio/qwen3.5-27b`. The proxy strips the `ollama/` and `lmstudio/` prefixes before forwarding so all local OpenAI-compatible APIs receive bare model names.

### Claude Opus intercept

When `AGENTSHROUD_MODEL_MODE` is not `cloud`, any request targeting a `claude-opus` model is intercepted and the model is forced to `AGENTSHROUD_LOCAL_MODEL`. This prevents internal system components from accidentally routing to expensive cloud models in local/dev mode.

## Quota Failover

When a cloud provider returns a quota-exhausted response, the proxy automatically retries the request against the configured local model (Ollama by default) without surfacing the error to the caller.

### Failover chain

```
Cloud API (Anthropic / OpenAI)
  └─ 429 / 402 detected by llm_quota_detector.is_quota_exhausted()
       ├─ OpenAI path: rewrite model → dispatch to Ollama /v1/chat/completions (drop-in)
       ├─ Anthropic path (/v1/messages): translate request via anthropic_to_openai_request()
       │    → dispatch to Ollama /v1/chat/completions
       │    → translate response via openai_to_anthropic_response()
       └─ Google / unknown: no translator — emit warning notice, return original 429
```

### Failover controls

| Control | Description |
|---------|-------------|
| `AGENTSHROUD_FAILOVER_ON_QUOTA=1` | Enable/disable failover globally (default: enabled) |
| `X-AgentShroud-No-Failover: 1` | Per-request opt-out header |
| `AGENTSHROUD_LOCAL_MODEL_REF` | Local model to fail over to (e.g. `ollama/qwen3:14b`) |
| Streaming path | Failover applies only on 429/402 status codes; 200 responses stream immediately without buffering |

### Failover notifications

On failover activation, `_emit_failover_notice` sends a single Telegram message to the owner. A file stamp at `/tmp/.gateway-failover-notify-stamp` rate-limits notices to one per 30-minute window per token type. The notice includes the quota token that was exhausted and the local model being used.

### Stats tracked

```
failover_quota_succeeded  — count of successful cloud→local failovers
failover_quota_failed     — count of failed failover attempts
failover_active           — bool: is failover currently in effect
failover_last_provider    — quota token from most recent failover
failover_last_event       — ISO-8601 timestamp of most recent failover
```

Failover events are also persisted to the `AuditChain` if one is injected at construction time.

## Streaming

### True-streaming path (`proxy_messages_streaming`)

Uses `httpx.AsyncClient` with `stream()` to yield SSE byte chunks to the caller as they arrive. This avoids the 60-second OpenClaw HTTP fetch timeout that would trigger when waiting for the first byte from a slow local model.

- Inbound scanning (PII + injection) is applied before the upstream request.
- For 200 responses, chunks are yielded immediately — no buffering. This ordering is required because buffering the first chunk and yielding it last causes `content_block_start` to arrive before `message_start`, breaking the Anthropic SDK streaming parser.
- For 429/402 error responses only: the small error body is read in full, quota failover is attempted. If failover succeeds and the path is `/v1/messages`, the Ollama SSE stream is translated to Anthropic SSE format via `translate_openai_sse_to_anthropic`.
- Errors during streaming are caught and emitted as an SSE `data:` error event.

### Buffered streaming filter (`_filter_outbound_streaming`)

When the buffered path (`proxy_messages`) receives a streaming response (i.e. the body is SSE text), it applies outbound filters line-by-line:
- Each `data:` line is parsed as JSON.
- XML/credential filters are applied to text content.
- ToolACL is enforced on `content_block_start` events (Anthropic streaming format).
- `reasoning_content` fields and `<think>...</think>` tags are stripped from OpenAI delta/message content.

### `<think>` tag stripping

Both the buffered and streaming outbound filter paths strip `<think>...</think>` blocks from OpenAI-format content. Qwen3 models (without `separateReasoningContentInAPI`) embed thinking as inline `<think>` tags. LM Studio models with `separateReasoningContentInAPI` emit a `reasoning_content` field instead, which is also handled: if `content` is empty, `reasoning_content` is promoted to `content`; the `reasoning_content` key is always removed from the forwarded response.

## Configuration

### Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AGENTSHROUD_LOCAL_MODEL` | `qwen2.5-coder:7b` | Bare model name used when MODEL_MODE is local and for the Claude Opus intercept |
| `AGENTSHROUD_LOCAL_MODEL_REF` | `ollama/qwen3:14b` | Provider-prefixed model reference used for quota failover |
| `AGENTSHROUD_MODEL_MODE` | `local` | `cloud` disables the Claude Opus intercept and quota failover routing |
| `AGENTSHROUD_FAILOVER_ON_QUOTA` | `1` | Set to `0` to disable cloud→local quota failover |
| `LMSTUDIO_API_BASE` | `http://host.docker.internal:1234` | LM Studio API base URL |
| `MLXLM_API_BASE` | `http://host.docker.internal:8234` | mlx_lm API base URL |
| `AGENTSHROUD_OWNER_CHAT_ID` | `8096968754` | Telegram chat ID for failover notifications |
| `GATEWAY_OP_PROXY_URL` | `http://gateway:8080` | Gateway URL used by failover notifier to send Telegram messages |
| `GATEWAY_AUTH_TOKEN` | — | Bearer token for internal gateway API calls |
| `TELEGRAM_BOT_TOKEN` | — | Telegram bot token for failover notifications |

### Constructor dependencies (dependency injection)

| Parameter | Description |
|-----------|-------------|
| `pipeline` | Security pipeline (currently unused in direct calls; reserved) |
| `middleware_manager` | Processes inbound request context; skipped for `user_id="unknown"` |
| `sanitizer` | PII redaction engine (Presidio); also provides `filter_xml_blocks` and `block_credentials` |
| `tool_acl_enforcer` | ToolACL enforcement on `tool_use` blocks in responses |
| `credential_injector` | Injects API credentials into outgoing Anthropic headers |
| `audit_chain` | AuditChain instance for persistent failover event logging; injected post-construction by `lifespan.py` |

### Header pass-through policy

Only these headers are forwarded to upstream providers:
`authorization`, `x-api-key`, `anthropic-version`, `anthropic-beta`, `content-type`, `accept`, `user-agent`, `x-goog-api-key`

All other headers (host, internal tracing, AgentShroud metadata) are stripped.

### Retry policy (`_forward_request`)

Retries on status codes 429, 503, 529 (Anthropic "overloaded") up to 3 times. Wait time is sourced from `Retry-After` header when present; otherwise exponential backoff (2s, 4s, 8s) with ±1s random jitter. Upstream timeout: 1800 seconds (30 minutes).

## Related

- [[anthropic_openai_translator.py]] — `anthropic_to_openai_request` / `openai_to_anthropic_response` used by failover
- [[anthropic_openai_sse_translator.py]] — `translate_openai_sse_to_anthropic` used by streaming failover
- [[llm_quota_detector.py]] — `is_quota_exhausted` detects 429/402 quota signals
- [[telegram_proxy.py]]
- [[pipeline.py]]
- [[forwarder.py]]
