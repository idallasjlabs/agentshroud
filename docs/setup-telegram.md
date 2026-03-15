# Telegram Channel Setup

## Prerequisites

- Docker stack running: `docker compose -f docker/docker-compose.yml up -d`
- A Telegram account

---

## Step 1: Create a Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot`
3. Follow prompts: choose a display name and a username (must end in `bot`)
4. BotFather returns a **bot token** — format: `1234567890:ABCdef...`

---

## Step 2: Write the Token to Secrets

```bash
echo 'YOUR_BOT_TOKEN_HERE' > docker/secrets/telegram_bot_token_production.txt
```

---

## Step 3: Find Your Telegram User ID

Send any message to **@userinfobot** on Telegram. It replies with your numeric user ID (e.g., `8096968754`).

---

## Step 4: Configure Environment

In `docker/docker-compose.yml`, gateway service environment:

```yaml
- AGENTSHROUD_OWNER_USER_ID=YOUR_NUMERIC_USER_ID
```

---

## Step 5: Configure agentshroud.yaml

```yaml
channels:
  telegram:
    enabled: true
```

---

## Step 6: Rebuild and Start

```bash
docker compose -f docker/docker-compose.yml build --no-cache
docker compose -f docker/docker-compose.yml up -d
```

---

## Step 7: Verify

```bash
# Confirm long-polling is active (gateway fetching updates from Telegram)
docker logs agentshroud-gateway 2>&1 | grep getUpdates | tail -3

# Confirm startup notification was sent
docker logs agentshroud-bot 2>&1 | grep "startup notification"
```

Send a message to your bot in Telegram. You should get a response.

---

## Collaborators

To grant collaborator access to another Telegram user:

```bash
# In docker/docker-compose.yml gateway environment:
- AGENTSHROUD_COLLABORATOR_USER_IDS=111111111,222222222
```

Or send `/approve <user_id>` to the bot from your owner account at runtime.

---

## Troubleshooting

| Symptom | Check |
|---------|-------|
| No response to messages | `docker logs agentshroud-gateway \| grep "getUpdates"` — should show 200 |
| Startup notification not received | Verify `telegram_bot_token_production.txt` has no trailing newline issues |
| 401 Unauthorized in logs | Token is wrong or revoked — regenerate via BotFather (`/revoke`) |
| Messages blocked | Gateway RBAC — check your user ID matches `AGENTSHROUD_OWNER_USER_ID` |
