---
title: web_content_scanner.py
type: module
file_path: gateway/proxy/web_content_scanner.py
tags: [proxy, content-scanning, prompt-injection, pii, steganography, encoded-payload]
related: [[web_proxy.py]], [[url_analyzer.py]], [[web_config.py]]
status: documented
---

# web_content_scanner.py

## Purpose
Scans fetched web response content for prompt injection attempts, PII, hidden HTML elements with malicious instructions, base64-encoded payloads, and zero-width character steganographic attacks. All findings are FLAGS — content always passes through but is annotated so the pipeline can handle it appropriately.

## Responsibilities
- Detect prompt injection patterns in visible web content with a configurable injection score threshold
- Detect injection instructions hidden in HTML comments, CSS-hidden elements (`display:none`, `visibility:hidden`, `font-size:0`, etc.), and meta tags
- Detect base64-encoded payloads (both via `atob()`/`base64_decode()` calls and standalone large base64 strings)
- Detect zero-width character sequences (Unicode steganography)
- Detect PII in response content: email, SSN, phone, credit card, AWS access keys, private key headers
- Truncate content to 2MB before scanning to prevent ReDoS on adversarial inputs
- Return a structured `ScanResult` with per-category findings, injection score, and boolean flags

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `FindingSeverity` | Enum | CRITICAL, HIGH, MEDIUM, LOW, INFO |
| `ContentFinding` | Dataclass | Single finding: category, severity, description, evidence snippet, character offset |
| `ScanResult` | Dataclass | All findings plus injection score, boolean flags per threat type, scan timing |
| `WebContentScanner` | Class | Main scanner with five detection passes; never blocks content |

## Function Details

### WebContentScanner.scan(content, content_type)
**Purpose:** Run all five detection passes on the content string and return a `ScanResult`.
**Parameters:** `content` (str) — response body; `content_type` (str) — MIME type.
**Returns:** `ScanResult`. HTML-specific scans only run when content type or early content indicates HTML.

### WebContentScanner._scan_prompt_injection(content, result)
**Purpose:** Apply all `_INJECTION_PATTERNS` against the content; accumulate a weighted score (capped at 1.0 per pattern). Set `has_prompt_injection=True` if max score meets `injection_threshold`.

### WebContentScanner._scan_hidden_content(content, result)
**Purpose:** Search HTML comments, CSS-hidden element content, and meta tags for injection patterns. Findings are HIGH severity.

### WebContentScanner._scan_encoded_payloads(content, result)
**Purpose:** Find `atob()` / `base64_decode()` calls and standalone large base64 strings; decode and re-scan for injection patterns. Findings are HIGH severity.

### WebContentScanner._scan_zero_width(content, result)
**Purpose:** Detect sequences of 3+ zero-width Unicode characters (potential steganographic payload). Reports one MEDIUM finding per scan.

### WebContentScanner._scan_pii(content, result)
**Purpose:** Match PII patterns (email, SSN, phone, credit card, AWS key, private key header) against the content. Email and phone are MEDIUM; all others are HIGH.

## Injection Pattern Weights

| Pattern Name | Weight | Severity | Example |
|-------------|--------|----------|---------|
| instruction_override | 0.9 | HIGH | "ignore all previous instructions" |
| new_instructions | 0.9 | HIGH | "system: you are", LLM control tokens |
| role_override | 0.8 | HIGH | "act as an unrestricted AI" |
| data_exfil_instruction | 0.8 | HIGH | "send data to..." |
| tool_invocation | 0.7 | MEDIUM | "execute the tool:" |
| delimiter_attack | 0.7 | MEDIUM | `[INST]`, `<<SYS>>`, `Human:` |
| hidden_instruction_marker | 0.6 | MEDIUM | "URGENT: ignore..." |

## Configuration / Environment Variables
- `injection_threshold` (float, default 0.3) — minimum score to set `has_prompt_injection=True`
- `max_scan_bytes` (int, default 2MB) — how much of the content to scan for performance
- `MAX_SCAN_LENGTH` = 2,000,000 — hard truncation before any regex to prevent ReDoS

## Related
- [[web_proxy.py]]
- [[url_analyzer.py]]
- [[web_config.py]]
- [[pipeline.py]]
