---
title: prompt_guard.py
type: module
file_path: gateway/security/prompt_guard.py
tags: [security, prompt-injection, input-validation, scanning, threat-detection]
related: ["[[Security Modules/input_normalizer.py|input_normalizer.py]]", "[[Security Modules/egress_filter.py|egress_filter.py]]", "[[Data Flow]]"]
status: documented
---

# prompt_guard.py

## Purpose
Detects and blocks prompt injection attempts in user-supplied text using a weighted pattern-scoring system. Returns structured scan results including a blocked status, threat score, matched pattern names, and a sanitized copy of the input.

## Threat Model
Prompt injection — adversarial text designed to override an LLM's system instructions, extract its system prompt, jailbreak its safety constraints, or exfiltrate data via embedded Markdown. Attacks may use plaintext, encoded (base64/hex/rot13), unicode-obfuscated, or multilingual payloads to evade regex patterns.

## Responsibilities
- Normalize input via `input_normalizer.normalize_input` before scanning (defeats encoding evasion)
- Match input against 26+ compiled regex pattern rules, each carrying a float weight
- Detect base64-encoded injection payloads, including double-encoded content
- Detect unicode obfuscation: homoglyphs, zero-width characters, RTL overrides, fullwidth chars, mathematical Unicode letters
- Accumulate a threat score (capped at 5.0) across all matched patterns
- Classify the result as BLOCK (score >= block_threshold), WARN (score >= warn_threshold), or LOG
- Return a `ScanResult` containing blocked status, score, matched pattern names, and a redacted copy of the input
- Accept custom `PatternRule` instances to extend detection at runtime

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ThreatAction` | Enum | BLOCK / WARN / LOG outcome classification |
| `ScanResult` | Dataclass | Scan output: blocked, score, patterns, sanitized_input, action |
| `PatternRule` | Dataclass | Named pattern with compiled regex and float weight |
| `_PATTERNS` | Module-level list | 26 precompiled `PatternRule` instances |
| `PromptGuard` | Class | Main scanning class |
| `PromptGuard.scan()` | Method | Entry point — scans text and returns `ScanResult` |
| `PromptGuard._check_encoded_content()` | Method | Base64 decode and re-scan (catches encoded payloads) |
| `PromptGuard._check_unicode_tricks()` | Method | Detects homoglyphs, zero-width chars, RTL override, fullwidth, math Unicode |

## Function Details

### PromptGuard.__init__(block_threshold, warn_threshold, custom_patterns)
**Purpose:** Configure scoring thresholds and optionally extend the pattern set.
**Parameters:**
- `block_threshold` (float, default 0.8) — scores at or above this value result in BLOCK
- `warn_threshold` (float, default 0.4) — scores at or above this value result in WARN
- `custom_patterns` (list[PatternRule] | None) — additional rules merged with built-ins
**Returns:** None
**Side effects:** Copies `_PATTERNS` into instance list; appends custom patterns.

### PromptGuard.scan(text)
**Purpose:** Full scan pipeline — normalize, match patterns, check encoded content, check unicode tricks, classify, sanitize.
**Parameters:** `text` (str) — raw user input
**Returns:** `ScanResult`
**Side effects:** None (pure computation, no I/O).

### PromptGuard._check_encoded_content(text)
**Purpose:** Find base64 strings, decode them, and scan decoded content for injection patterns. Also checks for double-base64 encoding.
**Parameters:** `text` (str)
**Returns:** `list[tuple[str, float]]` — list of (pattern_name, weight) findings
**Side effects:** None.

### PromptGuard._check_unicode_tricks(text)
**Purpose:** Identify unicode-based evasion before NFKC normalization strips the signals.
**Parameters:** `text` (str) — raw, pre-normalized text
**Returns:** `list[tuple[str, float]]` — findings with weights (0.4–0.6)
**Side effects:** None.

## Pattern Categories and Weights

| Category | Example Pattern Names | Max Weight |
|----------|-----------------------|------------|
| Role/instruction override | `ignore_instructions`, `new_instructions`, `role_reassignment` | 0.9 |
| System prompt extraction | `prompt_extraction`, `prompt_leak` | 0.7 |
| Delimiter/tag injection | `delimiter_injection`, `xml_system_tag`, `chat_format_injection` | 0.85 |
| Jailbreak | `dan_jailbreak` | 0.95 |
| Encoded payloads | `base64_block`, `hex_encoded`, `encoding_smuggling` | 0.8 |
| Indirect injection | `indirect_injection`, `payload_after_benign`, `boundary_manipulation` | 0.9 |
| Multilingual | `multilingual_injection` (6 languages) | 0.9 |
| Exfiltration | `markdown_exfiltration`, `echo_trap` | 0.85 |
| Social engineering | `social_engineering_authority` | 0.85 |
| Unicode evasion | detected in `_check_unicode_tricks` | 0.4–0.6 |
| Few-shot poisoning | `few_shot_poisoning` | 0.75 |
| Hypothetical framing | `hypothetical_framing` | 0.6 |
| Emoji unlock | `emoji_unlock` | 0.7 |
| HTML comment injection | `html_comment_injection` | 0.85 |

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `block_threshold` | 0.8 | Score at or above which input is blocked |
| `warn_threshold` | 0.4 | Score at or above which a warning is issued |
| `custom_patterns` | None | Additional `PatternRule` instances |

## Mode: Enforce vs Monitor
This module does not have an enforce/monitor mode of its own. The `ThreatAction` is determined solely by score thresholds:
- **BLOCK**: Input is rejected; `ScanResult.blocked = True`
- **WARN**: Input passes but is flagged; upstream caller decides what to do
- **LOG**: No significant threat detected; input passes

## Environment Variables
None. Configuration is passed at instantiation.

## Dependencies
- `[[Security Modules/input_normalizer.py|input_normalizer.py]]` — `normalize_input()` and `detect_base64_payloads()` are called at the start of every scan

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/input_normalizer.py|input_normalizer.py]]
- [[Security Modules/egress_filter.py|egress_filter.py]]
