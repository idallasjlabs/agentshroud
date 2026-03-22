# AgentShroud Podcast Outreach — Bot Send Instructions

## Overview

You are sending a podcast outreach email campaign on behalf of Isaiah Jefferson.
- **From:** agentshroud.ai@gmail.com
- **Cc (every email):** idallasj@gmail.com, isaiah_jefferson@mac.com
- **Campaign manifest:** `/home/node/agentshroud/workspace/outreach/campaign-manifest.json`
- **Total:** 44 podcasts — 24 with direct email, 20 require contact forms (skip those)

## Step 1 — Retrieve Gmail App Password

Run the following to get the Gmail app password from 1Password:

```bash
export OP_SERVICE_ACCOUNT_TOKEN=$(cat /run/secrets/1password_service_account) && \
op item get tdx3r77qoplljrv45luh7zkngi \
  --vault 'Agent Shroud Bot Credentials' \
  --fields label=password \
  --reveal
```

Store the output as `GMAIL_APP_PASSWORD` for use in Step 3.

## Step 2 — Start with the Test Email

Before sending all 44, send the sample email to confirm delivery:
- **To:** idallasj@gmail.com
- **Subject:** [TEST] AgentShroud Outreach Campaign — Sample Email
- **Body:** Use the body from `intelligent-machines` entry in the manifest

Wait for confirmation before proceeding to Step 3.

## Step 3 — Send All Emails with Direct Addresses

Read `campaign-manifest.json`. For each entry where `to` contains `@` and `sent` is `false`:

Write and execute a Node.js script using nodemailer:

```javascript
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 465,
  secure: true,
  auth: {
    user: 'agentshroud.ai@gmail.com',
    pass: GMAIL_APP_PASSWORD  // from Step 1
  }
});

await transporter.sendMail({
  from: '"Isaiah Jefferson | AgentShroud" <agentshroud.ai@gmail.com>',
  to: entry.to,
  cc: 'idallasj@gmail.com, isaiah_jefferson@mac.com',
  subject: entry.subject,
  text: entry.body.replace(/\*\*/g, '').replace(/^---$/gm, '---'),
  html: convertMarkdownToHtml(entry.body)  // optional: plain text is fine
});
```

After each successful send:
1. Report: `Sent: [folder] → [to] ✓`
2. Mark `sent: true` in the manifest (update the JSON file)

After each failure:
1. Report: `FAILED: [folder] → [to] — [error message]`
2. Leave `sent: false`

## Step 4 — Report Contact Form Entries

After all direct emails are sent, list the 20 entries that require contact forms:

```
CONTACT FORM REQUIRED (manual submission needed):
- clockwise: relay.fm/clockwise
- grumpy-old-geeks: gog.show
- mac-geek-gab: macgeekgab.com
- mac-observer-show: macobserver.com
- mac-roundtable: macobserver.com
- maccast: maccast.com
- macvoices: macvoices.com/contact/
- query: query podcast website
- should-this-exist: shouldthisexist.com
- tech-brew-ride-home: morningbrew.com
- techpinions: techpinions.com
- the-a16z-show: a16z.com/podcasts
- the-constant-geekery: constantgeekery.buzzsprout.com
- the-dalrymple-report: thedalrymplereport.libsyn.com
- the-rebound: reboundcast.com
- the-record: therecord.media
- the-talk-show: daringfireball.net
- undone: wnyc.org
- unwanted: podcast website
- upgrade: relay.fm/upgrade
```

## Step 5 — Final Status Report

Produce a summary:
```
Campaign complete.
✓ Sent: [N] emails
✗ Failed: [N] emails (list them)
⚠ Manual (contact form): 20 entries (listed above)
```

## Important Notes

- Send one email at a time — do not batch. Wait 5 seconds between sends to avoid Gmail rate limiting.
- If the 1Password op command fails, pause and report the error — do not attempt to send without the real credential.
- Do NOT log or display the Gmail app password in output.
- The CI Report appendix in each message.md is for internal reference only. The `body` field in campaign-manifest.json already contains only the clean email body (no appendix).
- All sends route through the approval queue — expect one approval prompt per email.
