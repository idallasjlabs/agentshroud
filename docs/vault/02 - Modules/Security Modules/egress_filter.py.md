---
title: egress_filter.py
type: module
file_path: gateway/security/egress_filter.py
tags: [security, egress, network, allowlist, ssrf-protection, exfiltration]
related: ["[[Security Modules/dns_filter.py|dns_filter.py]]", "[[Security Modules/trust_manager.py|trust_manager.py]]", "[[Data Flow]]"]
status: documented
---

# egress_filter.py

## Purpose
Enforces a default-deny outbound network policy for AI agents using domain and IP allowlists. Every egress attempt is logged; in enforce mode, unlisted destinations and private IPs are blocked outright.

## Threat Model
Unauthorized data exfiltration — a compromised or misbehaving agent making outbound HTTP/HTTPS/TCP connections to attacker-controlled infrastructure, internal SSRF (Server-Side Request Forgery) targets, or any destination not explicitly approved by the operator.

## Responsibilities
- Parse destination as URL, `host:port`, bare hostname, or IP address
- Block private/loopback/link-local IPs unconditionally (SSRF protection) unless explicitly allowlisted
- Check port against an allowed port list (default: 80, 443)
- Check domain against a denylist (overrides allowlist in strict mode)
- Check domain against config-based and policy-based allowlists (wildcard `*.example.com` supported, one level deep only)
- Check IP/CIDR against config-based and policy-based IP allowlists
- In `enforce` mode: deny anything not matched by the above checks
- In `monitor` mode: allow everything but log all attempts
- Support per-agent `EgressPolicy` overrides on top of the global default
- Maintain an in-memory ring-buffer audit log (max 10,000 entries)
- Expose aggregate statistics (total / allowed / denied)

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `EgressAction` | Enum | ALLOW or DENY |
| `EgressAttempt` | Dataclass | Record of a single egress check: agent, destination, port, action, rule |
| `EgressPolicy` | Dataclass | Per-agent or global policy with allowed domains, IPs, and ports |
| `EgressFilter` | Class | Main filter — evaluates egress attempts against policies |
| `EgressFilter.check()` | Method | Primary evaluation entry point |
| `EgressFilter.set_agent_policy()` | Method | Override policy for a specific agent |
| `EgressFilter.get_log()` | Method | Retrieve recent egress attempts, optionally per-agent |
| `EgressFilter.get_stats()` | Method | Summary of allowed vs denied counts |
| `EgressPolicy.matches_domain()` | Method | Wildcard-safe domain matching |
| `EgressPolicy.matches_ip()` | Method | CIDR-aware IP matching |

## Function Details

### EgressFilter.check(agent_id, destination, port)
**Purpose:** Evaluate whether an agent's outbound connection attempt is permitted.
**Parameters:**
- `agent_id` (str) — identifier of the requesting agent
- `destination` (str) — URL, `host:port`, hostname, or IP
- `port` (int | None) — explicit port; inferred from URL scheme if None
**Returns:** `EgressAttempt` with the allow/deny decision and the matching rule description
**Side effects:** Appends to `_log`; emits `logger.warning` on deny, `logger.info` on allow.

### EgressPolicy.matches_domain(domain)
**Purpose:** Wildcard domain matching, deliberately limited to one subdomain level.
`*.github.com` matches `api.github.com` but NOT `a.api.github.com`.
**Returns:** bool

### EgressFilter._is_private_ip(host)
**Purpose:** Static method covering RFC 1918, loopback (v4+v6), link-local, IPv6 ULA, IPv4-mapped IPv6, and `localhost` hostname variants.
**Returns:** bool — True if private/reserved (i.e., should be blocked for SSRF)

### EgressFilter._record(agent_id, dest, port, action, rule)
**Purpose:** Constructs and stores an `EgressAttempt`; adds a human-readable `details` message for enforce-mode denies.
**Side effects:** Appends to `_log`; rotates log if over 10,000 entries.

## Configuration
Loaded via `gateway.security.egress_config.get_egress_config()` returning an `EgressFilterConfig` object. Relevant fields:

| Field | Description |
|-------|-------------|
| `mode` | `"enforce"` or `"monitor"` |
| `allowed_ips` | List of CIDR/IP strings |
| `get_effective_allowlist(agent_id)` | Returns merged domain allowlist for agent |
| `is_denylisted(domain)` | Returns True if domain is in the explicit denylist |

## Mode: Enforce vs Monitor
- **enforce**: Unknown domains are DENIED; port violations are DENIED; denylisted domains are DENIED. Private IPs are always DENIED regardless of mode.
- **monitor**: Unknown domains and port violations are ALLOWED but logged. Denylisted domains are ALLOWED but logged. Private IPs still denied.

## Environment Variables
None directly. Configuration is loaded from the egress config module which may read from `agentshroud.yaml` or environment variables at initialization.

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/dns_filter.py|dns_filter.py]]
- [[Security Modules/trust_manager.py|trust_manager.py]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
