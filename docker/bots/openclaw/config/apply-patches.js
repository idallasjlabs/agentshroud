#!/usr/bin/env node
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
// Protected by common law trademark rights. Federal trademark registration pending.
// Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
/**
 * apply-patches.js — Idempotent openclaw.json patch script.
 *
 * Applies required configuration changes that must survive container rebuilds:
 *   1. Ensures `main` is the first (default) agent in agents.list
 *   2. Ensures Isaiah's Telegram ID (8096968754) is bound to the main agent
 *
 * NOTE: OpenClaw does not support MCP servers (it uses its own plugin system).
 * iMessage is handled by OpenClaw's built-in imessage extension via cliPath/imsg-ssh.
 *
 * Safe to run on every container startup:
 *   - If openclaw.json exists: patches it in-place, preserving all other fields
 *     (Telegram token, channel config, API keys, etc. are untouched)
 *   - If openclaw.json does not exist: creates a minimal seed file so OpenClaw
 *     inherits these settings when it initialises on first run
 *
 * Usage: node apply-patches.js /path/to/openclaw.json
 */

'use strict';

const fs = require('fs');
const path = require('path');

const configPath = process.argv[2] || '/home/node/.openclaw/openclaw.json';

// ── Load or seed ─────────────────────────────────────────────────────────────

let config = {};
let isNew = false;

if (fs.existsSync(configPath)) {
  try {
    config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch (err) {
    console.error(`[init-patch] ERROR: could not parse ${configPath}: ${err.message}`);
    process.exit(1);
  }
} else {
  console.log(`[init-patch] ${configPath} not found — creating seed file`);
  isNew = true;
  // Ensure the directory exists
  fs.mkdirSync(path.dirname(configPath), { recursive: true });
}

let changed = false;

// ── Patch 1: agents.list — main agent as first/default ───────────────────────

config.agents = config.agents || {};
config.agents.list = config.agents.list || [];

const hasMain = config.agents.list.some(a => a.id === 'main');
if (!hasMain) {
  config.agents.list.unshift({ id: 'main', name: 'AgentShroud Main Agent' });
  console.log('[init-patch] Added main agent to agents.list (now default)');
  changed = true;
} else {
  // Ensure main is first so it is the default
  const idx = config.agents.list.findIndex(a => a.id === 'main');
  if (idx > 0) {
    const [mainEntry] = config.agents.list.splice(idx, 1);
    config.agents.list.unshift(mainEntry);
    console.log('[init-patch] Moved main agent to front of agents.list');
    changed = true;
  }
}

// ── Patch 2: bindings — Isaiah's Telegram ID → main agent ────────────────────

config.bindings = config.bindings || [];

const ISAIAH_TELEGRAM_ID = '8096968754';
const hasBinding = config.bindings.some(
  b => b.agentId === 'main' &&
       b.match &&
       b.match.peer &&
       b.match.peer.id === ISAIAH_TELEGRAM_ID
);

if (!hasBinding) {
  config.bindings.unshift({
    agentId: 'main',
    match: {
      channel: 'telegram',
      peer: { kind: 'direct', id: ISAIAH_TELEGRAM_ID }
    }
  });
  console.log(`[init-patch] Added Telegram binding: peer ${ISAIAH_TELEGRAM_ID} → main`);
  changed = true;
}


// ── Patch 2c: collaborator agent — restricted advisor mode ───────────────────
// Collaborators get an isolated agent with Sonnet model, no dangerous tools,
// and a mandatory disclosure notice. This prevents collaborators from accessing
// owner tools (1Password, exec, SSH, etc.)

const COLLABORATOR_IDS = {
  '8506022825': 'Brett Galura',
  '8545356403': 'Chris Shelton',
  '8279589982': 'Steve Hay',
  '8526379012': 'TJ Winter',
  '7614658040': 'Isaiah (collaborator test)',
};

const hasCollaborator = config.agents.list.some(a => a.id === 'collaborator');
if (!hasCollaborator) {
  config.agents.list.push({
    id: 'collaborator',
    name: 'AgentShroud Collaborator',
    model: 'anthropic/claude-sonnet-4-20250514',
    params: { maxTokens: 2048 },
    tools: {
      profile: 'minimal',
      deny: [
        'exec', 'process', 'gateway', 'cron', 'message',
        'sessions_spawn', 'sessions_send', 'subagents',
        'memory_search', 'memory_get', 'tts', 'pdf',
        'nodes', 'browser', 'canvas', 'agents_list',
        'sessions_list', 'sessions_history', 'session_status',
        'image', 'read', 'write', 'edit', 'apply_patch',
        'ls', 'find', 'grep', 'web_search', 'web_fetch'
      ]
    },
    skills: [],
    workspace: '/home/node/.openclaw/workspace/collaborator-workspace',
    memorySearch: { enabled: false }
  });
  console.log('[init-patch] Added collaborator agent (Sonnet, restricted tools)');
  changed = true;
}

// ── Patch 2d: harden existing collaborator agent config ──────────────────────
// Ensures deny list includes all filesystem/web tools and fixes schema issues.
const existingCollab = config.agents.list.find(a => a.id === 'collaborator');
if (existingCollab) {
  const requiredDeny = [
    'exec', 'process', 'gateway', 'cron', 'message',
    'sessions_spawn', 'sessions_send', 'subagents',
    'memory_search', 'memory_get', 'tts', 'pdf',
    'nodes', 'browser', 'canvas', 'agents_list',
    'sessions_list', 'sessions_history', 'session_status',
    'image', 'read', 'write', 'edit', 'apply_patch',
    'ls', 'find', 'grep', 'web_search', 'web_fetch'
  ];
  if (!existingCollab.tools) existingCollab.tools = {};
  if (!existingCollab.tools.deny) existingCollab.tools.deny = [];
  const deny = existingCollab.tools.deny;
  for (const tool of requiredDeny) {
    if (!deny.includes(tool)) {
      deny.push(tool);
      changed = true;
      console.log('[init-patch] Added ' + tool + ' to collaborator deny list');
    }
  }
  // Fix memorySearch: boolean -> object
  if (typeof existingCollab.memorySearch === 'boolean') {
    existingCollab.memorySearch = { enabled: existingCollab.memorySearch };
    changed = true;
    console.log('[init-patch] Fixed collaborator memorySearch schema');
  }
  // Remove invalid heartbeat.enabled key
  if (existingCollab.heartbeat && 'enabled' in existingCollab.heartbeat) {
    delete existingCollab.heartbeat;
    changed = true;
    console.log('[init-patch] Removed invalid heartbeat config from collaborator');
  }
}

// ── Patch 2e: set ownerDisplay to hash ───────────────────────────────────────
// Prevents phone numbers from leaking to collaborator agents via system prompt.
if (!config.commands) config.commands = {};
if (config.commands.ownerDisplay !== 'hash') {
  config.commands.ownerDisplay = 'hash';
  changed = true;
  console.log('[init-patch] Set ownerDisplay to hash (phone number protection)');
}

// Ensure all collaborator IDs are bound to the collaborator agent
for (const [collabId, collabName] of Object.entries(COLLABORATOR_IDS)) {
  const hasBind = config.bindings.some(
    b => b.agentId === 'collaborator' &&
         b.match &&
         b.match.peer &&
         b.match.peer.id === collabId
  );
  if (!hasBind) {
    // Remove any stale binding that routes this ID to 'main'
    config.bindings = config.bindings.filter(
      b => !(b.match && b.match.peer && b.match.peer.id === collabId)
    );
    config.bindings.push({
      agentId: 'collaborator',
      match: {
        channel: 'telegram',
        peer: { kind: 'direct', id: collabId }
      }
    });
    console.log(`[init-patch] Added Telegram binding: peer ${collabId} (${collabName}) → collaborator`);
    changed = true;
  }
}

// ── Patch 3: mcpServers cleanup — remove legacy key rejected by OpenClaw ────

// ── Patch 2b: binding for Isaiah collaborator account (@idallasj) ────────────

const ISAIAH_COLLAB_ID = '7614658040';
const hasCollabBinding = config.bindings.some(
  b => b.agentId === 'collaborator' &&
       b.match &&
       b.match.peer &&
       b.match.peer.id === ISAIAH_COLLAB_ID
);

if (!hasCollabBinding) {
  // Remove any stale binding that routes this ID to 'main'
  config.bindings = config.bindings.filter(
    b => !(b.match && b.match.peer && b.match.peer.id === ISAIAH_COLLAB_ID)
  );
  config.bindings.push({
    agentId: 'collaborator',
    match: {
      channel: 'telegram',
      peer: { kind: 'direct', id: ISAIAH_COLLAB_ID }
    }
  });
  console.log(`[init-patch] Added Telegram binding: peer ${ISAIAH_COLLAB_ID} → collaborator`);
  changed = true;
}
// openclaw@latest rejects 'mcpServers' as an unrecognised top-level key and
// exits with code 1, putting the container into a crash loop.
// MCP proxy wrapping will be re-implemented via the correct OpenClaw API.

if (Object.prototype.hasOwnProperty.call(config, 'mcpServers')) {
  delete config.mcpServers;
  console.log('[init-patch] Removed legacy mcpServers key (unrecognised by current OpenClaw)');
  changed = true;
}

// ── Patch 4: agents.defaults.compaction.reserveTokensFloor ───────────────────

// Prevents "Context limit exceeded" resets by reserving a token buffer before
// the hard context limit is hit. OpenClaw triggers a hard reset when the buffer
// runs out; raising the floor gives the compaction pass room to summarise first.

config.agents = config.agents || {};
config.agents.defaults = config.agents.defaults || {};
config.agents.defaults.compaction = config.agents.defaults.compaction || {};

const RESERVE_FLOOR = 4000;
if ((config.agents.defaults.compaction.reserveTokensFloor || 0) < RESERVE_FLOOR) {
  config.agents.defaults.compaction.reserveTokensFloor = RESERVE_FLOOR;
  console.log(`[init-patch] Set agents.defaults.compaction.reserveTokensFloor = ${RESERVE_FLOOR}`);
  changed = true;
}


// ── Patch 5: plugins.entries.telegram — ensure Telegram plugin is enabled ────
// Without this, OpenClaw starts the gateway but never initialises the Telegram
// provider, so the bot appears online (startup notification fires via curl) but
// never receives or processes incoming messages.

config.plugins = config.plugins || {};
config.plugins.entries = config.plugins.entries || {};
config.plugins.entries.telegram = config.plugins.entries.telegram || {};

if (!config.plugins.entries.telegram.enabled) {
  config.plugins.entries.telegram.enabled = true;
  console.log('[init-patch] Enabled Telegram plugin (plugins.entries.telegram.enabled = true)');
  changed = true;
}

// ── Patch 6: gateway auth — read from OPENCLAW_GATEWAY_PASSWORD env ────
// OpenClaw checks gateway.auth.password for websocket auth (not gateway.auth.token).
// Both fields are set for compatibility. gateway.remote.password is what the CLI
// sends when connecting to the gateway; it must match gateway.auth.password.

const gwPassword = process.env.OPENCLAW_GATEWAY_PASSWORD;
if (gwPassword) {
  config.gateway = config.gateway || {};
  config.gateway.auth = config.gateway.auth || {};
  if (config.gateway.auth.token !== gwPassword) {
    config.gateway.auth.token = gwPassword;
    console.log('[init-patch] Set gateway.auth.token from OPENCLAW_GATEWAY_PASSWORD');
    changed = true;
  }
  // Security: Do NOT store password in config file (audit warning).
  // auth.token and remote.password are sufficient for OpenClaw auth.
  if (config.gateway.auth.password) {
    delete config.gateway.auth.password;
    console.log('[init-patch] Removed gateway.auth.password from config (use env var)');
    changed = true;
  }
  config.gateway.remote = config.gateway.remote || {};
  if (config.gateway.remote.password !== gwPassword) {
    config.gateway.remote.password = gwPassword;
    console.log('[init-patch] Set gateway.remote.password from OPENCLAW_GATEWAY_PASSWORD');
    changed = true;
  }
}

// ── Patch 7: gateway.controlUi — explicit CORS origins, fallback disabled ─────
// When gateway binds non-loopback (OPENCLAW_GATEWAY_BIND=lan), OpenClaw 2026.2.24+
// requires explicit CORS origins. We declare the localhost origins that match the
// 127.0.0.1:8080 port mapping and hard-disable the Host-header fallback.
// All Control UI traffic must originate from a declared origin — no exceptions.

config.gateway = config.gateway || {};
config.gateway.controlUi = config.gateway.controlUi || {};

// Enforce explicit allowed origins. The gateway port is configurable via
// GATEWAY_HOST_PORT (default: 8080) to support multi-instance deployments.
const gatewayPort = process.env.GATEWAY_HOST_PORT || '8080';
const REQUIRED_ORIGINS = [
  `http://localhost:${gatewayPort}`,   // gateway port mapping (host → container)
  `http://127.0.0.1:${gatewayPort}`,
  'http://localhost:18790',  // bot Control UI native port
  'http://127.0.0.1:18790',
];
const currentOrigins = config.gateway.controlUi.allowedOrigins || [];
const missingOrigins = REQUIRED_ORIGINS.filter(o => !currentOrigins.includes(o));
if (missingOrigins.length > 0) {
  config.gateway.controlUi.allowedOrigins = [...currentOrigins, ...missingOrigins];
  console.log(`[init-patch] Set gateway.controlUi.allowedOrigins: ${missingOrigins.join(', ')}`);
  changed = true;
}

// Hard-disable the Host-header fallback. Explicit origins are always required;
// the fallback is never acceptable regardless of what openclaw.json contains.
if (config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback !== false) {
  config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = false;
  console.log('[init-patch] Set gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = false');
  changed = true;
}

// ── Patch 8: channels.telegram.botToken — inject from TELEGRAM_BOT_TOKEN env ─
// Allows per-host bot token injection via Docker environment variable.
// If TELEGRAM_BOT_TOKEN is set, it overrides whatever is in the config.
// This enables the same image to run different bots on different hosts.

const telegramToken = process.env.TELEGRAM_BOT_TOKEN;
if (telegramToken) {
  config.channels = config.channels || {};
  config.channels.telegram = config.channels.telegram || {};
  if (config.channels.telegram.botToken !== telegramToken) {
    config.channels.telegram.botToken = telegramToken;
    console.log('[init-patch] Set channels.telegram.botToken from TELEGRAM_BOT_TOKEN env');
    changed = true;
  }
}


// ── Patch 9: channels.telegram.groups — default group config ─────────────────
// All groups default to requireMention: false so both bots respond without @mention.

config.channels = config.channels || {};
config.channels.telegram = config.channels.telegram || {};
config.channels.telegram.groups = config.channels.telegram.groups || {};

if (!config.channels.telegram.groups['*']) {
  config.channels.telegram.groups['*'] = { requireMention: false };
  console.log('[init-patch] Set channels.telegram.groups.* = { requireMention: false }');
  changed = true;
} else if (config.channels.telegram.groups['*'].requireMention !== false) {
  config.channels.telegram.groups['*'].requireMention = false;
  console.log('[init-patch] Set channels.telegram.groups.*.requireMention = false');
  changed = true;
}

// ── Patch 10: channels.telegram.allowFrom — authorized senders ───────────────
// Ensures all collaborators are in the allowFrom list for Telegram.

const AUTHORIZED_SENDERS = [
  // Humans
  '8096968754',   // Isaiah
  '8506022825',   // Brett
  '8545356403',   // Chris
  '8279589982',   // Steve
  '8526379012',   // TJ
  '7614658040',   // Isaiah (collaborator account @idallasj)
  // Bots (inter-bot group chat)
  '8481143014',   // @agentshroud_bot (production)
  '8736289266',   // @agentshroud_marvin_bot
  '8751040644',   // @agentshroud_trillian_bot
  '8690957340',   // @agentshroud_raspberrypi_bot
];

config.channels.telegram.allowFrom = config.channels.telegram.allowFrom || [];
let sendersChanged = false;
for (const sender of AUTHORIZED_SENDERS) {
  if (!config.channels.telegram.allowFrom.includes(sender)) {
    config.channels.telegram.allowFrom.push(sender);
    sendersChanged = true;
  }
}
if (sendersChanged) {
  console.log('[init-patch] Updated channels.telegram.allowFrom with authorized senders');
  changed = true;
}

// ── Patch 11: channels.telegram.groupPolicy — allowlist mode ─────────────────
if (config.channels.telegram.groupPolicy !== 'allowlist') {
  config.channels.telegram.groupPolicy = 'allowlist';
  console.log('[init-patch] Set channels.telegram.groupPolicy = allowlist');
  changed = true;
}


// ── Patch 12: Security hardening (from openclaw security audit) ──────────────
// Enforce workspaceOnly=true so filesystem tools are scoped to workspace.
config.tools = config.tools || {};
config.tools.fs = config.tools.fs || {};
if (!config.tools.fs.workspaceOnly) {
  config.tools.fs.workspaceOnly = true;
  console.log('[init-patch] Set tools.fs.workspaceOnly = true (security hardening)');
  changed = true;
}

// ── Patch 13: Group sender allowlist (groupAllowFrom) ────────────────────────
// Restricts who can invoke bot commands in group chats.
config.channels = config.channels || {};
config.channels.telegram = config.channels.telegram || {};
if (!config.channels.telegram.groupAllowFrom || config.channels.telegram.groupAllowFrom.length === 0) {
  config.channels.telegram.groupAllowFrom = AUTHORIZED_SENDERS.slice();
  console.log('[init-patch] Set channels.telegram.groupAllowFrom (group command allowlist)');
  changed = true;
}

// ── Write back ────────────────────────────────────────────────────────────────

if (changed || isNew) {
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
  console.log(`[init-patch] ✓ ${isNew ? 'Created seed' : 'Patched'} ${configPath}`);
} else {
  console.log('[init-patch] ✓ No changes needed — openclaw.json already correct');
}
