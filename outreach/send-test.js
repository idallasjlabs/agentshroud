#!/usr/bin/env node
// AgentShroud Outreach — Test Email Sender
// Default: iCloud SMTP (smtp.mail.me.com) from agentshroud.ai@icloud.com
// Gmail:   node send-test.js --gmail    (smtp.gmail.com:465 from agentshroud.ai@gmail.com)
// Preview: node send-test.js --preview  (sends real outreach body from first manifest entry to your inbox)
// Usage: node send-test.js [--gmail] [--preview]

const { spawnSync } = require('child_process');
const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');

const useGmail  = process.argv.includes('--gmail');
const preview   = process.argv.includes('--preview');

function stripMarkdown(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '$1')                       // **bold** → bold
    .replace(/\*(.+?)\*/g, '$1')                            // *italic* → italic
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1: $2');        // [text](url) → text: url
}

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

  let smtpUser, smtpPass, smtpConfig, fromAddress;

  if (useGmail) {
    // Retrieve Gmail app password (AgentShroud - Google, field: app password)
    const get = spawnSync('op', ['item', 'get', 'wgblbbbqkmnyobh2xtr6r65k34',
      '--vault', 'Agent Shroud Bot Credentials',
      '--fields', 'label=app password',
      '--reveal', '--session', session],
      { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
    smtpPass = get.stdout.trim().replace(/\s+/g, '');  // strip spaces (Google shows app passwords with spaces)
    if (!smtpPass) {
      console.error('FAILED: Gmail credential retrieval —', get.stderr.trim());
      process.exit(1);
    }
    smtpUser    = 'agentshroud.ai@gmail.com';
    fromAddress = '"Isaiah Jefferson | AgentShroud" <agentshroud.ai@gmail.com>';
    smtpConfig  = { host: 'smtp.gmail.com', port: 465, secure: true, auth: { user: smtpUser, pass: smtpPass } };
  } else {
    // Retrieve iCloud app-specific password (item 25ghxryyvup5wpufgfldgc2vjm)
    const get = spawnSync('op', ['item', 'get', '25ghxryyvup5wpufgfldgc2vjm',
      '--vault', 'Agent Shroud Bot Credentials',
      '--fields', 'label=agentshroud app-specific password',
      '--reveal', '--session', session],
      { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
    smtpPass = get.stdout.trim();
    if (!smtpPass) {
      console.error('FAILED: iCloud credential retrieval —', get.stderr.trim());
      process.exit(1);
    }
    smtpUser    = 'agentshroud.ai@icloud.com';
    fromAddress = '"Isaiah Jefferson | AgentShroud" <agentshroud.ai@icloud.com>';
    smtpConfig  = { host: 'smtp.mail.me.com', port: 587, secure: false, requireTLS: true, auth: { user: smtpUser, pass: smtpPass } };
  }

  const transporter = nodemailer.createTransport(smtpConfig);

  let subject, body, to, cc;

  if (preview) {
    const manifestPath = path.join(__dirname, 'campaign-manifest.json');
    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
    const entry = manifest.find(e => e.to && e.to.includes('@'));
    if (!entry) { console.error('FAILED: no direct-email entry found in manifest'); process.exit(1); }
    to      = 'idallasj@gmail.com';
    cc      = 'isaiah_jefferson@mac.com';
    subject = `[PREVIEW → ${entry.to}] ${entry.subject}`;
    body    = stripMarkdown(entry.body);
    console.log(`Sending preview of: ${entry.folder} (would go to ${entry.to})`);
  } else {
    to      = 'idallasj@gmail.com';
    cc      = 'isaiah_jefferson@mac.com';
    subject = '[TEST] AgentShroud Outreach Campaign — Ready to Send';
    body    = [
      'Hi Isaiah,',
      '',
      'This confirms the AgentShroud podcast outreach campaign is loaded and ready.',
      '',
      `  Campaign: 44 podcasts — 24 direct email, 20 contact form`,
      `  From: ${smtpUser}`,
      '  Cc: idallasj@gmail.com, isaiah_jefferson@mac.com',
      '',
      'Reply "GO" to the bot on Telegram to launch the full campaign.',
      '',
      '— AgentShroud Bot'
    ].join('\n');
  }

  const attachmentPath = path.join(__dirname, 'AgentShroud-Competitive-Intelligence-Report-2026-03-22.pdf');
  const attachments = fs.existsSync(attachmentPath)
    ? [{ filename: 'AgentShroud-Competitive-Intelligence-Report-2026-03-22.pdf', path: attachmentPath }]
    : [];

  try {
    const info = await transporter.sendMail({ from: fromAddress, to, cc, subject, text: body, attachments });
    console.log('OK: sent — ' + info.messageId + (attachments.length ? ' [+attachment]' : ''));
  } catch (e) {
    console.error('FAILED: SMTP —', e.message);
    process.exit(1);
  }
}

main();
