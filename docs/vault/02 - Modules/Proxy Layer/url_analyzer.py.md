---
title: url_analyzer.py
type: module
file_path: gateway/proxy/url_analyzer.py
tags: [proxy, url-analysis, ssrf, pii, exfiltration, dns-rebinding]
related: [[web_proxy.py]], [[web_content_scanner.py]], [[web_config.py]]
status: documented
---

# url_analyzer.py

## Purpose
Analyzes outbound URLs for Server-Side Request Forgery (SSRF) attempts, PII exposure, and data exfiltration patterns. SSRF is the only hard block; all other findings produce a FLAG verdict that annotates the request without blocking it.

## Responsibilities
- Detect SSRF by matching hostnames against private IP ranges, localhost variants, decimal/hex/octal IP encodings
- Optionally resolve hostnames to IPs to catch SSRF via DNS (with explicit TOCTOU/rebinding warning)
- Provide `analyze_and_pin()` to resolve once and return the pinned IP so callers can use it for the actual connection (DNS rebinding mitigation)
- Detect PII patterns (email, SSN, phone, credit card) in the decoded URL string
- Detect possible base64-encoded data in URL path segments and query parameter values
- Detect suspiciously long query strings (> 2000 chars) and large parameter counts (> 30 params)
- Return a structured `URLAnalysisResult` with verdict and all findings

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `URLVerdict` | Enum | ALLOW, FLAG, BLOCK |
| `URLFinding` | Dataclass | Single finding: category, severity, description, detail |
| `URLAnalysisResult` | Dataclass | Full analysis: URL, verdict, findings, resolved IP, domain, is_ssrf flag |
| `URLAnalyzer` | Class | Main analyzer; optional DNS resolution via `resolve_dns` constructor flag |
| `_looks_like_base64(s)` | Function | Heuristic: checks charset, case mix, and decodability for base64 detection |

## Function Details

### URLAnalyzer.analyze(url)
**Purpose:** Full URL security analysis. Returns BLOCK verdict only for SSRF; FLAG for all other findings; ALLOW when clean.
**Parameters:** `url` (str).
**Returns:** `URLAnalysisResult`.

### URLAnalyzer.analyze_and_pin(url)
**Purpose:** Like `analyze()` but also resolves the hostname to an IP and verifies it is not private. Returns the resolved IP in `resolved_ip` so callers can connect to that IP directly, preventing DNS rebinding attacks between the security check and the actual request.
**Parameters:** `url` (str).
**Returns:** `URLAnalysisResult` with `resolved_ip` populated.

### URLAnalyzer._is_ssrf(hostname)
**Purpose:** Check if a hostname is a private address. Handles:
- Localhost name variants
- Direct private IP addresses
- IPv6 addresses
- Decimal-encoded IPs (e.g., `2130706433` = 127.0.0.1)
- Hexadecimal-encoded IPs (e.g., `0x7f000001`)
**Returns:** bool.

### URLAnalyzer._is_private_ip(ip_str)
**Purpose:** Check an IP string against all private/reserved networks including IPv4-mapped IPv6.
**Returns:** bool.

### URLAnalyzer._check_base64(parsed, result)
**Purpose:** Scan URL path segments and query parameter values for base64-like strings using the `_looks_like_base64` heuristic.

## SSRF Detection Coverage

| Encoding | Example | Detected |
|----------|---------|---------|
| Hostname | `localhost`, `ip6-localhost` | Yes |
| Direct private IP | `192.168.1.1`, `10.0.0.1` | Yes |
| Decimal IP | `2130706433` | Yes |
| Hex IP | `0x7f000001` | Yes |
| IPv6 | `::1`, `fc00::1` | Yes |
| IPv4-mapped IPv6 | `::ffff:127.0.0.1` | Yes |
| DNS-resolved private | `internal.corp.example.com` → `10.x.x.x` | Yes (with `resolve_dns=True`) |

## Configuration / Environment Variables
- `resolve_dns` (bool, default False) — enable DNS resolution for SSRF detection; adds latency
- Private networks checked: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 127.0.0.0/8, 169.254.0.0/16, IPv6 ULA/link-local

## Related
- [[web_proxy.py]]
- [[web_content_scanner.py]]
- [[web_config.py]]
