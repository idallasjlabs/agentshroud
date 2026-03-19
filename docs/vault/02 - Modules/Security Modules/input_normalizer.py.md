---
title: input_normalizer.py
type: module
file_path: gateway/security/input_normalizer.py
tags: [security, input-validation, normalization, encoding, unicode, exfiltration]
related: ["[[Security Modules/prompt_guard.py|prompt_guard.py]]", "[[Security Modules/egress_filter.py|egress_filter.py]]", "[[Data Flow]]"]
status: documented
---

# input_normalizer.py

## Purpose
Pre-processes text before all security scanning by stripping encoding tricks, invisible Unicode characters, and HTML/URL encoding that would allow malicious payloads to bypass regex-based detection patterns.

## Threat Model
Encoding-based scanner evasion — attackers using fullwidth Unicode characters, zero-width spaces, HTML entities, URL percent-encoding, or base64 payloads to disguise injection patterns so they pass through regex-based filters undetected.

## Responsibilities
- Apply NFKC Unicode normalization to collapse fullwidth chars (e.g., `ｉｇｎｏｒｅ` → `ignore`) and compatibility ligatures
- Strip zero-width and invisible Unicode characters (zero-width spaces, soft hyphens, BOM, word joiners, invisible math operators, Mongolian vowel separator, interlinear annotations)
- Decode HTML entities (e.g., `&lt;system&gt;` → `<system>`)
- URL-decode percent-encoded sequences (single pass; only applied if decoded result contains alphabetic characters, preventing double-decode attacks)
- Collapse excessive whitespace (3+ spaces → 2 spaces; 4+ newlines → 3 newlines)
- Detect base64-encoded payloads that decode to human-readable / instruction-like text
- Strip potentially malicious Markdown from tool results (images, template-variable links, exfil-pattern links)

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `_INVISIBLE_CHARS` | Compiled regex | Matches 13 zero-width/invisible Unicode code points |
| `_MULTI_SPACE` | Compiled regex | Matches 3+ consecutive spaces or tabs |
| `_MULTI_NEWLINE` | Compiled regex | Matches 4+ consecutive newlines |
| `normalize_input()` | Function | Main normalization pipeline; returns cleaned string |
| `detect_base64_payloads()` | Function | Finds and decodes base64 strings that look like instructions |
| `strip_markdown_exfil()` | Function | Removes exfiltration-risk Markdown from tool outputs |

## Function Details

### normalize_input(text)
**Purpose:** Five-stage normalization pipeline applied before PromptGuard, ContextGuard, and ToolResultInjection scanners.
**Parameters:** `text` (str)
**Returns:** Normalized str (same reference if empty or non-string)
**Side effects:** None.

Normalization stages:
1. `unicodedata.normalize("NFKC", text)` — collapses compatibility characters
2. Strip `_INVISIBLE_CHARS` — removes zero-width and invisible code points
3. `html.unescape(text)` — decodes HTML entities
4. `urllib.parse.unquote(text)` — URL-decode (only if decoded differs and contains alpha chars)
5. Collapse `_MULTI_SPACE` to 2 spaces; `_MULTI_NEWLINE` to 3 newlines

### detect_base64_payloads(text)
**Purpose:** Scan for base64-like strings (min 20 chars), decode each, and return those that look like human-readable instructions (>60% word characters).
**Parameters:** `text` (str)
**Returns:** `list[str]` — decoded payloads that pass the word-character ratio heuristic
**Side effects:** None.

### strip_markdown_exfil(text)
**Purpose:** Remove Markdown constructs from tool results that could trigger data exfiltration:
- Markdown images with template variable URLs (`{{secret}}`, `${key}`, `SYSTEM`, `TOKEN`, etc.) → replaced with `[Image removed: potential data exfiltration]`
- All external Markdown images → replaced with `[Image: alt-text]`
- Links to URLs matching exfil patterns (`exfil`, `leak`, `steal`, `callback`, `webhook`, etc.) → replaced with `[Link removed: suspicious URL pattern]`

**Parameters:** `text` (str)
**Returns:** Sanitized str
**Side effects:** None.

## Invisible Characters Stripped

| Code Points | Description |
|-------------|-------------|
| U+200B–U+200F | Zero-width spaces, directional marks |
| U+00AD | Soft hyphen |
| U+FEFF | Byte Order Mark (BOM) |
| U+2060 | Word joiner |
| U+2061–U+2064 | Invisible math operators |
| U+180E | Mongolian vowel separator |
| U+FFF9–U+FFFB | Interlinear annotation anchors |

## Mode: Enforce vs Monitor
This module does not have an enforce/monitor mode. It always normalizes. Downstream scanners decide what to do with normalized output.

## Environment Variables
None.

## Usage Context
Called by:
- `PromptGuard.scan()` — as the first step before pattern matching
- `PromptGuard._check_encoded_content()` — indirectly via `detect_base64_payloads()`
- Any pipeline stage that scans tool results should call `strip_markdown_exfil()` on tool output before presenting it to the LLM

## Related
- [[Data Flow]]
- [[Security Modules/prompt_guard.py|prompt_guard.py]]
- [[Security Modules/egress_filter.py|egress_filter.py]]
