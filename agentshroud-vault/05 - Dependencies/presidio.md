---
title: Microsoft Presidio
type: dependency
tags: [#type/dependency, #status/active]
related: ["[[sanitizer]]", "[[lifespan]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# Microsoft Presidio

**Packages:** `presidio-analyzer>=2.2.0,<3.0.0` + `presidio-anonymizer>=2.2.0,<3.0.0`
**Also requires:** `spacy>=3.8.0,<4.0.0` + English language model

## What It Does

Open-source PII (Personally Identifiable Information) detection and anonymization engine from Microsoft. Used by [[sanitizer]] to detect and redact SSN, credit cards, phone numbers, email addresses, and location data from all messages.

## Two-Component Architecture

- **presidio-analyzer** — detects PII entities using NLP + pattern matching, returns spans with confidence scores
- **presidio-anonymizer** — applies redaction actions (replace, mask, hash) to detected spans

## Language Support

Default: English (`en`) only.

> [!WARNING] At startup, Presidio logs warnings about skipped language recognizers (es, it, pl). This is expected and benign — only English is configured.

## Entity Detection

Presidio uses multiple recognizers per entity type:
- Pattern-based (regex) — SSN, credit cards
- ML-based (spaCy NER) — person names, locations
- Rule-based (dictionary) — phone numbers

## Min Confidence Threshold

Set to `0.9` in `agentshroud.yaml`. Detections below this threshold are ignored. Lower = more aggressive (more false positives).

## What Breaks If Missing

[[lifespan]] raises exception at step 3 (PIISanitizer init). Gateway exits.

## Known Issues

> [!WARNING] Presidio spaCy model (`en_core_web_lg`) must be downloaded during image build. If the model is missing, `PIISanitizer` initialization fails. The Dockerfile handles this with `pip install spacy && python -m spacy download en_core_web_lg`.
