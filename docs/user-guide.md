# AgentShroud User Guide

> Last updated: 2026-02-18 | AgentShroud v0.2.0

## What is AgentShroud?

AgentShroud is a security-focused AI gateway that lets you interact with an AI assistant via Telegram while protecting your private data. It sits between you and the AI, automatically:

- **Stripping personal information** (emails, phone numbers, addresses) before it reaches the AI
- **Blocking credentials** from appearing in responses
- **Requiring approval** for sensitive operations like SSH commands
- **Logging everything** in a tamper-resistant audit trail

---

## Getting Started

### 1. Find the Bot

Open Telegram and search for your AgentShroud bot (the bot name is configured by your admin). Start a conversation with it.

### 2. Verify You're Authorized

AgentShroud only responds to authorized users. If you send a message and get no reply, your Telegram user ID hasn't been added to the allowed list. Ask your admin to add you.

### 3. Start Chatting

Just type naturally! AgentShroud forwards your messages to the AI and relays responses back. Behind the scenes, it's protecting your data.

---

## Interacting via Telegram

### Regular Messages

Just type your question or request. The bot will respond with the AI's answer.

### Commands

| Command | What It Does |
|---------|-------------|
| `/start` | Initialize the bot / show welcome message |
| `/help` | Show available commands |
| `/status` | Check system health |
| `/kill freeze` | Emergency: pause all processing |
| `/kill unfreeze` | Resume after a freeze |

### Tips

- **Be specific** — The AI works best with clear, detailed requests
- **PII protection** — The sanitizer automatically strips personal data, but avoid sending highly sensitive info when possible
- **Long responses** — The bot may split long replies into multiple messages
- **Patience** — AI responses take a few seconds; don't spam requests

---

## Understanding Approval Requests

Some operations require human approval before they execute. When this happens:

1. **You'll receive a notification** describing the requested action
2. **Review the request** — Is this what you intended?
3. **Approve or deny** using the inline buttons or reply commands
4. **The action executes** (or doesn't) based on your decision

### What Requires Approval?

- SSH commands on the server
- File system modifications
- Any action flagged as potentially dangerous

### Why Approvals Exist

This is a core safety feature. Even if the AI suggests a command, a human must confirm before it runs on real systems. This prevents accidents and limits damage from any AI mistakes.

---

## Dashboard Overview

Access the dashboard at your Tailscale URL (ask your admin for the address).

### What You'll See

- **Request Volume** — How many messages have been processed
- **Security Events** — PII detections, blocked credentials, kill switch activations
- **Audit Trail** — Searchable log of all actions
- **System Health** — Container status, uptime, resource usage

### Reading the Audit Trail

Each entry shows:
- **Timestamp** — When it happened
- **Event Type** — What kind of event (message, sanitization, approval, etc.)
- **User** — Who triggered it
- **Outcome** — What happened (allowed, denied, sanitized)

---

## SSH Access

If you need direct access to the AgentShroud server:

```bash
ssh agentshroud-bot@<your-tailscale-hostname>
```

**Requirements:**
- Tailscale installed on your device
- Your device authorized on the tailnet
- SSH key added to the server

**Important:** The `agentshroud-bot` account has limited permissions by design. It cannot run sudo or modify system files.

---

## FAQ

### Q: Can the AI see my personal information?

**A:** No. The PII sanitizer removes emails, phone numbers, addresses, and other personal data before your message reaches the AI. The AI sees redacted placeholders like `[EMAIL]` or `[PHONE]`.

### Q: What happens if I accidentally send a password?

**A:** The credential blocker detects common credential patterns and strips them. However, don't rely on this as your only defense — avoid sending passwords in chat.

### Q: Can I use the bot in group chats?

**A:** The bot is configured for private chats with authorized users. Group chat support depends on your admin's configuration.

### Q: The bot isn't responding. What do I do?

**A:** Try these steps:
1. Wait 30 seconds and try again (might be a temporary issue)
2. Send `/status` to check if the bot is alive
3. Contact your admin — the service may need a restart

### Q: What's the kill switch?

**A:** It's an emergency stop button. If something goes wrong, you (or the admin) can freeze the bot immediately. It has three levels:
- **Freeze** — Pauses processing (reversible)
- **Shutdown** — Stops all services (needs manual restart)
- **Disconnect** — Cuts all network connections (nuclear option)

### Q: How do I know my data is being protected?

**A:** Check the dashboard's security events panel. Every time the sanitizer catches PII or the credential blocker activates, it's logged. You can also ask the admin for an audit report.

### Q: Can I request the AI to do something on the server?

**A:** Yes, but it goes through the approval queue. The AI can suggest SSH commands, but a human must approve before they execute. This keeps you in control.

---

## Need Help?

- **Check bot status:** Send `/status` in Telegram
- **View dashboard:** Ask your admin for the URL
- **Contact admin:** For access issues, configuration changes, or incidents
