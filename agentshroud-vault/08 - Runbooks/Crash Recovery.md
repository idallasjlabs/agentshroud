---
title: Crash Recovery
type: process
tags: [#type/process, #status/critical]
related: ["[[Shutdown & Recovery]]", "[[Restart Procedure]]", "[[Gateway Startup Failure]]", "[[Error Index]]"]
status: active
last_reviewed: 2026-03-09
---

# Crash Recovery

## Determine Crash Type

```bash
# Check exit codes and status
docker compose -f docker/docker-compose.yml ps --format json | python3 -m json.tool

# Check if OOM killed
docker inspect agentshroud-gateway --format '{{.State.OOMKilled}}'
docker inspect agentshroud-bot --format '{{.State.OOMKilled}}'

# Check exit code
docker inspect agentshroud-gateway --format '{{.State.ExitCode}}'
# 0 = clean shutdown
# 1 = application error
# 137 = OOM killed (SIGKILL)
# 143 = SIGTERM (graceful stop)
```

## Clean vs Dirty Crash

| Indicator | Clean | Dirty |
|-----------|-------|-------|
| Exit code | 0 or 143 | 1, 137, or other |
| Log ends with `Shutdown complete` | Yes | No |
| SQLite WAL files present | No | Possibly |
| Audit DB integrity check passes | Yes | Verify |

## Database Integrity Check

```bash
# Start a temporary gateway container for DB inspection
docker run --rm \
  -v agentshroud_gateway-data:/app/data \
  python:3.13-slim \
  python3 -c "
import sqlite3
for db in ['/app/data/audit.db', '/app/data/ledger.db', '/app/data/agentshroud_approvals.db']:
    try:
        conn = sqlite3.connect(db)
        result = conn.execute('PRAGMA integrity_check;').fetchone()
        print(f'{db}: {result[0]}')
        conn.close()
    except Exception as e:
        print(f'{db}: ERROR - {e}')
"
```

Expected output: `ok` for each database.

## Recovery Sequence

### Step 1: Capture Logs Before Restart

```bash
docker logs agentshroud-gateway > /tmp/gateway-crash-$(date +%Y%m%d_%H%M%S).log
docker logs agentshroud-bot > /tmp/bot-crash-$(date +%Y%m%d_%H%M%S).log
```

### Step 2: Check Database Integrity

Run the integrity check above. If any database fails:

```bash
# Back up corrupted DB
docker run --rm \
  -v agentshroud_gateway-data:/app/data \
  -v /tmp:/backup \
  alpine cp /app/data/audit.db /backup/audit-$(date +%Y%m%d_%H%M%S).db.bak

# SQLite has WAL recovery built-in; just opening the DB usually recovers it
docker run --rm \
  -v agentshroud_gateway-data:/app/data \
  python:3.13-slim \
  python3 -c "import sqlite3; conn=sqlite3.connect('/app/data/audit.db'); conn.execute('PRAGMA wal_checkpoint(FULL)'); conn.close(); print('WAL checkpoint complete')"
```

### Step 3: Restart Stack

```bash
docker compose -f docker/docker-compose.yml up -d
```

### Step 4: Verify Recovery

```bash
# Gateway healthy
sleep 15
curl http://localhost:8080/status

# No lingering errors
docker logs agentshroud-gateway | grep -E "CRITICAL|ERROR" | tail -20

# Audit chain intact (logged at startup)
docker logs agentshroud-gateway | grep AuditChain

# Telegram polling resumed
docker logs agentshroud-gateway | grep getUpdates | tail -3

# Bot healthy
sleep 60
curl -sf http://localhost:18790/ && echo "Bot OK"
```

## OOM Crash Recovery

If either container was OOM killed:

```bash
# Check memory usage before restart
docker stats --no-stream agentshroud-gateway agentshroud-bot

# If OOM was bot:
# Option 1: Reduce Playwright concurrency (fewer browser instances)
# Option 2: Increase bot mem_limit in docker-compose.yml (to max 6GB)
sed -i 's/mem_limit: 4g/mem_limit: 6g/' docker/docker-compose.yml
docker compose -f docker/docker-compose.yml up -d bot
```

## Lock Files and PID Files

OpenClaw does not use PID files. The gateway does not create lock files.

If you see stale lock files in tmpfs mounts:
```bash
# tmpfs is ephemeral — clears on container restart
# No manual cleanup needed
```
