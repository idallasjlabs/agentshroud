---
title: Health Checks
type: process
tags: [#type/process, #status/active]
related: ["[[Restart Procedure]]", "[[Troubleshooting Matrix]]", "[[agentshroud-gateway]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# Health Checks

## Quick Stack Status

```bash
# All containers — status + health
docker compose -f docker/docker-compose.yml ps

# Watch continuously (every 2s)
watch -n 2 docker ps
```

## Gateway Health

```bash
# HTTP health endpoint
curl http://localhost:8080/status
# Expected: {"status": "ok", "version": "...", "uptime": ..., ...}

# Internal check (same as Docker healthcheck)
docker exec agentshroud-gateway \
  python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()" \
  && echo "PASS"

# Gateway log tail
docker logs agentshroud-gateway --tail 30

# Startup confirmation
docker logs agentshroud-gateway | grep "Gateway ready"
```

## Bot Health

```bash
# HTTP health (port 18790 = host-side mapping of 18789)
curl -sf http://localhost:18790/ && echo "Bot OK"

# Bot log tail
docker logs agentshroud-bot --tail 30
```

## Telegram Connectivity

```bash
# Long-poll should show 200 responses
docker logs agentshroud-gateway | grep getUpdates | tail -5
# Expected pattern: getUpdates 200 OK

# Messages flowing outbound
docker logs agentshroud-bot | grep "sendMessage ok" | tail -5
```

## Security Module Health

```bash
# Check all module init succeeded
docker logs agentshroud-gateway | grep -E "✓|✗" | head -30
# ✓ = initialized successfully
# ✗ = failed (non-fatal if P3 module)

# Audit chain heartbeat (every 60s)
docker logs agentshroud-gateway | grep AuditChain | tail -5
# Expected: "AuditChain heartbeat: Chain valid"

# Alert log (security events)
docker exec agentshroud-gateway \
  cat /tmp/security/alerts/alerts.jsonl 2>/dev/null | tail -5
```

## Database Health

```bash
# Audit DB (quick check)
docker exec agentshroud-gateway \
  python3 -c "
import sqlite3
conn = sqlite3.connect('/app/data/audit.db')
count = conn.execute('SELECT count(*) FROM audit_entries').fetchone()[0]
print(f'Audit entries: {count}')
conn.close()
" 2>/dev/null || echo "Audit DB not accessible"

# Pending approvals
docker exec agentshroud-gateway \
  python3 -c "
import sqlite3
conn = sqlite3.connect('/app/data/agentshroud_approvals.db')
count = conn.execute(\"SELECT count(*) FROM approvals WHERE status='pending'\").fetchone()[0]
print(f'Pending approvals: {count}')
conn.close()
" 2>/dev/null || echo "Approval DB not accessible"
```

## Resource Usage

```bash
# Live CPU/memory stats
docker stats agentshroud-gateway agentshroud-bot --no-stream

# Disk usage (volumes)
docker system df -v 2>/dev/null | grep agentshroud
```

## Full System Health Summary Script

```bash
#!/bin/bash
echo "=== AgentShroud Health Check ==="
echo ""
echo "--- Container Status ---"
docker compose -f docker/docker-compose.yml ps

echo ""
echo "--- Gateway API ---"
curl -s http://localhost:8080/status | python3 -m json.tool 2>/dev/null || echo "Gateway API: UNREACHABLE"

echo ""
echo "--- Telegram Long-Poll ---"
docker logs agentshroud-gateway 2>/dev/null | grep getUpdates | tail -3

echo ""
echo "--- Security Module Init ---"
docker logs agentshroud-gateway 2>/dev/null | grep -E "✓|✗" | tail -20

echo ""
echo "--- Recent Errors ---"
docker logs agentshroud-gateway 2>/dev/null | grep -E "ERROR|CRITICAL" | tail -10
```
