# 1Password Vault Sharing Instructions

**Date**: 2026-02-16
**Status**: ✅ Bot signin working | ⚠️ Vault not shared yet

---

## Current Situation

The bot's 1Password account (agentshroud.ai@gmail.com) is now working! The signin is successful and the bot can access its own "Private" vault.

However, the "AgentShroud Bot Credentials" vault is **not visible** to the bot yet. This means the vault sharing step hasn't been completed.

### What the bot can currently see:

```
Available vaults: Private

Items in Private vault:
- 1Password Account (The Jeffersons)
- AgentShroud Bot
```

### What the bot needs to see:

```
Available vaults: Private, AgentShroud Bot Credentials

Items in AgentShroud Bot Credentials vault:
- Gmail - agentshroud.ai (with username, password, TOTP)
- [Any other credentials you want the bot to access]
```

---

## How to Share the Vault

You need to share the "AgentShroud Bot Credentials" vault from **your main 1Password account** to the bot's account.

### Option 1: Share Existing Vault

If you already created "AgentShroud Bot Credentials" vault in your main account:

1. **Sign in to your main 1Password account** at https://my.1password.com
   - Use your personal email (not agentshroud.ai@gmail.com)

2. **Go to the vault**:
   - Click "Vaults" in the sidebar
   - Find "AgentShroud Bot Credentials"

3. **Share the vault**:
   - Click the vault settings (gear icon)
   - Click "Manage Access" or "Share Vault"
   - Add: `agentshroud.ai@gmail.com` (the bot's account)
   - Grant: **Read-only** access (bot doesn't need to edit)

4. **Confirm sharing**:
   - The bot will receive an invitation
   - Since the bot account is controlled by you, you can accept it

### Option 2: Create and Share New Vault

If you haven't created the vault yet:

1. **Sign in to your main 1Password account** at https://my.1password.com

2. **Create the vault**:
   - Click "Vaults" → "Create Vault"
   - Name: `AgentShroud Bot Credentials`
   - Description: `Credentials for OpenClaw bot to access via CLI`

3. **Add credentials**:
   - Click "New Item" in the vault
   - Add Gmail credentials:
     - Title: `Gmail - agentshroud.ai`
     - Username: `agentshroud.ai@gmail.com`
     - Password: [Your Gmail app password]
     - TOTP: [Your 2FA secret if needed]

4. **Share the vault** (see Option 1, step 3 above)

### Option 3: Use the Bot's Private Vault

Alternative approach - just add credentials to the bot's existing "Private" vault:

1. **Sign in as the bot** at https://my.1password.com
   - Email: `agentshroud.ai@gmail.com`
   - Master Password: [the one you created]
   - Secret Key: `A3-5Q7Q4G-9P59AL-CK3QN-83KVZ-VC8GL-BPV8H`

2. **Add credentials to Private vault**:
   - Click "New Item"
   - Add Gmail credentials:
     - Title: `Gmail - agentshroud.ai`
     - Username: `agentshroud.ai@gmail.com`
     - Password: [Your Gmail app password]
     - TOTP: [Your 2FA secret if needed]

3. **No sharing needed** - the bot already has access to its own Private vault

---

## Testing After Sharing

Once you've shared the vault (or added credentials to Private vault):

```bash
# Restart the container to see the new startup messages
docker compose -f docker/docker-compose.yml restart openclaw

# Wait a moment, then check the startup logs
docker logs openclaw-bot 2>&1 | grep -E "\[startup\]|1Password"
```

You should now see:
```
[startup] Signing in to 1Password as agentshroud.ai@gmail.com...
[startup] ✓ Signed in to 1Password successfully
[startup] ✓ 1Password vault access confirmed
[startup] Available vaults: Private, AgentShroud Bot Credentials
```

### Verify vault access:

```bash
# List all vaults
docker exec openclaw-bot op vault list

# Should show both Private and AgentShroud Bot Credentials

# List items in the shared vault
docker exec openclaw-bot op item list --vault "AgentShroud Bot Credentials"

# Get Gmail password
docker exec openclaw-bot op item get "Gmail - agentshroud.ai" \
  --vault "AgentShroud Bot Credentials" \
  --fields label=password
```

**OR** if using the bot's Private vault:

```bash
# List items in Private vault
docker exec openclaw-bot op item list --vault "Private"

# Get Gmail password
docker exec openclaw-bot op item get "Gmail - agentshroud.ai" \
  --vault "Private" \
  --fields label=password
```

---

## Recommended Approach

I recommend **Option 3** (use the bot's Private vault) because:

✅ No sharing needed - the bot owns the vault
✅ Simpler setup - just add items to the bot's existing vault
✅ Better security - credentials stay in one account
✅ Easier to manage - all bot credentials in one place

Then update commands to reference `--vault "Private"` instead of `--vault "AgentShroud Bot Credentials"`.

---

## What Happens After This Works

Once the bot can access credentials from 1Password:

1. **Secure credential sharing via Telegram**:
   ```
   You: "Bot, get my Gmail password and configure email"
   Bot: [Reads from 1Password, configures, never displays password]
   ```

2. **No more plain text passwords in chat**:
   - All sensitive credentials stored in 1Password
   - Bot retrieves them automatically
   - Audit trail in gateway ledger

3. **Easy credential rotation**:
   - Update password in 1Password
   - Bot gets new password automatically
   - No need to update Docker secrets

---

## Current Files Status

| File | Status |
|------|--------|
| `docker/secrets/1password_bot_email.txt` | ✅ Configured |
| `docker/secrets/1password_bot_master_password.txt` | ✅ Configured |
| `docker/secrets/1password_bot_secret_key.txt` | ✅ Configured |
| `docker/scripts/start-openclaw.sh` | ✅ Updated (better signin handling) |
| Bot's 1Password account | ✅ Created and working |
| Bot's "Private" vault | ✅ Exists and accessible |
| "AgentShroud Bot Credentials" vault | ⚠️ Not shared yet (OR doesn't exist) |
| Gmail credentials in 1Password | ⚠️ Needs to be added |

---

## Next Steps

1. **You**: Choose an approach (Option 1, 2, or 3)
2. **You**: Add Gmail credentials to 1Password
3. **You**: Share vault (if using Option 1 or 2)
4. **Me**: Restart container and verify access
5. **Me**: Test retrieving Gmail password
6. **Me**: Configure Gmail for the bot

---

**Need help?** Let me know which option you prefer and I can guide you through it!
