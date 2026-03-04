---
title: playwright
type: dependency
tags: [browser, automation, nodejs]
related: [Dependencies/All Dependencies, Containers & Services/agentshroud-bot, Security Modules/browser_security.py]
status: documented
---

# Playwright

**Package:** `playwright` (npm) + Chromium browser
**Version:** latest
**Used in:** Bot container (browser automation skill)

## Purpose

Playwright enables the OpenClaw agent to interact with web browsers. The `browser-fetch` skill uses Playwright to:
- Navigate web pages
- Extract content from JavaScript-heavy sites
- Take screenshots
- Fill forms

## Container Integration

```dockerfile
RUN npm install -g playwright@latest && \
    npx playwright install --with-deps chromium
```

Chromium binaries are stored in the `agentshroud-browsers` volume for persistence across restarts.

## Security Controls

All Playwright browser operations are subject to:
- `OPENCLAW_SANDBOX_MODE=strict` — sandboxed contexts
- `browser_security.py` — browser fingerprinting and isolation
- Web content passes through `web_proxy.py` and `web_content_scanner.py` for PII scanning
- URL validation via `url_analyzer.py`

## Volume

Browser binaries: `agentshroud-browsers` volume at `/home/node/.cache/ms-playwright`

Persistent volume prevents ~400-600 MB re-download on every restart.

## Related Notes

- [[Security Modules/browser_security.py|browser_security.py]] — Browser security controls
- [[Proxy Layer/web_proxy.py|web_proxy.py]] — Web content proxy
- [[Containers & Services/volumes]] — `agentshroud-browsers` volume
- [[Dependencies/All Dependencies]] — Full dependency list
