---
title: agentshroud.yaml
type: config
file_path: agentshroud.yaml
tags: [configuration, security, gateway]
related: [Gateway Core/config.py, Configuration/All Environment Variables, Architecture Overview]
status: documented
---

# agentshroud.yaml

**Location:** `agentshroud.yaml` (repo root)
**Mounted into gateway:** `/app/agentshroud.yaml` (read-only)
**Loaded by:** [[Gateway Core/config.py|config.py]] `load_config()`

## Purpose

Master configuration file for the AgentShroud gateway. Controls all security postures, network policies, PII redaction rules, channel permissions, SSH host allowlists, and MCP tool permissions. The gateway reads this on startup and re-reads it only on restart.

## Config Search Order

1. Explicit path argument to `load_config()`
2. `$AGENTSHROUD_CONFIG` environment variable
3. `./agentshroud.yaml` (relative to CWD)
4. `../agentshroud.yaml`

---

## Top-Level Sections

| Section | Purpose |
|---------|---------|
| `security` | PII redaction, network isolation, approval queue |
| `gateway` | Bind address, port, auth, ledger, router |
| `proxy` | HTTP CONNECT proxy mode, port, allowed domains |
| `container` | Runtime (podman/docker), resource limits |
| `agentshroud` | Version, model, ports |
| `shortcuts` | iOS/macOS Shortcuts endpoint and auth |
| `browser_extension` | Browser extension domain filters, privacy settings |
| `dashboard` | Dashboard bind/port, kill switch |
| `telemetry` | Telemetry disabled flag |
| `logging` | Log level, rotation settings |
| `channels` | Email, Telegram, iMessage permissions |
| `mcp_proxy` | Per-server and per-tool MCP permissions |
| `ssh` | SSH proxy host allowlist |
| `security_modules` | Per-module enforce/monitor mode |

---

## security section

```yaml
security:
  network_isolation: true
  allowed_networks:
    - "0.0.0.0/0"        # Internet
  blocked_networks:
    - "192.168.0.0/16"   # RFC1918
    - "10.0.0.0/8"
    - "172.16.0.0/12"
  pii_min_confidence: 0.9
  pii_redaction: true
  pii_detection_engine: "presidio"
  redaction_rules:
    - type: "SSN"
    - type: "CREDIT_CARD"
    - type: "PHONE_NUMBER"
    - type: "EMAIL_ADDRESS"
    - type: "STREET_ADDRESS"
  approval_queue: true
  require_approval_for:
    - email_sending
    - file_deletion
    - external_api_calls
    - skill_installation
```

**Key:** `pii_min_confidence: 0.9` — raise to reduce false positives; lower to catch more PII at the cost of more false redactions.

---

## gateway section

```yaml
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_method: "shared_secret"
  auth_token: ""   # empty = auto-generated; set via GATEWAY_AUTH_TOKEN_FILE
  ledger_database: "sqlite:///data/ledger.db"
  retention_days: 90
  router_enabled: true
  default_agent: "general"
```

**Auth token resolution order:**
1. `$GATEWAY_AUTH_TOKEN_FILE` (Docker secret file)
2. `auth_token` in this file
3. Auto-generated 32-byte hex (logged to stdout as warning)

---

## proxy section

```yaml
proxy:
  mode: allowlist   # default-deny egress
  listen_port: 8181
  allowed_domains:
    - api.openai.com
    - api.anthropic.com
    - api.telegram.org
    - oauth2.googleapis.com
    - www.googleapis.com
    - "*.github.com"
    - "*.githubusercontent.com"
    - imap.mail.me.com
    - smtp.mail.me.com
```

**Adding new domains:** Append to `allowed_domains` and restart the gateway.

---

## mcp_proxy section

```yaml
mcp_proxy:
  servers:
    mac-messages:
      transport: http_sse
      url: "http://host.docker.internal:8200"
      timeout_seconds: 30
      tools:
        tool_send_message:
          permission_level: write
          rate_limit: 30
          sensitive: true
        tool_get_recent_messages:
          permission_level: read
          rate_limit: 60
```

**Permission levels:** `read` (inspection only) or `write` (mutations allowed).
**rate_limit:** Max calls per minute. Exceeding this returns 429.

---

## ssh section

```yaml
ssh:
  enabled: true
  require_approval: false
  global_denied_commands:
    - "rm -rf /"
    - "mkfs"
    - "dd if="
  hosts:
    pi:
      host: "raspberrypi.tail240ea8.ts.net"
      port: 22
      username: "agentshroud-bot"
      key_path: "/var/agentshroud-ssh/id_ed25519"
      max_session_seconds: 300
```

**Adding a new SSH host:** Add entry under `ssh.hosts` with host, port, username, key_path, and max_session_seconds.

---

## security_modules section

```yaml
security_modules:
  pii_sanitizer:
    mode: enforce      # or: monitor
    action: redact     # or: block
  prompt_guard:
    mode: enforce
  egress_filter:
    mode: enforce
  mcp_proxy:
    mode: enforce
```

**Global override:** Set `$AGENTSHROUD_MODE=monitor` to put ALL modules in monitor mode (log only, no blocking). Never use in production.

---

## channels section

```yaml
channels:
  email:
    enabled: true
    provider: icloud
    allowed_recipients: []   # empty = all require approval
    rate_limit_per_hour: 10
    require_approval_for_new: true
  telegram:
    enabled: true
  imessage:
    enabled: true
    allowed_recipients:
      - "+13015188813"
    rate_limit_per_hour: 30
    require_approval_for_new: true
```

---

## Related Notes

- [[Gateway Core/config.py|config.py]] — Pydantic models that validate this file
- [[Configuration/All Environment Variables]] — Env vars that override config values
- [[Security Modules/egress_filter.py|egress_filter.py]] — Reads `proxy.allowed_domains`
- [[Proxy Layer/mcp_config.py|mcp_config.py]] — Reads `mcp_proxy` section
- [[Gateway Core/auth.py|auth.py]] — Reads `gateway.auth_token`
