# Telegram Bot Setup for OpenClaw

**Goal**: Control your OpenClaw bot (therealidallasj) via Telegram on Mac, iPhone, iPad, and Apple Watch.

---

## Step 1: Create a Telegram Bot

1. **Open Telegram** on any device (Mac, iPhone, iPad)
2. **Search for @BotFather** (the official Telegram bot creator)
3. **Start a chat** with BotFather and send: `/newbot`
4. **Choose a name** for your bot (e.g., "therealidallasj")
5. **Choose a username** (must end in 'bot', e.g., "therealidallasj_bot")
6. **Copy the API token** BotFather gives you (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

---

## Step 2: Configure OpenClaw to Use Telegram

Add the Telegram channel to OpenClaw:

```bash
# From your Mac terminal
cd /Users/ijefferson.admin/Development/oneclaw

# Add Telegram channel
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels add \
  --channel telegram \
  --token "YOUR_TELEGRAM_BOT_TOKEN"

# Verify it was added
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list
```

Replace `YOUR_TELEGRAM_BOT_TOKEN` with the token from BotFather.

---

## Step 3: Start Chatting

1. **Find your bot** in Telegram (search for the username you created)
2. **Start a conversation** by sending `/start`
3. **Send messages** to control your bot:
   - "What's on my calendar today?"
   - "Draft an email to..."
   - "Check my GitHub notifications"
   - Any task you'd normally ask your assistant

---

## Multi-Device Access

Telegram syncs across all your devices automatically. Once you set up the bot:

- **Mac**: Use Telegram Desktop or web.telegram.org
- **iPhone**: Use Telegram app from App Store
- **iPad**: Use Telegram app from App Store
- **Apple Watch**: Use Telegram app (if installed on iPhone, it shows notifications)

All conversations sync in real-time across all devices.

---

## Security Considerations

### How Messages Flow

```
You (Telegram on any device)
    ↓
Telegram Bot API (Telegram's servers)
    ↓
OpenClaw Container (polls Telegram API)
    ↓
AgentShroud Gateway (optional - if you enable it)
    ↓
OpenAI/Anthropic APIs (for LLM processing)
```

### Important Notes

1. **Telegram API Keys**: The bot token gives OpenClaw access to read/send messages through your bot. Keep it secret.

2. **Message Privacy**: Messages travel through Telegram's servers, then to your OpenClaw container. Telegram can technically read messages (they're not end-to-end encrypted for bots).

3. **Bot Identity**: The bot runs as "therealidallasj@gmail.com" with its own accounts (NOT your personal accounts).

4. **Data Storage**: All conversations are stored in the `openclaw-config` Docker volume.

5. **Gateway Integration** (optional): You can route Telegram messages through AgentShroud Gateway for additional PII sanitization and audit logging:
   - Edit `gateway/ingest_api/channels.py` to add Telegram webhook handler
   - Configure Telegram to send messages to Gateway first (port 8080)
   - Gateway sanitizes and forwards to OpenClaw

---

## Optional: Restrict Bot Access

By default, anyone who finds your bot can message it. To restrict access:

```bash
# Configure allowed Telegram user IDs
docker compose -f docker/docker-compose.yml exec openclaw openclaw config set \
  --key "channels.telegram.allowedUsers" \
  --value "[123456789, 987654321]"  # Your Telegram user IDs
```

To find your Telegram user ID:
1. Message your bot
2. Check OpenClaw logs: `docker logs openclaw-bot | grep "Telegram user"`
3. Or use @userinfobot in Telegram

---

## Troubleshooting

### Bot doesn't respond

```bash
# Check OpenClaw logs
docker logs openclaw-bot -f

# Verify channel is configured
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list

# Test API connectivity
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels test telegram
```

### Messages delayed

Telegram bots use **polling** by default (OpenClaw checks Telegram every few seconds). This is normal and conserves resources.

For instant delivery, you can configure **webhooks** (requires publicly accessible URL or Tailscale).

### Cannot find bot

- Make sure the username ends in "bot"
- Username must be unique across all of Telegram
- Try searching with @username format

---

## Advanced: Telegram Commands

You can configure custom Telegram commands for quick actions:

```bash
# In BotFather, send /setcommands
# Then paste:
start - Initialize the bot
help - Show available commands
status - Check bot status
calendar - Show today's calendar
email - Draft an email
github - Check GitHub notifications
cancel - Cancel current operation
```

---

## Next Steps

1. ✅ Create Telegram bot with @BotFather
2. ✅ Add bot token to OpenClaw
3. ✅ Test by sending a message
4. ⬜ Configure allowed users (optional)
5. ⬜ Set up custom commands (optional)
6. ⬜ Enable Gateway routing for PII sanitization (optional)

---

**Questions?** Check OpenClaw docs: https://docs.openclaw.ai/channels/telegram
