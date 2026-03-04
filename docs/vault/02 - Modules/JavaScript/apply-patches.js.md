---
title: apply-patches.js
type: module
file_path: docker/config/openclaw/apply-patches.js
tags: [javascript, nodejs, configuration, openclaw]
related: [Configuration/Dockerfile.bot, Startup Sequence, JavaScript/mcp-proxy-wrapper.js]
status: documented
---

# apply-patches.js

**Location:** `docker/config/openclaw/apply-patches.js`
**Lines:** 262
**Runtime:** Node.js (inside bot container)
**Called by:** `init-openclaw-config.sh` (on every container startup)

## Purpose

Idempotent script that patches `~/.openclaw/openclaw.json` with required configuration on every container startup. Ensures that config required for AgentShroud's security model survives container rebuilds and volume resets.

## Behavior

- **If `openclaw.json` exists:** patches in-place, preserving all existing fields
- **If `openclaw.json` doesn't exist:** creates a minimal seed file for OpenClaw to inherit on first run
- **Idempotent:** safe to run on every startup — re-running produces the same result

## Patches Applied

### Patch 1: Main Agent as Default

Ensures `main` agent is first in `agents.list` (makes it the default agent):
```javascript
config.agents.list.unshift({ id: 'main', name: 'AgentShroud Main Agent' });
```

### Patch 2: Telegram Binding

Binds Isaiah's Telegram ID (`8096968754`) to the main agent:
```javascript
config.bindings.push({
  agentId: 'main',
  channel: 'telegram',
  userId: '8096968754'
});
```

### Patch 3: Telegram Bot Token (if $TELEGRAM_BOT_TOKEN is set)

Injects the Telegram bot token loaded from Docker secret:
```javascript
config.channels.telegram.botToken = process.env.TELEGRAM_BOT_TOKEN;
```

### Additional Patches

Based on the 262-line script, additional patches include:
- System prompt customizations
- Agent behavior configurations
- Channel enable/disable flags

## Usage

```bash
# Applied by init-openclaw-config.sh on every startup
node apply-patches.js /home/node/.openclaw/openclaw.json

# Or with default path:
node apply-patches.js
```

## Why Required

OpenClaw creates its config on first run from defaults. Without these patches:
- The wrong agent would be default
- Telegram messages might not route to the correct agent
- Bot token would not be injected (stays as empty string)

## Related Notes

- [[Configuration/Dockerfile.bot]] — Script is baked into the image
- [[Startup Sequence]] — Called by `init-openclaw-config.sh` at step 23d
- [[Dependencies/openclaw]] — OpenClaw platform being configured
