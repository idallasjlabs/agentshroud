# OpenClaw Workspace Usage Guide

**Date**: 2026-02-16
**Decision**: Using Docker volume (Option 1) for workspace

---

## What is the Workspace?

The workspace is where you and the bot share files:
- **You** put files here for the bot to read/process
- **Bot** creates files here (reports, screenshots, scripts)
- **Location**: Docker volume `openclaw-workspace` mounted at `/home/node/openclaw/workspace/`

---

## Quick Reference

### Using the Helper Script

```bash
# List files in workspace
./docker/scripts/workspace.sh ls

# Copy file TO workspace
./docker/scripts/workspace.sh cp-to ~/Documents/report.pdf

# Copy file FROM workspace
./docker/scripts/workspace.sh cp-from report.pdf ~/Downloads/

# View file contents
./docker/scripts/workspace.sh cat notes.txt

# Create directory
./docker/scripts/workspace.sh mkdir screenshots

# Delete file (with confirmation)
./docker/scripts/workspace.sh rm old-file.txt

# Open shell in workspace
./docker/scripts/workspace.sh shell

# Show directory tree
./docker/scripts/workspace.sh tree
```

---

## Common Workflows

### Workflow 1: Give Bot a File to Process

**Scenario**: You have a CSV file on your Mac, want bot to analyze it

```bash
# 1. Copy file to workspace
./docker/scripts/workspace.sh cp-to ~/Documents/sales-data.csv

# 2. Tell bot via Telegram
"Please analyze the file sales-data.csv in workspace and create a summary report"

# 3. Bot processes and creates workspace/sales-summary.md

# 4. Copy report back to Mac
./docker/scripts/workspace.sh cp-from sales-summary.md ~/Documents/
```

---

### Workflow 2: Bot Creates Files for You

**Scenario**: Ask bot to generate a report

```bash
# 1. Tell bot via Telegram
"Create a weekly status report in workspace/reports/week-7.md"

# 2. Bot creates the file

# 3. Check what was created
./docker/scripts/workspace.sh ls reports/

# 4. View the file
./docker/scripts/workspace.sh cat reports/week-7.md

# 5. Copy to Mac if needed
./docker/scripts/workspace.sh cp-from reports/week-7.md ~/Documents/
```

---

### Workflow 3: Bot Takes Screenshots

**Scenario**: Bot uses SecureBrowser to capture screenshots

```bash
# 1. Tell bot via Telegram
"Please take a screenshot of anthropic.com homepage and save to workspace"

# 2. Bot uses SecureBrowser skill, saves to workspace/screenshots/

# 3. List screenshots
./docker/scripts/workspace.sh ls screenshots/

# 4. Copy screenshot to Mac
./docker/scripts/workspace.sh cp-from screenshots/anthropic-homepage.png ~/Desktop/
```

---

### Workflow 4: Bulk File Operations

**Scenario**: Share multiple files with bot

```bash
# 1. Create workspace directory for project
./docker/scripts/workspace.sh mkdir project-x

# 2. Copy multiple files
./docker/scripts/workspace.sh cp-to ~/Documents/file1.txt project-x/
./docker/scripts/workspace.sh cp-to ~/Documents/file2.csv project-x/
./docker/scripts/workspace.sh cp-to ~/Documents/file3.pdf project-x/

# 3. Verify
./docker/scripts/workspace.sh ls project-x/

# 4. Tell bot
"Please process all files in workspace/project-x/ and create a summary"
```

---

### Workflow 5: Interactive Editing

**Scenario**: Work directly in workspace via shell

```bash
# 1. Open shell in workspace
./docker/scripts/workspace.sh shell

# Now you're inside the container in /home/node/openclaw/workspace/

# 2. Create files, edit, etc.
echo "Notes from meeting" > meeting-notes.txt
mkdir -p reports/2026-02/
ls -la

# 3. Exit when done
exit

# 4. Files persist in Docker volume
./docker/scripts/workspace.sh ls
```

---

## Advanced: Direct Docker Commands

If you prefer using docker directly:

```bash
# List workspace
docker exec openclaw-bot ls -la /home/node/openclaw/workspace/

# Copy TO workspace
docker cp ~/Documents/file.txt openclaw-bot:/home/node/openclaw/workspace/

# Copy FROM workspace
docker cp openclaw-bot:/home/node/openclaw/workspace/file.txt ~/Downloads/

# View file
docker exec openclaw-bot cat /home/node/openclaw/workspace/notes.txt

# Delete file
docker exec openclaw-bot rm /home/node/openclaw/workspace/old-file.txt

# Shell access
docker exec -it openclaw-bot bash
cd /home/node/openclaw/workspace
ls
```

---

## Workspace Organization Tips

### Recommended Structure

```
workspace/
├── inbox/           # Files you put here for bot to process
├── output/          # Bot's generated files
│   ├── reports/
│   ├── screenshots/
│   └── scripts/
├── projects/        # Organized by project
│   ├── project-a/
│   └── project-b/
└── archive/         # Completed work
```

### Create Structure

```bash
./docker/scripts/workspace.sh mkdir inbox
./docker/scripts/workspace.sh mkdir output/reports
./docker/scripts/workspace.sh mkdir output/screenshots
./docker/scripts/workspace.sh mkdir output/scripts
./docker/scripts/workspace.sh mkdir projects
./docker/scripts/workspace.sh mkdir archive
```

---

## File Permissions

**Inside container**:
- User: `node` (UID 1000, GID 1000)
- All files created by bot are owned by UID 1000

**On Mac**:
- When you copy files in, they're accessible by the container
- When you copy files out, they're owned by your Mac user

**No permission issues** because Docker handles the mapping.

---

## Workspace Size

**Current limit**: Docker volume has no hard limit (uses available disk)

**To check size**:
```bash
docker exec openclaw-bot du -sh /home/node/openclaw/workspace/
```

**To check available space**:
```bash
docker exec openclaw-bot df -h /home/node/openclaw/workspace/
```

---

## Backup and Restore

### Backup Workspace

```bash
# Create backup archive
docker run --rm \
  --volumes-from openclaw-bot \
  -v $(pwd):/backup \
  debian:bookworm-slim \
  tar czf /backup/workspace-backup-$(date +%Y%m%d).tar.gz \
  -C /home/node/openclaw workspace

# Creates: workspace-backup-20260216.tar.gz
```

### Restore Workspace

```bash
# Restore from backup
docker run --rm \
  --volumes-from openclaw-bot \
  -v $(pwd):/backup \
  debian:bookworm-slim \
  tar xzf /backup/workspace-backup-20260216.tar.gz \
  -C /home/node/openclaw
```

---

## Troubleshooting

### Problem: "Container not running"

```bash
# Check container status
docker ps -a | grep openclaw-bot

# Start container
docker-compose -f docker/docker-compose.yml up -d

# Wait for healthy
docker-compose -f docker/docker-compose.yml ps
```

### Problem: "File not found"

```bash
# List workspace to verify path
./docker/scripts/workspace.sh ls

# Check file exists in subdirectory
./docker/scripts/workspace.sh ls reports/
```

### Problem: "Permission denied"

```bash
# This shouldn't happen with Docker volumes, but if it does:

# Check file ownership
docker exec openclaw-bot ls -la /home/node/openclaw/workspace/file.txt

# Fix ownership (if needed)
docker exec openclaw-bot chown node:node /home/node/openclaw/workspace/file.txt
```

---

## Integration with Bot

### Via Telegram

```
"Read the file data.csv from workspace"
"Create a report in workspace/reports/summary.md"
"Save this screenshot to workspace/screenshots/"
"List all files in workspace"
"Delete old files from workspace/archive/"
```

### Via Skills

Skills can access workspace at `/home/node/openclaw/workspace/`:

```javascript
// In a skill script
const fs = require('fs');
const workspacePath = '/home/node/openclaw/workspace';

// Read file user provided
const data = fs.readFileSync(`${workspacePath}/input.csv`, 'utf8');

// Process data
const result = processData(data);

// Write output
fs.writeFileSync(`${workspacePath}/output/result.json`, JSON.stringify(result));
```

---

## Why Docker Volume vs Bind Mount?

**Docker Volume (Our Choice)**:
- ✅ Better performance on Mac (no filesystem translation)
- ✅ Managed by Docker (automatic cleanup, snapshots)
- ✅ No permission mapping issues
- ✅ Portable between systems
- ✅ More secure (not tied to host filesystem)

**Bind Mount (Alternative)**:
- ✅ Directly visible in Finder
- ❌ Slower on Mac (filesystem translation overhead)
- ❌ Permission issues (UID mapping)
- ❌ Security: bot could read your entire mounted directory

**We chose Docker volume for security, performance, and simplicity.**

---

## Summary

**What you need to know**:

1. **Workspace is for file sharing** between you and bot
2. **Use the helper script** for easy file operations
3. **Files persist** across container restarts
4. **Bot can read/write** workspace freely
5. **You can backup** the entire workspace easily

**Common commands**:
```bash
./docker/scripts/workspace.sh ls          # List files
./docker/scripts/workspace.sh cp-to FILE  # Copy to workspace
./docker/scripts/workspace.sh cp-from FILE # Copy from workspace
./docker/scripts/workspace.sh shell       # Interactive access
```

**That's it!** The helper script makes working with Docker volumes as easy as a regular folder.
