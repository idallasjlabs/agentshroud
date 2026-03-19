---
type: runbook
created: 2026-03-03
tags: [shutdown, recovery, operations]
related: [Startup Sequence, Runbooks/Crash Recovery, Runbooks/Kill Switch Procedure]
---

# Shutdown & Recovery

## Graceful Shutdown

### Normal Stop

```bash
# Graceful shutdown (15s stop_grace_period per container)
docker compose -f docker/docker-compose.yml down

# Stop without removing volumes (preferred for restart)
docker compose -f docker/docker-compose.yml stop

# Stop single container
docker compose -f docker/docker-compose.yml stop agentshroud-gateway
docker compose -f docker/docker-compose.yml stop agentshroud-bot
```

### Shutdown Sequence

```
1. Docker sends SIGTERM to each container
2. Bot container (start-agentshroud.sh) trap fires:
   - Sends Telegram notification: "🔴 AgentShroud shutting down"
   - Forwards SIGTERM to openclaw process
3. OpenClaw completes in-flight requests (15s grace period)
4. Gateway container receives SIGTERM:
   - FastAPI lifespan cleanup runs
   - DataLedger flushes pending writes
   - Open SQLite connections closed
5. After 15s grace_period: Docker sends SIGKILL if still running
6. Volumes persist (gateway-data, agentshroud-config, agentshroud-workspace)
```

---

## Kill Switch (Emergency Stop)

The kill switch performs an **immediate halt** without waiting for in-flight requests.

```bash
# Option 1: Script
./docker/scripts/killswitch.sh

# Option 2: REST API
curl -X POST \
  -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8080/admin/kill-switch \
  -d '{"action": "shutdown"}'

# Option 3: Dashboard
# Navigate to http://localhost:18790 → Kill Switch

# Option 4: Raw Docker
docker compose -f docker/docker-compose.yml kill
```

**Kill switch actions (set in `agentshroud.yaml`):**

| Action | Effect |
|--------|--------|
| `freeze` | Pause all agent actions; containers stay running |
| `shutdown` | Stop all containers immediately |
| `disconnect` | Drop all network connections; processes continue |

---

## Crash Recovery

### Detecting a Crash

```bash
# Check container state
docker compose -f docker/docker-compose.yml ps

# View exit code
docker inspect agentshroud-gateway --format='{{.State.ExitCode}}'
docker inspect agentshroud-bot --format='{{.State.ExitCode}}'

# View crash logs (last 200 lines)
docker logs --tail=200 agentshroud-gateway
docker logs --tail=200 agentshroud-bot
```

**Exit codes:**
| Code | Meaning |
|------|---------|
| 0 | Clean exit |
| 1 | Python/Node exception |
| 137 | SIGKILL (OOM or force kill) |
| 139 | Segfault |
| 143 | SIGTERM |

### Auto-Restart

Both containers have `restart: unless-stopped`. Docker automatically restarts them unless they were manually stopped. Check if auto-restart is working:

```bash
docker events --filter container=agentshroud-gateway --filter event=restart
```

### Manual Recovery

```bash
# 1. Check what failed
docker logs --tail=100 agentshroud-gateway 2>&1 | grep -i "error\|exception\|critical"

# 2. If config issue: fix agentshroud.yaml, then restart
docker compose -f docker/docker-compose.yml restart agentshroud-gateway

# 3. If dependency issue (spaCy model corrupt): rebuild image
docker compose -f docker/docker-compose.yml build agentshroud-gateway
docker compose -f docker/docker-compose.yml up -d agentshroud-gateway

# 4. Full restart with fresh containers (preserves volumes)
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up -d

# 5. Nuclear option: destroy and recreate everything
# WARNING: Destroys gateway-data (audit ledger), agentshroud-config
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
```

### OOM Recovery

If the gateway container is killed by OOM (exit code 137):

```bash
# 1. Check current memory usage
docker stats agentshroud-gateway --no-stream

# 2. Increase memory limit in docker-compose.yml
# mem_limit: 2560m  (increase from 1280m)

# 3. Check for memory leaks in logs
docker logs agentshroud-gateway 2>&1 | grep -i "memory\|oom\|killed"

# 4. Consider enabling swap (memswap_limit)
```

---

## Data Integrity After Crash

### Ledger Database

The SQLite ledger (`gateway-data:/app/data/ledger.db`) uses WAL mode and is crash-safe. After a crash:

```bash
# Verify ledger integrity
docker compose -f docker/docker-compose.yml run --rm agentshroud-gateway \
  python3 -c "
import sqlite3
conn = sqlite3.connect('/app/data/ledger.db')
result = conn.execute('PRAGMA integrity_check').fetchone()
print('Integrity:', result)
"
```

### Approval Queue

The approval queue is **in-memory** with persistence via `approval_queue/store.py`. Pending approvals survive restarts if the store was flushed. Check the store after restart:

```bash
curl -H "Authorization: Bearer $GATEWAY_AUTH_TOKEN" \
  http://localhost:8080/admin/approvals | jq '.pending | length'
```

---

## State After Recovery

After recovery, verify:

1. Gateway is healthy: `curl -s http://localhost:8080/health | jq .status`
2. Bot is connected: check `docker logs agentshroud-bot | tail -20`
3. Telegram notification received: `🛡️ AgentShroud online`
4. Ledger has integrity: `PRAGMA integrity_check` returns "ok"
5. Dashboard accessible: `http://localhost:18790`

---

## Related Notes

- [[Startup Sequence]] — Full boot sequence
- [[Runbooks/Restart Procedure]] — Normal restart steps
- [[Runbooks/Crash Recovery]] — Crash recovery runbook
- [[Runbooks/Kill Switch Procedure]] — Emergency shutdown
- [[Errors & Troubleshooting/Container Errors]] — Container-level errors
