#!/usr/bin/env node
// AgentShroud Outreach — Test Email Sender
// Uses iCloud SMTP (smtp.mail.me.com) with app-specific password from 1Password.
// Usage: node send-test.js

const { spawnSync } = require('child_process');
const nodemailer = require('nodemailer');
const fs = require('fs');

function secret(name) {
  try { return fs.readFileSync(`/run/secrets/${name}`, 'utf8').trim(); } catch { return null; }
}

async function main() {
  const masterPass = secret('1password_bot_master_password');
  const botEmail   = secret('1password_bot_email');
  const secretKey  = secret('1password_bot_secret_key');

  if (!masterPass || !botEmail || !secretKey) {
    console.error('FAILED: /run/secrets not available');
    process.exit(1);
  }

  // Sign in to 1Password
  spawnSync('op', ['account', 'add', '--address', 'my.1password.com',
    '--email', botEmail, '--secret-key', secretKey], { stdio: 'pipe' });

  const signin = spawnSync('op', ['signin', '--account', 'my', '--raw'],
    { input: masterPass, encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
  const session = signin.stdout.trim();
  if (!session) {
    console.error('FAILED: op signin —', signin.stderr.trim());
    process.exit(1);
  }

  // Retrieve iCloud app-specific password (item 25ghxryyvup5wpufgfldgc2vjm)
  const get = spawnSync('op', ['item', 'get', '25ghxryyvup5wpufgfldgc2vjm',
    '--vault', 'Agent Shroud Bot Credentials',
    '--fields', 'label=agentshroud app-specific password',
    '--reveal', '--session', session],
    { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
  const icloudPass = get.stdout.trim();
  if (!icloudPass) {
    console.error('FAILED: iCloud credential retrieval —', get.stderr.trim());
    process.exit(1);
  }

  // Send via iCloud SMTP
  const transporter = nodemailer.createTransport({
    host: 'smtp.mail.me.com',
    port: 587,
    secure: false,
    requireTLS: true,
    auth: { user: 'agentshroud.ai@icloud.com', pass: icloudPass }
  });

  try {
    const info = await transporter.sendMail({
      from: '"Isaiah Jefferson | AgentShroud" <agentshroud.ai@icloud.com>',
      to: 'idallasj@gmail.com',
      cc: 'isaiah_jefferson@mac.com',
      subject: '[TEST] AgentShroud Outreach Campaign — Ready to Send',
      text: [
        'Hi Isaiah,',
        '',
        'This confirms the AgentShroud podcast outreach campaign is loaded and ready.',
        '',
        '  Campaign: 44 podcasts — 24 direct email, 20 contact form',
        '  From: agentshroud.ai@icloud.com',
        '  Cc: idallasj@gmail.com, isaiah_jefferson@mac.com',
        '',
        'Reply "GO" to the bot on Telegram to launch the full campaign.',
        '',
        '— AgentShroud Bot'
      ].join('\n')
    });
    console.log('OK: sent — ' + info.messageId);
  } catch (e) {
    console.error('FAILED: SMTP —', e.message);
    process.exit(1);
  }
}

main();
