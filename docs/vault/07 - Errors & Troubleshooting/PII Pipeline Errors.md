---
title: PII Pipeline Errors
type: troubleshooting
tags: [pii, errors, sanitizer]
related: [Gateway Core/sanitizer.py, Configuration/agentshroud.yaml, Errors & Troubleshooting/Error Index]
status: documented
---

# PII Pipeline Errors

## PII Engine Not Initialized

**Error (500):** `PII sanitizer not initialized`

**Cause:** Gateway received a request before the Presidio/spaCy engine finished loading.

**Fix:** Wait 10-30 seconds after gateway startup before sending requests. The health check at `/status` confirms when all components are ready.

---

## Excessive False Positives

**Symptom:** Legitimate content (product codes, IDs, references) being redacted

**Cause:** `pii_min_confidence` set too low

**Fix:**
```yaml
# agentshroud.yaml
security:
  pii_min_confidence: 0.95   # Increase from 0.9 (default)
```

Common false-positive-prone content:
- 9-digit numbers (mistaken for SSNs)
- Product serial numbers
- IPv4 addresses (can match phone number patterns)

---

## PII Not Being Detected

**Symptom:** Known PII passing through without redaction

**Possible causes:**

| Cause | Fix |
|-------|-----|
| Entity type not in `redaction_rules` | Add entity type to the list |
| `pii_min_confidence` too high | Lower to 0.85 |
| `pii_redaction: false` | Set to `true` |
| Module in `monitor` mode | Check `security_modules.pii_sanitizer.mode` |
| `AGENTSHROUD_MODE=monitor` | Remove this env var |

---

## Redaction Breaking JSON/Structured Data

**Symptom:** Tool results return malformed JSON after PII redaction

**Cause:** Presidio is redacting values inside JSON strings, replacing them with `<REDACTED_EMAIL>` which may break downstream parsing.

**Fix:** This is expected behavior — the redacted values are still valid strings. Update downstream consumers to handle `<REDACTED_*>` tokens gracefully.

---

## spaCy Model Issues

**Symptom:**
- `OSError: [E050] Can't find model 'en_core_web_lg'`
- Slow PII detection

**Cause:** Using a model name that wasn't downloaded, or model files corrupted.

**Fix:**
```bash
# Rebuild image (redownloads model)
docker compose build --no-cache agentshroud-gateway
```

**Fallback:** If spaCy fails to load, Presidio falls back to regex-based detection. This is less accurate but prevents complete PII pipeline failure.

---

## Tool Result PII Not Scanned

**Symptom:** Tool results containing PII are not being scanned

**Cause:** Tool result sanitizer is not enabled for that tool

**Fix in `agentshroud.yaml`:**
```yaml
tool_result_pii:
  enabled: true
  tool_overrides:
    my-tool:
      entities: ["EMAIL_ADDRESS", "PHONE_NUMBER"]
      min_confidence: 0.8
```

---

## Related Notes

- [[Gateway Core/sanitizer.py|sanitizer.py]] — PII sanitizer implementation
- [[Dependencies/presidio-analyzer]] — Presidio details
- [[Dependencies/spacy]] — spaCy NLP model
- [[Configuration/agentshroud.yaml]] — PII configuration
- [[Errors & Troubleshooting/Error Index]] — Full error index
