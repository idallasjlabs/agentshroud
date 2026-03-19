---
title: browser-fetch.js
type: module
file_path: docker/scripts/ (or similar)
tags: [javascript, browser, playwright, fetch]
related: [Security Modules/browser_security.py, Dependencies/playwright, Proxy Layer/web_proxy.py]
status: inferred
---

# browser-fetch.js

> **Note:** This note is inferred from the project structure. The exact file location may differ — check `docker/scripts/` or OpenClaw's skill directories.

## Purpose

Browser automation script using Playwright for fetching and interacting with web pages. Used by the `browser-fetch` skill in OpenClaw to access JavaScript-heavy sites that regular HTTP clients can't handle.

## Expected Behavior

Based on the broader project context:
- Launches a sandboxed Chromium instance
- Navigates to the requested URL
- Extracts page content (text, HTML, or rendered DOM)
- Returns content to the agent for processing
- All fetched content passes through `web_proxy.py` and `web_content_scanner.py` for PII scanning

## Security Controls

| Control | Implementation |
|---------|---------------|
| URL allowlisting | `url_analyzer.py` validates URLs before browser opens them |
| Content scanning | `web_content_scanner.py` scans fetched content |
| PII removal | Presidio scans fetched content before returning to agent |
| Sandboxed context | Playwright isolated browser context per request |
| Browser security | `browser_security.py` fingerprinting and isolation |

## Related Notes

- [[Security Modules/browser_security.py|browser_security.py]] — Browser security controls
- [[Proxy Layer/web_proxy.py|web_proxy.py]] — Web content proxy
- [[Proxy Layer/url_analyzer.py|url_analyzer.py]] — URL validation
- [[Dependencies/playwright]] — Playwright browser engine
