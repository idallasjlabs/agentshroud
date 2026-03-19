---
title: apply-patches.js
type: config
file_path: /Users/ijefferson.admin/Development/agentshroud/docker/bots/openclaw/config/apply-patches.js
tags: [#type/config, #status/critical]
related: ["[[agentshroud-bot]]", "[[bot_config]]", "[[patch-telegram-sdk.sh]]"]
status: active
last_reviewed: 2026-03-09
---

# apply-patches.js — OpenClaw Runtime Configuration Patches

## Purpose

A Node.js script that patches the live `openclaw.json` configuration file at bot startup. Modifies model selection, tool allow/deny lists, workspace path, and collaborator settings — without requiring a full image rebuild.

## When It Runs

Called by the bot entrypoint script (`start-agentshroud.sh`) before OpenClaw starts:
```sh
node /home/node/.agentshroud/apply-patches.js
```

## Key Patches Applied

| Setting | Value | Reason |
|---------|-------|--------|
| `maxTokens` | 2048 | Limits token usage per response |
| `model` | (from config) | Enforces approved model |
| `workspace` | `.agentshroud/collaborator-workspace` | Writable volume path (avoids read-only rootfs error) |
| Denied tools | `write`, `edit`, `web_search`, `web_fetch` | Restricts dangerous capabilities |
| Collaborator settings | Rate limit, disclosure | Applied to collaborator sessions |

## Collaborator Workspace Fix

**Problem:** `workspace: 'collaborator-workspace'` resolved to `/home/node/collaborator-workspace` — on the read-only rootfs, `mkdir` fails.

**Fix:** Changed to `.agentshroud/collaborator-workspace` which is inside the `agentshroud-config` volume at `/home/node/.agentshroud/` (writable).

**Migration block:** Detects stale configs with the old path and updates them:
```javascript
if (hasCollaborator && config.workspace === 'collaborator-workspace') {
    config.workspace = '.agentshroud/collaborator-workspace';
}
```

## Tool Deny List

```javascript
const DENIED_TOOLS = ['write', 'edit', 'web_search', 'web_fetch'];
```

These tools are removed from OpenClaw's active tool list at runtime. Note: `web_search` and `web_fetch` are denied at the OpenClaw level here; the gateway also filters via egress allowlist.

## Related

- [[patch-telegram-sdk.sh]] — SDK-level URL patching (separate from this runtime config)
- [[agentshroud-bot]] — the container this runs inside
- [[bot_config]] — defines `workspace_path` and `config_dir`
