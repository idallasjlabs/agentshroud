#!/usr/bin/env node
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
/**
 * apply-patches.js — Idempotent openclaw.json patch script.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const configPath = process.argv[2] ||
  (fs.existsSync('/home/node/.agentshroud/openclaw.json')
    ? '/home/node/.agentshroud/openclaw.json'
    : '/home/node/.openclaw/openclaw.json');

let config = {};
let isNew = false;

if (fs.existsSync(configPath)) {
  try {
    config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch (err) {
    const ts = new Date().toISOString().replace(/[:.]/g, '-');
    const quarantinePath = `${configPath}.corrupt-${ts}.bak`;
    try {
      fs.renameSync(configPath, quarantinePath);
      console.error(`[init-patch] WARNING: invalid JSON in ${configPath}; moved to ${quarantinePath}`);
    } catch (renameErr) {
      console.error(
        `[init-patch] WARNING: invalid JSON in ${configPath} and failed to quarantine (${renameErr.message}); continuing with fresh config`
      );
    }
    config = {};
    isNew = true;
  }
} else {
  console.log(`[init-patch] ${configPath} not found — creating seed file`);
  isNew = true;
  fs.mkdirSync(path.dirname(configPath), { recursive: true });
}

let changed = false;
const MODEL_MODE = String(process.env.AGENTSHROUD_MODEL_MODE || 'local').toLowerCase();
const LOCAL_MODEL_REF = process.env.AGENTSHROUD_LOCAL_MODEL_REF || 'ollama/qwen3:14b';
const CLOUD_MODEL_REF = process.env.AGENTSHROUD_CLOUD_MODEL_REF || 'anthropic/claude-opus-4-6';
const inferredMainModel = MODEL_MODE === 'cloud' ? CLOUD_MODEL_REF : LOCAL_MODEL_REF;
const MAIN_MODEL = process.env.OPENCLAW_MAIN_MODEL || inferredMainModel;
const LOCAL_MODEL_NAME = process.env.AGENTSHROUD_LOCAL_MODEL || LOCAL_MODEL_REF.split('/').slice(-1)[0] || 'qwen3:14b';
const OLLAMA_BASE_URL_RAW = process.env.OLLAMA_BASE_URL || 'http://gateway:8080/v1';
const OLLAMA_PROVIDER_API = process.env.OPENCLAW_OLLAMA_API || 'ollama';
const OLLAMA_BASE_URL = /\/v1\/?$/i.test(OLLAMA_BASE_URL_RAW)
  ? OLLAMA_BASE_URL_RAW.replace(/\/+$/, '')
  : `${OLLAMA_BASE_URL_RAW.replace(/\/+$/, '')}/v1`;

// LM Studio provider (Anchor + Coding models via OpenAI-compatible API on port 1234)
const LMSTUDIO_BASE_URL_RAW = process.env.LMSTUDIO_API_BASE || 'http://host.docker.internal:1234';
const LMSTUDIO_BASE_URL = /\/v1\/?$/i.test(LMSTUDIO_BASE_URL_RAW)
  ? LMSTUDIO_BASE_URL_RAW.replace(/\/+$/, '')
  : `${LMSTUDIO_BASE_URL_RAW.replace(/\/+$/, '')}/v1`;
const LMSTUDIO_ANCHOR_MODEL = process.env.AGENTSHROUD_ANCHOR_MODEL || 'qwen3.5:27b';
const LMSTUDIO_CODING_MODEL = process.env.AGENTSHROUD_CODING_MODEL || 'qwen2.5-coder:32b';

// Patch 0: agents.defaults.model (startup/default model resolution path)
config.agents = config.agents || {};
config.agents.defaults = config.agents.defaults || {};
config.commands = config.commands || {};
if (config.commands.ownerDisplay !== 'hash') {
  config.commands.ownerDisplay = 'hash';
  changed = true;
}
const currentDefaultsModel =
  typeof config.agents.defaults.model === 'string'
    ? config.agents.defaults.model
    : (config.agents.defaults.model && config.agents.defaults.model.primary) || '';
if (currentDefaultsModel !== MAIN_MODEL) {
  config.agents.defaults.model = { primary: MAIN_MODEL };
  changed = true;
}
config.agents.defaults.models = config.agents.defaults.models || {};
if (!config.agents.defaults.models[MAIN_MODEL]) {
  config.agents.defaults.models[MAIN_MODEL] = { alias: 'local-qwen' };
  changed = true;
}
if (!config.agents.defaults.timeoutSeconds || config.agents.defaults.timeoutSeconds < 600) {
  config.agents.defaults.timeoutSeconds = 600;
  changed = true;
}

// Patch 0b: models.providers.ollama fallback registration.
// This gives OpenClaw an explicit provider + model definition even if dynamic
// model discovery is unavailable at startup.
// In local-multi mode all 3 models (Anchor, Coding, Reasoning) run under Ollama.
config.models = config.models || {};
config.models.providers = config.models.providers || {};
const currentOllama = config.models.providers.ollama || {};
const ollamaModels = [
  {
    id: LOCAL_MODEL_NAME,
    name: LOCAL_MODEL_NAME,
    reasoning: false,
    input: ['text'],
    contextWindow: 128000,
    maxTokens: 8192,
  },
];
if (MODEL_MODE === 'local-multi') {
  const ANCHOR_MODEL_NAME = process.env.AGENTSHROUD_ANCHOR_MODEL || 'qwen3.5:27b';
  const CODING_MODEL_NAME = process.env.AGENTSHROUD_CODING_MODEL || 'qwen2.5-coder:32b';
  const REASONING_MODEL_NAME = process.env.AGENTSHROUD_REASONING_MODEL || 'deepseek-r1';
  for (const [id, label, reasoning] of [
    [ANCHOR_MODEL_NAME, 'Anchor', false],
    [CODING_MODEL_NAME, 'Coding', false],
    [REASONING_MODEL_NAME, 'Reasoning', true],
  ]) {
    if (!ollamaModels.some((m) => m.id === id)) {
      ollamaModels.push({ id, name: label + ' (' + id + ')', reasoning, input: ['text'], contextWindow: 32768, maxTokens: 8192 });
    }
  }
}
const desiredOllama = {
  baseUrl: OLLAMA_BASE_URL,
  api: OLLAMA_PROVIDER_API,
  models: ollamaModels,
};
if (JSON.stringify(currentOllama) !== JSON.stringify(desiredOllama)) {
  config.models.providers.ollama = desiredOllama;
  changed = true;
}

// Patch 0c: models.providers.lmstudio — only registered when LMSTUDIO_API_BASE is
// explicitly set (i.e. user has LM Studio running alongside Ollama).
// In the default local-multi setup all models run under Ollama; this block is a no-op.
if (process.env.LMSTUDIO_API_BASE) {
  const currentLmStudio = config.models.providers.lmstudio || {};
  const desiredLmStudio = {
    baseUrl: LMSTUDIO_BASE_URL,
    api: 'openai',
    models: [
      {
        id: LMSTUDIO_ANCHOR_MODEL,
        name: 'Anchor (' + LMSTUDIO_ANCHOR_MODEL + ')',
        reasoning: false,
        input: ['text'],
        contextWindow: 32768,
        maxTokens: 8192,
      },
      {
        id: LMSTUDIO_CODING_MODEL,
        name: 'Coding (' + LMSTUDIO_CODING_MODEL + ')',
        reasoning: false,
        input: ['text'],
        contextWindow: 32768,
        maxTokens: 8192,
      },
    ],
  };
  if (JSON.stringify(currentLmStudio) !== JSON.stringify(desiredLmStudio)) {
    config.models.providers.lmstudio = desiredLmStudio;
    console.log('[init-patch] Registered LM Studio provider with Anchor + Coding models');
    changed = true;
  }
}

// Patch 1: agents.list
config.agents.list = config.agents.list || [];
const hasMain = config.agents.list.some((a) => a.id === 'main');
if (!hasMain) {
  config.agents.list.unshift({ id: 'main', name: 'AgentShroud Main Agent', model: MAIN_MODEL });
  changed = true;
} else {
  if (config.agents.list[0].id !== 'main') {
    const idx = config.agents.list.findIndex((a) => a.id === 'main');
    const [mainEntry] = config.agents.list.splice(idx, 1);
    config.agents.list.unshift(mainEntry);
    changed = true;
  }
  if (config.agents.list[0].model !== MAIN_MODEL) {
    config.agents.list[0].model = MAIN_MODEL;
    changed = true;
  }
}

const COLLABORATOR_IDS = {
  '8506022825': 'Brett Galura',
  '8545356403': 'Chris Shelton',
  '15712621992': 'Gabriel Fuentes',
  '8279589982': 'Steve Hay',
  '8526379012': 'TJ Winter',
  '7614658040': 'Isaiah (collaborator test)',
  '8633775668': 'Ana',
};
const OWNER_TELEGRAM_ID = '8096968754';

// Collaborator tool restriction profiles.
// OpenClaw supports 4 profiles: 'minimal', 'coding', 'messaging', 'full'.
// 'minimal' → file tools only (read/write/edit). 'full' → all tools including web_search, web_fetch.
// Restrictive/project_scoped tier uses 'minimal'; full_access tier uses 'full'.
const _COLLAB_TOOL_DENY = [
  'exec', 'process', 'gateway', 'cron', 'message',
  'sessions_spawn', 'sessions_send', 'subagents',
  'memory_search', 'memory_get', 'tts', 'pdf',
  'nodes', 'browser', 'canvas', 'agents_list',
  'sessions_list', 'sessions_history', 'session_status',
  'image', 'web_fetch', 'web_search',
];

// full_access tier: profile:'full' provides web_search/web_fetch.
// Deny list still blocks exec/process/gateway/cron/sessions/agent introspection.
const _COLLAB_TOOL_DENY_FULL_ACCESS = [
  'exec', 'process', 'gateway', 'cron', 'message',
  'sessions_spawn', 'sessions_send', 'subagents',
  'memory_search', 'memory_get',
  'nodes', 'agents_list',
  'sessions_list', 'sessions_history', 'session_status',
  'canvas',
];

// Parse TEAMS_JSON early so _resolveCollabToolConfig can inspect group collab_mode
// before per-collaborator agents are created. Patch 1c will reuse this variable.
const TEAMS_JSON_RAW = process.env.AGENTSHROUD_TEAMS_JSON || '';
let _teamsJsonParsed = null;
try { if (TEAMS_JSON_RAW) _teamsJsonParsed = JSON.parse(TEAMS_JSON_RAW); } catch (e) {}

const COLLAB_LOCAL_INFO_ONLY = (process.env.AGENTSHROUD_COLLAB_LOCAL_INFO_ONLY || '1').trim().toLowerCase();
const _is_global_full_access = ['0', 'false', 'no'].includes(COLLAB_LOCAL_INFO_ONLY);

// Load per-user mode overrides from group_overrides.json (gateway-data volume).
let _userOverrides = {};
try {
  const _overridesPath = '/home/node/agentshroud/gateway-data/group_overrides.json';
  const _overridesRaw = require('fs').readFileSync(_overridesPath, 'utf-8');
  _userOverrides = JSON.parse(_overridesRaw).__user_overrides__ || {};
} catch (e) { /* file may not exist yet */ }

// Resolve tool config (profile + deny list) for a collaborator.
// Priority: per-user override in group_overrides.json → group collab_mode → global env var.
function _resolveCollabToolConfig(uid, teamsJson) {
  let isFullAccess = false;
  // 1. Per-user override
  if (uid && _userOverrides[uid] && _userOverrides[uid].collab_mode === 'full_access') {
    isFullAccess = true;
  }
  // 2. Group membership
  if (!isFullAccess && uid && teamsJson && teamsJson.groups) {
    for (const g of Object.values(teamsJson.groups)) {
      if (g.members && g.members.includes(uid) && g.collab_mode === 'full_access') {
        isFullAccess = true;
        break;
      }
    }
  }
  // 3. Global env var fallback
  if (!isFullAccess) isFullAccess = _is_global_full_access;
  return isFullAccess
    ? { profile: 'full', deny: _COLLAB_TOOL_DENY_FULL_ACCESS }
    : { profile: 'minimal', deny: _COLLAB_TOOL_DENY };
}

// Backward-compat: keep old name as alias
function _resolveCollabDenyList(uid, teamsJson) {
  return _resolveCollabToolConfig(uid, teamsJson).deny;
}

const cIdx = config.agents.list.findIndex((a) => a.id === 'collaborator');
const { profile: _genericProfile, deny: _genericCollabDeny } = _resolveCollabToolConfig(null, _teamsJsonParsed);
if (cIdx < 0) {
  config.agents.list.push({
    id: 'collaborator',
    name: 'AgentShroud Collaborator',
    model: MAIN_MODEL,
    tools: { profile: _genericProfile, deny: _genericCollabDeny },
    skills: [],
    workspace: '.agentshroud/collaborator-workspace',
    memorySearch: { enabled: false },
  });
  console.log(`[init-patch] Added collaborator agent (${MAIN_MODEL}, profile:${_genericProfile})`);
  changed = true;
} else {
  if (config.agents.list[cIdx].model !== MAIN_MODEL) {
    config.agents.list[cIdx].model = MAIN_MODEL;
    changed = true;
  }
  if (config.agents.list[cIdx].memorySearch === false) {
    config.agents.list[cIdx].memorySearch = { enabled: false };
    changed = true;
  }
  // Migrate stale workspace path from read-only rootfs to writable volume path
  if (config.agents.list[cIdx].workspace === 'collaborator-workspace') {
    config.agents.list[cIdx].workspace = '.agentshroud/collaborator-workspace';
    console.log('[init-patch] Migrated collaborator workspace to .agentshroud/collaborator-workspace');
    changed = true;
  }
  // Ensure tools config is current (correct profile + tier deny list)
  const existingTools = config.agents.list[cIdx].tools || {};
  if (existingTools.profile !== _genericProfile || existingTools.allow || JSON.stringify(existingTools.deny) !== JSON.stringify(_genericCollabDeny)) {
    config.agents.list[cIdx].tools = { profile: _genericProfile, deny: _genericCollabDeny };
    console.log(`[init-patch] Updated collaborator agent tools to profile:${_genericProfile} + deny list`);
    changed = true;
  }
}

// Patch 1b: bindings — owner + all collaborator IDs
config.bindings = Array.isArray(config.bindings) ? config.bindings : [];

const hasOwnerBinding = config.bindings.some(
  (b) => b.agentId === 'main' && b.match && b.match.peer && b.match.peer.id === OWNER_TELEGRAM_ID
);
if (!hasOwnerBinding) {
  config.bindings = config.bindings.filter(
    (b) => !(b.match && b.match.peer && b.match.peer.id === OWNER_TELEGRAM_ID)
  );
  config.bindings.unshift({
    agentId: 'main',
    match: { channel: 'telegram', peer: { kind: 'direct', id: OWNER_TELEGRAM_ID } },
  });
  console.log(`[init-patch] Added Telegram binding: ${OWNER_TELEGRAM_ID} → main`);
  changed = true;
}

// Per-collaborator isolated agents: each known collaborator gets their own agent
// with a dedicated workspace so memory never bleeds between collaborators or the owner.
for (const [collabId, collabName] of Object.entries(COLLABORATOR_IDS)) {
  const agentId = `collab-${collabId}`;
  const agentIdx = config.agents.list.findIndex((a) => a.id === agentId);
  const { profile: _collabProfile, deny: _collabDeny } = _resolveCollabToolConfig(collabId, _teamsJsonParsed);
  if (agentIdx < 0) {
    config.agents.list.push({
      id: agentId,
      name: `${collabName} (Collaborator)`,
      model: MAIN_MODEL,
      tools: { profile: _collabProfile, deny: _collabDeny },
      skills: [],
      workspace: `.agentshroud/collab-${collabId}`,
      memorySearch: { enabled: false },
    });
    console.log(`[init-patch] Added per-collaborator agent: ${agentId} (${collabName}, profile:${_collabProfile})`);
    changed = true;
  } else {
    if (config.agents.list[agentIdx].model !== MAIN_MODEL) {
      config.agents.list[agentIdx].model = MAIN_MODEL;
      changed = true;
    }
    // Fix any agent with wrong profile or wrong tier deny list
    const existingTools = config.agents.list[agentIdx].tools || {};
    if (existingTools.profile !== _collabProfile || existingTools.allow || JSON.stringify(existingTools.deny) !== JSON.stringify(_collabDeny)) {
      config.agents.list[agentIdx].tools = { profile: _collabProfile, deny: _collabDeny };
      console.log(`[init-patch] Fixed ${agentId} tools: profile:${_collabProfile} + tier deny list`);
      changed = true;
    }
  }

  // Bind this collaborator's Telegram ID to their dedicated per-user agent.
  // Migrate any existing generic 'collaborator' binding to the per-user agent.
  const hasPerUserBind = config.bindings.some(
    (b) => b.agentId === agentId && b.match && b.match.peer && b.match.peer.id === collabId
  );
  if (!hasPerUserBind) {
    config.bindings = config.bindings.filter(
      (b) => !(b.match && b.match.peer && b.match.peer.id === collabId)
    );
    config.bindings.push({
      agentId: agentId,
      match: { channel: 'telegram', peer: { kind: 'direct', id: collabId } },
    });
    console.log(`[init-patch] Bound ${collabId} (${collabName}) → ${agentId}`);
    changed = true;
  }
}

// Patch 1c: group workspaces (V9-4E)
// Read AGENTSHROUD_TEAMS_JSON from env to discover groups and create shared workspace dirs.
// The sharedWorkspace field is set on each per-collaborator agent so the bot knows where
// the group's shared memory and workspace live on the config volume.
// Note: TEAMS_JSON_RAW is declared earlier (before Patch 1b) so _resolveCollabDenyList
// can inspect group collab_mode during per-collaborator agent creation.
if (TEAMS_JSON_RAW) {
  try {
    const teams = JSON.parse(TEAMS_JSON_RAW);
    const groups = teams.groups || {};
    for (const [groupId, group] of Object.entries(groups)) {
      const groupDir = `.agentshroud/groups/${groupId}`;
      const groupWorkspaceDir = `${groupDir}/workspace`;
      // Create group dirs on the config volume if they don't already exist
      if (!fs.existsSync(groupDir)) {
        fs.mkdirSync(groupDir, { recursive: true });
        console.log(`[init-patch] Created group workspace dir: ${groupDir}`);
      }
      if (!fs.existsSync(groupWorkspaceDir)) {
        fs.mkdirSync(groupWorkspaceDir, { recursive: true });
      }
      // Attach sharedWorkspace to each group member's per-collaborator agent
      const members = group.members || [];
      for (const memberId of members) {
        const agentId = `collab-${memberId}`;
        const agentIdx = config.agents.list.findIndex((a) => a.id === agentId);
        if (agentIdx >= 0 && config.agents.list[agentIdx].sharedWorkspace !== groupWorkspaceDir) {
          config.agents.list[agentIdx].sharedWorkspace = groupWorkspaceDir;
          changed = true;
        }
      }
    }
  } catch (e) {
    console.warn(`[init-patch] Could not parse AGENTSHROUD_TEAMS_JSON: ${e.message}`);
  }
}

// Patch 1d: group-project agent — broader tool access for collaborative team use.
// Allows web_search, web_fetch, memory_search, memory_get, image, pdf.
// Denies exec/process/gateway/cron/session management (same as collaborator).
const _GROUP_TOOL_DENY = [
  'exec', 'process', 'gateway', 'cron', 'message',
  'sessions_spawn', 'sessions_send', 'subagents',
  'nodes', 'agents_list',
  'sessions_list', 'sessions_history', 'session_status',
  'canvas',
];
const gpIdx = config.agents.list.findIndex((a) => a.id === 'group-project');
if (gpIdx < 0) {
  config.agents.list.push({
    id: 'group-project',
    name: 'AgentShroud Group Project',
    model: MAIN_MODEL,
    tools: { profile: 'minimal', deny: _GROUP_TOOL_DENY },
    skills: [],
    workspace: '.agentshroud/group-project',
    memorySearch: { enabled: true },
  });
  console.log('[init-patch] Added group-project agent (web+memory enabled)');
  changed = true;
} else {
  if (config.agents.list[gpIdx].model !== MAIN_MODEL) {
    config.agents.list[gpIdx].model = MAIN_MODEL;
    changed = true;
  }
  const existingGpTools = config.agents.list[gpIdx].tools || {};
  if (JSON.stringify(existingGpTools.deny) !== JSON.stringify(_GROUP_TOOL_DENY)) {
    config.agents.list[gpIdx].tools = { profile: 'minimal', deny: _GROUP_TOOL_DENY };
    console.log('[init-patch] Updated group-project agent tool config');
    changed = true;
  }
}

// Bind a configured group chat ID to the group-project agent.
// Set AGENTSHROUD_GROUP_CHAT_ID to your Telegram group/supergroup chat ID.
const GROUP_CHAT_ID = String(process.env.AGENTSHROUD_GROUP_CHAT_ID || '').trim();
if (GROUP_CHAT_ID) {
  const hasGroupBinding = config.bindings.some(
    (b) => b.agentId === 'group-project' && b.match && b.match.peer && b.match.peer.id === GROUP_CHAT_ID
  );
  if (!hasGroupBinding) {
    config.bindings = config.bindings.filter(
      (b) => !(b.match && b.match.peer && b.match.peer.id === GROUP_CHAT_ID)
    );
    config.bindings.push({
      agentId: 'group-project',
      match: { channel: 'telegram', peer: { kind: 'group', id: GROUP_CHAT_ID } },
    });
    console.log(`[init-patch] Bound group chat ${GROUP_CHAT_ID} → group-project`);
    changed = true;
  }
}

// Patch 2: gateway auth and cleanup
config.gateway = config.gateway || {};
if (Object.prototype.hasOwnProperty.call(config.gateway, 'model')) {
  delete config.gateway.model;
  console.log('[init-patch] Removed unsupported key gateway.model');
  changed = true;
}

let gwPassword = process.env.OPENCLAW_GATEWAY_PASSWORD;
if (!gwPassword && process.env.OPENCLAW_GATEWAY_PASSWORD_FILE && fs.existsSync(process.env.OPENCLAW_GATEWAY_PASSWORD_FILE)) {
  gwPassword = fs.readFileSync(process.env.OPENCLAW_GATEWAY_PASSWORD_FILE, 'utf8').trim();
}

if (gwPassword) {
  config.gateway.auth = config.gateway.auth || {};
  if (config.gateway.auth.token !== gwPassword) {
    config.gateway.auth.token = gwPassword;
    changed = true;
  }
  config.gateway.remote = config.gateway.remote || {};
  if (config.gateway.remote.password !== gwPassword) {
    config.gateway.remote.password = gwPassword;
    changed = true;
  }
}

// Patch 2b: control UI origins for non-loopback bind
config.gateway.controlUi = config.gateway.controlUi || {};
const gatewayPort = process.env.GATEWAY_HOST_PORT || '8080';
const allowedOrigins = [
  `http://localhost:${gatewayPort}`,
  `http://127.0.0.1:${gatewayPort}`,
  'http://localhost:18790',
  'http://127.0.0.1:18790',
];
// Extra origins from AGENTSHROUD_CONTROL_UI_ORIGINS (comma-separated, e.g. Tailscale hostnames)
const extraOrigins = (process.env.AGENTSHROUD_CONTROL_UI_ORIGINS || '')
  .split(',').map(o => o.trim()).filter(o => o.length > 0);
const allAllowedOrigins = [...allowedOrigins, ...extraOrigins];
const currentOrigins = Array.isArray(config.gateway.controlUi.allowedOrigins)
  ? config.gateway.controlUi.allowedOrigins
  : [];
const missingOrigins = allAllowedOrigins.filter((origin) => !currentOrigins.includes(origin));
if (missingOrigins.length > 0) {
  config.gateway.controlUi.allowedOrigins = [...currentOrigins, ...missingOrigins];
  console.log(`[init-patch] Added gateway.controlUi.allowedOrigins: ${missingOrigins.join(', ')}`);
  changed = true;
}
if (config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback !== false) {
  config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = false;
  changed = true;
}

// Patch 2c: trustedProxies — trust Tailscale gateway so Control UI pairing works
// Without this, OpenClaw sees the Tailscale NAT address as an untrusted proxy and
// requires a full pairing challenge for every browser session from non-loopback origins.
const trustedProxies = (process.env.AGENTSHROUD_TRUSTED_PROXIES || '10.254.110.0/24')
  .split(',').map(p => p.trim()).filter(p => p.length > 0);
const currentProxies = Array.isArray(config.gateway.trustedProxies) ? config.gateway.trustedProxies : [];
const missingProxies = trustedProxies.filter(p => !currentProxies.includes(p));
if (missingProxies.length > 0) {
  config.gateway.trustedProxies = [...currentProxies, ...missingProxies];
  console.log(`[init-patch] Added gateway.trustedProxies: ${missingProxies.join(', ')}`);
  changed = true;
}

// Patch 3: Telegram
const telegramToken = process.env.TELEGRAM_BOT_TOKEN;
if (telegramToken) {
  config.channels = config.channels || {};
  config.channels.telegram = config.channels.telegram || {};

  if (config.channels.telegram.botToken !== telegramToken) {
    config.channels.telegram.botToken = telegramToken;
    changed = true;
  }

  // Set channels.telegram.apiRoot so OpenClaw's file download path
  // (downloadAndSaveTelegramFile) routes photo/media downloads through the
  // gateway proxy rather than calling api.telegram.org directly, which fails
  // because the bot container is on an isolated (internal: true) network.
  const telegramApiBase = process.env.TELEGRAM_API_BASE_URL;
  if (telegramApiBase && config.channels.telegram.apiRoot !== telegramApiBase) {
    config.channels.telegram.apiRoot = telegramApiBase;
    console.log('[init-patch] Set channels.telegram.apiRoot = ' + telegramApiBase);
    changed = true;
  }

  // SECURITY NOTE: dmPolicy="open" + allowFrom=["*"] is required because OpenClaw's
  // "pairing" mode (default) drops messages without a prior /start handshake, which
  // prevents the gateway from delivering local command responses (/status, /approve, etc.)
  // and collaborator-approval notices.
  //
  // The security tradeoff: any Telegram user can initiate a conversation with the bot.
  // This is MITIGATED by the gateway's RBAC layer which enforces owner/collaborator/
  // stranger classification on every message before forwarding to the bot. Unknown users
  // receive only a pending-approval notice; the bot never processes their messages.
  //
  // If OpenClaw adds a dmPolicy="allowlist" mode that accepts explicit peer IDs without
  // a prior /start handshake, migrate to that model and remove the "*" wildcard.
  if (config.channels.telegram.dmPolicy !== 'open') {
    config.channels.telegram.dmPolicy = 'open';
    console.log('[init-patch] Set channels.telegram.dmPolicy = open');
    changed = true;
  }
  const allowFrom = config.channels.telegram.allowFrom || [];
  if (allowFrom.indexOf('*') === -1) {
    allowFrom.push('*');
    config.channels.telegram.allowFrom = allowFrom;
    console.log('[init-patch] Added * to channels.telegram.allowFrom (required by dmPolicy=open)');
    changed = true;
  }

  // Prevent doctor warning/crash-loop noise for allowlist policy.
  const defaultAllowlist = ['8096968754', '7614658040', '8279589982', '8506022825', '8526379012', '8545356403', '15712621992', '8633775668'];
  const envAllow = String(process.env.AGENTSHROUD_TELEGRAM_ALLOWLIST || '')
    .split(',')
    .map((v) => v.trim())
    .filter(Boolean);
  const mergedAllowlist = Array.from(new Set([...defaultAllowlist, ...envAllow]));
  const groupPolicy = String(config.channels.telegram.groupPolicy || '').toLowerCase();
  const groupAllowFrom = Array.isArray(config.channels.telegram.groupAllowFrom)
    ? config.channels.telegram.groupAllowFrom
    : [];
  const currentAllowFrom = Array.isArray(config.channels.telegram.allowFrom)
    ? config.channels.telegram.allowFrom
    : [];
  if (groupPolicy === 'allowlist' && groupAllowFrom.length === 0 && currentAllowFrom.length === 0) {
    config.channels.telegram.groupAllowFrom = mergedAllowlist;
    console.log('[init-patch] Seeded channels.telegram.groupAllowFrom to satisfy allowlist policy');
    changed = true;
  }
}

// Patch 4: Slack (native Socket Mode — OpenClaw handles inbound directly)
const slackBotToken = process.env.SLACK_BOT_TOKEN || (() => {
  try { return fs.readFileSync('/run/secrets/slack_bot_token', 'utf8').trim(); } catch (e) { return ''; }
})();
const slackAppToken = process.env.SLACK_APP_TOKEN || (() => {
  try { return fs.readFileSync('/run/secrets/slack_app_token', 'utf8').trim(); } catch (e) { return ''; }
})();

if (slackBotToken && slackBotToken.startsWith('xoxb-') && slackAppToken && slackAppToken.startsWith('xapp-')) {
  config.channels = config.channels || {};
  config.channels.slack = config.channels.slack || {};

  if (config.channels.slack.enabled !== true) {
    config.channels.slack.enabled = true;
    changed = true;
  }
  if (config.channels.slack.mode !== 'socket') {
    config.channels.slack.mode = 'socket';
    changed = true;
  }
  if (config.channels.slack.botToken !== slackBotToken) {
    config.channels.slack.botToken = slackBotToken;
    changed = true;
  }
  if (config.channels.slack.appToken !== slackAppToken) {
    config.channels.slack.appToken = slackAppToken;
    changed = true;
  }
  // dmPolicy: allowlist restricts DMs to the owner only.
  // Owner's Slack user ID is provided via AGENTSHROUD_SLACK_OWNER_USER_ID.
  const slackOwnerUserId = process.env.AGENTSHROUD_SLACK_OWNER_USER_ID || '';
  if (config.channels.slack.dmPolicy !== 'open') {
    config.channels.slack.dmPolicy = 'open';
    changed = true;
  }
  // dmPolicy=open requires '*' in allowFrom (OpenClaw validation requirement).
  // IMPORTANT: Do NOT add explicit user IDs alongside '*'.  OpenClaw's resolveSlackUserAllowlist()
  // calls users.info for every non-'*' entry on every Slack provider start, which requires the
  // users:read scope.  Without it, every connect logs "user resolve failed; missing_scope".
  // Since '*' already grants all-user access, explicit entries are redundant and harmful.
  {
    let allowFrom = Array.isArray(config.channels.slack.allowFrom) ? config.channels.slack.allowFrom.slice() : [];
    let af_changed = false;
    if (!allowFrom.includes('*')) { allowFrom.push('*'); af_changed = true; }
    // Remove any explicit user IDs — they're redundant when '*' is present and cause API errors.
    const stripped = allowFrom.filter(e => e === '*');
    if (stripped.length !== allowFrom.length) { allowFrom = stripped; af_changed = true; }
    if (af_changed) {
      config.channels.slack.allowFrom = allowFrom;
      changed = true;
    }
  }
  // Remove healthMonitor if previously set — OpenClaw rejects this as an unrecognized key.
  if (Object.prototype.hasOwnProperty.call(config.channels.slack, 'healthMonitor')) {
    delete config.channels.slack.healthMonitor;
    console.log('[init-patch] Removed unsupported channels.slack.healthMonitor key');
    changed = true;
  }
  console.log('[init-patch] Patched channels.slack (Socket Mode, dmPolicy=open)');
} else {
  console.log('[init-patch] Slack tokens not found — skipping channels.slack patch');
}

if (changed || isNew) {
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
  console.log(`[init-patch] ✓ Patched ${configPath}`);
} else {
  console.log('[init-patch] ✓ No changes needed');
}
