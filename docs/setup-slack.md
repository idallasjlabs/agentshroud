# Slack Channel Setup

## Architecture

Slack uses **Socket Mode** — the gateway opens an outbound WebSocket to Slack.
No inbound port is exposed. No internet exposure required.

```
[Slack] ←WSS→ [Gateway Socket Mode client] → [Bridge] → [Bot getUpdates poll]
                                                             ↓
[Slack] ←chat.postMessage← [Gateway Telegram proxy] ←sendMessage← [Bot]
```

Messages from Slack appear to the bot as standard Telegram updates.
Bot replies are intercepted by the gateway and routed to Slack via `chat.postMessage`.

---

## Step 1: Create a Slack App

1. Go to **https://api.slack.com/apps** → **Create New App** → **From scratch**
2. Name it (e.g., `AgentShroudBot`), select your workspace

---

## Step 2: Enable Socket Mode

**Settings → Socket Mode** → **Enable Socket Mode: On**

Generate an **App-Level Token**:
- Token name: `agentshroud-socket`
- Scope: `connections:write`
- Click **Generate** → copy the `xapp-` token

```bash
echo 'xapp-YOUR-TOKEN-HERE' > docker/secrets/slack_app_token.txt
```

---

## Step 3: Add Bot Token Scopes

**Features → OAuth & Permissions → Bot Token Scopes** — add:

| Scope | Purpose |
|-------|---------|
| `chat:write` | Send messages |
| `channels:history` | Read channel messages |
| `groups:history` | Read private channel messages |
| `im:history` | Read DMs |
| `im:read` | List DM channels |
| `im:write` | Open DM channels |
| `reactions:write` | Add emoji reactions |

---

## Step 4: Enable Event Subscriptions

**Features → Event Subscriptions** → **Enable Events: On**

Under **Subscribe to bot events**, add:
- `message.channels`
- `message.groups`
- `message.im`

Click **Save Changes**.

---

## Step 5: Enable App Home Messages Tab

**Features → App Home** → **Show Tabs**:
- **Messages Tab**: On
- ☑ **Allow users to send Slash commands and messages from the messages tab**

---

## Step 6: Install the App

**Settings → OAuth & Permissions** → **Install to Workspace** → **Allow**

Copy the **Bot User OAuth Token** (`xoxb-...`):

```bash
echo 'xoxb-YOUR-BOT-TOKEN-HERE' > docker/secrets/slack_bot_token.txt
```

Copy the **Signing Secret** from **Basic Information → App Credentials**:

```bash
echo 'YOUR-32-CHAR-SIGNING-SECRET' > docker/secrets/slack_signing_secret.txt
```

---

## Step 7: Find Your Slack User ID

In Slack: click your profile photo → **View full profile** → three-dot menu (⋯) → **Copy member ID**
Format: `U0XXXXXXXXX`

---

## Step 8: Configure Environment

In `docker/docker-compose.yml`, gateway service environment:

```yaml
- AGENTSHROUD_SLACK_OWNER_USER_ID=U0XXXXXXXXX
```

In `agentshroud.yaml`:

```yaml
channels:
  slack:
    enabled: true
    channel_id: "C0XXXXXXXXX"   # optional: channel for startup/shutdown notifications
```

---

## Step 9: Rebuild and Start

```bash
docker compose -f docker/docker-compose.yml build --no-cache
docker compose -f docker/docker-compose.yml up -d
```

---

## Step 10: Verify

```bash
# Confirm Socket Mode connected
docker logs agentshroud-gateway 2>&1 | grep -i "slack"
# Expected: "Slack Socket Mode: connected (1 active connection(s))"
```

Open Slack → **Apps → AgentShroudBot** (left sidebar) → send `hello`

You should receive a reply in-thread.

---

## Sending Messages to the Bot

The correct interface is **Apps → AgentShroudBot** in the Slack sidebar.
This is the App Home Messages Tab — the standard interface for messaging a Slack app.

If AgentShroudBot disappears from the sidebar:
1. Click **+** next to **Apps** in the left sidebar
2. Search `AgentShroudBot` → click to open

---

## Collaborators

To grant collaborator access to a Slack user, add their Slack user ID to the gateway env:

```yaml
- AGENTSHROUD_COLLABORATOR_USER_IDS=U0XXXXXXXXX,U0YYYYYYYYY
```

Slack user IDs and Telegram user IDs can coexist in the same comma-separated list —
Slack IDs are alphanumeric (`U0ABC...`) and Telegram IDs are numeric, so there is no collision.

Runtime approval also works: send `approve U0XXXXXXXXX` to the bot from your owner account.

---

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Socket Mode not connecting | Verify `slack_app_token.txt` contains `xapp-` token with `connections:write` scope |
| Events not arriving | Check Event Subscriptions are saved and app is reinstalled after scope changes |
| Bot treats owner as stranger | Verify `AGENTSHROUD_SLACK_OWNER_USER_ID` is set in **gateway** service (not bot service) |
| Bot replies not appearing in Slack | Verify `slack_bot_token.txt` has valid `xoxb-` token |
| App missing from sidebar | Click `+` next to Apps → search AgentShroudBot |
| "access request queued" response | Your Slack user ID doesn't match `AGENTSHROUD_SLACK_OWNER_USER_ID` |
