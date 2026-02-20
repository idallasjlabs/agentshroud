# AgentShroud Security Scripts Reference

Quick reference for the security validation and emergency response scripts.

---

## verify-security.sh

**Purpose:** Comprehensive automated security validation

**Location:** `docker/scripts/verify-security.sh`

**Usage:**
```bash
./docker/scripts/verify-security.sh
```

**Checks Performed (13 total):**
1. ✓ Non-root users on both containers
2. ✓ Read-only root filesystem (both)
3. ✓ All capabilities dropped
4. ✓ No NET_RAW capability
5. ✓ no-new-privileges enabled
6. ✓ Seccomp profiles active
7. ✓ Localhost-only port binding
8. ✓ Resource limits set
9. ✓ Docker secrets mounted
10. ✓ Network isolation
11. ✓ Container health status
12. ✓ Security environment variables
13. ✓ No hardcoded secrets

**Exit Codes:**
- `0` - All checks passed (or passed with warnings)
- `1` - One or more checks failed

**When to Run:**
- After docker-compose.yml changes
- After container rebuilds
- Before production deployment
- As part of CI/CD pipeline
- After suspicious activity

---

## scan.sh

**Purpose:** Run OpenSCAP compliance scans and manual security checks

**Location:** `docker/scripts/scan.sh`

**Usage:**
```bash
./docker/scripts/scan.sh
```

**Features:**
- OpenSCAP SCAP content evaluation (if installed)
- Docker Bench Security integration (if available)
- Manual security checks:
  - Container user verification
  - Read-only filesystem tests
  - Network connectivity tests
  - Port binding verification
  - Security options review
  - Capability inspection

**Output Location:** `docker/reports/`

**Report Files:**
- `openclaw-scan-TIMESTAMP.html` - OpenClaw SCAP report
- `openclaw-scan-TIMESTAMP.xml` - OpenClaw SCAP results (ARF format)
- `gateway-scan-TIMESTAMP.html` - Gateway SCAP report
- `gateway-scan-TIMESTAMP.xml` - Gateway SCAP results (ARF format)
- `docker-bench-TIMESTAMP.log` - Docker Bench Security results
- `manual-checks-TIMESTAMP.log` - Manual security checks

**View Reports:**
```bash
open docker/reports/openclaw-scan-*.html
open docker/reports/gateway-scan-*.html
```

**When to Run:**
- Weekly compliance validation
- Before production deployment
- After major security changes
- For audit documentation
- During security reviews

---

## killswitch.sh

**Purpose:** Emergency shutdown with optional credential revocation

**Location:** `docker/scripts/killswitch.sh`

**Usage:**
```bash
./docker/scripts/killswitch.sh <mode>
```

### Mode 1: freeze
**Purpose:** Quick pause for investigation

```bash
./docker/scripts/killswitch.sh freeze
```

**Actions:**
- Pauses both containers immediately
- Preserves all state for forensics
- No data loss

**Resume:**
```bash
docker compose -f docker/docker-compose.yml unpause
```

**When to Use:**
- Suspicious activity detected
- Need to investigate bot behavior
- Temporary halt for analysis
- Quick response to anomalies

---

### Mode 2: shutdown
**Purpose:** Graceful shutdown preserving data

```bash
./docker/scripts/killswitch.sh shutdown
```

**Actions:**
- Stops containers gracefully
- Preserves all Docker volumes
- No credential changes

**Resume:**
```bash
docker compose -f docker/docker-compose.yml up -d
```

**When to Use:**
- Planned maintenance
- Configuration changes
- Testing updates
- Normal shutdown

---

### Mode 3: disconnect (⚠️ DANGEROUS)
**Purpose:** Nuclear option - complete disconnection

```bash
./docker/scripts/killswitch.sh disconnect
```

**Confirmations Required:**
1. Type "yes" to confirm
2. Type "DISCONNECT" to double-confirm

**Actions:**
1. Exports audit ledger to `docker/incidents/ledger-export-TIMESTAMP.db`
2. Stops all containers
3. Clears cached credentials from Docker volumes
4. Overwrites secret files with random data
5. Generates incident report: `docker/incidents/incident-TIMESTAMP.md`
6. Prints manual revocation instructions

**Manual Revocation Required:**
1. **OpenAI**: https://platform.openai.com/api-keys
2. **Anthropic**: https://console.anthropic.com/settings/keys
3. **1Password**: https://my.1password.com/ → Active Sessions
4. **Telegram**: Message @BotFather → /revoke → @therealidallasj_bot

**Incident Report Includes:**
- Complete container state snapshots
- Recent logs from both containers
- Network configuration
- Security settings
- Manual revocation checklist

**When to Use:**
- Confirmed security breach
- Credential exposure suspected
- Container compromise detected
- Unauthorized access confirmed
- Emergency credential rotation needed

**⚠️ WARNING:** This mode:
- **OVERWRITES** secret files (backup first!)
- **REQUIRES** manual API key revocation
- **PREVENTS** restart until new credentials added
- **CANNOT** be undone

**Recovery After Disconnect:**
1. Review incident report: `docker/incidents/incident-TIMESTAMP.md`
2. Analyze audit ledger: `sqlite3 docker/incidents/ledger-export-TIMESTAMP.db`
3. Manually revoke all API keys (see incident report)
4. Generate new credentials
5. Update secret files in `docker/secrets/`
6. Restart containers: `docker compose -f docker/docker-compose.yml up -d`

---

## Script Permissions

All scripts are executable:
```bash
chmod +x docker/scripts/verify-security.sh
chmod +x docker/scripts/scan.sh
chmod +x docker/scripts/killswitch.sh
```

---

## Automation Examples

### Daily Security Check (cron)
```bash
# Add to crontab: crontab -e
0 9 * * * /Users/ijefferson.admin/Development/agentshroud/docker/scripts/verify-security.sh
```

### Weekly Compliance Scan (cron)
```bash
# Add to crontab: crontab -e
0 2 * * 0 /Users/ijefferson.admin/Development/agentshroud/docker/scripts/scan.sh
```

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Security Verification
  run: ./docker/scripts/verify-security.sh

- name: Compliance Scan
  run: ./docker/scripts/scan.sh

- name: Upload Reports
  uses: actions/upload-artifact@v3
  with:
    name: security-reports
    path: docker/reports/
```

---

## Monitoring Integration

### Prometheus/Grafana
Export metrics from verify-security.sh:
```bash
./docker/scripts/verify-security.sh > /var/log/agentshroud/security-check.log
# Parse log for metrics
```

### Alerting
Set up alerts for:
- `verify-security.sh` exit code != 0
- Failed checks > 0
- Warnings > 1
- Container health != healthy

### Logging
All scripts log to stdout/stderr. Redirect as needed:
```bash
./docker/scripts/verify-security.sh 2>&1 | tee -a /var/log/agentshroud/verify-$(date +%Y%m%d).log
./docker/scripts/scan.sh 2>&1 | tee -a /var/log/agentshroud/scan-$(date +%Y%m%d).log
```

---

## Troubleshooting

### verify-security.sh fails
```bash
# Run with debug output
bash -x ./docker/scripts/verify-security.sh

# Check specific container
docker inspect openclaw-bot | less
docker logs openclaw-bot
```

### scan.sh reports missing OpenSCAP
```bash
# Install in containers (add to Dockerfile)
RUN apt-get install -y ssg-base ssg-debderived
```

### killswitch.sh doesn't confirm
```bash
# Use echo to auto-confirm (DANGEROUS!)
echo "yes" | ./docker/scripts/killswitch.sh freeze
echo -e "yes\nDISCONNECT" | ./docker/scripts/killswitch.sh disconnect
```

---

## Best Practices

1. **Run verify-security.sh** after every docker-compose.yml change
2. **Run scan.sh** weekly for compliance audit trail
3. **Test killswitch.sh freeze** monthly to ensure it works
4. **Never use disconnect** unless absolutely necessary
5. **Always backup** before using disconnect mode
6. **Review incident reports** after any kill switch activation
7. **Keep audit ledger** exports for compliance (90+ days)

---

**Last Updated:** 2026-02-16
**Scripts Version:** Phase 3A/3B
