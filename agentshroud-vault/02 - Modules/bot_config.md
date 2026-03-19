---
title: bot_config.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/ingest_api/bot_config.py
tags: [#type/module, #status/active]
related: ["[[config]]", "[[lifespan]]", "[[agentshroud.yaml]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# bot_config.py — Per-Bot Protocol Specification

## Purpose

Defines the `BotConfig` Pydantic model — the contract that any bot must satisfy to be encapsulated by AgentShroud. Gateway code resolves all bot-specific values (hostnames, ports, workspace paths, endpoint paths) from this model, rather than from hardcoded OpenClaw-specific constants. This is what makes AgentShroud bot-agnostic.

## BotConfig Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | str | Yes | Unique identifier, e.g. `"openclaw"` |
| `name` | str | Yes | Human name, e.g. `"OpenClaw"` |
| `runtime` | str | No | `"node"` or `"python"` |
| `hostname` | str | Yes | Docker service hostname on isolated network |
| `port` | int | Yes | Bot HTTP port inside container |
| `health_path` | str | No | Default: `"/health"` |
| `chat_path` | str | No | Default: `"/chat"` |
| `webhook_path` | str | No | Default: `"/webhook"` |
| `workspace_path` | str | Yes | Workspace dir inside container |
| `config_dir` | str | Yes | Bot config dir inside container |
| `dockerfile` | str | No | Relative path to Dockerfile |
| `env_prefix` | str | No | Env var prefix e.g. `"OPENCLAW_"` |
| `egress_domains` | list[str] | No | Extra egress domains for this bot |
| `default` | bool | No | Whether this is the default routing target |

## Property: `base_url`

```python
@property
def base_url(self) -> str:
    return f"http://{self.hostname}:{self.port}"
```

Used by `RouterConfig` to compute `default_url`. For OpenClaw: `http://agentshroud:18789`.

## Current OpenClaw Config (from agentshroud.yaml)

```yaml
openclaw:
  name: "OpenClaw"
  runtime: node
  hostname: agentshroud
  port: 18789
  health_path: /health
  chat_path: /chat
  webhook_path: /webhook
  workspace_path: /home/node/.openclaw/workspace
  config_dir: /home/node/.openclaw
  dockerfile: docker/bots/openclaw/Dockerfile
  env_prefix: OPENCLAW_
  default: true
```

## Adding a New Bot

To add a second bot (e.g., `nanobot`):

1. Add to `agentshroud.yaml bots:` section (see commented `nanobot` example in YAML)
2. Create `docker/bots/nanobot/Dockerfile`
3. Implement the required HTTP endpoints:
   - `GET /health` → `{"status": "ok"}`
   - `POST /chat` → receive forwarded messages
   - `POST /webhook` → receive sanitized Telegram webhooks
4. Add service to `docker/docker-compose.yml`
5. Set `default: false` (only one bot can be default)

## Required Env Vars Set by AgentShroud on Bot Container

```
ANTHROPIC_BASE_URL=http://gateway:8080
HTTP_PROXY=http://gateway:8181
HTTPS_PROXY=http://gateway:8181
AGENTSHROUD_GATEWAY_PASSWORD=<gateway auth token>
AGENTSHROUD_BOT_ID=openclaw
AGENTSHROUD_WORKSPACE=/home/node/.openclaw/workspace
```

## Related

- [[agentshroud.yaml]] — where bot configs are declared
- [[config]] — `load_config()` parses YAML into `BotConfig` instances
- [[lifespan]] — iterates over `config.bots` to register agents and wire policies
- [[agentshroud-bot]] — the OpenClaw bot container implementation
