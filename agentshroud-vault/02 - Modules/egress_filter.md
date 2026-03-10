---
title: egress_filter.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/security/egress_filter.py
tags: [#type/module, #status/critical]
related: ["[[pipeline]]", "[[lifespan]]", "[[agentshroud.yaml]]", "[[AGENTSHROUD_MODE]]"]
status: active
last_reviewed: 2026-03-09
---

# egress_filter.py — Outbound Domain Allowlist Enforcement

## Purpose

Enforces domain-level egress policy — only allows outbound connections to explicitly whitelisted domains. Operates in `enforce` (block) or `monitor` (log-only) mode. Supports per-bot policies layered on top of a global default.

## Key Classes

### `EgressPolicy`
Defines allowed domains, IPs, and ports for an agent.

```python
@dataclass
class EgressPolicy:
    allowed_domains: list[str]  # supports wildcards: "*.github.com"
    allowed_ips: list[str]      # CIDR or single IP
    allowed_ports: list[int]    # default: [80, 443]
    deny_all: bool = True       # default-deny
```

**Wildcard matching:** `*.github.com` matches `foo.github.com` but NOT `foo.bar.github.com` (one level only).

### `EgressFilter`
Main class. Holds global default policy + per-agent overrides.

```python
class EgressFilter:
    def __init__(self, default_policy: EgressPolicy):
        self._default_policy = default_policy
        self._agent_policies: dict[str, EgressPolicy] = {}
        self._attempts: list[EgressAttempt] = []
        self._notifier = None   # EgressTelegramNotifier (wired in lifespan)
        self._audit_store = None  # AuditStore (wired in lifespan GAP-1)
```

## Methods

### `check(destination, agent_id, port) → EgressAction`

Main check method. Called for every outbound connection attempt.

1. Resolve effective policy (per-agent override or global default)
2. Parse destination as domain or IP
3. Check domain against allowlist (supports wildcards)
4. Check IP against CIDR list
5. Return `EgressAction.ALLOW` or `EgressAction.DENY`
6. Log attempt; notify via Telegram on DENY; persist to AuditStore

### `set_agent_policy(agent_id, policy)`

Register a per-bot egress policy. Called in [[lifespan]] for each bot that has `egress_domains` in its `BotConfig`.

### `set_notifier(notifier)`

Wire in `EgressTelegramNotifier` for real-time Telegram alerts on denial events.

## Global Allowlist (from lifespan)

```python
EgressPolicy(allowed_domains=[
    "api.anthropic.com",
    "api.openai.com",
    "imap.gmail.com",
    "smtp.gmail.com",
    "*.googleapis.com",
    "api.telegram.org",
] + config.proxy_allowed_domains)  # from agentshroud.yaml proxy.allowed_domains
```

## proxy.allowed_domains (from agentshroud.yaml)

Additional domains from YAML `proxy:` section include:
- `api.openai.com`, `api.anthropic.com`, `api.telegram.org`
- `oauth2.googleapis.com`, `*.google.com`
- `*.github.com`, `*.githubusercontent.com`
- `imap.mail.me.com`, `smtp.mail.me.com`
- `*.1password.com`, `*.1password.ca`, `*.agilebits.com`
- `host.docker.internal`, `marvin`, `trillian`, `raspberrypi`

## Mode Behavior

| Mode | DENY behavior |
|------|--------------|
| `enforce` | Returns `EgressAction.DENY`, logs, notifies |
| `monitor` | Logs only, returns `EgressAction.ALLOW` |

Mode is set via `get_module_mode(config, "egress_filter")` — can be overridden globally with [[AGENTSHROUD_MODE]].

## Environment Variables Used

- [[AGENTSHROUD_MODE]] — `monitor` disables enforcement

## Related

- [[pipeline]] — EgressFilter is step 5 in the outbound pipeline
- [[lifespan]] — initializes EgressFilter with default + per-bot policies
- [[agentshroud.yaml]] — `proxy.allowed_domains` and `bots[*].egress_domains`
