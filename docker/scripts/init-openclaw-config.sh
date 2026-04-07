#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# init-openclaw-config.sh — Bootstrap OpenClaw config from image defaults.
#
# Called by entrypoint-agentshroud.sh before OpenClaw starts.
# Safe to run on every container startup (all operations are idempotent).
#
# What this does:
#   1. Bootstraps cron/jobs.json from image defaults (only on fresh volume)
#   2. Patches openclaw.json for required agent routing (always, idempotent)
#   3. Manages workspace brand/identity files
#   4. Refreshes SSH config (approved host allowlist) from image defaults

set -euo pipefail

DEFAULTS_DIR="/app/config-defaults/openclaw"
OPENCLAW_DIR="/home/node/.openclaw"

# ── 1. cron/jobs.json — bootstrap only if missing ────────────────────────────
# We only copy on first run (missing file) so that live CLI changes via
# `openclaw cron edit` are not overwritten on restart.
# If you want to forcibly reset cron jobs, delete the volume file and restart.

CRON_DIR="${OPENCLAW_DIR}/cron"
CRON_JOBS="${CRON_DIR}/jobs.json"

mkdir -p "${CRON_DIR}"

if [ ! -f "${CRON_JOBS}" ]; then
  cp "${DEFAULTS_DIR}/cron/jobs.json" "${CRON_JOBS}"
  echo "[init] ✓ Bootstrapped cron/jobs.json from image defaults (first run)"
else
  echo "[init] ✓ cron/jobs.json already present — skipping (use CLI to modify)"
fi

# ── 2. openclaw.json — patch required fields (idempotent) ────────────────────
# Applies agents.list and bindings patches every startup.
# All other fields (Telegram token, channel config, etc.) are preserved.

node "${DEFAULTS_DIR}/apply-patches.js" "${OPENCLAW_DIR}/openclaw.json"

# ── 2b. auth-profiles.json — inject provider credentials (cloud + local) ─────
# OpenClaw validates credentials from its per-agent auth store before making
# API calls. We seed provider keys here so model-mode switching is one env var.
AUTH_PROFILES_DIR="${OPENCLAW_DIR}/agents/main/agent"
AUTH_PROFILES="${AUTH_PROFILES_DIR}/auth-profiles.json"

mkdir -p "${AUTH_PROFILES_DIR}"

node -e "
  const fs = require('fs');
  const p = '${AUTH_PROFILES}';
  let raw = {};
  try { raw = JSON.parse(fs.readFileSync(p, 'utf8')); } catch (e) {}

  const store = (raw && typeof raw === 'object' && raw.profiles && typeof raw.profiles === 'object')
    ? raw
    : { version: 1, profiles: {} };

  let changed = !raw.profiles;

  // Migrate legacy { provider: { apiKey } } shape to OpenClaw auth profile store.
  if (!raw.profiles && raw && typeof raw === 'object') {
    for (const [provider, value] of Object.entries(raw)) {
      const apiKey = value && typeof value === 'object' ? String(value.apiKey || value.key || '').trim() : '';
      if (!apiKey) continue;
      const profileId = provider + ':default';
      store.profiles[profileId] = { type: 'api_key', provider, key: apiKey };
      changed = true;
    }
  }

  const setApiKey = (provider, key) => {
    const normalized = String(key || '').trim();
    if (!normalized) return;
    const profileId = provider + ':default';
    const next = { type: 'api_key', provider, key: normalized };
    const prev = store.profiles[profileId];
    if (!prev || prev.type !== next.type || prev.provider !== next.provider || prev.key !== next.key) {
      store.profiles[profileId] = next;
      changed = true;
    }
  };

  setApiKey('anthropic', process.env.ANTHROPIC_OAUTH_TOKEN || process.env.ANTHROPIC_API_KEY || '');
  setApiKey('google', process.env.GOOGLE_API_KEY || '');
  setApiKey('openai', process.env.OPENAI_API_KEY || '');

  const modelMode = String(process.env.AGENTSHROUD_MODEL_MODE || 'local').toLowerCase();
  const localOnly = modelMode !== 'cloud' || String(process.env.OPENCLAW_MAIN_MODEL || '').startsWith('ollama/');
  if (localOnly) {
    setApiKey('ollama', process.env.OLLAMA_API_KEY || 'ollama-local');
  }

  if (changed) {
    fs.writeFileSync(p, JSON.stringify({
      version: Number(store.version || 1),
      profiles: store.profiles || {}
    }, null, 2), 'utf8');
    console.log('[init] ✓ Seeded auth-profiles.json for available providers (anthropic/google/openai/ollama)');
  } else {
    console.log('[init] ✓ auth-profiles.json already up-to-date');
  }
"
chmod 600 "${AUTH_PROFILES}" 2>/dev/null || true

# Mirror provider auth at OpenClaw root. Some OpenClaw flows (including pairing/
# channel runs) resolve provider auth from ~/.openclaw/auth-profiles.json.
ROOT_AUTH_PROFILES="${OPENCLAW_DIR}/auth-profiles.json"
cp "${AUTH_PROFILES}" "${ROOT_AUTH_PROFILES}"
chmod 600 "${ROOT_AUTH_PROFILES}" 2>/dev/null || true

# ── 2c. models.json — ensure Ollama provider/model registration for local mode ─
# OpenClaw can fail with "Unknown model: ollama/<model>" when provider metadata
# is left at image defaults (127.0.0.1 + empty models[]). We register the active
# Ollama endpoint and local model name on every startup.
MODELS_JSON="${AUTH_PROFILES_DIR}/models.json"

node -e "
  const fs = require('fs');
  const p = '${MODELS_JSON}';
  let cfg = {};
  try { cfg = JSON.parse(fs.readFileSync(p, 'utf8')); } catch (e) {}
  cfg.providers = cfg.providers || {};
  cfg.providers.ollama = cfg.providers.ollama || {};

  const modelRef = String(process.env.AGENTSHROUD_LOCAL_MODEL_REF || 'ollama/qwen3:14b');
  const modelName = String(process.env.AGENTSHROUD_LOCAL_MODEL || modelRef.split('/').slice(-1)[0] || 'qwen3:14b');
  const rawBaseUrl = String(process.env.OLLAMA_BASE_URL || 'http://gateway:8080/v1').replace(/\/+$/, '');
  const baseUrl = /\/v1$/i.test(rawBaseUrl) ? rawBaseUrl : rawBaseUrl + '/v1';

  let changed = false;
  const setIfChanged = (k, v) => {
    if (cfg.providers.ollama[k] !== v) {
      cfg.providers.ollama[k] = v;
      changed = true;
    }
  };

  setIfChanged('baseUrl', baseUrl);
  setIfChanged('api', 'ollama');
  setIfChanged('apiKey', 'OLLAMA_API_KEY');

  const existingModels = Array.isArray(cfg.providers.ollama.models) ? cfg.providers.ollama.models : [];
  if (!existingModels.includes(modelName)) {
    cfg.providers.ollama.models = [...existingModels, modelName];
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(p, JSON.stringify(cfg, null, 2), 'utf8');
    console.log('[init] ✓ Registered Ollama provider/models in models.json');
  } else {
    console.log('[init] ✓ models.json already up-to-date');
  }
"
chmod 600 "${MODELS_JSON}" 2>/dev/null || true

# Mirror provider catalog at OpenClaw root for channel/runtime resolvers.
ROOT_MODELS_JSON="${OPENCLAW_DIR}/models.json"
cp "${MODELS_JSON}" "${ROOT_MODELS_JSON}"
chmod 600 "${ROOT_MODELS_JSON}" 2>/dev/null || true

# Security: harden config and state dir permissions
chmod 700 "${OPENCLAW_DIR}" 2>/dev/null || true
chmod 600 "${OPENCLAW_DIR}/openclaw.json" 2>/dev/null || true

# ── 3. Workspace brand/identity files ────────────────────────────────────────
# BRAND.md    — always refreshed from image (authoritative trademark & brand rules)
# IDENTITY.md — seeded on first run only (bot evolves this over time)
# AGENTS.md   — append "read BRAND.md" instruction if not already present

WORKSPACE_DIR="${OPENCLAW_DIR}/workspace"
mkdir -p "${WORKSPACE_DIR}"

# BRAND.md: always overwrite — it's the authoritative source from the repo.
cp "${DEFAULTS_DIR}/workspace/BRAND.md" "${WORKSPACE_DIR}/BRAND.md"
echo "[init] ✓ Refreshed BRAND.md (trademark & brand rules)"

# SOUL.md: always overwrite — anti-hallucination rules for the main agent.
# Without this, after long sessions the bot generates fake security block messages
# instead of answering questions plainly (B1.14b regression).
if [ -f "${DEFAULTS_DIR}/workspace/SOUL.md" ]; then
  cp "${DEFAULTS_DIR}/workspace/SOUL.md" "${WORKSPACE_DIR}/SOUL.md"
  echo "[init] ✓ Refreshed SOUL.md (anti-hallucination rules for main agent)"
fi

# DEVELOPER.md: always overwrite — development context (TDD, SDLC, skill/agent lookup).
# Gives the bot the same development standards as Claude Code when working on the repo.
# Must match repo on every restart so changes baked into the image take effect immediately.
if [ -f "${DEFAULTS_DIR}/workspace/DEVELOPER.md" ]; then
  cp "${DEFAULTS_DIR}/workspace/DEVELOPER.md" "${WORKSPACE_DIR}/DEVELOPER.md"
  echo "[init] ✓ Refreshed DEVELOPER.md (development context)"
fi

# IDENTITY.md: seed only if missing or still the unfilled OpenClaw default.
IDENTITY_FILE="${WORKSPACE_DIR}/IDENTITY.md"
if [ ! -f "${IDENTITY_FILE}" ] || grep -q "_Fill this in during your first conversation_" "${IDENTITY_FILE}" 2>/dev/null; then
  cp "${DEFAULTS_DIR}/workspace/IDENTITY.md" "${IDENTITY_FILE}"
  echo "[init] ✓ Seeded IDENTITY.md with AgentShroud identity"
else
  echo "[init] ✓ IDENTITY.md already set — skipping"
fi

# context.md: seed only if missing — nightly cron overwrites daily
CONTEXT_FILE="${WORKSPACE_DIR}/memory/context.md"
mkdir -p "${WORKSPACE_DIR}/memory/journal"
if [ ! -f "${CONTEXT_FILE}" ]; then
  if [ -f "${DEFAULTS_DIR}/workspace/memory/context.md" ]; then
    cp "${DEFAULTS_DIR}/workspace/memory/context.md" "${CONTEXT_FILE}"
    echo "[init] ✓ Seeded context.md (initial operational context)"
  fi
else
  echo "[init] ✓ context.md already exists — skipping"
fi

# --- OpenClaw runtime version management ---
# Seeds openclaw into the NPM_CONFIG_PREFIX volume (writable at runtime).
# This enables the "Update now" button to install newer versions without
# hitting the read-only rootfs (/usr/local/).
IMAGE_VERSION_FILE="/app/.openclaw-image-version"
RUNTIME_VERSION_FILE="${NPM_CONFIG_PREFIX:-/usr/local}/.openclaw-runtime-version"

if [ -n "${NPM_CONFIG_PREFIX}" ] && [ -d "${NPM_CONFIG_PREFIX}" ]; then
  IMAGE_VER="unknown"
  [ -f "${IMAGE_VERSION_FILE}" ] && IMAGE_VER=$(cat "${IMAGE_VERSION_FILE}")

  RUNTIME_VER="none"
  [ -f "${RUNTIME_VERSION_FILE}" ] && RUNTIME_VER=$(cat "${RUNTIME_VERSION_FILE}")

  if [ "${RUNTIME_VER}" != "${IMAGE_VER}" ]; then
    echo "[init] Seeding openclaw ${IMAGE_VER} into NPM_CONFIG_PREFIX (was: ${RUNTIME_VER})..."
    if npm install -g "openclaw@${IMAGE_VER}" 2>&1 | tail -5; then
      echo "${IMAGE_VER}" > "${RUNTIME_VERSION_FILE}"
      echo "[init] ✓ openclaw ${IMAGE_VER} seeded to ${NPM_CONFIG_PREFIX}"
      # Re-apply SDK patches to the volume-installed openclaw.
      # The image build patches /usr/local/lib/node_modules/openclaw/, but the
      # volume copy at NPM_CONFIG_PREFIX/lib/node_modules/ is unpatched.
      # Without this, grammY and the Anthropic SDK bypass the gateway proxy.
      for _patch in patch-anthropic-sdk.sh patch-telegram-sdk.sh patch-slack-sdk.sh patch-ws-proxy.sh; do
        if [ -x "/usr/local/bin/${_patch}" ]; then
          echo "[init] Re-applying ${_patch} to NPM_CONFIG_PREFIX install..."
          sh "/usr/local/bin/${_patch}" 2>&1 || echo "[init] ⚠ ${_patch} failed (non-fatal)"
        fi
      done
    else
      echo "[init] ⚠ openclaw seed failed — bot will use image-bundled version (/usr/local/bin/openclaw)"
    fi
  else
    echo "[init] ✓ openclaw ${RUNTIME_VER} already in NPM_CONFIG_PREFIX"
  fi

  # Always ensure ws proxy patch is applied to the runtime volume.
  # The patch is idempotent (skips if AGENTSHROUD_WS_PROXY_PATCHED marker found).
  # Must run outside the version-check block because existing volumes pre-date the patch.
  if [ -x "/usr/local/bin/patch-ws-proxy.sh" ]; then
    echo "[init] Ensuring ws proxy patch on NPM_CONFIG_PREFIX install..."
    sh /usr/local/bin/patch-ws-proxy.sh 2>&1 || echo "[init] ⚠ patch-ws-proxy.sh failed (non-fatal)"
  fi

  # Always ensure Telegram/Anthropic/Slack SDK patches are applied to the runtime volume.
  # These patches route API calls through the gateway proxy. They are idempotent — each
  # checks for the old string before replacing, so re-running on already-patched files is safe.
  # Must run outside the version-check block: plain container recreates (same image version)
  # skip the version-check block entirely, leaving the runtime volume copy unpatched.
  for _sdk_patch in patch-telegram-sdk.sh patch-anthropic-sdk.sh patch-slack-sdk.sh; do
    if [ -x "/usr/local/bin/${_sdk_patch}" ]; then
      echo "[init] Ensuring ${_sdk_patch} on NPM_CONFIG_PREFIX install..."
      sh "/usr/local/bin/${_sdk_patch}" 2>&1 || echo "[init] ⚠ ${_sdk_patch} failed (non-fatal)"
    fi
  done
fi

# AGENTS.md: add "read BRAND.md" to the session startup checklist if absent.
AGENTS_FILE="${WORKSPACE_DIR}/AGENTS.md"
if [ -f "${AGENTS_FILE}" ] && ! grep -q "BRAND.md" "${AGENTS_FILE}" 2>/dev/null; then
  # Insert after the last numbered item in the "Every Session" section
  sed -i 's/4\. \*\*If in MAIN SESSION\*\*/5. Read `BRAND.md` — AgentShroud trademark \& communication standards\n4. **If in MAIN SESSION**/' "${AGENTS_FILE}"
  echo "[init] ✓ Added BRAND.md to AGENTS.md session startup checklist"
else
  echo "[init] ✓ AGENTS.md already references BRAND.md — skipping"
fi

# ── 3b. Collaborator workspace files ─────────────────────────────────────────
# SOUL.md    — always refresh (authoritative anti-hallucination rules)
# PUBLIC-INFO.md — seed only if missing (collaborator can't overwrite project info)
#
# The collaborator agent runs in a separate workspace at .agentshroud/collaborator-workspace/.
# Without these files the agent has no anti-hallucination rules and fabricates
# fake security block messages instead of answering questions normally.

COLLAB_WORKSPACE_DIR="${OPENCLAW_DIR}/collaborator-workspace"
COLLAB_DEFAULTS="${DEFAULTS_DIR}/collaborator-workspace"

if [ -d "${COLLAB_DEFAULTS}" ]; then
  mkdir -p "${COLLAB_WORKSPACE_DIR}"

  # SOUL.md: always overwrite — authoritative, must match repo on every restart
  if [ -f "${COLLAB_DEFAULTS}/SOUL.md" ]; then
    cp "${COLLAB_DEFAULTS}/SOUL.md" "${COLLAB_WORKSPACE_DIR}/SOUL.md"
    echo "[init] ✓ Refreshed collaborator SOUL.md (anti-hallucination rules)"
  fi

  # PUBLIC-INFO.md: seed only if missing
  if [ ! -f "${COLLAB_WORKSPACE_DIR}/PUBLIC-INFO.md" ] && [ -f "${COLLAB_DEFAULTS}/PUBLIC-INFO.md" ]; then
    cp "${COLLAB_DEFAULTS}/PUBLIC-INFO.md" "${COLLAB_WORKSPACE_DIR}/PUBLIC-INFO.md"
    echo "[init] ✓ Seeded collaborator PUBLIC-INFO.md"
  else
    echo "[init] ✓ Collaborator PUBLIC-INFO.md already present — skipping"
  fi
else
  echo "[init] ⚠ Collaborator workspace defaults not found at ${COLLAB_DEFAULTS} — skipping"
fi

# ── 3c. Claude Code config — agents, skills, hooks, ORCHESTRATOR.md ──────────
# Always refresh on every startup so repo changes take effect after rebuild.
# Hooks fail gracefully (check for tools before running) so safe in container.

CLAUDE_DEFAULTS="/app/config-defaults/claude"
CLAUDE_CONFIG_DIR="${WORKSPACE_DIR}/.claude"

if [ -d "${CLAUDE_DEFAULTS}" ]; then
  mkdir -p "${CLAUDE_CONFIG_DIR}"

  # settings.json and ORCHESTRATOR.md — always overwrite (authoritative from image)
  [ -f "${CLAUDE_DEFAULTS}/settings.json" ] && cp "${CLAUDE_DEFAULTS}/settings.json" "${CLAUDE_CONFIG_DIR}/settings.json"
  [ -f "${CLAUDE_DEFAULTS}/ORCHESTRATOR.md" ] && cp "${CLAUDE_DEFAULTS}/ORCHESTRATOR.md" "${CLAUDE_CONFIG_DIR}/ORCHESTRATOR.md"

  # agents/ — always overwrite (authoritative from image)
  if [ -d "${CLAUDE_DEFAULTS}/agents" ]; then
    mkdir -p "${CLAUDE_CONFIG_DIR}/agents"
    cp -r "${CLAUDE_DEFAULTS}/agents/"* "${CLAUDE_CONFIG_DIR}/agents/" 2>/dev/null || true
  fi

  # skills/ — always overwrite (authoritative from image)
  if [ -d "${CLAUDE_DEFAULTS}/skills" ]; then
    mkdir -p "${CLAUDE_CONFIG_DIR}/skills"
    cp -r "${CLAUDE_DEFAULTS}/skills/"* "${CLAUDE_CONFIG_DIR}/skills/" 2>/dev/null || true
  fi

  # scripts/ (hook scripts) — always overwrite, ensure executable
  if [ -d "${CLAUDE_DEFAULTS}/scripts" ]; then
    mkdir -p "${CLAUDE_CONFIG_DIR}/scripts"
    cp -r "${CLAUDE_DEFAULTS}/scripts/"* "${CLAUDE_CONFIG_DIR}/scripts/" 2>/dev/null || true
    find "${CLAUDE_CONFIG_DIR}/scripts" -type f -name "*.sh" -exec chmod +x {} + 2>/dev/null || true
  fi

  echo "[init] ✓ Refreshed .claude config ($(ls "${CLAUDE_CONFIG_DIR}/agents" 2>/dev/null | wc -l | tr -d ' ') agents, $(ls "${CLAUDE_CONFIG_DIR}/skills" 2>/dev/null | wc -l | tr -d ' ') skills, hooks)"
else
  echo "[init] ⚠ Claude config defaults not found at ${CLAUDE_DEFAULTS} — skipping"
fi

# ── 3d. Gemini CLI config — agents, GEMINI.md, settings.json ─────────────────
# Always refresh on every startup so repo changes take effect after rebuild.

GEMINI_DEFAULTS="/app/config-defaults/gemini"
GEMINI_CONFIG_DIR="${WORKSPACE_DIR}/.gemini"

if [ -d "${GEMINI_DEFAULTS}" ]; then
  mkdir -p "${GEMINI_CONFIG_DIR}"

  [ -f "${GEMINI_DEFAULTS}/GEMINI.md" ] && cp "${GEMINI_DEFAULTS}/GEMINI.md" "${GEMINI_CONFIG_DIR}/GEMINI.md"
  [ -f "${GEMINI_DEFAULTS}/settings.json" ] && cp "${GEMINI_DEFAULTS}/settings.json" "${GEMINI_CONFIG_DIR}/settings.json"

  if [ -d "${GEMINI_DEFAULTS}/agents" ]; then
    mkdir -p "${GEMINI_CONFIG_DIR}/agents"
    cp -r "${GEMINI_DEFAULTS}/agents/"* "${GEMINI_CONFIG_DIR}/agents/" 2>/dev/null || true
  fi

  echo "[init] ✓ Refreshed .gemini config ($(ls "${GEMINI_CONFIG_DIR}/agents" 2>/dev/null | wc -l | tr -d ' ') agents)"
else
  echo "[init] ⚠ Gemini config defaults not found at ${GEMINI_DEFAULTS} — skipping"
fi

# ── 3e. Codex config — agents, AGENTS.md, config.toml ────────────────────────
# Always refresh on every startup so repo changes take effect after rebuild.

CODEX_DEFAULTS="/app/config-defaults/codex"
CODEX_CONFIG_DIR="${WORKSPACE_DIR}/.codex"

if [ -d "${CODEX_DEFAULTS}" ]; then
  mkdir -p "${CODEX_CONFIG_DIR}"

  [ -f "${CODEX_DEFAULTS}/AGENTS.md" ] && cp "${CODEX_DEFAULTS}/AGENTS.md" "${CODEX_CONFIG_DIR}/AGENTS.md"
  [ -f "${CODEX_DEFAULTS}/config.toml" ] && cp "${CODEX_DEFAULTS}/config.toml" "${CODEX_CONFIG_DIR}/config.toml"

  if [ -d "${CODEX_DEFAULTS}/agents" ]; then
    mkdir -p "${CODEX_CONFIG_DIR}/agents"
    cp -r "${CODEX_DEFAULTS}/agents/"* "${CODEX_CONFIG_DIR}/agents/" 2>/dev/null || true
  fi

  echo "[init] ✓ Refreshed .codex config ($(ls "${CODEX_CONFIG_DIR}/agents" 2>/dev/null | wc -l | tr -d ' ') agents)"
else
  echo "[init] ⚠ Codex config defaults not found at ${CODEX_DEFAULTS} — skipping"
fi

# ── 4. Memory persistence — backup/restore across fresh installs ─────────────
# Memory files (MEMORY.md, memory/*.md) are the bot's continuity.
# They live on the workspace volume, which survives rebuilds but not volume
# deletion. A host-mounted backup directory provides durability across
# fresh installs, volume resets, and machine migrations.

MEMORY_BACKUP_DIR="/app/memory-backups"
MEMORY_DIR="${WORKSPACE_DIR}/memory"
MEMORY_FILE="${WORKSPACE_DIR}/MEMORY.md"

# Restore: independently restore each memory artifact if missing from workspace.
# Each check is independent so a partial backup (e.g. memory/ present but MEMORY.md
# missing) still restores whatever is available.
if [ -d "${MEMORY_BACKUP_DIR}" ] && [ "$(ls -A ${MEMORY_BACKUP_DIR} 2>/dev/null)" ]; then
  _restored=0
  # MEMORY.md — restore if missing from workspace and present in backup
  if [ ! -f "${MEMORY_FILE}" ] && [ -f "${MEMORY_BACKUP_DIR}/MEMORY.md" ]; then
    cp "${MEMORY_BACKUP_DIR}/MEMORY.md" "${MEMORY_FILE}"
    echo "[init] ✓ Restored MEMORY.md"
    _restored=$((_restored + 1))
  fi
  # memory/ directory — restore if missing or empty
  if { [ ! -d "${MEMORY_DIR}" ] || [ -z "$(ls -A "${MEMORY_DIR}" 2>/dev/null)" ]; } && [ -d "${MEMORY_BACKUP_DIR}/memory" ]; then
    mkdir -p "${MEMORY_DIR}"
    cp -r "${MEMORY_BACKUP_DIR}/memory/"* "${MEMORY_DIR}/" 2>/dev/null || true
    echo "[init] ✓ Restored memory/ directory ($(ls "${MEMORY_DIR}" 2>/dev/null | wc -l | tr -d ' ') files)"
    _restored=$((_restored + 1))
  fi
  # Workspace files — restore each independently if missing
  for f in USER.md TOOLS.md HEARTBEAT.md; do
    if [ ! -f "${WORKSPACE_DIR}/${f}" ] && [ -f "${MEMORY_BACKUP_DIR}/${f}" ]; then
      cp "${MEMORY_BACKUP_DIR}/${f}" "${WORKSPACE_DIR}/${f}"
      echo "[init] ✓ Restored ${f}"
      _restored=$((_restored + 1))
    fi
  done
  if [ "${_restored}" -eq 0 ]; then
    echo "[init] ✓ Memory already present — no restore needed"
  fi
else
  echo "[init] ✓ No memory backup found (first-ever install or backup not mounted)"
fi

# Backup: save current memory to backup directory (runs every startup)
if [ -d "${MEMORY_BACKUP_DIR}" ]; then
  if [ -f "${MEMORY_FILE}" ] || [ -d "${MEMORY_DIR}" ]; then
    if touch "${MEMORY_BACKUP_DIR}/.write-test" 2>/dev/null && rm -f "${MEMORY_BACKUP_DIR}/.write-test"; then
      [ -f "${MEMORY_FILE}" ] && cp -f "${MEMORY_FILE}" "${MEMORY_BACKUP_DIR}/MEMORY.md"
      if [ -d "${MEMORY_DIR}" ]; then
        mkdir -p "${MEMORY_BACKUP_DIR}/memory"
        cp -rf "${MEMORY_DIR}/"* "${MEMORY_BACKUP_DIR}/memory/" 2>/dev/null || true
      fi
      for f in USER.md TOOLS.md HEARTBEAT.md; do
        [ -f "${WORKSPACE_DIR}/${f}" ] && cp -f "${WORKSPACE_DIR}/${f}" "${MEMORY_BACKUP_DIR}/${f}"
      done
      echo "[init] ✓ Memory backed up to ${MEMORY_BACKUP_DIR}"
    else
      echo "[init] ⚠ Memory backup mount is read-only — skipping backup (memory NOT persisted to host)"
    fi
  fi
fi

# ── 4. SSH config — always refresh from image (approved host allowlist) ──────
# Authoritative allowlist of approved SSH hosts.
# Overwrites on every startup so repo changes take effect on next restart.
# To add a new host: update docker/config/ssh/config in the repo, rebuild image.

SSH_CONFIG_SRC="/app/config-defaults/ssh/config"
SSH_TMP="/home/node/.ssh-tmp"

# SECURITY (H1): SSH volume is mounted read-only.
# - SSH key stays in the RO volume (/home/node/.ssh/id_ed25519)
# - Config and known_hosts go to tmpfs (/home/node/.ssh-tmp/)
# - OpenClaw SSH commands will use the tmpfs config

if [ -f "${SSH_CONFIG_SRC}" ]; then
  mkdir -p "${SSH_TMP}"
  cp "${SSH_CONFIG_SRC}" "${SSH_TMP}/config"
  chmod 600 "${SSH_TMP}/config"
  # Ensure IdentityFile points to RO volume key (absolute path)
  sed -i 's|~/.ssh/id_ed25519|/home/node/.ssh/id_ed25519|g' "${SSH_TMP}/config"
  # known_hosts in tmpfs (ephemeral, resets on restart)
  printf '\n# H1 fix: known_hosts in tmpfs\nHost *\n    UserKnownHostsFile /home/node/.ssh-tmp/known_hosts\n' >> "${SSH_TMP}/config"
  echo "[init] ✓ SSH config in tmpfs (key volume is read-only)"
else
  echo "[init] ⚠ SSH config defaults not found — skipping"
fi

