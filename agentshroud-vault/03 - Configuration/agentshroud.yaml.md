---
title: agentshroud.yaml
type: config
file_path: /Users/ijefferson.admin/Development/agentshroud/agentshroud.yaml
tags: [#type/config, #status/critical]
related: ["[[config]]", "[[lifespan]]", "[[egress_filter]]", "[[prompt_guard]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# agentshroud.yaml — Master Configuration File

The single source of truth for all gateway security posture, bot declarations, proxy allowlists, and channel settings. Mounted read-only into the gateway container at `/app/agentshroud.yaml`.

## Section Reference

### `security:` — Network and PII Settings

```yaml
security:
  network_isolation: true
  blocked_networks:
    - "192.168.0.0/16"   # RFC1918 private — blocked outbound
    - "10.0.0.0/8"
    - "172.16.0.0/12"
  pii_min_confidence: 0.9  # High threshold = fewer false positives
  pii_redaction: true
  pii_detection_engine: "presidio"
  redaction_rules:
    - type: SSN
    - type: CREDIT_CARD
    - type: PHONE_NUMBER
    - type: EMAIL_ADDRESS
    - type: STREET_ADDRESS
  approval_queue: true
  require_approval_for:
    - email_sending
    - file_deletion
    - external_api_calls
    - skill_installation
```

> [!WARNING] `pii_min_confidence: 0.9` — was 0.8 in earlier versions. Increased to reduce false positives (over-redaction of normal text). Decrease for stricter redaction.

### `gateway:` — API Server Settings

```yaml
gateway:
  bind: "127.0.0.1"     # Host-only; never 0.0.0.0 in production
  port: 8080
  auth_method: "shared_secret"
  auth_token: ""        # REQUIRED: from Docker secret file
  ledger_database: "sqlite:///data/ledger.db"
  retention_days: 90
  router_enabled: true
```

### `proxy:` — HTTP CONNECT Proxy Allowlist

```yaml
proxy:
  mode: allowlist        # default-deny
  listen_port: 8181
  allowed_domains:
    - api.openai.com
    - api.anthropic.com
    - api.telegram.org
    - "*.github.com"
    - "*.1password.com"
    - host.docker.internal
    - marvin / trillian / raspberrypi  # SSH relay targets
```

> [!WARNING] `host.docker.internal` in the allowlist allows the bot to reach any service on the Docker host at its exposed ports. Be aware of what services are exposed on the host.

### `bots:` — Bot Declarations

```yaml
bots:
  openclaw:              # Bot ID (key)
    name: "OpenClaw"
    runtime: node
    hostname: agentshroud   # Docker service name
    port: 18789
    workspace_path: /home/node/.openclaw/workspace
    config_dir: /home/node/.openclaw
    dockerfile: docker/bots/openclaw/Dockerfile
    env_prefix: OPENCLAW_
    default: true
```

See [[bot_config]] for full field reference.

### `security_modules:` — Enforce/Monitor Per Module

```yaml
security_modules:
  pii_sanitizer:
    mode: enforce    # redacts PII
  prompt_guard:
    mode: enforce    # blocks injection
  egress_filter:
    mode: enforce    # blocks unauthorized domains
  mcp_proxy:
    mode: enforce    # enforces per-tool permissions
  dns_filter:
    mode: enforce    # blocks DNS tunneling
  subagent_monitor:
    mode: enforce    # limits concurrency
  egress_monitor:
    mode: enforce    # anomaly detection
  killswitch:
    mode: enforce    # live kill switch
```

> [!DANGER] Changing any of these to `monitor` disables blocking for that module. Only do this for debugging. Alternatively, set `AGENTSHROUD_MODE=monitor` env var to override ALL modules at once.

### `mcp_proxy:` — MCP Server Permissions

```yaml
mcp_proxy:
  servers:
    mac-messages:
      transport: http_sse
      url: "http://host.docker.internal:8200"
      tools:
        tool_send_message:
          permission_level: write
          rate_limit: 30        # 30 sends/minute
          sensitive: true
        tool_get_recent_messages:
          permission_level: read
          rate_limit: 60
```

### `ssh:` — SSH Proxy Configuration

```yaml
ssh:
  enabled: true
  hosts:
    pi:
      host: "raspberrypi"
      port: 22
      username: "agentshroud-bot"
      key_path: "/var/agentshroud-ssh/id_ed25519"
      max_session_seconds: 300
    marvin:
      host: "marvin"
      ...
    trillian:
      host: "trillian"
      ...
```

### `channels:` — Telegram, Email, iMessage

```yaml
channels:
  telegram:
    enabled: true
  email:
    enabled: true
    imap_host: imap.mail.me.com
    smtp_host: smtp.mail.me.com
    allowed_recipients: []
    rate_limit_per_hour: 10
  imessage:
    enabled: true
    allowed_recipients:
      - "+13015188813"   # Isaiah (US)
    rate_limit_per_hour: 30
    require_approval_for_new: true
```

## What Happens If This File Is Missing or Malformed

> [!DANGER] Gateway exits immediately at startup with `FileNotFoundError` or `ValueError`. Check the mount in `docker-compose.yml`:
> ```yaml
> volumes:
>   - ../agentshroud.yaml:/app/agentshroud.yaml:ro
> ```
> Verify the file exists and is valid YAML: `python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))"`

## Related

- [[config]] — the Python loader for this file
- [[lifespan]] — reads config at startup step 2
- [[egress_filter]] — uses `proxy.allowed_domains`
- [[sanitizer]] — uses `security.pii_*` settings
- [[prompt_guard]] — uses `security_modules.prompt_guard.mode`
