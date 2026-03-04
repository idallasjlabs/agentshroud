---
title: egress_config.py
type: module
file_path: gateway/security/egress_config.py
tags: [security, egress-filtering, allowlist, denylist, data-exfiltration, network-control]
related: [[egress_monitor.py]], [[key_vault.py]], [[subagent_monitor.py]]
status: documented
---

# egress_config.py

## Purpose
Defines the configuration model for the AgentShroud egress filter, including default domain allowlists, denylists of known exfiltration targets, per-agent allowlist overrides, port restrictions, and operating mode (enforce vs. monitor). Provides a global configuration singleton and environment-variable-based initialization.

## Threat Model
Defends against data exfiltration by AI agents through network egress. Specific threat vectors addressed: paste-site exfiltration (Pastebin, Hastebin, and 15+ similar services), file-sharing service exfiltration (WeTransfer, MediaFire, etc.), URL-shortener-mediated exfiltration (obfuscating the true destination), and Discord webhook abuse. The allowlist-default-deny model ensures that only explicitly permitted domains can receive outbound traffic from agent containers.

## Responsibilities
- Define the default allowlist of permitted domains for agent operation (AI APIs, email, communication, package registries)
- Define the default denylist of known exfiltration-risk domains
- Support per-agent allowlist overrides to extend permissions for specific agent IDs
- Provide wildcard pattern matching with single-subdomain expansion (`*.domain.com` matches `sub.domain.com` but not `a.sub.domain.com`)
- Support CIDR-notation IP allowlists and port restrictions (default: 80, 443 only)
- Operate in `enforce` mode (block non-allowlisted) or `monitor` mode (log only)
- Load configuration from environment variables (`AGENTSHROUD_MODE`, `AGENTSHROUD_EGRESS_MODE`)
- Provide global config getter and setter for runtime updates

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `EgressFilterConfig` | Dataclass | Full egress filter configuration model |
| `EgressFilterConfig.from_environment` | Class method | Creates a config instance from environment variables |
| `EgressFilterConfig.get_effective_allowlist` | Method | Returns the effective allowlist for a given agent ID |
| `EgressFilterConfig.is_denylisted` | Method | Checks if a domain matches the denylist |
| `EgressFilterConfig._matches_any_pattern` | Method | Wildcard-aware domain pattern matching |
| `get_egress_config` | Function | Returns the global config singleton |
| `set_egress_config` | Function | Replaces the global config singleton |

## Function Details

### EgressFilterConfig.from_environment()
**Purpose:** Checks `AGENTSHROUD_MODE` and `AGENTSHROUD_EGRESS_MODE` environment variables to determine operating mode. `AGENTSHROUD_EGRESS_MODE` takes precedence over `AGENTSHROUD_MODE`. Defaults to `"monitor"` if neither is set or set to a recognized value.
**Returns:** `EgressFilterConfig` instance

### EgressFilterConfig.get_effective_allowlist(agent_id)
**Purpose:** Starts with `default_allowlist`, merges any agent-specific overrides from `agent_allowlists[agent_id]`, and in strict mode removes any domain that matches a denylist pattern.
**Parameters:** `agent_id` (str)
**Returns:** `set[str]`

### EgressFilterConfig.is_denylisted(domain)
**Purpose:** Checks whether a domain matches any pattern in `default_denylist` using the wildcard matcher.
**Parameters:** `domain` (str)
**Returns:** `bool`

### EgressFilterConfig._matches_any_pattern(domain, patterns)
**Purpose:** Normalizes domains to lowercase with trailing dot stripped. Supports `*.` prefix for single-level subdomain matching. Exact matches also evaluated.
**Parameters:** `domain` (str), `patterns` (list[str])
**Returns:** `bool`

## Configuration / Environment Variables

| Variable | Effect |
|---|---|
| `AGENTSHROUD_MODE=enforce` | Sets egress mode to `enforce` |
| `AGENTSHROUD_EGRESS_MODE=enforce` | Overrides egress mode specifically to `enforce` |
| `AGENTSHROUD_EGRESS_MODE=monitor` | Overrides egress mode specifically to `monitor` |

Default mode is `monitor` if no variables are set.

## Default Allowlist

| Category | Domains |
|---|---|
| AI APIs | `api.anthropic.com`, `api.openai.com` |
| Email | `imap.gmail.com`, `smtp.gmail.com`, `*.icloud.com` |
| Communication | `api.telegram.org` |
| Search | `api.brave.com` |
| Dev/Package | `*.github.com`, `*.githubusercontent.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` |

## Default Denylist Categories
- Paste sites: Pastebin, Hastebin, Pastie, Paste.ee, DPaste, ControlC, Paste2, Ghostbin, Snipplr, Rentry, and others
- File sharing: WeTransfer, SendSpace, MediaFire, ZippyShare, TempMail, 10MinuteMail
- URL shorteners: bit.ly, tinyurl.com, t.co, goo.gl, ow.ly, short.link, tiny.one
- Webhook abuse: `discord.com/api/webhooks`

## Related
- [[egress_monitor.py]]
- [[key_vault.py]]
- [[subagent_monitor.py]]
