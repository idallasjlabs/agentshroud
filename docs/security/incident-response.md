# Incident Response Playbook — SecureClaw

> Last updated: 2026-02-18 | SecureClaw v0.2.0

## 1. Detection — What Triggers an Incident

| Trigger | Source | Severity |
|---------|--------|----------|
| Repeated failed authentication (>5 in 1 min) | Audit ledger, gateway logs | P2 |
| PII detected in outbound LLM request | PII sanitizer alert | P2 |
| PII leaked in response despite sanitizer | Manual detection | P1 |
| Credential detected in command output | Credential blocker | P1 |
| Kill switch activated | Audit ledger | P2–P1 |
| Unauthorized SSH command attempt | Approval queue rejection log | P3 |
| Unexpected container restart | Docker events | P3 |
| Tailscale connection lost | Monitoring | P3 |
| Suspected bot token compromise | External report / anomalous activity | P1 |
| Audit ledger tampering suspected | Integrity check failure | P1 |

---

## 2. Severity Classification

| Level | Name | Description | Response Time | Examples |
|-------|------|-------------|--------------|---------|
| **P1** | Critical | Active data breach, credential exposure, system compromise | **Immediate** (<15 min) | PII leak, token compromise, credential exposure |
| **P2** | High | Security control triggered, potential breach | **<1 hour** | Kill switch activation, repeated auth failures, PII caught by sanitizer |
| **P3** | Medium | Anomaly detected, no confirmed breach | **<4 hours** | Unexpected restarts, unauthorized command attempts |
| **P4** | Low | Informational, hardening opportunity | **<24 hours** | Configuration drift, missed update, new CVE in dependency |

---

## 3. Response Procedures

### P1 — Critical

1. **Contain immediately:**
   ```bash
   # Kill switch — full shutdown
   # Via Telegram: /kill shutdown
   # Or directly:
   docker compose down
   ```

2. **Preserve evidence:**
   ```bash
   # Export audit ledger
   cp data/audit_ledger.jsonl /tmp/incident-$(date +%Y%m%d-%H%M%S)/
   # Export container logs
   docker logs secureclaw-gateway > /tmp/incident-$(date +%Y%m%d-%H%M%S)/gateway.log 2>&1
   # Snapshot running state if container still up
   docker inspect secureclaw-gateway > /tmp/incident-$(date +%Y%m%d-%H%M%S)/inspect.json
   ```

3. **Rotate compromised credentials:**
   - Telegram bot token → BotFather → update in 1Password → Docker Secrets
   - LLM API key → provider dashboard → update in 1Password → Docker Secrets
   - SSH keys → regenerate → distribute

4. **Investigate root cause** (see Section 6)

5. **Notify stakeholders** (see Section 8)

6. **Rebuild and redeploy** from clean source

### P2 — High

1. **Assess:** Review audit ledger for scope
2. **Contain:** Activate kill switch in **freeze** mode (stops new requests, preserves state)
   ```
   # Via Telegram: /kill freeze
   ```
3. **Investigate:** Check what triggered the alert
4. **Resolve:** Fix root cause, unfreeze if safe
5. **Document:** Update audit ledger with investigation notes

### P3 — Medium

1. **Log:** Document the anomaly
2. **Investigate:** Review logs within 4 hours
3. **Remediate:** Apply fix if needed
4. **Monitor:** Watch for recurrence

### P4 — Low

1. **Track:** Create issue/task
2. **Schedule:** Address in next maintenance window
3. **Document:** Update security documentation

---

## 4. Kill Switch Usage Guide

The kill switch has three modes. Choose based on the situation:

| Mode | Command | Effect | When to Use |
|------|---------|--------|-------------|
| **Freeze** | `/kill freeze` | Stops processing new requests; preserves state | Investigation needed, no active breach |
| **Shutdown** | `/kill shutdown` | Graceful stop of all services | Confirmed incident, need evidence preserved |
| **Disconnect** | `/kill disconnect` | Severs all network connections immediately | Active exfiltration, compromised system |

### Decision Tree

```
Is data actively being exfiltrated?
├── YES → DISCONNECT immediately
└── NO → Is there a confirmed breach?
    ├── YES → SHUTDOWN, preserve evidence
    └── NO → FREEZE, investigate
```

### Recovering from Kill Switch

```bash
# After freeze:
# Via Telegram: /kill unfreeze

# After shutdown:
docker compose up -d

# After disconnect:
# 1. Fix the issue offline
# 2. Rotate all credentials
# 3. docker compose up -d
# 4. Verify Tailscale connectivity
```

---

## 5. Evidence Preservation

### What to Capture

| Evidence | Location | Command |
|----------|----------|---------|
| Audit ledger | `data/audit_ledger.jsonl` | `cp data/audit_ledger.jsonl /tmp/evidence/` |
| Gateway logs | Docker stdout | `docker logs secureclaw-gateway > evidence/gateway.log 2>&1` |
| Container state | Docker inspect | `docker inspect secureclaw-gateway > evidence/inspect.json` |
| Network connections | Container exec | `docker exec secureclaw-gateway ss -tlnp > evidence/netstat.log` |
| Docker events | Docker daemon | `docker events --since 24h --format '{{json .}}' > evidence/events.json` |
| Tailscale status | Tailscale CLI | `tailscale status > evidence/tailscale.log` |

### Audit Ledger Export

The audit ledger is append-only JSONL. Each entry contains:
- Timestamp (ISO 8601)
- Event type
- User ID
- Action details
- Outcome (allow/deny/sanitized)

```bash
# Export last 24 hours
python3 -c "
import json, sys
from datetime import datetime, timedelta
cutoff = (datetime.utcnow() - timedelta(hours=24)).isoformat()
for line in open('data/audit_ledger.jsonl'):
    entry = json.loads(line)
    if entry.get('timestamp', '') >= cutoff:
        print(line.strip())
" > evidence/last_24h.jsonl
```

---

## 6. Post-Incident Review Template

Complete within 48 hours of incident resolution.

```markdown
# Incident Review: [INCIDENT-YYYY-MM-DD-NNN]

## Summary
- **Date/Time:** 
- **Duration:** 
- **Severity:** P1/P2/P3/P4
- **Detected by:** 
- **Resolved by:** 

## Timeline
| Time (UTC) | Event |
|------------|-------|
| HH:MM | First indicator |
| HH:MM | Detection |
| HH:MM | Response initiated |
| HH:MM | Contained |
| HH:MM | Resolved |

## Root Cause
[Description of what caused the incident]

## Impact
- Data exposed: [yes/no, scope]
- Services affected: [list]
- Users affected: [count]

## Response Evaluation
- What worked well:
- What could improve:
- Response time: [acceptable/slow]

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| | | | |

## Lessons Learned
[Key takeaways for prevention]
```

---

## 7. Communication Templates

### Internal Alert (Telegram)

```
🚨 SECURITY INCIDENT — [SEVERITY]

What: [Brief description]
When: [Time UTC]
Status: [Investigating / Contained / Resolved]
Action: [What was done / what to do]

Kill switch: [Active / Not needed]
```

### Stakeholder Notification

```
Subject: SecureClaw Security Incident Notification — [Date]

We are writing to inform you of a security incident affecting the SecureClaw system.

Date of detection: [Date/Time UTC]
Nature: [Brief description]
Impact: [What was affected]
Current status: [Contained / Resolved]
Actions taken: [Summary]
Preventive measures: [What's being done to prevent recurrence]

Next update: [Time/Date]
```

---

## 8. Contacts and Escalation

| Role | Contact | Method |
|------|---------|--------|
| System Owner | [Configure] | Telegram / Phone |
| Security Lead | [Configure] | Telegram / Phone |
| Tailscale Admin | [Configure] | Tailscale admin console |

Update this table with actual contacts before going to production.
