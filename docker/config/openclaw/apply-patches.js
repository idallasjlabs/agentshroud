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

// Patch 0b: models.providers.ollama fallback registration.
// This gives OpenClaw an explicit provider + model definition even if dynamic
// model discovery is unavailable at startup.
config.models = config.models || {};
config.models.providers = config.models.providers || {};
const currentOllama = config.models.providers.ollama || {};
const desiredOllamaModel = {
  id: LOCAL_MODEL_NAME,
  name: LOCAL_MODEL_NAME,
  reasoning: false,
  input: ['text'],
  contextWindow: 128000,
  maxTokens: 8192,
};
const desiredOllama = {
  baseUrl: OLLAMA_BASE_URL,
  api: OLLAMA_PROVIDER_API,
  models: [desiredOllamaModel],
};
if (JSON.stringify(currentOllama) !== JSON.stringify(desiredOllama)) {
  config.models.providers.ollama = desiredOllama;
  changed = true;
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

const cIdx = config.agents.list.findIndex((a) => a.id === 'collaborator');
if (cIdx >= 0) {
  if (config.agents.list[cIdx].model !== MAIN_MODEL) {
    config.agents.list[cIdx].model = MAIN_MODEL;
    changed = true;
  }
  if (config.agents.list[cIdx].memorySearch === false) {
    config.agents.list[cIdx].memorySearch = { enabled: false };
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
const currentOrigins = Array.isArray(config.gateway.controlUi.allowedOrigins)
  ? config.gateway.controlUi.allowedOrigins
  : [];
const missingOrigins = allowedOrigins.filter((origin) => !currentOrigins.includes(origin));
if (missingOrigins.length > 0) {
  config.gateway.controlUi.allowedOrigins = [...currentOrigins, ...missingOrigins];
  console.log(`[init-patch] Added gateway.controlUi.allowedOrigins: ${missingOrigins.join(', ')}`);
  changed = true;
}
if (config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback !== false) {
  config.gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback = false;
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

  // Prevent doctor warning/crash-loop noise for allowlist policy.
  const defaultAllowlist = ['8096968754', '7614658040', '8279589982', '8506022825', '8526379012', '8545356403'];
  const envAllow = String(process.env.AGENTSHROUD_TELEGRAM_ALLOWLIST || '')
    .split(',')
    .map((v) => v.trim())
    .filter(Boolean);
  const mergedAllowlist = Array.from(new Set([...defaultAllowlist, ...envAllow]));
  const groupPolicy = String(config.channels.telegram.groupPolicy || '').toLowerCase();
  const groupAllowFrom = Array.isArray(config.channels.telegram.groupAllowFrom)
    ? config.channels.telegram.groupAllowFrom
    : [];
  const allowFrom = Array.isArray(config.channels.telegram.allowFrom)
    ? config.channels.telegram.allowFrom
    : [];
  if (groupPolicy === 'allowlist' && groupAllowFrom.length === 0 && allowFrom.length === 0) {
    config.channels.telegram.groupAllowFrom = mergedAllowlist;
    console.log('[init-patch] Seeded channels.telegram.groupAllowFrom to satisfy allowlist policy');
    changed = true;
  }
}

if (changed || isNew) {
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
  console.log(`[init-patch] ✓ Patched ${configPath}`);
} else {
  console.log('[init-patch] ✓ No changes needed');
}
