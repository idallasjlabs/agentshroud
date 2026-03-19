---
title: browser_security.py
type: module
file_path: gateway/security/browser_security.py
tags: [security, browser, social-engineering, phishing, url-validation, credential-protection]
related: [[consent_framework.py]], [[egress_config.py]], [[session_security.py]]
status: documented
---

# browser_security.py

## Purpose
Detects social engineering content and phishing URLs encountered by agents during browser-based tool usage. Provides fake popup/dialog detection via regex pattern matching, URL reputation checking with brand impersonation and homograph detection, credential entry protection, and an extensible screenshot analysis hook system.

## Threat Model
Addresses browser-based attacks against AI agents documented in Wu et al. 2026 (arXiv:2601.07263). A malicious website can display fake browser dialogs, tech support scam overlays, urgent credential re-entry prompts, or fake CAPTCHA challenges that instruct the agent to run shell commands. The module intercepts these attack patterns before the agent acts on the deceptive content.

## Responsibilities
- Analyze web page content for social engineering patterns (malware scares, phone scams, tech support scams, fake error codes, fake CAPTCHA/command execution, urgency manipulation, identity verification scams, account suspension threats)
- Check URL reputation for data URIs, homograph attacks (non-ASCII hostnames), brand impersonation in subdomains, lookalike domain spellings, raw IP address URLs, and excessive subdomain depth
- Block credential entry on non-HTTPS URLs, raw IP addresses, and lookalike domains
- Support pluggable screenshot analysis via registered hook callbacks
- Return structured `ThreatAssessment` objects with severity level and threat description list

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `BrowserSecurityGuard` | Class | Main guard; exposes content analysis, URL checking, credential gating, screenshot hooks |
| `ThreatAssessment` | Dataclass | Result of analysis: `threat_level` (`ThreatLevel`) and `threats` list of matched descriptions |
| `ThreatLevel` | IntEnum | Severity: NONE (0), LOW (1), MEDIUM (2), HIGH (3), CRITICAL (4) |
| `SocialEngineeringDetected` | Exception | (Declared; not raised by guard — used by callers as needed) |
| `PhishingURLDetected` | Exception | (Declared; not raised by guard — callers raise after `check_url_reputation`) |
| `CredentialEntryBlocked` | Exception | Raised by `can_enter_credentials` when a URL fails safety checks |

## Function Details

### BrowserSecurityGuard.analyze_content(content)
**Purpose:** Applies all social engineering regex patterns to the provided content string. Returns a `ThreatAssessment` with the highest matched severity and a list of all matched threat descriptions.
**Parameters:** `content` (str)
**Returns:** `ThreatAssessment`

### BrowserSecurityGuard.check_url_reputation(url)
**Purpose:** Evaluates a URL for multiple reputation signals: data URI, non-ASCII hostname (homograph), brand name appearing in non-authoritative subdomain position, lookalike character substitutions (g0ogle, payp@l, amaz0n, faceb00k), raw IP address, or 4+ subdomain levels.
**Parameters:** `url` (str)
**Returns:** `ThreatLevel` — `HIGH` for strong indicators, `LOW` for weak indicators, `NONE` for clean

### BrowserSecurityGuard.can_enter_credentials(url)
**Purpose:** Enforces safe credential entry rules. Allows localhost. Requires HTTPS for all other hosts. Blocks raw IP addresses and lookalike domain patterns. Blocks any URL with a HIGH+ reputation score.
**Parameters:** `url` (str)
**Returns:** `True` if safe; raises `CredentialEntryBlocked` with a descriptive message otherwise

### BrowserSecurityGuard.register_screenshot_hook(hook)
**Purpose:** Adds a callable that accepts `bytes` (image data) and returns a `ThreatAssessment`. Used to plug in LLM-based or OCR-based visual social engineering detection.
**Parameters:** `hook` — `Callable[[bytes], ThreatAssessment]`

### BrowserSecurityGuard.analyze_screenshot(image_data)
**Purpose:** Runs all registered screenshot hooks and returns the highest-severity `ThreatAssessment`. Returns `ThreatLevel.NONE` if no hooks are registered.
**Parameters:** `image_data` (bytes)
**Returns:** `ThreatAssessment`

## Social Engineering Patterns

| Pattern Description | Severity |
|---|---|
| Malware scare ("virus", "infected", "malware") | HIGH |
| Phone scam ("call now", "call immediately") | HIGH |
| Tech support scam ("Windows Defender alert") | HIGH |
| Fake error code ("Error #ABCD1234") | HIGH |
| Fake CAPTCHA / command execution ("Press Win", "powershell -e") | HIGH |
| Account suspension threat | MEDIUM |
| Urgency manipulation ("urgent", "immediately") | MEDIUM |
| Identity verification scam | MEDIUM |

## URL Reputation Signals

| Signal | Result |
|---|---|
| Data URI | HIGH |
| Non-ASCII hostname (homograph) | HIGH |
| Brand name in non-authoritative subdomain | HIGH |
| Lookalike character substitution | HIGH |
| Raw IP address | LOW |
| 4+ subdomain levels | LOW |

## Related
- [[consent_framework.py]]
- [[egress_config.py]]
- [[session_security.py]]
