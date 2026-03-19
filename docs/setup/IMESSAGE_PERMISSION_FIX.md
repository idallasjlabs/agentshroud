# iMessage Permission Fix - Step by Step

## The Error We're Getting

```
Not authorized to send Apple events to Messages. (-1743)
```

## How to Fix (5 Minutes)

### Step 1: Switch to agentshroud-bot User

**On Marvin:**

**Option A - Fast User Switching:**
1. Click your user name in the menu bar (top right)
2. Select **agentshroud-bot** from the list
3. Enter password if prompted

**Option B - Via Terminal:**
```bash
su - agentshroud-bot
```

### Step 2: Grant Automation Permission

Once logged in as `agentshroud-bot`:

1. **Open System Settings** (System Preferences on older macOS)

2. **Navigate to:**
   - **Privacy & Security** → **Automation**

   OR on older macOS:
   - **Security & Privacy** → **Privacy** tab → **Automation**

3. **Find one of these in the list:**
   - `Terminal`
   - `sshd-keygen-wrapper`
   - `bash`
   - `zsh`

4. **Enable the checkbox** next to **Messages** or **Messages.app**

5. If you don't see any of these apps, you may need to:
   - Open Terminal as agentshroud-bot user
   - Run: `imsg send --to "+13015188813" --text "test"`
   - macOS will prompt you to grant permission

### Step 3: Test It

**As agentshroud-bot user, in Terminal:**

```bash
imsg send --to "+13015188813" --text "Test from agentshroud-bot"
```

**Expected result:** Message sends successfully (no error)

If you get an error, check:
- Messages.app is signed in (should be with agentshroud.ai@gmail.com)
- You're really logged in as agentshroud-bot user (run `whoami`)

### Step 4: Verify from Docker

Once the manual test works, verify the container can send:

```bash
docker exec agentshroud-bot sh -c '/home/node/.openclaw/scripts/imsg-ssh send --to "+13015188813" --text "Test from container"'
```

**Expected result:** Message sends successfully

## If It Still Doesn't Work

1. **Check Messages.app is signed in:**
   - Switch to agentshroud-bot user
   - Open Messages.app
   - Verify it's signed in with an Apple ID
   - Should be `agentshroud.ai@gmail.com`

2. **Try running imsg while Messages.app is open**
   - The first run might trigger the permission prompt

3. **Check Full Disk Access:**
   - System Settings → Privacy & Security → Full Disk Access
   - Add Terminal if not already there

## Current Status

Run this to check if it's working:

```bash
docker exec agentshroud-bot sh -c '/home/node/.openclaw/scripts/imsg-ssh send --to "+13015188813" --text "AgentShroud iMessage test $(date)"'
```

If no error = **IT WORKS!** ✅
