# Daily Operations Runbook — SecureClaw

> Last updated: 2026-02-18

## Morning Checklist (5 minutes)

### 1. Service Health
```bash
# Check all containers are running
docker compose ps

# Expected: all services "Up", healthy
# If any are restarting, check logs immediately
```

### 2. Tailscale Connectivity
```bash
./scripts/tailscale-check.sh
```

### 3. Audit Ledger Review
```bash
# Review last 24 hours of security events
tail -100 data/audit_ledger.jsonl | python3 -c "
import json, sys
for line in sys.stdin:
    e = json.loads(line)
    ts = e.get('timestamp','')[:19]
    print(f\"{ts} | {e.get('event_type','?'):20s} | {e.get('outcome','?')}\")
"
```

**Look for:**
- Failed authentication attempts (>3 is suspicious)
- PII sanitization events (verify they're being caught)
- Kill switch activations (should be rare)
- Unusual patterns in timing or frequency

### 4. Log Review
```bash
# Check for errors in gateway
docker logs --since 24h secureclaw-gateway 2>&1 | grep -i error

# Check for warnings
docker logs --since 24h secureclaw-gateway 2>&1 | grep -i warning
```

### 5. Resource Usage
```bash
# Container resource consumption
docker stats --no-stream

# Disk usage
df -h /
du -sh data/
```

---

## Weekly Checklist (15 minutes)

### 1. Dependency Updates
```bash
# Check for known vulnerabilities
~/miniforge3/envs/oneclaw/bin/pip audit

# Check for outdated packages
~/miniforge3/envs/oneclaw/bin/pip list --outdated
```

### 2. Backup Verification
```bash
# Verify latest backup exists and is recent
ls -la backups/

# Test restore procedure (to temp location)
# See backup-restore.md
```

### 3. Tailscale ACL Review
```bash
# Verify only expected devices are connected
tailscale status
```

### 4. Test Suite
```bash
~/miniforge3/envs/oneclaw/bin/python -m pytest gateway/tests/ -v
# All tests should pass. Failures indicate drift.
```

---

## Monthly Checklist (30 minutes)

1. **Secret rotation review** — Are any secrets >90 days old?
2. **Access review** — Is `ALLOWED_USERS` still correct?
3. **Audit ledger archival** — Archive old entries, verify integrity
4. **Security documentation review** — Are runbooks still accurate?
5. **Incident review** — Were there incidents? Are action items done?
6. **Dependency major version review** — Any major upgrades needed?

---

## Dashboard Monitoring

Access the dashboard at `https://<tailscale-hostname>/dashboard` or `http://localhost:8050`.

Key metrics to check:
- Request volume (unusual spikes?)
- Error rate (should be <1%)
- Sanitization events (PII being caught)
- Approval queue (any stuck requests?)
