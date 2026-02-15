# OpenClaw Management Scripts

Useful scripts for managing your OpenClaw + SecureClaw deployment.

## Quick Reference

| Script | Purpose |
|--------|---------|
| `check-status.sh` | View status of all services, channels, and models |
| `set-model.sh` | Change the default AI model |
| `logs.sh` | View container logs |
| `restart.sh` | Restart services |
| `telegram.sh` | Manage Telegram bot configuration |
| `devices.sh` | Manage trusted devices (browser pairing) |
| `openclaw-entrypoint.sh` | Internal: Loads API keys from secrets |

---

## check-status.sh

View the status of all services, Telegram channel, model configuration, and gateway health.

```bash
./docker/scripts/check-status.sh
```

**Output**:
- Container status (healthy/unhealthy)
- Telegram channel status
- Active AI model
- Configured providers (OpenAI, Anthropic)
- Gateway health check
- Control UI URL

---

## set-model.sh

Change the default AI model used by OpenClaw.

```bash
# View available models
./docker/scripts/set-model.sh

# Set to Claude Opus 4.6
./docker/scripts/set-model.sh anthropic/claude-opus-4-6

# Set to Claude Sonnet 4.5
./docker/scripts/set-model.sh anthropic/claude-sonnet-4-5

# Set to GPT-4o
./docker/scripts/set-model.sh openai/gpt-4o
```

---

## logs.sh

View container logs for debugging.

```bash
# View all logs (last 50 lines)
./docker/scripts/logs.sh

# View OpenClaw logs only
./docker/scripts/logs.sh openclaw

# View Gateway logs only
./docker/scripts/logs.sh gateway

# View last 100 lines
./docker/scripts/logs.sh all 100
```

**Shortcuts**:
- `openclaw` or `oc` → OpenClaw logs
- `gateway` or `gw` → Gateway logs
- `all` → Both (default)

---

## restart.sh

Restart services when configuration changes or troubleshooting.

```bash
# Restart all services
./docker/scripts/restart.sh

# Restart OpenClaw only
./docker/scripts/restart.sh openclaw

# Restart Gateway only
./docker/scripts/restart.sh gateway

# Rebuild everything (when Dockerfile changes)
./docker/scripts/restart.sh rebuild
```

**When to use**:
- After updating API keys
- After changing bot configuration
- When containers are unhealthy
- After modifying docker-compose.yml

---

## telegram.sh

Manage Telegram bot configuration.

```bash
# Check Telegram channel status
./docker/scripts/telegram.sh status

# Add Telegram bot (get token from @BotFather)
./docker/scripts/telegram.sh add 1234567890:ABCdef...

# Remove Telegram channel
./docker/scripts/telegram.sh remove

# Approve pending pairing (after adding channel)
./docker/scripts/telegram.sh approve telegram:123456
```

**Workflow**:
1. Get bot token from @BotFather on Telegram
2. Add channel: `./telegram.sh add <TOKEN>`
3. Check pairings: `./telegram.sh status`
4. Approve pairing: `./telegram.sh approve <PAIRING_ID>`

---

## Common Tasks

### Initial Setup

```bash
# 1. Check everything is working
./docker/scripts/check-status.sh

# 2. Set your preferred AI model
./docker/scripts/set-model.sh anthropic/claude-opus-4-6

# 3. Check Telegram bot status
./docker/scripts/telegram.sh status
```

### Debugging Issues

```bash
# View recent logs
./docker/scripts/logs.sh all 100

# Check service health
./docker/scripts/check-status.sh

# Restart if needed
./docker/scripts/restart.sh
```

### Changing AI Model

```bash
# Switch to Claude
./docker/scripts/set-model.sh anthropic/claude-opus-4-6

# Switch to GPT-4o
./docker/scripts/set-model.sh openai/gpt-4o

# Verify change
./docker/scripts/check-status.sh
```

### Updating Telegram Bot Token

```bash
# Remove old channel
./docker/scripts/telegram.sh remove

# Add new token
./docker/scripts/telegram.sh add NEW_TOKEN_HERE

# Approve pairing
./docker/scripts/telegram.sh status
./docker/scripts/telegram.sh approve PAIRING_ID
```

---

## Direct Docker Commands

If you prefer using docker compose commands directly:

### Container Management

```bash
# Start services
docker compose -f docker/docker-compose.yml up -d

# Stop services
docker compose -f docker/docker-compose.yml down

# Restart specific service
docker compose -f docker/docker-compose.yml restart openclaw

# View status
docker compose -f docker/docker-compose.yml ps

# View logs
docker logs openclaw-bot --tail 50
docker logs secureclaw-gateway --tail 50
```

### OpenClaw CLI

```bash
# Run OpenClaw commands
docker compose -f docker/docker-compose.yml exec openclaw openclaw <command>

# Examples:
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list
docker compose -f docker/docker-compose.yml exec openclaw openclaw models status
docker compose -f docker/docker-compose.yml exec openclaw openclaw pairing list
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list
```

### API Keys

```bash
# Check API keys are mounted
docker compose -f docker/docker-compose.yml exec openclaw bash -c '
echo "OpenAI: $(cat $OPENAI_API_KEY_FILE | head -c 25)..."
echo "Anthropic: $(cat $ANTHROPIC_API_KEY_FILE | head -c 25)..."
'

# Test model with environment variables
docker compose -f docker/docker-compose.yml exec openclaw bash -c '
export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
openclaw models status
'
```

---

## Troubleshooting

### "Missing auth" for API providers

The scripts automatically export the API keys from secret files. If you see "Missing auth":

1. Check secrets exist:
```bash
ls -la docker/secrets/*.txt
```

2. Verify secrets are mounted:
```bash
docker compose -f docker/docker-compose.yml exec openclaw ls -la /run/secrets/
```

3. Restart stack to remount secrets:
```bash
./docker/scripts/restart.sh rebuild
```

### Telegram bot not responding

```bash
# Check channel status
./docker/scripts/telegram.sh status

# Check logs for errors
./docker/scripts/logs.sh openclaw 100

# Verify model is set and authenticated
./docker/scripts/check-status.sh
```

### Container unhealthy

```bash
# Check logs
./docker/scripts/logs.sh

# Restart services
./docker/scripts/restart.sh

# If persists, rebuild
./docker/scripts/restart.sh rebuild
```

---

## File Locations

- **Scripts**: `/Users/ijefferson.admin/Development/oneclaw/docker/scripts/`
- **API Keys**: `/Users/ijefferson.admin/Development/oneclaw/docker/secrets/`
- **Docker Compose**: `/Users/ijefferson.admin/Development/oneclaw/docker/docker-compose.yml`
- **OpenClaw Config**: Docker volume `openclaw-config` (inside container: `~/.openclaw/`)
- **Gateway Data**: Docker volume `gateway-data`

---

## Security Notes

- Scripts automatically load API keys from secure Docker secrets
- Never commit secret files to git
- All services bound to localhost only (127.0.0.1)
- Containers run with security hardening (no-new-privileges, cap_drop ALL)

---

**Last Updated**: 2026-02-15
**System**: OpenClaw 2026.2.14 + SecureClaw Gateway 0.2.0

---

## devices.sh

Manage trusted devices for Control UI access.

```bash
# View all devices (pending and paired)
./docker/scripts/devices.sh list

# Approve a pending device
./docker/scripts/devices.sh approve REQUEST_ID

# Approve all pending devices (use with caution)
./docker/scripts/devices.sh approve-all

# Remove a paired device
./docker/scripts/devices.sh remove DEVICE_ID
```

**When to use**:
- New browser shows "pairing required"
- Need to remove old/unused devices
- Audit which devices have access

**Workflow**:
1. Browser shows "pairing required" error
2. Run `./devices.sh list` to see pending requests
3. Copy the Request ID
4. Run `./devices.sh approve REQUEST_ID`
5. Refresh browser - now connected!

See `DEVICE_PAIRING.md` for complete documentation.

