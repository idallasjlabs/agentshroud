# Quick Reference Card

**Bot**: @agentshroud.ai_bot | **User**: @agentshroud.ai | **UI**: http://localhost:18790

---

## Most Common Commands

```bash
# Check everything is working
./docker/scripts/check-status.sh

# View logs
./docker/scripts/logs.sh

# Restart services
./docker/scripts/restart.sh

# Change AI model to Claude
./docker/scripts/set-model.sh anthropic/claude-opus-4-6

# Check Telegram status
./docker/scripts/telegram.sh status
```

---

## Container Management

```bash
# Start
docker compose -f docker/docker-compose.yml up -d

# Stop
docker compose -f docker/docker-compose.yml down

# Restart
docker compose -f docker/docker-compose.yml restart

# Status
docker compose -f docker/docker-compose.yml ps

# Logs
docker logs openclaw-bot --tail 50
docker logs agentshroud-gateway --tail 50
```

---

## AI Models

```bash
# Claude Opus 4.6 (best quality)
./docker/scripts/set-model.sh anthropic/claude-opus-4-6

# Claude Sonnet 4.5 (balanced)
./docker/scripts/set-model.sh anthropic/claude-sonnet-4-5

# GPT-4o (fast)
./docker/scripts/set-model.sh openai/gpt-4o
```

---

## Telegram Bot

```bash
# Status
./docker/scripts/telegram.sh status

# Add bot
./docker/scripts/telegram.sh add BOT_TOKEN

# Approve pairing
./docker/scripts/telegram.sh approve PAIRING_ID
```

---

## Troubleshooting

```bash
# Full health check
./docker/scripts/check-status.sh

# Recent logs (100 lines)
./docker/scripts/logs.sh all 100

# Restart everything
./docker/scripts/restart.sh

# Rebuild from scratch
./docker/scripts/restart.sh rebuild
```

---

## API Keys

```bash
# View keys (first 25 chars)
docker compose -f docker/docker-compose.yml exec openclaw bash -c '
echo "OpenAI: $(cat $OPENAI_API_KEY_FILE | head -c 25)..."
echo "Anthropic: $(cat $ANTHROPIC_API_KEY_FILE | head -c 25)..."
'

# Edit keys
nano docker/secrets/openai_api_key.txt
nano docker/secrets/anthropic_oauth_token.txt

# After editing, restart
./docker/scripts/restart.sh rebuild
```

---

## Access Points

- **Control UI**: http://localhost:18790
- **Gateway**: http://localhost:8080
- **Password**: `b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05`

---

## Files

- **Scripts**: `docker/scripts/`
- **API Keys**: `docker/secrets/`
- **Docker Compose**: `docker/docker-compose.yml`
- **Documentation**: `SETUP_API_KEYS.md`, `SETUP_SUMMARY.md`

---

**Test**: Message @agentshroud.ai_bot on Telegram!
