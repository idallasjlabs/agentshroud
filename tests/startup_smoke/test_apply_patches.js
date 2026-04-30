#!/usr/bin/env node
// tests/startup_smoke/test_apply_patches.js
//
// Validates key behaviors of docker/config/openclaw/apply-patches.js
// WITHOUT running Docker or OpenClaw. Invokes the script as a child process
// passing a temp config file path via argv[2] (the supported override).
//
// Run: node tests/startup_smoke/test_apply_patches.js
// Exit 0 = all assertions pass. Exit 1 = one or more failures.
//
// Assertions:
//   A1. channels.telegram.apiRoot is set to TELEGRAM_API_BASE_URL when env var is present.
//   A2. channels.telegram.apiRoot is NOT overwritten when env var is empty.
//   A3. Slack channels block is added when xoxb-/xapp- tokens are present.
//   A4. Slack channels block is NOT added when tokens are empty.
//   A5. Slack channels block is NOT added when tokens lack xoxb-/xapp- prefix.
//   A6. Stale Slack block removed when tokens are absent.
//   A7. Garbled multi-line Telegram token blob is rejected (shape guard) — botToken NOT written.
//   A8. Well-formed Telegram token is accepted and written to channels.telegram.botToken.

'use strict';

const path = require('path');
const fs = require('fs');
const os = require('os');
const { spawnSync } = require('child_process');

const PATCHES_FILE = path.resolve(__dirname, '../../docker/config/openclaw/apply-patches.js');

if (!fs.existsSync(PATCHES_FILE)) {
  console.error('FAIL: apply-patches.js not found at', PATCHES_FILE);
  process.exit(1);
}

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

/**
 * Run apply-patches.js against a fresh temp openclaw.json.
 * Passes the config path as argv[2] so the script uses it directly.
 * Returns the mutated config object.
 */
function runPatches(envOverrides, initialConfig) {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'asb-smoke-'));
  const configPath = path.join(tmpDir, 'openclaw.json');
  fs.writeFileSync(configPath, JSON.stringify(initialConfig, null, 2));

  const env = { ...process.env, ...envOverrides };

  const result = spawnSync(
    process.execPath,
    [PATCHES_FILE, configPath],
    { env, encoding: 'utf8', timeout: 10000 },
  );

  let mutated = initialConfig;
  try {
    mutated = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch (_) {
    // If the file was not written (error), return the original
  }

  fs.rmSync(tmpDir, { recursive: true, force: true });
  return mutated;
}

// Minimal valid openclaw.json skeleton
function baseConfig() {
  return {
    channels: {
      telegram: {
        token: 'fake-token',
      },
    },
  };
}

// ── Assertion Suite ────────────────────────────────────────────────────────

console.log('\n=== test_apply_patches.js ===\n');

// A1: apiRoot is set when TELEGRAM_API_BASE_URL is present
// Note: the telegram block in apply-patches.js is gated on TELEGRAM_BOT_TOKEN being non-empty.
{
  const cfg = runPatches(
    {
      TELEGRAM_BOT_TOKEN: '1234567890:AAFakeFakeFakeFakeFakeFakeFakeFakeFake123',
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A1: apiRoot set when TELEGRAM_API_BASE_URL present',
    cfg?.channels?.telegram?.apiRoot === 'http://gateway:8080/telegram-api',
    `got ${cfg?.channels?.telegram?.apiRoot}`,
  );
}

// A2: apiRoot is NOT overwritten when TELEGRAM_API_BASE_URL is empty
{
  const base = {
    channels: { telegram: { token: 'fake', apiRoot: 'http://existing:1234' } },
  };
  const cfg = runPatches({
    TELEGRAM_BOT_TOKEN: '1234567890:AAFakeFakeFakeFakeFakeFakeFakeFakeFake123',
    TELEGRAM_API_BASE_URL: '',
  }, base);
  assert(
    'A2: apiRoot not overwritten when TELEGRAM_API_BASE_URL is empty',
    cfg?.channels?.telegram?.apiRoot === 'http://existing:1234',
    `got ${cfg?.channels?.telegram?.apiRoot}`,
  );
}

// A3: Slack block added when valid tokens present
{
  const cfg = runPatches(
    {
      SLACK_BOT_TOKEN: 'xoxb-valid-token',
      SLACK_APP_TOKEN: 'xapp-valid-token',
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A3: Slack channel block added with valid xoxb-/xapp- tokens',
    cfg?.channels?.slack !== undefined,
    `channels.slack = ${JSON.stringify(cfg?.channels?.slack)}`,
  );
}

// A4: Slack block NOT added when tokens empty
{
  const cfg = runPatches(
    {
      SLACK_BOT_TOKEN: '',
      SLACK_APP_TOKEN: '',
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A4: Slack channel block not added with empty tokens',
    cfg?.channels?.slack === undefined,
    `channels.slack = ${JSON.stringify(cfg?.channels?.slack)}`,
  );
}

// A5: Slack block NOT added when tokens lack xoxb-/xapp- prefix
{
  const cfg = runPatches(
    {
      SLACK_BOT_TOKEN: 'invalid-bot-token',
      SLACK_APP_TOKEN: 'invalid-app-token',
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A5: Slack channel block not added with invalid token format',
    cfg?.channels?.slack === undefined,
    `channels.slack = ${JSON.stringify(cfg?.channels?.slack)}`,
  );
}

// A6: Stale Slack block REMOVED when tokens are absent (prevent invalid_auth crash loop)
{
  const staleConfig = {
    channels: {
      telegram: { token: 'fake' },
      slack: { enabled: true, mode: 'socket', botToken: 'xoxb-old', appToken: 'xapp-old' },
    },
  };
  const cfg = runPatches(
    {
      SLACK_BOT_TOKEN: '',
      SLACK_APP_TOKEN: '',
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    staleConfig,
  );
  assert(
    'A6: Stale channels.slack block removed when no valid tokens present',
    cfg?.channels?.slack === undefined,
    `channels.slack = ${JSON.stringify(cfg?.channels?.slack)}`,
  );
}

// A7: Garbled multi-line Telegram token is rejected — botToken NOT written to config
// Regression test for the marvin-dev secret issue: a pre-017e7bd Keychain entry
// that captured TUI output (label + asterisks + real token) instead of a bare value.
{
  const garbledToken = '\n  \u2192 Telegram bot token (marvin dev): **********************************************\n8736289266:AAGVzcmqiSaTSyPz5B8lJCcxkmZPg9jTe28';
  const cfg = runPatches(
    {
      TELEGRAM_BOT_TOKEN: garbledToken,
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A7: Garbled multi-line token: channels.telegram.botToken is NOT the full blob',
    cfg?.channels?.telegram?.botToken !== garbledToken,
    `got ${JSON.stringify(cfg?.channels?.telegram?.botToken)}`,
  );
  assert(
    'A7b: Garbled multi-line token: last-line normalizer extracts the real token',
    cfg?.channels?.telegram?.botToken === '8736289266:AAGVzcmqiSaTSyPz5B8lJCcxkmZPg9jTe28',
    `got ${JSON.stringify(cfg?.channels?.telegram?.botToken)}`,
  );
}

// A8: Well-formed Telegram token is written verbatim
{
  const validToken = '9876543210:BBValidTokenBBValidTokenBBValidToken1';
  const cfg = runPatches(
    {
      TELEGRAM_BOT_TOKEN: validToken,
      TELEGRAM_API_BASE_URL: 'http://gateway:8080/telegram-api',
    },
    baseConfig(),
  );
  assert(
    'A8: Well-formed Telegram token written verbatim to channels.telegram.botToken',
    cfg?.channels?.telegram?.botToken === validToken,
    `got ${JSON.stringify(cfg?.channels?.telegram?.botToken)}`,
  );
}

// ── Summary ────────────────────────────────────────────────────────────────

console.log(`\n${pass + fail} assertions: ${pass} passed, ${fail} failed\n`);

if (fail > 0) {
  process.exit(1);
}
