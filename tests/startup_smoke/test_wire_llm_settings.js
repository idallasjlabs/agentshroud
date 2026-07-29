#!/usr/bin/env node
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
// Patent Pending — U.S. Provisional Application No. 64/018,744
//
// tests/startup_smoke/test_wire_llm_settings.js
//
// Validates that the ~/.llm_settings-synced config (skills, MCP servers, persona)
// is ACTUALLY CONSUMED by each bot's init script — on SEPARATE per-agent paths.
//
// It runs the real init scripts (no Docker) against sandboxed HOME/data dirs with a
// stub `openclaw`/`hermes`/`node`/`python3`/`sha256sum` on PATH so the CLI-driven
// MCP registration is observable, then asserts on the resulting on-disk state.
//
// Run: node tests/startup_smoke/test_wire_llm_settings.js
// Exit 0 = all assertions pass. Exit 1 = one or more failures.
//
// Assertions:
//   OpenClaw path (init-openclaw-config.sh, .openclaw/*):
//     O1. graphify skill installed into ${OPENCLAW_DIR}/skills/graphify/SKILL.md
//     O2. agentshroud-gateway MCP registered via `openclaw mcp add` with the URL
//         read from the synced mcp/servers.json (NOT hardcoded).
//     O3. IDENTITY.md seeded from the synced agents/openclaw-identity.md persona.
//     O4. ISOLATION: Hermes' persona (hermes-soul.md) is NEVER written into OpenClaw.
//   Hermes path (init-config.sh, /opt/data/*):
//     H1. SOUL.md seeded from the synced agents/hermes-soul.md persona.
//     H2. graphify skill installed into ${DATA_DIR}/skills/graphify/SKILL.md
//     H3. agentshroud-gateway MCP registered via `hermes mcp add` with the URL from
//         the synced mcp/servers.json.
//     H4. ISOLATION: OpenClaw's persona (openclaw-identity) is NEVER seeded into SOUL.md.

'use strict';

const path = require('path');
const fs = require('fs');
const os = require('os');
const { spawnSync } = require('child_process');

const REPO = path.resolve(__dirname, '../..');
const OC_INIT = path.join(REPO, 'docker/scripts/init-openclaw-config.sh');
const HERMES_INIT = path.join(REPO, 'docker/bots/hermes/init-config.sh');

let pass = 0;
let fail = 0;

function assert(name, condition, detail) {
  if (condition) {
    console.log('  PASS:', name);
    pass++;
  } else {
    console.error('  FAIL:', name, detail ? `(${detail})` : '');
    fail++;
  }
}

function read(p) {
  try {
    return fs.readFileSync(p, 'utf8');
  } catch (_) {
    return '';
  }
}

// Build a fake ${DEFAULTS_DIR} tree mirroring what sync-llm-settings.sh bakes into
// the image at /app/config-defaults/<bot>/. Uses the REAL synced files from the repo
// so the test exercises the actual persona/skill/mcp content, not a fabricated stub.
function stageDefaults(defaultsDir, syncedRoot) {
  fs.mkdirSync(defaultsDir, { recursive: true });
  for (const sub of ['skills', 'mcp', 'agents']) {
    const src = path.join(syncedRoot, sub);
    if (fs.existsSync(src)) {
      fs.cpSync(src, path.join(defaultsDir, sub), { recursive: true });
    }
  }
}

// Write an executable stub script to `dir/name` that logs its argv to `logFile`
// and, for `mcp list`, prints nothing (so every server is treated as new).
function writeStub(dir, name, body) {
  const p = path.join(dir, name);
  fs.writeFileSync(p, body, { mode: 0o755 });
  fs.chmodSync(p, 0o755);
  return p;
}

// ── OpenClaw ────────────────────────────────────────────────────────────────
function runOpenClawInit() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'wire-oc-'));
  const home = path.join(tmp, 'home', 'node');
  const openclawDir = path.join(home, '.openclaw');
  const defaults = path.join(tmp, 'config-defaults', 'openclaw');
  const binDir = path.join(tmp, 'bin');
  const mcpLog = path.join(tmp, 'openclaw-mcp.log');

  fs.mkdirSync(openclawDir, { recursive: true });
  fs.mkdirSync(binDir, { recursive: true });
  // Stage the FULL baked defaults tree (cron/, workspace/, apply-patches.js, plus the
  // synced skills/mcp/agents) so the init script's earlier steps run to completion.
  fs.cpSync(path.join(REPO, 'docker/config/openclaw'), defaults, { recursive: true });

  // Stub `openclaw`: record `mcp set` (the correct verb — `add` probes the server
  // and fails at init). `mcp list` prints nothing so every server is treated as new.
  // If init ever regresses to `mcp add`, MCP_SET is never logged and O2 fails.
  writeStub(
    binDir,
    'openclaw',
    `#!/bin/bash\n` +
      `if [ "$1" = "mcp" ] && [ "$2" = "set" ]; then echo "MCP_SET $*" >> "${mcpLog}"; exit 0; fi\n` +
      `if [ "$1" = "mcp" ] && [ "$2" = "add" ]; then echo "MCP_ADD $*" >> "${mcpLog}"; exit 0; fi\n` +
      `if [ "$1" = "mcp" ] && [ "$2" = "list" ]; then exit 0; fi\n` +
      `exit 0\n`,
  );

  const env = {
    ...process.env,
    HOME: home,
    PATH: `${binDir}:${process.env.PATH}`,
    // Redirect the two hardcoded absolute paths the script uses via env-free consts:
    // the script derives OPENCLAW_DIR from HOME and DEFAULTS_DIR is a literal
    // /app/config-defaults/openclaw. We override that literal by pre-seeding the
    // literal path is not possible; instead the script is patched to honour these
    // envs when present (see INIT_DEFAULTS_DIR / INIT_OPENCLAW_DIR below).
    INIT_DEFAULTS_DIR: defaults,
    INIT_OPENCLAW_DIR: openclawDir,
    // Keep the init script's optional provider seeding quiet/deterministic.
    AGENTSHROUD_MODEL_MODE: 'local',
    NPM_CONFIG_PREFIX: '',
  };

  const res = spawnSync('bash', [OC_INIT], { env, encoding: 'utf8', timeout: 30000 });
  return { tmp, openclawDir, defaults, mcpLog, res };
}

// ── Hermes ──────────────────────────────────────────────────────────────────
// opts.staleSoul: if set, pre-place a stale, UNWRITABLE (mode 0444) SOUL.md on the
// volume before init runs. This reproduces the production trap where the volume holds
// a foreign-owned SOUL.md that a plain `cp` cannot overwrite (EACCES). A non-root test
// runner cannot chown to a foreign uid, but a 0444 file it owns triggers the identical
// "cp: cannot create ... Permission denied" open-for-write failure — so the init's
// rm+temp+mv path (which relies on the writable parent dir) is what must succeed.
function runHermesInit(opts = {}) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'wire-h-'));
  const dataDir = path.join(tmp, 'opt', 'data');
  const defaults = path.join(tmp, 'config-defaults', 'hermes');
  const binDir = path.join(tmp, 'bin');
  const mcpLog = path.join(tmp, 'hermes-mcp.log');

  fs.mkdirSync(dataDir, { recursive: true });
  fs.mkdirSync(binDir, { recursive: true });
  stageDefaults(defaults, path.join(REPO, 'docker/config/hermes'));
  // The Hermes init also seeds config.yaml/cron/workspace from defaults; stage those
  // so the script's earlier steps run to completion.
  for (const f of ['config.yaml.tmpl', 'SOUL.md']) {
    const src = path.join(REPO, 'docker/config/hermes', f);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(defaults, f));
  }
  for (const d of ['cron', 'workspace']) {
    const src = path.join(REPO, 'docker/config/hermes', d);
    if (fs.existsSync(src)) fs.cpSync(src, path.join(defaults, d), { recursive: true });
  }

  if (opts.staleSoul) {
    const staleFile = path.join(dataDir, 'SOUL.md');
    // Stale content that does NOT contain the connectivity-fix ssh-exec wrapper.
    fs.writeFileSync(staleFile, '# STALE SOUL (Jun 27)\nNo ssh-exec wrapper here.\n');
    fs.chmodSync(staleFile, 0o444); // read-only → plain cp overwrite fails (EACCES)
  }

  // Stub `hermes`: `mcp add`/`mcp list`/`cron *` succeed & print nothing. The gateway
  // MCP no longer routes through `hermes mcp add` (it is written into config.yaml
  // directly), so this stub only covers the pre-existing github-MCP stdio add.
  writeStub(
    binDir,
    'hermes',
    `#!/bin/bash\n` +
      `if [ "$1" = "mcp" ] && [ "$2" = "add" ]; then echo "MCP_ADD $*" >> "${mcpLog}"; exit 0; fi\n` +
      `if [ "$1" = "mcp" ] && [ "$2" = "list" ]; then exit 0; fi\n` +
      `exit 0\n`,
  );

  const env = {
    ...process.env,
    HOME: dataDir,
    PATH: `${binDir}:${process.env.PATH}`,
    INIT_DEFAULTS_DIR: defaults,
    INIT_DATA_DIR: dataDir,
  };

  const res = spawnSync('bash', [HERMES_INIT], { env, encoding: 'utf8', timeout: 30000 });
  return { tmp, dataDir, defaults, mcpLog, res };
}

console.log('\n=== test_wire_llm_settings.js ===\n');

// ── OpenClaw assertions ─────────────────────────────────────────────────────
console.log('OpenClaw (init-openclaw-config.sh):');
{
  const { openclawDir, mcpLog, res } = runOpenClawInit();
  if (res.status !== 0) {
    console.error('  init-openclaw-config.sh stderr:\n' + (res.stderr || '').slice(-2000));
  }

  // O1: graphify skill installed on OpenClaw's discovery path
  const ocSkill = path.join(openclawDir, 'skills', 'graphify', 'SKILL.md');
  assert('O1: graphify SKILL.md installed into .openclaw/skills/', fs.existsSync(ocSkill), ocSkill);

  // O2: MCP registered via the CORRECT verb `openclaw mcp set` (NOT `mcp add`, which
  // probes the endpoint and fails at init) with the URL from servers.json and the
  // canonical HTTP transport value "streamable-http".
  const ocMcp = read(mcpLog);
  assert(
    'O2: `openclaw mcp set agentshroud-gateway` called with servers.json URL + streamable-http',
    ocMcp.includes('MCP_SET') &&
      ocMcp.includes('agentshroud-gateway') &&
      ocMcp.includes('http://gateway:8080/mcp') &&
      ocMcp.includes('streamable-http'),
    `mcp log: ${JSON.stringify(ocMcp)}`,
  );
  assert(
    'O2b: init does NOT use the wrong verb `openclaw mcp add` for the gateway server',
    !ocMcp.includes('MCP_ADD'),
    `mcp log: ${JSON.stringify(ocMcp)}`,
  );

  // O3: IDENTITY.md seeded from the synced openclaw-identity persona
  const ocIdentity = read(path.join(openclawDir, 'workspace', 'IDENTITY.md'));
  assert(
    'O3: IDENTITY.md seeded from synced openclaw-identity.md (contains OpenClaw identity)',
    ocIdentity.includes('AgentShroud') && ocIdentity.includes('IDENTITY.md - Who I Am'),
    `identity head: ${JSON.stringify(ocIdentity.slice(0, 80))}`,
  );

  // O4: ISOLATION — Hermes' SOUL persona must never leak into OpenClaw workspace
  const ocIdentityLower = ocIdentity.toLowerCase();
  assert(
    'O4: ISOLATION — OpenClaw IDENTITY.md does NOT contain Hermes-soul persona',
    !ocIdentityLower.includes('you are **hermes**') &&
      !ocIdentityLower.includes('hermes — system identity'),
    'hermes persona leaked into openclaw identity',
  );
}

// Read the mcp_servers map from a Hermes config.yaml (minimal YAML — no PyYAML dep
// in-node; parse the flat two-level block we write).
function readHermesMcpServers(configPath) {
  const txt = read(configPath);
  const out = {};
  const lines = txt.split('\n');
  let inMcp = false;
  let curName = null;
  for (const line of lines) {
    if (/^mcp_servers:\s*$/.test(line)) { inMcp = true; continue; }
    if (inMcp && /^\S/.test(line)) break; // dedent to another top-level key
    if (!inMcp) continue;
    const nameM = line.match(/^ {2}([^\s:]+):\s*$/);
    if (nameM) { curName = nameM[1]; out[curName] = {}; continue; }
    const kvM = line.match(/^ {4}([^\s:]+):\s*(.+)\s*$/);
    if (kvM && curName) out[curName][kvM[1]] = kvM[2];
  }
  return out;
}

// ── Hermes assertions ───────────────────────────────────────────────────────
console.log('\nHermes (init-config.sh):');
{
  const { dataDir, res } = runHermesInit();
  if (res.status !== 0) {
    console.error('  init-config.sh stderr:\n' + (res.stderr || '').slice(-2000));
  }

  // H1: SOUL.md seeded from the synced hermes-soul persona
  const soul = read(path.join(dataDir, 'SOUL.md'));
  assert(
    'H1: SOUL.md seeded from synced hermes-soul.md (contains Hermes identity)',
    soul.includes('Hermes') && soul.toLowerCase().includes('system identity'),
    `soul head: ${JSON.stringify(soul.slice(0, 80))}`,
  );

  // H2: graphify skill installed on Hermes' discovery path
  const hSkill = path.join(dataDir, 'skills', 'graphify', 'SKILL.md');
  assert('H2: graphify SKILL.md installed into /opt/data/skills/', fs.existsSync(hSkill), hSkill);

  // H3: agentshroud-gateway is intentionally disabled in the synced servers.json
  // (2026-07-18: the gateway has never actually served /mcp — confirmed 404 —
  // so every Hermes boot failed this connection after 3 retries, which on the
  // vendored hermes-agent version correlates with a fatal container-wide
  // shutdown; see docker/config/hermes/mcp/servers.json and
  // ~/.llm_settings/mcp/servers.json). The reconciliation code skips disabled
  // entries entirely (init-config.sh: `if ... s.get("enabled") is False: continue`),
  // so it must NOT appear in config.yaml's mcp_servers at all.
  const servers = readHermesMcpServers(path.join(dataDir, 'config.yaml'));
  assert(
    'H3: config.yaml mcp_servers has no agentshroud-gateway entry (disabled in servers.json, gateway does not serve /mcp)',
    !servers['agentshroud-gateway'],
    `mcp_servers: ${JSON.stringify(servers)}`,
  );

  // H4: ISOLATION — OpenClaw's identity persona must never seed Hermes' SOUL
  const soulLower = soul.toLowerCase();
  assert(
    'H4: ISOLATION — Hermes SOUL.md does NOT contain OpenClaw identity persona',
    !soulLower.includes('identity.md - who i am') && !soulLower.includes('creature:'),
    'openclaw identity leaked into hermes soul',
  );
}

// ── Hermes SOUL overwrite over a foreign-owned / unwritable stale file ────────
console.log('\nHermes SOUL re-seed over a stale unwritable file:');
{
  const { dataDir, res } = runHermesInit({ staleSoul: true });
  if (res.status !== 0) {
    console.error('  init-config.sh stderr:\n' + (res.stderr || '').slice(-2000));
  }
  const soul = read(path.join(dataDir, 'SOUL.md'));
  // H5: the stale (0444) SOUL.md must be REPLACED by the synced persona.
  assert(
    'H5: stale unwritable SOUL.md replaced with synced hermes-soul.md',
    soul.includes('Hermes') && soul.toLowerCase().includes('system identity') &&
      !soul.includes('STALE SOUL'),
    `soul head: ${JSON.stringify(soul.slice(0, 80))}`,
  );
  // H6: the connectivity-fix ssh-exec wrapper is present after re-seed (the exact
  // production symptom: grep -c agentshroud-ssh-exec /opt/data/SOUL.md must be >= 1).
  const sshExecCount = (soul.match(/agentshroud-ssh-exec/g) || []).length;
  assert(
    'H6: re-seeded SOUL.md contains the connectivity-fix ssh-exec wrapper (>=1)',
    sshExecCount >= 1,
    `agentshroud-ssh-exec occurrences: ${sshExecCount}`,
  );
}

// ── Summary ──────────────────────────────────────────────────────────────────
console.log(`\n${pass + fail} assertions: ${pass} passed, ${fail} failed\n`);
if (fail > 0) process.exit(1);
