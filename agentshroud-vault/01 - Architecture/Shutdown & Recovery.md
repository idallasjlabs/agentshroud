---
title: Shutdown & Recovery
type: process
tags: [#type/process, #status/critical]
related: ["[[Crash Recovery]]", "[[Restart Procedure]]", "[[lifespan]]", "[[Startup Sequence]]"]
status: active
last_reviewed: 2026-03-09
---

# Shutdown & Recovery

## Graceful Shutdown Sequence

When `docker compose down` or `SIGTERM` is received:

1. **FastAPI lifespan exits `yield`** — shutdown block begins
2. **HTTP CONNECT proxy stopped** — `app_state.http_proxy.stop()`
3. **Approval queue closed** — `app_state.approval_queue.close()` — flushes pending items
4. **AuditStore closed** — `app_state.audit_store.close()` — flushes WAL to disk
5. **DNS Blocklist periodic updates stopped** — `app_state.dns_blocklist.stop()`
6. **Data ledger closed** — `app_state.ledger.close()`
7. **Container exits** — Docker waits up to `stop_grace_period: 15s`

> [!WARNING] If the container is killed (SIGKILL) before step 4, the SQLite WAL may not be flushed. The AuditStore will recover on next startup but may be missing the last few entries.

## Files/State to Check After Crash

| Item | Location | Check Command |
|------|----------|---------------|
| Audit DB WAL | `/app/data/audit.db-wal` | Should be absent or 0-byte after clean shutdown |
| Approval DB | `/app/data/agentshroud_approvals.db` | `docker exec agentshroud-gateway sqlite3 /app/data/agentshroud_approvals.db "PRAGMA integrity_check;"` |
| Ledger DB | `/app/data/ledger.db` | `docker exec agentshroud-gateway sqlite3 /app/data/ledger.db "PRAGMA integrity_check;"` |
| Alert log | `/tmp/security/alerts/alerts.jsonl` | Lost on restart (tmpfs) — expected |
| Memory monitor | `/app/data/memory-monitor/` | Persisted on gateway-data volume |

## Crash Recovery Procedure

See [[Crash Recovery]] for the full runbook. Summary:

```bash
# 1. Check what failed
docker logs agentshroud-gateway --tail 100
docker logs agentshroud-bot --tail 100

# 2. Check volume integrity
docker exec agentshroud-gateway \
  sqlite3 /app/data/audit.db "PRAGMA integrity_check;"

# 3. Restart
docker compose -f docker/docker-compose.yml up -d

# 4. Verify
curl http://localhost:8080/status
docker logs agentshroud-gateway | grep "Gateway ready"
```

## Data Integrity Checks Post-Recovery

```bash
# Check audit chain integrity (gateway logs this on startup)
docker logs agentshroud-gateway | grep -i "AuditChain"

# Check approval DB
docker exec agentshroud-gateway \
  sqlite3 /app/data/agentshroud_approvals.db \
  "SELECT count(*) FROM approvals WHERE status='pending';"

# Verify Telegram long-poll resumed
docker logs agentshroud-gateway | grep getUpdates | tail -5
```

## When to Rebuild vs Restart

| Scenario | Action |
|----------|--------|
| Config change in `agentshroud.yaml` | `docker compose restart gateway` |
| Secret file changed | `docker compose restart gateway` |
| Patch script changed (`patch-telegram-sdk.sh`) | Full rebuild: `docker compose build bot --no-cache && docker compose up -d bot` |
| Python dependency change (`requirements.txt`) | Full rebuild: `docker compose build gateway --no-cache && docker compose up -d gateway` |
| OpenClaw version update | Full rebuild: `docker compose build bot --no-cache && docker compose up -d bot` |
| Colima VM restart | `docker compose -f docker/docker-compose.yml up -d` (Colima restores containers) |

## Colima-Specific Recovery

If using Colima and the vmnet route is lost:

```bash
# Check if col0 route is active
colima ssh -- ip route show

# If 192.168.64.0/24 is not metric 100, re-apply route
colima ssh -- sudo ip route change 192.168.64.0/24 dev col0 metric 100

# Verify fix
colima ssh -- ping -c 2 8.8.8.8
```

The systemd service `/etc/systemd/system/colima-vmnet-route.service` inside the VM should handle this automatically. See [[Architecture Overview]] for Colima VPN networking details.
