# What Does OpenClaw Actually Need to Write?

**Date**: 2026-02-16
**Question**: Can a single shared folder be enough, or will it cripple functionality?

---

## TL;DR

**A single shared folder is NOT enough.** OpenClaw needs to write to several locations:

1. **`.openclaw/` directory** - Skills, memory, configuration (REQUIRED)
2. **`workspace/` directory** - Your shared folder (REQUIRED)
3. **Temporary directories** - npm cache, temp files (REQUIRED for skills)

**But you don't need the entire container writable.** We can mount specific directories and use tmpfs for the rest.

---

## What OpenClaw Writes During Normal Operation

### 1. Skills Installation (`.openclaw/skills/`)

**What happens**: When you say "install the gmail skill"

**OpenClaw writes**:
```
/home/node/.openclaw/skills/
├── gmail/
│   ├── SKILL.md           # Skill documentation
│   ├── scripts/
│   │   ├── read.js        # Email reading script
│   │   └── send.js        # Email sending script
│   └── node_modules/      # npm dependencies for the skill
│       └── imap/
│           └── ...
```

**Why it needs write access**:
- Downloads skill from ClawHub or GitHub
- Installs npm dependencies (`npm install`)
- Registers skill with OpenClaw

**Can this be in shared folder?** NO
- Skills are OpenClaw's internal configuration
- You don't edit these manually
- Skills need to persist across restarts

**Mount**: Volume at `/home/node/.openclaw/`

---

### 2. Conversation Memory (`.openclaw/MEMORY.md`)

**What happens**: After every conversation

**OpenClaw writes**:
```
/home/node/.openclaw/MEMORY.md

# Conversation History
## 2026-02-16
- User asked about Gmail integration
- Configured IMAP successfully
- Password stored in 1Password

## 2026-02-15
- Set up iCloud services
- Calendar and Contacts working
```

**Why it needs write access**:
- Maintains context across sessions
- Bot "remembers" what you discussed
- Critical for continuity

**Can this be in shared folder?** NO
- This is OpenClaw's internal state
- You want the bot to remember, not you to manage this file

**Mount**: Volume at `/home/node/.openclaw/`

---

### 3. Workspace Files (`workspace/`)

**What happens**: When bot executes tasks

**OpenClaw writes**:
```
/home/node/openclaw/workspace/
├── screenshots/           # Browser screenshots
│   └── login-page.png
├── reports/              # Generated reports
│   └── analysis.md
├── scripts/              # Scripts it created
│   └── backup.sh
└── data/                 # Data it processes
    └── contacts.csv
```

**Why it needs write access**:
- Stores task output
- Saves files you asked it to create
- Working directory for operations

**Can this be in shared folder?** YES! THIS IS YOUR SHARED FOLDER
- This is what you want to share with the bot
- Bot reads/writes files here
- You can access these files on host

**Mount**: Volume `openclaw-workspace` at `/home/node/openclaw/workspace/`

---

### 4. npm Cache (`.npm/`, `.cache/`)

**What happens**: When installing skills or packages

**OpenClaw writes**:
```
/home/node/.npm/
└── _cacache/             # npm package cache
    └── ...

/home/node/.cache/
└── ms-playwright/        # Playwright browser binaries
    └── chromium-123/
```

**Why it needs write access**:
- npm downloads packages here before installing
- Playwright stores browser binaries (500MB+)
- Speeds up subsequent installs

**Can this be in shared folder?** NO
- This is cache data, not useful to you
- Large binary files (browsers)
- Temporary, regenerated as needed

**Mount**: tmpfs (temporary filesystem in RAM)

---

### 5. Temporary Files (`/tmp/`)

**What happens**: During script execution

**OpenClaw writes**:
```
/tmp/
├── playwright-temp-12345/  # Browser temp files
├── screenshot-abc.png      # Temp screenshots before move
└── node-ipc-socket-xyz    # Inter-process communication
```

**Why it needs write access**:
- Standard Unix temporary directory
- All processes expect /tmp to be writable
- Cleaned automatically on restart

**Can this be in shared folder?** NO
- Temporary data, not persistent
- System standard location

**Mount**: tmpfs (temporary filesystem in RAM)

---

### 6. Session Configuration (`.config/`, `.local/`)

**What happens**: When apps store session data

**OpenClaw writes**:
```
/home/node/.config/
└── op/                    # 1Password session token
    └── config

/home/node/.local/
└── share/                 # Application data
    └── node/
```

**Why it needs write access**:
- 1Password session lasts for duration of container run
- Apps expect these directories to exist and be writable
- Standard XDG Base Directory locations

**Can this be in shared folder?** NO
- Session data, not persistent
- Regenerated on each signin

**Mount**: tmpfs (temporary filesystem in RAM)

---

## What Does the Bot NOT Need to Write?

### ❌ System Directories (Read-Only in Production)

```
/usr/bin/          # System binaries (node, npm, etc.)
/usr/lib/          # System libraries
/etc/              # System configuration
/bin/, /sbin/      # Core system binaries
/lib/              # Core libraries
/root/             # Root user home (bot is non-root)
/var/log/          # System logs
```

**Why they should be read-only**:
- Bot should NEVER modify system files
- Prevents privilege escalation
- Immutable infrastructure principle

---

## Current Docker Configuration

Here's what's currently mounted in your SecureClaw setup:

### ✅ Persistent Volumes (Data Survives Container Restart)

```yaml
volumes:
  # OpenClaw's brain - config, skills, memory
  - openclaw-config:/home/node/.openclaw

  # Bot's workspace - YOUR shared folder
  - openclaw-workspace:/home/node/openclaw/workspace

  # SSH keys for remote connections
  - openclaw-ssh:/home/node/.ssh

  # Playwright browsers (500MB+, persist to avoid re-download)
  - openclaw-browsers:/home/node/.cache/ms-playwright
```

### ✅ Temporary Filesystems (Cleared on Container Restart)

```yaml
tmpfs:
  # Standard temp directory
  - /tmp:noexec,nosuid,size=500m

  # Alternative temp directory
  - /var/tmp:noexec,nosuid,size=100m

  # npm package cache (speeds up skill installs)
  - /home/node/.npm:noexec,nosuid,size=200m
```

### ❌ Currently Missing (Would Break Read-Only)

```yaml
# NEEDED but not currently mounted:
tmpfs:
  - /home/node/.cache:uid=1000,gid=1000      # General app cache
  - /home/node/.local:uid=1000,gid=1000      # User-local data
  - /home/node/.config:uid=1000,gid=1000     # 1Password session, configs
```

**These are missing because we're in development mode with `read_only: false`.**
When we enable `read_only: true`, these will be required.

---

## Your Shared Folder: The Workspace

### Current Location

**Inside container**: `/home/node/openclaw/workspace/`
**Docker volume**: `openclaw-workspace`

### What You Can Do

**From your Mac**, access the workspace volume:

```bash
# List files in workspace
docker exec openclaw-bot ls -la /home/node/openclaw/workspace/

# Copy file from Mac to workspace
docker cp ~/Documents/myfile.txt openclaw-bot:/home/node/openclaw/workspace/

# Copy file from workspace to Mac
docker cp openclaw-bot:/home/node/openclaw/workspace/report.pdf ~/Downloads/

# Enter container and navigate to workspace
docker exec -it openclaw-bot bash
cd /home/node/openclaw/workspace
ls -la
```

**Via Telegram/Chat**:
```
"Create a file called notes.txt in workspace with my meeting notes"
"Read the file data.csv from workspace"
"Save this screenshot to workspace/screenshots/"
```

---

## Bind Mount vs Docker Volume

You mentioned wanting a "mounted folder" - there are two ways:

### Option 1: Docker Volume (Current Setup - Recommended)

**How it works**:
```yaml
volumes:
  - openclaw-workspace:/home/node/openclaw/workspace
```

**Pros**:
- ✅ Managed by Docker (automatic backups, snapshots)
- ✅ Better performance (especially on Mac)
- ✅ Portable between systems
- ✅ Not tied to host filesystem structure

**Cons**:
- ❌ Not directly visible in Finder
- ❌ Need `docker cp` or `docker exec` to access

**Access**:
```bash
# View workspace location
docker volume inspect openclaw-workspace

# Copy file in
docker cp myfile.txt openclaw-bot:/home/node/openclaw/workspace/

# Copy file out
docker cp openclaw-bot:/home/node/openclaw/workspace/report.pdf .
```

---

### Option 2: Bind Mount (Alternative - More Accessible)

**How it works**:
```yaml
volumes:
  - ~/OpenClaw/workspace:/home/node/openclaw/workspace
```

**Pros**:
- ✅ Directly visible in Finder
- ✅ Edit files with Mac apps (VS Code, etc.)
- ✅ No docker cp needed
- ✅ Easier file sharing

**Cons**:
- ❌ Performance hit on Mac (slower I/O)
- ❌ Permission issues (Mac UID vs container UID)
- ❌ Security: Bot can read your entire mounted directory

**To enable bind mount**:
```yaml
# docker/docker-compose.yml
volumes:
  # Replace this:
  - openclaw-workspace:/home/node/openclaw/workspace

  # With this:
  - /Users/ijefferson.admin/OpenClaw-Workspace:/home/node/openclaw/workspace
```

**Then create the folder**:
```bash
mkdir -p ~/OpenClaw-Workspace
docker-compose -f docker/docker-compose.yml restart openclaw
```

**Access**:
- Just open Finder → `~/OpenClaw-Workspace`
- Drag and drop files
- Edit directly with Mac apps

---

## Can We Use ONLY a Shared Folder?

### ❌ NO - Here's What Would Break

**If we ONLY mount workspace and nothing else**:

```yaml
volumes:
  - ~/OpenClaw-Workspace:/home/node/openclaw/workspace
  # NO other volumes
tmpfs: []
  # NO tmpfs mounts
read_only: true
  # Read-only filesystem
```

**What breaks**:

1. **Skills installation fails**
   ```
   Error: Cannot write to /home/node/.openclaw/skills/gmail
   Read-only file system
   ```

2. **Memory/context lost every restart**
   ```
   Error: Cannot write to /home/node/.openclaw/MEMORY.md
   Read-only file system
   ```

3. **npm install fails**
   ```
   Error: Cannot create /home/node/.npm/_cacache
   Read-only file system
   ```

4. **1Password signin fails**
   ```
   Error: Cannot write session to /home/node/.config/op/
   Read-only file system
   ```

5. **Temporary files fail**
   ```
   Error: Cannot create temp file in /tmp
   Read-only file system
   ```

**Result**: Bot is completely crippled, can't do anything except read files.

---

## Minimum Required Configuration

### For Read-Only to Work

```yaml
services:
  openclaw:
    read_only: true

    volumes:
      # REQUIRED: OpenClaw config, skills, memory
      - openclaw-config:/home/node/.openclaw:rw

      # REQUIRED: Your shared workspace
      - openclaw-workspace:/home/node/openclaw/workspace:rw

      # REQUIRED: SSH keys (if using SSH features)
      - openclaw-ssh:/home/node/.ssh:rw

      # OPTIONAL: Playwright browsers (or use tmpfs, but slower)
      - openclaw-browsers:/home/node/.cache/ms-playwright:rw

    tmpfs:
      # REQUIRED: Standard temp directory
      - /tmp:exec,mode=1777,size=500m

      # REQUIRED: npm package cache
      - /home/node/.npm:uid=1000,gid=1000,size=200m

      # REQUIRED: General application cache
      - /home/node/.cache:uid=1000,gid=1000,size=200m

      # REQUIRED: 1Password and app sessions
      - /home/node/.config:uid=1000,gid=1000,size=50m

      # REQUIRED: User-local application data
      - /home/node/.local:uid=1000,gid=1000,size=50m
```

**This gives you**:
- ✅ Read-only OS (bot cannot modify system files)
- ✅ Workspace for file sharing
- ✅ Skills can install
- ✅ Memory persists
- ✅ 1Password works
- ✅ All features functional

---

## Recommended Configuration for Your Use Case

Based on your requirements:

### Goals:
1. ✅ Bot cannot modify container OS
2. ✅ You can share files with bot easily
3. ✅ Multi-user secure (credentials not leaked)
4. ✅ External hosting ready

### Configuration:

```yaml
services:
  openclaw:
    # PRODUCTION: Read-only OS
    read_only: true

    volumes:
      # Bot's brain (skills, memory, config)
      - openclaw-config:/home/node/.openclaw:rw

      # YOUR SHARED FOLDER - bind mount for easy access
      - /Users/ijefferson.admin/OpenClaw-Workspace:/home/node/openclaw/workspace:rw

      # SSH keys
      - openclaw-ssh:/home/node/.ssh:rw

      # Playwright browsers (large, persist to avoid re-download)
      - openclaw-browsers:/home/node/.cache/ms-playwright:rw

    tmpfs:
      # Temp files
      - /tmp:exec,mode=1777,size=500m
      - /var/tmp:exec,mode=1777,size=100m

      # Node.js and app caches
      - /home/node/.npm:uid=1000,gid=1000,size=200m
      - /home/node/.cache:uid=1000,gid=1000,size=200m
      - /home/node/.config:uid=1000,gid=1000,size=50m
      - /home/node/.local:uid=1000,gid=1000,size=50m
```

**Benefits**:
- ✅ Workspace is a Mac folder (Finder access, drag-drop files)
- ✅ Bot cannot modify OS
- ✅ All features work
- ✅ Skills install correctly
- ✅ Memory persists
- ✅ Secure and isolated

---

## How to Access Workspace Files

### Option A: Docker Volume (Current)

```bash
# List files
docker exec openclaw-bot ls /home/node/openclaw/workspace/

# Copy TO workspace
docker cp myfile.txt openclaw-bot:/home/node/openclaw/workspace/

# Copy FROM workspace
docker cp openclaw-bot:/home/node/openclaw/workspace/report.pdf ~/Downloads/

# Shell access
docker exec -it openclaw-bot bash
cd /home/node/openclaw/workspace
```

### Option B: Bind Mount (Easier for You)

```bash
# 1. Create shared folder on Mac
mkdir -p ~/OpenClaw-Workspace

# 2. Change docker-compose.yml
# Replace:    - openclaw-workspace:/home/node/openclaw/workspace
# With:       - /Users/ijefferson.admin/OpenClaw-Workspace:/home/node/openclaw/workspace

# 3. Restart
docker-compose -f docker/docker-compose.yml restart openclaw

# 4. Use Finder
# Open ~/OpenClaw-Workspace
# Drag and drop files
# Edit with VS Code, etc.
```

---

## Summary: What the Bot Needs to Write

| Location | Type | Purpose | Size | Can Be Shared Folder? |
|----------|------|---------|------|----------------------|
| `/home/node/.openclaw/` | Volume | Skills, memory, config | 100MB | ❌ NO - Internal |
| `/home/node/openclaw/workspace/` | Volume or Bind | **YOUR files** | Variable | ✅ **YES - THIS IS IT** |
| `/home/node/.ssh/` | Volume | SSH keys | 1MB | ❌ NO - Security |
| `/home/node/.cache/ms-playwright/` | Volume | Browsers | 500MB | ❌ NO - Binaries |
| `/tmp/` | tmpfs | Temp files | 500MB | ❌ NO - System |
| `/home/node/.npm/` | tmpfs | npm cache | 200MB | ❌ NO - Cache |
| `/home/node/.cache/` | tmpfs | App cache | 200MB | ❌ NO - Cache |
| `/home/node/.config/` | tmpfs | Sessions | 50MB | ❌ NO - Temp |
| `/home/node/.local/` | tmpfs | App data | 50MB | ❌ NO - Temp |

**Total persistent storage**: ~600MB (mostly browsers)
**Total temp storage**: ~1GB (RAM)

---

## Answer to Your Question

> "I don't currently understand what the bot would need to write. We plan to have a mounted folder where I can share files that the bot can read/write, perhaps this is enough or will it cripple functionality?"

**A shared folder for workspace is essential, but NOT sufficient on its own.**

**What you NEED**:
1. ✅ **Shared workspace folder** - For files you and bot share
2. ✅ **OpenClaw config volume** - For bot's skills and memory
3. ✅ **Temporary directories (tmpfs)** - For npm, cache, sessions

**What happens with ONLY shared folder**:
- ❌ Bot cannot install skills
- ❌ Bot cannot remember conversations
- ❌ 1Password signin fails
- ❌ npm install fails
- ❌ Most functionality broken

**Recommended approach**:
- Use bind mount for workspace (easy Mac access)
- Use Docker volumes for OpenClaw internals (managed by Docker)
- Use tmpfs for temporary data (fast, secure)
- Enable read-only OS (bot cannot modify system files)

**This gives you the security AND functionality you need.**

---

Would you like me to:
1. **Show you how to set up a bind mount** for easier workspace access?
2. **Keep the current Docker volume** and use `docker cp` for file transfers?
3. **Create a helper script** to make file sharing easier?
