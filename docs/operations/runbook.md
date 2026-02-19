# AgentShroud Operations Runbook

This runbook provides step-by-step procedures for operating AgentShroud in production environments.

## System Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   External      │    │   AgentShroud     │    │   OpenClaw      │
│   Clients       │───▶│   Gateway        │───▶│   Container     │
│                 │    │   (Port 8443)    │    │   (Port 8000)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   SQLite DB     │
                       │   Audit Logs    │
                       │   (/data/*)     │
                       └─────────────────┘
```

## 1. Starting and Stopping AgentShroud

### Starting the System

**Standard startup sequence:**

```bash
# 1. Navigate to AgentShroud directory
cd /path/to/agentshroud

# 2. Verify configuration files exist
ls -la config/
# Should see: agentshroud.yaml, egress-config.yml, mcp-config.yml

# 3. Check Docker secrets are available
docker secret ls
# Should include: openclaw-api-key, admin-token, ssl-cert, ssl-key

# 4. Start the stack
docker compose up -d

# 5. Verify services are running
docker compose ps
# All services should show "Up" status

# 6. Check logs for startup errors
docker compose logs -f agentshroud
```

**Alternative: Manual service start**

```bash
# Start database first
docker compose up -d db

# Wait for database readiness
docker compose exec db sqlite3 /data/agentshroud.db ".databases"

# Start AgentShroud gateway
docker compose up -d agentshroud

# Start monitoring
docker compose up -d prometheus grafana
```

### Stopping the System

**Graceful shutdown (recommended):**

```bash
# 1. Activate kill switch (optional - for maintenance)
curl -X POST https://localhost:8443/admin/kill-switch \
  -H "Authorization: Bearer $(cat /run/secrets/admin-token)" \
  -d '{"mode": "soft_kill", "reason": "maintenance"}'

# 2. Wait for active requests to complete (check dashboard)
# Monitor: https://localhost:3000/d/agentshroud

# 3. Stop services gracefully
docker compose stop

# 4. Verify all containers stopped
docker compose ps -a
```

**Emergency shutdown:**

```bash
# Immediate stop (use only in emergencies)
docker compose kill
docker compose down
```

### Restart Procedure

```bash
# Full restart
docker compose restart

# Restart specific service
docker compose restart agentshroud

# Restart with configuration reload
docker compose down
docker compose up -d
```

## 2. Health Monitoring

### System Health Checks

**Automated health endpoint:**

```bash
# Primary health check
curl -s https://localhost:8443/health | jq '.'
# Expected response:
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "components": {
    "database": "healthy",
    "openclaw": "healthy",
    "disk_space": "healthy",
    "memory_usage": "healthy"
  },
  "version": "1.0.0"
}

# Detailed health with metrics
curl -s https://localhost:8443/health/detailed | jq '.'
```

**Component-specific checks:**

```bash
# Database connectivity
docker compose exec agentshroud python -c "
import sqlite3
conn = sqlite3.connect('/data/agentshroud.db')
print(f'Tables: {conn.execute(\"SELECT name FROM sqlite_master WHERE type=\\\"table\\\"\").fetchall()}')
conn.close()
print('Database: OK')
"

# OpenClaw connectivity
curl -s http://localhost:8000/health || echo "OpenClaw unreachable"

# Disk space check
df -h /var/lib/docker/volumes/secureclaw_data/_data

# Memory usage
docker stats secureclaw_secureclaw_1 --no-stream
```

### Dashboard Access

**Grafana Dashboard:**

```bash
# Access dashboard
open https://localhost:3000

# Default credentials (change immediately):
# User: admin
# Pass: admin

# Key dashboards:
# - AgentShroud Overview: System metrics, request rates
# - Security Events: Blocked requests, violations
# - Audit Trail: Recent audit entries, trust levels
# - Performance: Response times, resource usage
```

**Prometheus Metrics:**

```bash
# Direct metrics access
curl -s http://localhost:9090/metrics | grep agentshroud

# Key metrics to monitor:
# secureclaw_requests_total
# secureclaw_blocks_total  
# secureclaw_trust_level_changes
# secureclaw_response_time_seconds
# secureclaw_audit_chain_length
```

## 3. Viewing Audit Logs

### Command-Line Access

**SQLite direct access:**

```bash
# Connect to audit database
docker compose exec agentshroud sqlite3 /data/agentshroud.db

# Recent audit entries
.mode column
.headers on
SELECT id, timestamp, agent_id, threat_level, direction 
FROM audit_entries 
ORDER BY timestamp DESC 
LIMIT 20;

# MCP audit entries
SELECT ae.timestamp, mcp.server_name, mcp.tool_name, mcp.blocked, mcp.block_reason
FROM audit_entries ae
JOIN mcp_audit_entries mcp ON ae.id = mcp.id
WHERE ae.timestamp > datetime('now', '-1 hour')
ORDER BY ae.timestamp DESC;

# Exit SQLite
.quit
```

**Log file access:**

```bash
# Real-time log monitoring
docker compose logs -f agentshroud

# Filter by log level
docker compose logs agentshroud 2>&1 | grep "ERROR\|WARN"

# Export logs for analysis
docker compose logs --since "24h" agentshroud > agentshroud-logs-$(date +%Y%m%d).txt
```

### Web Interface Access

**Admin API endpoints:**

```bash
# Set admin token
export ADMIN_TOKEN=$(cat /run/secrets/admin-token)

# Recent audit entries (last 100)
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?limit=100" | jq '.'

# Audit entries by agent
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?agent_id=agent-123&limit=50" | jq '.'

# High-threat entries
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?threat_level=HIGH&limit=20" | jq '.'

# Blocked actions
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit/blocked?since=24h" | jq '.'
```

## 4. Handling Alerts

### Alert Severity Levels

| Level | Description | Response Time | Actions |
|-------|-------------|---------------|---------|
| **CRITICAL** | System compromise, data breach | Immediate (15 min) | Activate incident response |
| **HIGH** | Security violation, kill switch trigger | 1 hour | Investigate, document |
| **MEDIUM** | Suspicious activity, rate limits | 4 hours | Review, tune rules |
| **LOW** | Configuration issues, warnings | Next business day | Log, schedule fix |

### Critical Alert Response

**Kill Switch Triggered:**

```bash
# Check kill switch status
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/kill-switch | jq '.'

# Response actions:
# 1. Verify trigger reason in logs
docker compose logs agentshroud | grep -i "kill.*switch"

# 2. Check for ongoing threats
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?threat_level=CRITICAL&limit=10" | jq '.'

# 3. If false positive, deactivate kill switch
curl -X POST -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/kill-switch \
  -d '{"mode": "deactivate", "reason": "false_positive_investigation"}'

# 4. Document incident in runbook
```

**Audit Chain Integrity Failure:**

```bash
# Check audit chain status
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/audit/integrity | jq '.'

# Response actions:
# 1. Immediately activate kill switch
curl -X POST -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/kill-switch \
  -d '{"mode": "hard_kill", "reason": "audit_integrity_failure"}'

# 2. Export audit logs before any changes
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".output audit_backup_$(date +%Y%m%d_%H%M%S).sql" \
  ".dump audit_entries"

# 3. Start incident response procedure (see incident-response.md)
```

### High Alert Response

**Multiple Authentication Failures:**

```bash
# Check recent auth failures
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/metrics?filter=auth_failures&since=1h" | jq '.'

# Response actions:
# 1. Review source IPs
# 2. Consider IP blocking
# 3. Check for brute force patterns
# 4. Adjust rate limits if needed
```

**Trust Level Violations:**

```bash
# Check recent trust level changes
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/trust-levels?recent_changes=true | jq '.'

# Response actions:
# 1. Review violation details
# 2. Validate trust level decisions
# 3. Adjust trust promotion criteria if needed
```

## 5. API Key Rotation

### OpenClaw API Key

```bash
# 1. Generate new API key in OpenClaw dashboard

# 2. Update Docker secret
echo "new_api_key_here" | docker secret create openclaw-api-key-new -

# 3. Update service configuration
docker service update --secret-rm openclaw-api-key \
  --secret-add source=openclaw-api-key-new,target=openclaw-api-key \
  secureclaw_secureclaw

# 4. Test connectivity
curl -s https://localhost:8443/health | grep openclaw

# 5. Remove old secret
docker secret rm openclaw-api-key-old
```

### Admin API Token

```bash
# 1. Generate new JWT token
python scripts/generate-admin-token.py > new-admin-token.txt

# 2. Update secret
docker secret create admin-token-new new-admin-token.txt

# 3. Update service
docker service update --secret-rm admin-token \
  --secret-add source=admin-token-new,target=admin-token \
  secureclaw_secureclaw

# 4. Test admin endpoints
export ADMIN_TOKEN=$(cat new-admin-token.txt)
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/health
```

### SSL Certificates

```bash
# 1. Generate new certificates
openssl req -x509 -newkey rsa:4096 -keyout new-server.key \
  -out new-server.crt -days 365 -nodes \
  -subj "/CN=agentshroud.local"

# 2. Update secrets
docker secret create ssl-cert-new new-server.crt
docker secret create ssl-key-new new-server.key

# 3. Update service (requires restart)
docker service update --secret-rm ssl-cert --secret-rm ssl-key \
  --secret-add source=ssl-cert-new,target=ssl-cert \
  --secret-add source=ssl-key-new,target=ssl-key \
  secureclaw_secureclaw

# 4. Restart to load new certificates
docker service update --force secureclaw_secureclaw
```

## 6. System Updates

### AgentShroud Updates

```bash
# 1. Run update script
chmod +x scripts/update-agentshroud.sh
./scripts/update-agentshroud.sh

# Script performs:
# - Backup current configuration
# - Pull new Docker image
# - Run database migrations
# - Update configuration if needed
# - Restart services
# - Verify health

# 2. Manual update process
# Backup current state
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".backup /data/backup_$(date +%Y%m%d).db"

# Pull new image
docker compose pull agentshroud

# Stop current service
docker compose stop agentshroud

# Start with new image
docker compose up -d agentshroud

# Check logs for migration messages
docker compose logs -f agentshroud

# Verify system health
curl -s https://localhost:8443/health
```

### Configuration Updates

```bash
# 1. Backup current configuration
cp config/agentshroud.yaml config/agentshroud.yaml.backup.$(date +%Y%m%d)

# 2. Edit configuration
vim config/agentshroud.yaml

# 3. Validate configuration
docker compose exec agentshroud python -c "
import yaml
with open('/config/agentshroud.yaml') as f:
    config = yaml.safe_load(f)
print('Configuration valid')
"

# 4. Apply changes (requires restart)
docker compose restart agentshroud

# 5. Verify changes took effect
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/config | jq '.gateway'
```

## 7. Backup and Restore Procedures

### Backup Procedures

**Daily automated backup:**

```bash
#!/bin/bash
# backup-agentshroud.sh (run via cron)

BACKUP_DIR="/backup/agentshroud/$(date +%Y/%m)"
mkdir -p "$BACKUP_DIR"

# Database backup
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".backup $BACKUP_DIR/audit_$(date +%Y%m%d_%H%M%S).db"

# Configuration backup
cp -r config/ "$BACKUP_DIR/config_$(date +%Y%m%d)/"

# Secrets backup (encrypted)
docker secret ls --format "table {{.Name}}\t{{.CreatedAt}}" > \
  "$BACKUP_DIR/secrets_inventory_$(date +%Y%m%d).txt"

# Compress and encrypt
tar czf "$BACKUP_DIR/backup_$(date +%Y%m%d).tar.gz" \
  config/ logs/ "$BACKUP_DIR"/*.db
gpg --encrypt --armor -r backup@company.com \
  "$BACKUP_DIR/backup_$(date +%Y%m%d).tar.gz"

# Clean up old backups (>30 days)
find /backup/agentshroud -name "*.gz" -mtime +30 -delete

echo "Backup completed: $BACKUP_DIR"
```

**On-demand backup:**

```bash
# Quick backup before changes
./scripts/backup-now.sh maintenance-$(date +%Y%m%d)

# Export audit trail for compliance
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  -header -csv "SELECT * FROM audit_entries WHERE timestamp > '2024-01-01'" \
  > audit_export_$(date +%Y%m%d).csv
```

### Restore Procedures

**Database restore:**

```bash
# 1. Stop AgentShroud
docker compose stop agentshroud

# 2. Backup current database
docker compose exec db sqlite3 /data/agentshroud.db \
  ".backup /data/current_backup.db"

# 3. Restore from backup
docker compose exec db sqlite3 /data/agentshroud.db \
  ".restore /data/backup_20240115.db"

# 4. Verify integrity
docker compose exec db sqlite3 /data/agentshroud.db \
  "PRAGMA integrity_check;"

# 5. Start service
docker compose start agentshroud

# 6. Verify audit chain
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/audit/integrity
```

**Configuration restore:**

```bash
# 1. Restore configuration files
cp backup/config_20240115/agentshroud.yaml config/
cp backup/config_20240115/egress-config.yml config/
cp backup/config_20240115/mcp-config.yml config/

# 2. Restart with restored config
docker compose restart agentshroud

# 3. Verify configuration
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/config
```

## 8. Common Troubleshooting Scenarios

### Service Won't Start

**Symptoms:** `docker compose up` fails or service immediately exits

**Troubleshooting steps:**

```bash
# 1. Check logs for error messages
docker compose logs agentshroud | tail -50

# 2. Verify configuration syntax
docker compose config

# 3. Check port conflicts
netstat -tlnp | grep :8443
# If in use, set AGENTSHROUD_PORT_OFFSET environment variable

# 4. Verify secrets exist
docker secret ls | grep -E "(openclaw-api-key|admin-token|ssl-cert)"

# 5. Check disk space
df -h /var/lib/docker

# 6. Verify Docker daemon is running
systemctl status docker
```

**Common fixes:**

```bash
# Port conflict resolution
export AGENTSHROUD_PORT_OFFSET=100
docker compose up -d
# Service will use port 8543 instead of 8443

# Missing secrets
echo "your_openclaw_api_key" | docker secret create openclaw-api-key -
echo "your_admin_token" | docker secret create admin-token -

# Configuration fix
docker compose exec agentshroud python -c "
import yaml
with open('/config/agentshroud.yaml') as f:
    yaml.safe_load(f)  # Will raise exception if invalid
"
```

### High Memory Usage

**Symptoms:** Server becomes slow, out-of-memory errors

**Investigation:**

```bash
# 1. Check memory usage
docker stats --no-stream
free -h

# 2. Check audit table size
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT COUNT(*) as entries, 
          SUM(LENGTH(content)) as content_bytes,
          MAX(timestamp) as latest_entry
   FROM audit_entries;"

# 3. Check for memory leaks in logs
docker compose logs agentshroud | grep -i "memory\|oom"
```

**Mitigation:**

```bash
# 1. Increase Docker memory limits
# Edit docker-compose.yml:
# agentshroud:
#   mem_limit: 2g
#   mem_reservation: 1g

# 2. Archive old audit entries
docker compose exec agentshroud python scripts/archive_old_audits.py --days=90

# 3. Restart service to clear memory
docker compose restart agentshroud

# 4. Enable audit compression in config
# agentshroud.yaml:
# audit:
#   compression: true
#   batch_size: 50
```

### Database Locked Errors

**Symptoms:** "database is locked" errors in logs

**Resolution:**

```bash
# 1. Check for long-running transactions
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "PRAGMA busy_timeout = 30000;"

# 2. Enable WAL mode for better concurrency
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "PRAGMA journal_mode=WAL;"

# 3. Check for abandoned connections
docker compose logs agentshroud | grep -i "database.*lock"

# 4. Restart service if issue persists
docker compose restart agentshroud
```

### SSL/TLS Certificate Issues

**Symptoms:** Certificate errors, HTTPS connection failures

**Diagnosis:**

```bash
# 1. Check certificate validity
openssl x509 -in /run/secrets/ssl-cert -text -noout | grep -A 2 "Validity"

# 2. Test SSL connection
openssl s_client -connect localhost:8443 -servername agentshroud.local

# 3. Check certificate chain
curl -vI https://localhost:8443/health
```

**Resolution:**

```bash
# 1. Generate new self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt \
  -days 365 -nodes -subj "/CN=agentshroud.local"

# 2. Update Docker secrets (requires restart)
docker secret create ssl-cert-new server.crt
docker secret create ssl-key-new server.key

# 3. Update service
docker compose down
# Update docker-compose.yml to use new secret names
docker compose up -d
```

### Performance Issues

**Symptoms:** Slow response times, timeouts

**Performance analysis:**

```bash
# 1. Check response times
curl -w "@curl-format.txt" -s https://localhost:8443/health

# curl-format.txt:
# time_namelookup: %{time_namelookup}\n
# time_connect: %{time_connect}\n
# time_appconnect: %{time_appconnect}\n
# time_pretransfer: %{time_pretransfer}\n
# time_redirect: %{time_redirect}\n
# time_starttransfer: %{time_starttransfer}\n
# time_total: %{time_total}\n

# 2. Check database performance
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".timer on" \
  "SELECT COUNT(*) FROM audit_entries WHERE timestamp > datetime('now', '-1 day');"

# 3. Monitor resource usage
top -p $(docker inspect --format '{{.State.Pid}}' secureclaw_secureclaw_1)
```

**Performance tuning:**

```bash
# 1. Optimize SQLite settings (in configuration)
# database:
#   cache_size: -4096        # 4MB cache
#   synchronous: NORMAL      # Faster than FULL
#   journal_mode: WAL        # Better concurrency

# 2. Tune rate limiting
# rate_limiting:
#   algorithm: "sliding_window"  # More efficient than token bucket

# 3. Enable audit compression
# audit:
#   compression: true
#   batch_size: 200

# 4. Add database indexes if missing
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_entries(timestamp);"
```

This runbook provides the essential procedures for day-to-day AgentShroud operations. Keep it updated as the system evolves and add site-specific procedures as needed.