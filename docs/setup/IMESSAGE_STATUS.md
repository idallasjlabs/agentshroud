# iMessage Integration Status

## Current State: Partially Working

iMessage channel is **configured** but **cannot send messages** due to macOS permissions.

## The Error

```
Error: Not authorized to send Apple events to Messages. (-1743)
```

## What This Means

The OpenClaw container is trying to use AppleScript to send iMessages through Messages.app on the host Mac, but macOS is blocking it because:

1. The `agentshroud-bot` user doesn't have "Automation" permission for Messages.app
2. The container process (running as `node` user) doesn't have the required permissions

## Current Configuration

From OpenClaw config:
```json
{
  "enabled": true,
  "cliPath": "/home/node/.openclaw/scripts/imsg-ssh",
  "dbPath": "/Users/agentshroud-bot/Library/Messages/chat.db",
  "remoteHost": "agentshroud-bot@host.docker.internal",
  "dmPolicy": "pairing",
  "allowFrom": ["+13015188813", "8096968754", "8506022825", "8545356403", "8279589982"]
}
```

## Solutions

### Option 1: Grant Permissions (NOT RECOMMENDED - Won't Work from Container)

Even if we grant permissions, the container running as `node` user cannot access macOS permissions for a different user (`agentshroud-bot`).

### Option 2: Use BlueBubbles (RECOMMENDED ✅)

BlueBubbles runs as a native macOS application under the `agentshroud-bot` user and has proper permissions.

**Prerequisites:**
1. Sign into Messages.app with `agentshroud.ai@gmail.com` as the `agentshroud-bot` macOS user
2. Install BlueBubbles Server on the Mac
3. Complete Firebase setup
4. Grant BlueBubbles the required macOS permissions (Automation, Full Disk Access, Accessibility)
5. Get the BlueBubbles server URL and API password

**Then I can:**
1. Add BlueBubbles channel to OpenClaw
2. Test message sending/receiving
3. Disable the broken SSH-based iMessage integration

## Next Steps

**User Action Required:**
1. Fast User Switch to `agentshroud-bot` user on Marvin
2. Complete BlueBubbles setup (see TELEGRAM_GMAIL_SETUP.md for similar process)
3. Provide BlueBubbles server URL and API password

**After User Setup:**
I will configure OpenClaw to use BlueBubbles and verify end-to-end functionality.

## Current Status Summary

| Feature | Status | Notes |
|---------|--------|-------|
| iMessage via SSH | ❌ Broken | Permission errors, not fixable from container |
| iMessage via BlueBubbles | 🔄 Ready to Configure | Waiting for user to complete macOS setup |
| Message Receiving | ✅ Working | Can read Messages database via SSH |
| Message Sending | ❌ Broken | Requires BlueBubbles |
