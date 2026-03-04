---
title: spacy
type: dependency
tags: [nlp, pii, python]
related: [Dependencies/presidio-analyzer, Gateway Core/sanitizer.py, Configuration/Dockerfile.gateway]
status: documented
---

# spaCy

**Package:** `spacy`
**Version:** ≥3.8.0,<4.0.0
**Model:** `en_core_web_sm` (baked into Docker image)
**Used in:** Gateway container (NLP backend for Presidio PII detection)

## Purpose

spaCy provides the Named Entity Recognition (NER) model that Microsoft Presidio uses to detect PII in text. It performs linguistic analysis — tokenization, part-of-speech tagging, dependency parsing — that enables accurate entity detection.

## Model

`en_core_web_sm` — small English model
- Approx size: ~12 MB
- Download command: `python3 -m spacy download en_core_web_sm`
- Baked into the Docker image at build time to avoid download on startup

## Where Used

- `gateway/ingest_api/sanitizer.py` — NLP engine for Presidio's AnalyzerEngine
- PII detection pipeline for all incoming messages and tool results

## Fallback Behavior

If spaCy model download fails at build time, the gateway uses regex-based fallback for PII detection:
```
"spaCy model download failed — will use regex fallback"
```

Regex fallback is less accurate but prevents complete failure.

## First-Boot Performance

spaCy model initialization takes ~2-3 seconds on first load. Subsequent request handling is fast after the model is warmed up.

## Related Notes

- [[Dependencies/presidio-analyzer]] — Uses spaCy as NLP backend
- [[Gateway Core/sanitizer.py|sanitizer.py]] — PII detection implementation
- [[Configuration/Dockerfile.gateway]] — Model downloaded at build time
