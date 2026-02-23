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

// ── Patch 3: mcpServers cleanup — remove legacy key rejected by OpenClaw ────
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

// ── Write back ────────────────────────────────────────────────────────────────

if (changed || isNew) {
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
  console.log(`[init-patch] ✓ ${isNew ? 'Created seed' : 'Patched'} ${configPath}`);
} else {
  console.log('[init-patch] ✓ No changes needed — openclaw.json already correct');
}
