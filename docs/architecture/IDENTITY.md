# Identity Reference - AgentShroud System

**Last Updated**: 2026-02-15

---

## 👤 You (The Real Person)

- **Telegram**: @agentshroud.ai
- **Name**: Dallas Jefferson
- **Role**: User, owner, operator

---

## 🤖 Your AI Bot

- **Telegram Bot**: @agentshroud.ai_bot
- **Email**: agentshroud.ai@gmail.com
- **Role**: AI assistant, automated agent
- **Platform**: OpenClaw + AgentShroud

---

## 📱 How It Works

```
You (@idallasj)
    ↓
Message @idallasj_bot
    ↓
Bot processes with AI (OpenAI/Claude)
    ↓
You get intelligent response
```

---

## 🔐 Security

- **Your Telegram**: @idallasj (you control this)
- **Bot's Telegram**: @idallasj_bot (AI controls this)
- **Bot uses separate accounts** - NOT your personal accounts
- **Bot email**: agentshroud.ai@gmail.com (separate from your personal email)

---

## 💬 Communication Flow

### Via Telegram:
1. You (@agentshroud.ai) message @agentshroud.ai_bot
2. Message goes through Telegram
3. OpenClaw bot receives it
4. AI processes (via OpenAI/Anthropic API)
5. Bot responds as @agentshroud.ai_bot
6. You see response in Telegram

### Via Control UI:
- You access http://localhost:18790 on your Mac
- Direct chat with AI
- Same bot identity (@agentshroud.ai_bot)

---

## 🎯 Bot Identity Configuration

In the system:
- `OPENCLAW_BOT_NAME=agentshroud.ai_bot`
- `OPENCLAW_BOT_EMAIL=agentshroud.ai@gmail.com`
- Telegram bot username: `@agentshroud.ai_bot`

---

**Remember**:
- **@agentshroud.ai** = You (real person)
- **@agentshroud.ai_bot** = Your AI bot (automated)
