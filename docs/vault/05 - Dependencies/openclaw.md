---
title: openclaw
type: dependency
tags: [agent, nodejs, platform, openclaw]
related: [Containers & Services/agentshroud-bot, Configuration/Dockerfile.bot, JavaScript/mcp-proxy-wrapper.js]
status: documented
---

# OpenClaw

**Package:** `openclaw` (npm)
**Version:** latest (pinned version recommended for production)
**Used in:** Bot container

## Purpose

OpenClaw is the autonomous AI agent platform that provides:
- Multi-provider LLM integration (Anthropic, OpenAI)
- MCP (Model Context Protocol) tool framework
- Skill system (reusable agent capabilities)
- Telegram bot integration
- Browser automation
- File and system tools

## Role in AgentShroud

OpenClaw is the **agent runtime**. AgentShroud wraps it with a security gateway. The gateway intercepts all outbound API calls from OpenClaw before they reach external services.

## Key Intercepted Paths

| OpenClaw Behavior | AgentShroud Interception |
|------------------|--------------------------|
| Sends LLM requests to `api.anthropic.com` | Redirected to gateway via `ANTHROPIC_BASE_URL` |
| Sends Telegram messages to `api.telegram.org` | Redirected via `TELEGRAM_API_BASE_URL` |
| Makes MCP tool calls (stdio) | Intercepted by `mcp-proxy-wrapper.js` |
| Accesses 1Password | Proxied through gateway op-proxy |

## Config Location

OpenClaw stores its config at `~/.openclaw/openclaw.json` (symlinked from `~/.agentshroud`).
Patched at startup by `apply-patches.js` with:
- Telegram bot token
- Gateway authentication credentials
- SSH allowlist
- Agent customizations

## Version Note

Currently installed as `openclaw@latest`. For production:
```dockerfile
RUN npm install -g openclaw@X.Y.Z
```

Pin to a specific version to avoid unexpected breaking changes.

## Related Notes

- [[Configuration/Dockerfile.bot]] — Installation
- [[Containers & Services/agentshroud-bot]] — Container that runs OpenClaw
- [[JavaScript/apply-patches.js|apply-patches.js]] — Config patching on startup
- [[JavaScript/mcp-proxy-wrapper.js|mcp-proxy-wrapper.js]] — MCP call interception
