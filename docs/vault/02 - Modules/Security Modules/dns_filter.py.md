---
title: dns_filter.py
type: module
file_path: gateway/security/dns_filter.py
tags: [security, dns, exfiltration, tunneling, entropy, allowlist]
related: ["[[Security Modules/egress_filter.py|egress_filter.py]]", "[[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]", "[[Data Flow]]"]
status: documented
---

# dns_filter.py

## Purpose
Detects and optionally blocks DNS-based data exfiltration (DNS tunneling) by analyzing query patterns for high-entropy subdomains, hex/base64-encoded labels, abnormal label lengths, rate-limiting violations, and domain allowlist compliance.

## Threat Model
DNS tunneling and covert channel exfiltration — a compromised agent encoding and transmitting data by embedding it in DNS query subdomains (e.g., `aGVsbG8=.evil.com`), bypassing HTTP-level egress controls since DNS is often allowed unconditionally.

## Responsibilities
- Check each DNS query against an optional allowlist (suffix matching, not prefix)
- Detect tunneling indicators in subdomain labels: long labels, hex-encoded labels, base64-encoded labels, high Shannon entropy
- Detect excessive subdomain total length
- Rate-limit queries per agent to `max_queries_per_minute`
- In monitor mode: flag and log all suspicious queries, allow all
- In enforce mode: block queries that fail the allowlist check or match tunneling patterns
- Maintain a bounded in-memory audit log (max 50,000 entries, halved on overflow)
- Expose audit log retrieval and flagged query filtering

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `EntropyCalculator` | Class | Static Shannon entropy calculation |
| `DNSFilterConfig` | Dataclass | All tunable parameters |
| `DNSQuery` | Dataclass | Audit record of one DNS query |
| `DNSVerdict` | Dataclass | allowed (bool), flagged (bool), reason (str) |
| `TunnelingPattern` | Dataclass | Detected pattern: type, label, score |
| `DNSFilter` | Class | Main filter |
| `DNSFilter.check()` | Method | Evaluate one DNS query; returns DNSVerdict |
| `DNSFilter._detect_tunneling()` | Method | Per-label pattern detection |
| `DNSFilter._domain_in_allowlist()` | Method | Suffix-based allowlist match |
| `DNSFilter.get_audit_log()` | Method | All or per-agent audit entries |
| `DNSFilter.get_flagged_queries()` | Method | Filtered view of flagged-only entries |

## Function Details

### DNSFilter.check(domain, agent_id)
**Purpose:** Evaluate a single DNS query for tunneling indicators and allowlist compliance. Records result in the audit log.
**Parameters:**
- `domain` (str) — fully qualified domain name being queried
- `agent_id` (str) — agent making the query
**Returns:** `DNSVerdict(allowed, flagged, reason)`
**Side effects:** Appends to `_audit`; updates `_query_times` for rate limiting; emits `logger.warning` if flagged.

### DNSFilter._detect_tunneling(domain)
**Purpose:** Inspect each subdomain label (excluding the registered domain and TLD) for:
- Length exceeding `max_label_length` (default 50) → `long_label`
- Match against `^[0-9a-f]{24,}$` → `hex_encoding`
- Match against `^[A-Za-z0-9+/]{20,}={0,2}$` → `base64_encoding`
- Shannon entropy >= `entropy_threshold` (default 4.0) on labels >= 12 chars → `high_entropy`
- Total subdomain string length exceeding `max_subdomain_length` (default 80) → `long_subdomain`
**Returns:** `list[TunnelingPattern]`

### EntropyCalculator.shannon_entropy(s)
**Purpose:** Compute Shannon entropy in bits per character using character frequency.
**Returns:** float — 0.0 for empty strings; higher values (>4.0) indicate encoded/random data.

## Configuration (DNSFilterConfig)

| Field | Default | Description |
|-------|---------|-------------|
| `mode` | `"monitor"` | `"monitor"` or `"enforce"` |
| `allowed_domains` | None | Allowlist; None = allow all domains |
| `max_subdomain_length` | 80 | Max combined subdomain length |
| `max_label_length` | 50 | Max single label length |
| `entropy_threshold` | 4.0 | Shannon entropy threshold for high-entropy flag |
| `max_queries_per_minute` | 120 | Rate limit per agent |
| `hex_pattern_min_length` | 24 | Min hex label length to flag |
| `base64_pattern_min_length` | 20 | Min base64 label length to flag |

## Mode: Enforce vs Monitor
- **monitor**: All DNS queries are allowed (`allowed=True`). Suspicious queries are flagged and logged but not blocked.
- **enforce**: Queries failing the allowlist check OR matching tunneling patterns are denied (`allowed=False`). Rate-limit violations are flagged but do not block in either mode (informational only in current implementation).

## Environment Variables
None. Configuration is passed via `DNSFilterConfig` at instantiation.

## Allowlist Behavior
- `allowed_domains=None` — no allowlist enforced; all domains pass the allowlist check
- Allowlist matching uses suffix matching: `evil.com` in the allowlist matches `sub.evil.com` and `evil.com`
- Unlike `EgressFilter`, DNS allowlist does not use wildcard `*.` notation; any suffix match is accepted

## Audit Log
- Max 50,000 entries (`MAX_AUDIT_ENTRIES`). On overflow, the oldest half is evicted.
- Each `DNSQuery` entry contains: timestamp, agent_id, domain, allowed, flagged, reason.

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/egress_filter.py|egress_filter.py]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
