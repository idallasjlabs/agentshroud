---
title: presidio-analyzer
type: dependency
tags: [pii, nlp, security, microsoft]
related: [Dependencies/spacy, Gateway Core/sanitizer.py, Dependencies/All Dependencies]
status: documented
---

# Presidio Analyzer

**Package:** `presidio-analyzer` + `presidio-anonymizer`
**Version:** ≥2.2.0,<3.0.0
**Source:** Microsoft
**Used in:** Gateway container (PII detection pipeline)

## Purpose

Microsoft Presidio is the PII (Personally Identifiable Information) detection and redaction engine. It:
1. Analyzes text to detect PII entities (SSN, credit cards, email addresses, phone numbers, locations)
2. Returns entity spans with confidence scores
3. The anonymizer module then replaces detected PII with replacement tokens

## Architecture

```
Input text
  → AnalyzerEngine (NLP detection)
  → filters by confidence threshold (0.9)
  → AnonymizerEngine (redaction)
  → Output: text with <REDACTED_*> tokens
```

## Configured Entities

| Entity Type | Config Name | Description |
|-------------|-------------|-------------|
| `US_SSN` | `SSN` | US Social Security Numbers |
| `CREDIT_CARD` | `CREDIT_CARD` | Credit card numbers |
| `PHONE_NUMBER` | `PHONE_NUMBER` | Phone numbers |
| `EMAIL_ADDRESS` | `EMAIL_ADDRESS` | Email addresses |
| `LOCATION` | `STREET_ADDRESS` | Physical addresses |

## Confidence Threshold

Set in `agentshroud.yaml`:
```yaml
pii_min_confidence: 0.9
```

Higher values = fewer false positives but may miss some PII. Lower values = more aggressive redaction with more false positives.

## NLP Backend

Presidio uses **spaCy** as its NLP backend for Named Entity Recognition (NER). The `en_core_web_sm` model is used.

## Where Used

- `gateway/ingest_api/sanitizer.py` — Primary PII scanner for all incoming messages
- `gateway/security/tool_result_sanitizer.py` — PII scanning of tool call results
- `gateway/security/tool_result_sanitizer_enhanced.py` — Enhanced tool result scanning
- `gateway/security/log_sanitizer.py` — Log content PII removal

## Related Notes

- [[Dependencies/spacy]] — NLP engine that Presidio uses
- [[Gateway Core/sanitizer.py|sanitizer.py]] — PII sanitizer implementation
- [[Configuration/agentshroud.yaml]] — `pii_min_confidence` configuration
- [[Dependencies/All Dependencies]] — Full dependency list
