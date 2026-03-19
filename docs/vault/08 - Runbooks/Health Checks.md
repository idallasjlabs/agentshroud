---
title: Health Checks
type: runbook
tags: [health, monitoring, runbook]
related: [Quick Reference, Security Modules/health_report.py, Runbooks/Crash Recovery]
status: documented
---

# Health Checks

## Gateway Health Endpoints

### Basic Status (No Auth)

```bash
curl -s http://localhost:8080/status | jq .
```

**Healthy response:**
```json
{
  "status": "healthy",
  "version": "0.9.x",
  "uptime": 3600
}
```

**Unhealthy response:**
```json
{
  "status": "starting"
}
```

---

### Full Health Report (Auth Required)

```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)

curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/health | jq .
```

**Expected response:**
```json
{
  "status": "healthy",
  "components": {
    "pii_sanitizer": {"status": "ok", "engine": "presidio"},
    "prompt_guard": {"status": "ok"},
    "egress_filter": {"status": "ok", "domains_loaded": 10},
    "ledger": {"status": "ok", "entries": 42, "db_path": "/app/data/ledger.db"},
    "approval_queue": {"status": "ok", "pending": 0},
    "mcp_proxy": {"status": "ok", "servers": 1}
  }
}
```

---

## Container Health Check

Docker runs the built-in health check automatically. Check status:

```bash
# Status summary
docker compose -f docker/docker-compose.yml ps

# Detailed health info for gateway
docker inspect agentshroud-gateway | jq '.[0].State.Health'

# Expected output:
{
  "Status": "healthy",
  "FailingStreak": 0,
  "Log": [
    {"ExitCode": 0, "Output": ""}
  ]
}
```

---

## Security Health Report

Get the full security health report from `health_report.py`:

```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)

curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/health/report | jq .
```

This includes:
- Security module status
- Recent security events
- Kill switch state
- Falco/Wazuh connectivity (if configured)
- ClamAV definition freshness
- Trivy scan results

---

## Approval Queue Health

```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)

curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/admin/approvals | jq '{pending: .pending, total: .total}'
```

---

## Ledger Health

```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)

# Recent entries
curl -s -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8080/ledger?limit=10" | jq .total

# Should be incrementing with each forwarded request
```

---

## Bot Health Check

```bash
# Direct health check (from host)
curl -s http://localhost:18790/api/health | jq .

# From inside gateway network (service-to-service)
docker exec agentshroud-gateway curl -s http://agentshroud:18789/api/health | jq .
```

---

## Monitoring Script

Create a simple monitoring loop:

```bash
#!/bin/bash
# monitoring.sh — Run every 5 minutes via cron
TOKEN=$(cat /path/to/docker/secrets/gateway_password.txt)

GATEWAY_STATUS=$(curl -sf --max-time 5 http://localhost:8080/status | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','unknown'))" 2>/dev/null || echo "unreachable")
BOT_STATUS=$(curl -sf --max-time 5 http://localhost:18790/api/health 2>/dev/null && echo "healthy" || echo "unreachable")

if [ "$GATEWAY_STATUS" != "healthy" ] || [ "$BOT_STATUS" = "unreachable" ]; then
    echo "[$(date)] ALERT: Gateway=$GATEWAY_STATUS Bot=$BOT_STATUS"
    # Add alerting here (email, Slack, etc.)
fi
```

---

## Health Check Intervals (Docker)

| Container | Interval | Timeout | Retries | Start Period |
|-----------|---------|---------|---------|-------------|
| gateway | 30s | 10s | 3 | 10s |
| bot | 30s | 10s | 3 | 60s |

---

## Related Notes

- [[Security Modules/health_report.py|health_report.py]] — Full health report implementation
- [[Quick Reference]] — Health check quick commands
- [[Runbooks/Crash Recovery]] — When health checks fail
- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Full diagnostic matrix
