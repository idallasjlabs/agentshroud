---
title: Dockerfile.bot
type: config
file_path: docker/Dockerfile.agentshroud
tags: [docker, build, bot, nodejs]
related: [Configuration/docker-compose.yml, Containers & Services/agentshroud-bot, JavaScript/mcp-proxy-wrapper.js]
status: documented
---

# Dockerfile — Bot (OpenClaw)

**Location:** `docker/Dockerfile.agentshroud`
**Runtime:** Node.js 22
**Base image:** `node:22-bookworm-slim`
**Exposes:** Port 18789
**User:** `node` (UID 1000, non-root)

## Build Process

```
node:22-bookworm-slim
├── apt: openssh-client, git, curl, ca-certificates, unzip
├── apt: libopenscap25, openscap-scanner
├── apt: gosu, clamav, clamav-daemon
├── curl install: trivy
├── npm install -g bun@latest
├── corepack enable (pnpm support)
├── npm install -g openclaw@latest        # OpenClaw agent platform
├── patch-anthropic-sdk.sh                # Route LLM → gateway:8080
├── npm install -g playwright@latest
├── npx playwright install --with-deps chromium
├── patch-telegram-sdk.sh                 # Route Telegram → gateway:8080
├── 1Password CLI v2.32.0 (multi-arch)
├── mkdir /home/node/.agentshroud
├── ln -s ~/.agentshroud ~/.openclaw     # Symlink for OpenClaw compatibility
├── COPY config-defaults/openclaw/       # Default OpenClaw config
├── COPY config-defaults/ssh/            # SSH allowlist config
├── COPY docker/scripts/*.sh → /usr/local/bin/
├── COPY mcp-proxy-wrapper.js
├── USER node
├── EXPOSE 18789
└── CMD ["/usr/local/bin/start-agentshroud.sh"]
```

## Security Patches Applied at Build Time

| Patch | Script | Effect |
|-------|--------|--------|
| Anthropic SDK routing | `patch-anthropic-sdk.sh` | All LLM API calls go to `$ANTHROPIC_BASE_URL` (gateway:8080) |
| Telegram SDK routing | `patch-telegram-sdk.sh` | All Telegram API calls go to `$TELEGRAM_API_BASE_URL` |

> These patches are baked into the image at build time so they cannot be bypassed by environment variable manipulation after container start.

## Pre-installed Tools

| Tool | Purpose |
|------|---------|
| OpenClaw | AI agent platform (MCP, skills, agents) |
| Playwright + Chromium | Browser automation for `browser-fetch` skill |
| 1Password CLI v2.32.0 | Secret retrieval (proxied through gateway) |
| ClamAV | Malware scanning |
| Trivy | Vulnerability scanning |
| gosu | Privilege dropping helper |
| bun | Fast JS runtime (used by some OpenClaw tools) |

## Scripts Copied to `/usr/local/bin`

| Script | Purpose |
|--------|---------|
| `start-agentshroud.sh` | Container entrypoint — loads secrets, starts OpenClaw |
| `op-wrapper.sh` | Routes `op read` through gateway op-proxy |
| `init-openclaw-config.sh` | Applies config defaults on every startup |
| `mcp-proxy-wrapper.js` | Intercepts MCP stdio calls |
| `1password-skill.sh` | Agent skill for 1Password access |
| `get-credential.sh` | Credential retrieval helper |
| `security-entrypoint.sh` | Security scan entrypoint |
| `security-scheduler.sh` | Scheduled security scan runner |

## Config Defaults (Baked In)

`/app/config-defaults/openclaw/` — Applied by `init-openclaw-config.sh` at each startup:
- `apply-patches.js` — Idempotent OpenClaw JSON config patching
- Default agent settings, SSH allowlist, tool permissions

## Directory Structure

```
/home/node/
├── .agentshroud/        (volume: agentshroud-config)
├── .openclaw -> .agentshroud   (symlink)
├── .ssh/                (volume: agentshroud-ssh)
├── .cache/ms-playwright/ (volume: agentshroud-browsers)
└── agentshroud/
    └── workspace/       (volume: agentshroud-workspace)
```

## Image Labels (OCI)

```
org.opencontainers.image.title: AgentShroud Bot
org.opencontainers.image.version: 0.2.0
```

## TODO (from source)

- Pin base image to digest for reproducible builds: `FROM node:22-bookworm-slim@sha256:<digest>`
- Pin OpenClaw to specific version: `openclaw@X.Y.Z`

## Related Notes

- [[Configuration/Dockerfile.gateway]] — Gateway Dockerfile
- [[Containers & Services/agentshroud-bot]] — Runtime container details
- [[JavaScript/mcp-proxy-wrapper.js|mcp-proxy-wrapper.js]] — MCP intercept logic
- [[JavaScript/apply-patches.js|apply-patches.js]] — Config patching
- [[Startup Sequence]] — How start-agentshroud.sh works
