# Backup & Restore Runbook — AgentShroud

> Last updated: 2026-02-18

## What to Back Up

| Data | Location | Frequency | Priority |
|------|----------|-----------|----------|
| Audit ledger | `data/audit_ledger.jsonl` | Daily | **Critical** |
| Configuration | `docker-compose.yml`, `.env` | On change | High |
| Source code | GitHub repo | Every push | High (already in git) |
| Secrets | 1Password | On rotation | **Critical** (managed by 1Password) |
| Database (if any) | `data/*.db` | Daily | High |

## Backup Procedure

### Daily Automated Backup

Add to crontab (`crontab -e`):

```cron
# Daily backup at 02:00 UTC (create scripts/backup.sh from the manual procedure below)
0 2 * * * /home/agentshroud-bot/Development/agentshroud/scripts/backup.sh
```

### Manual Backup

```bash
cd ~/Development/agentshroud

# Create timestamped backup
BACKUP_DIR="backups/$(date +%Y-%m-%d)"
mkdir -p "$BACKUP_DIR"

# Audit ledger
cp data/audit_ledger.jsonl "$BACKUP_DIR/"

# Config files (no secrets!)
cp docker-compose.yml "$BACKUP_DIR/"

# Database files
cp data/*.db "$BACKUP_DIR/" 2>/dev/null || true

# Compress
tar -czf "backups/agentshroud-$(date +%Y-%m-%d).tar.gz" "$BACKUP_DIR"
rm -rf "$BACKUP_DIR"

echo "Backup saved to backups/agentshroud-$(date +%Y-%m-%d).tar.gz"
```

### Off-Site Backup

```bash
# Copy to another Tailscale device
scp backups/agentshroud-$(date +%Y-%m-%d).tar.gz \
    user@other-device.tail240ea8.ts.net:/backups/agentshroud/
```

---

## Restore Procedure

### Restore from Backup

```bash
cd ~/Development/agentshroud

# Stop services
docker compose down

# Extract backup
tar -xzf backups/agentshroud-YYYY-MM-DD.tar.gz

# Restore data
cp YYYY-MM-DD/audit_ledger.jsonl data/
cp YYYY-MM-DD/*.db data/ 2>/dev/null || true

# Restart services
docker compose up -d

# Verify
curl -s http://localhost:8080/health
```

### Disaster Recovery (Full Rebuild)

If the Pi is completely lost:

1. **New Pi setup:** Follow [Raspberry Pi Setup Guide](../deploy/raspberry-pi.md)

2. **Restore code:**
   ```bash
   git clone https://github.com/idallasj/agentshroud.git ~/Development/agentshroud
   ```

3. **Restore conda env:**
   ```bash
   conda create -n agentshroud python=3.13
   conda activate agentshroud
   pip install -r requirements.txt
   ```

4. **Restore secrets from 1Password:**
   ```bash
   # Re-create Docker Secrets from 1Password
   op item get "AgentShroud Bot" --fields "telegram_token" | docker secret create telegram_token -
   # ... repeat for other secrets
   ```

5. **Restore data from backup:**
   ```bash
   scp user@backup-host:/backups/agentshroud/latest.tar.gz /tmp/
   tar -xzf /tmp/latest.tar.gz -C data/
   ```

6. **Start services:**
   ```bash
   docker compose up -d
   sudo ./scripts/tailscale-serve.sh start
   ```

7. **Verify everything:**
   ```bash
   ./scripts/tailscale-check.sh
   curl http://localhost:8080/health
   ~/miniforge3/envs/agentshroud/bin/python -m pytest gateway/tests/ -v
   ```

---

## Backup Retention

| Type | Retention | Storage |
|------|-----------|---------|
| Daily backups | 7 days | Local `backups/` |
| Weekly backups | 4 weeks | Off-site |
| Monthly backups | 6 months | Off-site |

Clean up old backups:
```bash
# Remove local backups older than 7 days
find backups/ -name "*.tar.gz" -mtime +7 -delete
```
