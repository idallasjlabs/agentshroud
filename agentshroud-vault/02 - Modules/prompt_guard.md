---
title: prompt_guard.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/security/prompt_guard.py
tags: [#type/module, #status/critical]
related: ["[[pipeline]]", "[[lifespan]]", "[[heuristic_classifier]]", "[[AGENTSHROUD_MODE]]"]
status: active
last_reviewed: 2026-03-09
---

# prompt_guard.py — Prompt Injection Detection

## Purpose

Detects and scores prompt injection attempts in inbound messages. Uses a weighted pattern-matching system (no ML model needed). Returns a `ScanResult` with a threat score (0.0–1.0), matched patterns, and sanitized input.

## Scoring System

Each matched pattern adds its `weight` to the cumulative score (capped at 1.0).

| Pattern | Weight | Examples |
|---------|--------|---------|
| `ignore_instructions` | 0.9 | "ignore all previous instructions" |
| `role_reassignment` | 0.5 | "act as if you are", "pretend to be" |
| `new_instructions` | 0.9 | "new instructions", "override rules", "forget everything" |
| `prompt_extraction` | varies | "print your system prompt", "reveal your instructions" |
| `jailbreak_dan` | varies | "DAN mode", "developer mode" |
| `base64_instruction` | varies | Base64-encoded instructions in input |
| Multilingual patterns | varies | Thai, Vietnamese, Swahili, Amharic injection |

## Thresholds

| Score Range | Action | Behavior |
|-------------|--------|---------|
| < 0.4 | LOG | No blocking, logged |
| 0.4–0.8 | WARN | Not blocked but flagged |
| ≥ 0.8 | BLOCK | Message rejected, 403 returned |

In **monitor mode**, both thresholds are set to `999.0` — nothing blocks.
In **enforce mode**, defaults: `block_threshold=0.8`, `warn_threshold=0.4`.

## Class: `PromptGuard`

```python
class PromptGuard:
    def __init__(self, block_threshold: float = 0.8, warn_threshold: float = 0.4):
        ...

    def scan(self, text: str) -> ScanResult:
        """Scan text for prompt injection patterns."""
```

## `ScanResult` Fields

| Field | Type | Description |
|-------|------|-------------|
| `blocked` | bool | True if score ≥ block_threshold |
| `score` | float | Cumulative threat score (0–1) |
| `patterns` | list[str] | Names of matched patterns |
| `sanitized_input` | str | Input with detected injection stripped |
| `action` | ThreatAction | BLOCK, WARN, or LOG |

## Input Normalization

Before scanning, input is normalized via `input_normalizer.normalize_input()`:
- Unicode homoglyph normalization (NFKC)
- Multi-pass URL decoding (up to 5 iterations)
- Base64 payload detection via `detect_base64_payloads()`

This prevents obfuscation bypass (e.g., `%69gnore` → `ignore`, Cyrillic "о" → "o").

## Pipeline Integration

```python
# In SecurityPipeline.process_inbound():
result = prompt_guard.scan(normalized_message)
if result.blocked:
    return PipelineResult(action=BLOCK, block_reason=result.patterns)
```

## Related

- [[heuristic_classifier]] — additional ML-free injection heuristics (step 1.1 in pipeline)
- [[pipeline]] — `process_inbound()` calls `prompt_guard.scan()`
- [[lifespan]] — initializes PromptGuard with mode-appropriate thresholds
- [[AGENTSHROUD_MODE]] — `monitor` sets thresholds to 999 (no blocking)
