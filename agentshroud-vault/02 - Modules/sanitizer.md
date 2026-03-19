---
title: sanitizer.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/ingest_api/sanitizer.py
tags: [#type/module, #status/critical]
related: ["[[pipeline]]", "[[lifespan]]", "[[presidio]]", "[[agentshroud.yaml]]"]
status: active
last_reviewed: 2026-03-09
---

# sanitizer.py — PII Detection and Redaction

## Purpose

Wraps Microsoft Presidio to detect and redact Personally Identifiable Information (PII) from all messages passing through the gateway — both inbound (user messages) and outbound (LLM responses).

## Engine

- **Default:** `presidio` (Microsoft Presidio Analyzer + Anonymizer)
- **Alternative:** `spacy` (configurable via `agentshroud.yaml security.pii_detection_engine`)
- **Language:** English (`en`) — Presidio logs warnings when es/it/pl recognizers are skipped (expected/benign)

## Entities Scanned (from agentshroud.yaml)

| Entity Type | YAML Name | Presidio Entity |
|-------------|-----------|-----------------|
| Social Security Number | `SSN` | `US_SSN` |
| Credit Card | `CREDIT_CARD` | `CREDIT_CARD` |
| Phone Number | `PHONE_NUMBER` | `PHONE_NUMBER` |
| Email Address | `EMAIL_ADDRESS` | `EMAIL_ADDRESS` |
| Street Address | `STREET_ADDRESS` | `LOCATION` |

## `PIISanitizer` Class

```python
class PIISanitizer:
    def __init__(self, config: PIIConfig, mode: str = "enforce", action: str = "redact"):
        ...

    def sanitize(self, text: str) -> tuple[str, list[str]]:
        """Returns (sanitized_text, list_of_redacted_entity_types)"""

    def get_mode(self) -> str:
        """Returns 'enforce' or 'monitor'"""
```

## Actions

| Mode | Action | Behavior |
|------|--------|---------|
| `enforce` | `redact` | Replace PII with `<ENTITY_TYPE>` placeholder |
| `enforce` | `block` | Reject message entirely if PII found |
| `monitor` | any | Log PII found but do not modify message |

## Min Confidence Threshold

```yaml
# agentshroud.yaml
security:
  pii_min_confidence: 0.9  # High threshold to reduce false positives
```

Default 0.9 — increased from 0.8 to reduce over-redaction. Lower = more aggressive (more false positives).

## Tool Result PII Configuration

Per-tool entity overrides in `config.tool_result_pii`:

| Tool Source | Entities | Min Confidence |
|-------------|----------|----------------|
| `icloud` | SSN, CC, Phone, Email, Location | 0.7 |
| `email` | SSN, CC, Phone, Email | 0.7 |
| `contacts` | Phone, Email, Location | 0.8 |
| `web_search` | SSN, CC, Phone | 0.8 |
| `browser` | SSN, CC | 0.9 |

## Related

- [[presidio]] — the underlying PII detection library
- [[pipeline]] — PIISanitizer used at step 2 (inbound) and step 1 (outbound)
- [[lifespan]] — initializes PIISanitizer, passes mode and action from config
- [[agentshroud.yaml]] — `security.pii_*` and `security_modules.pii_sanitizer` settings
