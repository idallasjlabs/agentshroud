---
title: web_config.py
type: module
file_path: gateway/proxy/web_config.py
tags: [proxy, web, configuration, domain-policy, rate-limiting, content-type]
related: [[web_proxy.py]], [[url_analyzer.py]], [[web_content_scanner.py]]
status: documented
---

# web_config.py

## Purpose
Defines the configuration model for the `WebProxy`. Controls domain filtering mode, allowlist and denylist entries, per-domain settings overrides, response size limits, rate limits, content type policies, and scanning flags. Default policy is denylist mode (default-allow) with SSRF always hard-blocked.

## Responsibilities
- Model per-domain overrides for response size, content type, rate limit, and timeout
- Support two domain policy modes: `"denylist"` (default-allow) and `"allowlist"` (default-deny)
- Allowlist matching supports wildcard prefix notation (`*.github.com` matches subdomains and the apex)
- Provide `is_domain_allowed()`, `is_domain_denied()`, and `get_domain_settings()` helpers with wildcard resolution
- Configure prompt injection scanning threshold and PII detection flags
- Configure passthrough/debug mode

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `DomainSettings` | Dataclass | Per-domain overrides: max response bytes, allowed content types, rate limit RPM, timeout |
| `WebProxyConfig` | Dataclass | Full web proxy configuration including domain lists, scan settings, and logging options |

## Function Details

### WebProxyConfig.is_domain_allowed(domain)
**Purpose:** Check if a domain is on the allowlist (used only when `mode == "allowlist"`). Supports exact match and `*.suffix` wildcard — matches both the suffix apex and all subdomains.
**Parameters:** `domain` (str).
**Returns:** bool.

### WebProxyConfig.get_domain_settings(domain)
**Purpose:** Return the `DomainSettings` for a domain, checking exact match then wildcard patterns, falling back to defaults.
**Parameters:** `domain` (str).
**Returns:** `DomainSettings`.

### WebProxyConfig.is_domain_denied(domain)
**Purpose:** Check if a domain is on the denylist. Matches exact domain and all subdomains of denied entries.
**Parameters:** `domain` (str).
**Returns:** bool.

## WebProxyConfig Fields

| Field | Default | Description |
|-------|---------|-------------|
| `denied_domains` | [evil.com, malware-payload.net, ...] | Hard-blocked domains in denylist mode |
| `mode` | `"denylist"` | `"denylist"` = default-allow; `"allowlist"` = default-deny |
| `allowed_domains` | [api.anthropic.com, api.telegram.org, *.github.com, ...] | Permitted domains in allowlist mode |
| `default_max_response_bytes` | 15MB | Response size limit before flagging |
| `default_rate_limit_rpm` | 120 | Per-domain request rate limit |
| `default_timeout_seconds` | 30.0 | Per-domain request timeout |
| `scan_responses` | True | Enable content scanning of response bodies |
| `prompt_injection_flag_threshold` | 0.3 | Score above which responses are flagged for injection |
| `detect_pii_in_urls` | True | Flag PII found in URLs |
| `detect_pii_in_responses` | True | Flag PII found in response bodies |
| `block_private_ips` | True | SSRF protection (always applied regardless of mode) |
| `passthrough_mode` | False | Log only; skip all security checks |
| `suspicious_content_types` | [x-executable, x-msdos-program, x-msdownload] | Content types that get flagged |

## Configuration / Environment Variables
- No direct environment variable bindings; constructed programmatically or from a config dict
- Wildcard support: `"*.github.com"` → matches `github.com` and `foo.bar.github.com`

## Related
- [[web_proxy.py]]
- [[url_analyzer.py]]
- [[web_content_scanner.py]]
