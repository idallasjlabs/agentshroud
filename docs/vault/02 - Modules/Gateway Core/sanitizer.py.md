---
title: sanitizer.py
type: module
file_path: gateway/ingest_api/sanitizer.py
tags: [pii, sanitization, presidio, regex, security, gateway-core]
related: [Gateway Core/models.py, Gateway Core/main.py, Architecture Overview]
status: documented
---

# sanitizer.py

## Purpose
Implements the Personally Identifiable Information (PII) detection and redaction engine for the AgentShroud gateway. Supports two detection backends: Microsoft Presidio (with spaCy NLP) and a regex fallback, selectable via configuration.

## Responsibilities
- Detect and redact PII entities (SSN, credit card, phone, email, location) from inbound content
- Initialize and manage the Presidio + spaCy NLP pipeline when available
- Fall back to compiled regex patterns when Presidio or spaCy are unavailable
- Block credential display (passwords, API keys, tokens) via untrusted sources such as Telegram
- Strip Claude internal XML function call blocks (`<function_calls>`, `<thinking>`, `<system-reminder>`, etc.) from outbound responses
- Run as hybrid mode (Presidio first, then regex) to catch entities that the spaCy `en_core_web_sm` model misses

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `PIISanitizer` | class | Primary PII detection and redaction engine |
| `__init__` | method | Initializes mode, precompiles regex patterns, calls `_init_presidio` if configured |
| `_init_presidio` | method | Loads Presidio + spaCy; falls back to regex on failure or Python 3.14+ |
| `sanitize` | async method | Main entry point: dispatches to Presidio hybrid or regex path |
| `_sanitize_presidio` | async method | Runs Presidio in a thread pool via `asyncio.to_thread` |
| `_sanitize_regex` | async method | Applies precompiled regex patterns for all configured entity types |
| `get_supported_entities` | method | Returns list of enabled entity type names from config |
| `get_mode` | method | Returns current enforcement mode ("enforce" or "monitor") |
| `block_credentials` | async method | Blocks credential content from reaching untrusted sources (Telegram, external_api) |
| `filter_xml_blocks` | method | Removes Claude internal XML tool blocks from responses |

## Function Details

### sanitize(content)
**Purpose:** Detects and redacts PII from a text string. If PII sanitization is disabled, returns the original content unchanged.
**Parameters:** `content: str` — the text to sanitize
**Returns:** `RedactionResult` containing sanitized text, list of `RedactionDetail`, and entity types found
**Side effects:** Logs redaction activity at INFO/WARNING level

### _sanitize_presidio(content)
**Purpose:** Wraps synchronous Presidio `analyze` and `anonymize` calls in `asyncio.to_thread` to avoid blocking the event loop. Filters results by `min_confidence` threshold.
**Parameters:** `content: str`
**Returns:** `RedactionResult`; falls back to `_sanitize_regex` on exception

### _sanitize_regex(content)
**Purpose:** Applies ordered regex patterns for US_SSN, CREDIT_CARD, PHONE_NUMBER, EMAIL_ADDRESS, and LOCATION entity types. Replacements are applied in reverse position order to preserve offsets.
**Parameters:** `content: str`
**Returns:** `RedactionResult` with regex confidence score fixed at 1.0

### block_credentials(content, source)
**Purpose:** Inspects outbound response content for credential patterns. Only triggers for sources in the blocked list (`telegram`, `external_api`, `remote`, `untrusted`).
**Parameters:** `content: str`, `source: str`
**Returns:** `tuple[str, bool]` — (sanitized_content, was_blocked)
**Side effects:** Logs WARNING with credential type if blocked; returns a user-facing redaction message

### filter_xml_blocks(content)
**Purpose:** Removes Claude internal XML blocks from response text to prevent leaking tool internals to end users. Also collapses excessive newlines.
**Parameters:** `content: str`
**Returns:** `tuple[str, bool]` — (filtered_content, was_filtered)

## Environment Variables Used
- None directly — mode and configuration come from `PIIConfig` (loaded from `agentshroud.yaml`)

## Config Keys Read
- `config.engine` — `"presidio"` or `"regex"` to select detection backend
- `config.entities` — list of entity types to detect (e.g., `["US_SSN", "EMAIL_ADDRESS"]`)
- `config.min_confidence` — minimum Presidio confidence score for a detection to be accepted
- `config.enabled` — boolean flag to enable/disable PII sanitization entirely

## Imports From / Exports To
- Imports: [[Gateway Core/models.py]] (`RedactionDetail`, `RedactionResult`), `.config` (`PIIConfig`)
- Imported by: [[Gateway Core/main.py]], `gateway.proxy.pipeline.SecurityPipeline`, `gateway.proxy.telegram_proxy.TelegramAPIProxy`, `gateway.proxy.llm_proxy.LLMProxy`

## Known Issues / Notes
- Presidio is explicitly incompatible with Python 3.14+; the init method checks `sys.version_info` and auto-falls-back to regex.
- The hybrid mode runs Presidio then regex sequentially — this adds latency for presidio-mode deployments.
- `en_core_web_sm` misses SSN and phone patterns, which is why hybrid mode is used rather than Presidio alone.
- `block_credentials` uses a hard-coded list of blocked sources; adding new untrusted sources requires a code change.
- The `filter_xml_blocks` method uses both closed-pair and unclosed/truncated patterns — the latter catches streaming responses mid-delivery.
- Regex confidence is hard-coded to `1.0`; there is no false-positive filtering for regex matches.

## Related
- [[Gateway Core/models.py]]
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
