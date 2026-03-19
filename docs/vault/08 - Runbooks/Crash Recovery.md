---
title: Crash Recovery
type: runbook
tags: [recovery, crash, runbook, operations]
related: [Shutdown & Recovery, Runbooks/Restart Procedure, Errors & Troubleshooting/Container Errors]
status: documented
---

# Crash Recovery

## Immediate Assessment

```bash
# 1. Check current state
docker compose -f docker/docker-compose.yml ps

# 2. Check exit codes
docker inspect agentshroud-gateway --format='Exit: {{.State.ExitCode}} Status: {{.State.Status}}'
docker inspect agentshroud-bot --format='Exit: {{.State.ExitCode}} Status: {{.State.Status}}'

# 3. Capture crash logs
docker logs --tail=200 agentshroud-gateway 2>&1 | tee /tmp/gateway-crash.log
docker logs --tail=200 agentshroud-bot 2>&1 | tee /tmp/bot-crash.log
```

---

## Auto-Restart

Both containers have `restart: unless-stopped`. Docker will automatically restart them within ~5 seconds. Check if auto-restart is working:

```bash
docker events --filter container=agentshroud-gateway --since=10m | grep restart
```

If containers are restarting successfully on their own, skip to **Post-Recovery Verification**.

---

## Crash Diagnosis

### Python Exception (Exit Code 1)

```bash
# Find the exception
grep -E "Exception|Error|Traceback" /tmp/gateway-crash.log | head -30

# Common exceptions and fixes:
# ValueError: config validation → fix agentshroud.yaml
# ImportError: module not found → rebuild image
# OSError: file/permission → check volume mounts
```

### OOM Kill (Exit Code 137)

```bash
# Check if OOM killer triggered
dmesg | grep "oom_kill"

# Fix: increase mem_limit in docker-compose.yml
# Gateway: 1280m → 2560m
# Bot: 4g → 6g (if available)
```

### Segfault (Exit Code 139)

```bash
# Usually Node.js memory corruption
# Fix: restart bot container
docker compose -f docker/docker-compose.yml restart agentshroud-bot

# If recurring: reduce concurrent operations or update Node.js image
```

---

## Recovery Procedures

### Option 1: Simple Restart (most common fix)

```bash
docker compose -f docker/docker-compose.yml restart
```

### Option 2: Full Stop and Start

```bash
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up -d
```

### Option 3: Rebuild and Restart

Use when image is corrupt or dependencies need updating:

```bash
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml build --no-cache
docker compose -f docker/docker-compose.yml up -d
```

### Option 4: Volume-Safe Reset

Resets containers but preserves all data volumes:

```bash
# Remove containers only (volumes preserved)
docker compose -f docker/docker-compose.yml down --remove-orphans

# Start fresh
docker compose -f docker/docker-compose.yml up -d
```

### Option 5: Nuclear Reset (DATA LOSS WARNING)

Only use if all other options fail and you accept data loss:

```bash
# WARNING: Destroys audit ledger, bot config, memories
docker compose -f docker/docker-compose.yml down -v

# Re-setup (follow First Time Setup runbook)
docker compose -f docker/docker-compose.yml up -d
```

---

## Data Recovery

### Ledger Database

The SQLite ledger uses WAL mode and is crash-safe:

```bash
# Verify integrity after crash
docker run --rm \
  -v agentshroud_gateway-data:/data \
  python:3.13-slim \
  python3 -c "
import sqlite3
conn = sqlite3.connect('/data/ledger.db')
result = conn.execute('PRAGMA integrity_check').fetchone()
print('Integrity:', result[0])
conn.execute('PRAGMA wal_checkpoint(FULL)')
print('WAL checkpoint complete')
"
```

### Pending Approvals

Approval queue state in memory is lost on crash. The persistence store (`approval_queue/store.py`) may recover some items. Check after restart:

```bash
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/admin/approvals | jq '{total: .total, pending: .pending}'
```

---

## Post-Recovery Verification

```bash
# 1. Both containers healthy
docker compose -f docker/docker-compose.yml ps

# 2. Gateway API responding
curl -s http://localhost:8080/status | jq .status

# 3. Authenticated endpoint
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/health | jq .

# 4. Check ledger integrity
# (use command from Data Recovery section above)

# 5. Telegram notification
# Should receive "🛡️ AgentShroud online" when bot is healthy
```

---

## Recurring Crashes

If the same container crashes repeatedly:

1. Check resource usage: `docker stats agentshroud-gateway`
2. Check for zombie processes: `docker exec agentshroud-gateway ps aux`
3. Look for memory leaks in logs
4. Consider scheduling regular restarts (cron):
   ```bash
   # Weekly restart to clear memory accumulation
   0 4 * * 0 cd /path/to/agentshroud && docker compose restart
   ```

---

## Related Notes

- [[Shutdown & Recovery]] — Normal shutdown procedures
- [[Runbooks/Restart Procedure]] — Standard restart steps
- [[Errors & Troubleshooting/Container Errors]] — Container error reference
- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Symptom → fix matrix
