# iMessage Integration Fix - Using imsg + imessage-exporter

## Current Setup (CORRECT)

✅ **Tools Installed:**
- `imsg` - Installed at `/opt/homebrew/bin/imsg`
- `imessage-exporter` - Installed at `/opt/homebrew/bin/imessage-exporter`

✅ **OpenClaw Configuration:**
```json
{
  "enabled": true,
  "cliPath": "/home/node/.openclaw/scripts/imsg-ssh",
  "dbPath": "/Users/agentshroud-bot/Library/Messages/chat.db",
  "remoteHost": "agentshroud-bot@host.docker.internal"
}
```

✅ **SSH Connection:**
Container → Host SSH works correctly

## The Problem

**Error:**
```
Error: Not authorized to send Apple events to Messages. (-1743)
```

**Root Cause:**
`imsg` uses AppleScript to send messages through Messages.app, but the `agentshroud-bot` macOS user doesn't have Automation permissions.

## The Fix

### Option 1: Grant Automation Permission (REQUIRED)

On Marvin:

1. **Switch to agentshroud-bot user:**
   ```bash
   # Fast User Switch in menu bar
   # OR via command line:
   su - agentshroud-bot
   ```

2. **Open System Settings:**
   - Go to **Privacy & Security** → **Automation**

3. **Grant Terminal/SSH Automation Permission:**
   - Find `Terminal` or `sshd-keygen-wrapper` in the list
   - Enable permission to control **Messages**

4. **Test it:**
   ```bash
   # As agentshroud-bot user:
   imsg send "+13015188813" "Test message from agentshroud-bot"
   ```

If that works, OpenClaw will be able to send messages.

### Option 2: Check if Messages.app is Signed In

Verify Messages.app is signed in as `agentshroud-bot` user:

1. Switch to `agentshroud-bot` user
2. Open Messages.app
3. Check if signed into iMessage with the correct Apple ID
4. If not, sign in with `agentshroud.ai@gmail.com`

## Verification

After granting permissions, test from the container:

```bash
docker exec agentshroud-bot sh -c '/home/node/.openclaw/scripts/imsg-ssh send "+13015188813" "Test from container"'
```

If that works, iMessage integration is complete.

## Status

| Component | Status |
|-----------|--------|
| imsg installed | ✅ Working |
| imessage-exporter installed | ✅ Working |
| SSH from container | ✅ Working |
| OpenClaw config | ✅ Correct |
| Automation permission | ❌ **NEEDS FIX** |
| Messages.app signed in | ⚠️ Need to verify |

## Next Steps

**USER ACTION REQUIRED:**

1. Switch to `agentshroud-bot` user on Marvin
2. Grant Automation permission (System Settings → Privacy & Security → Automation)
3. Verify Messages.app is signed in
4. Test: `imsg send "+13015188813" "test"`
5. Report back if it works

Then OpenClaw will be able to send/receive iMessages.
