# AgentShroud Incident Response Plan

This document defines the procedures for responding to security incidents in AgentShroud deployments.

## Incident Classification System

### Priority Levels

| Priority | Description | Examples | Response Time | Impact |
|----------|-------------|----------|---------------|---------|
| **P1 - Critical** | Active security breach, system compromise | Data exfiltration, container escape, audit tampering | 15 minutes | Complete service disruption |
| **P2 - High** | Serious security threat, potential breach | Kill switch triggered, mass violations, injection detected | 1 hour | Major service degradation |
| **P3 - Medium** | Security event requiring investigation | Trust level anomalies, suspicious patterns, rate limit bypass | 4 hours | Limited service impact |
| **P4 - Low** | Minor security issue, policy violation | Configuration drift, single agent violation, monitoring alerts | Next business day | No service impact |

### Severity Assessment Matrix

```
   Impact →   Low    Medium    High     Critical
Likelihood ↓
High         P3      P2        P1       P1
Medium       P4      P3        P2       P1  
Low          P4      P4        P3       P2
```

## Incident Response Team Structure

### Primary Roles

| Role | Responsibility | Contact Method | Authority Level |
|------|----------------|----------------|-----------------|
| **Incident Commander** | Overall incident coordination | Phone + Slack | Full system access |
| **Security Analyst** | Threat analysis, forensics | Slack + Email | Read-only security logs |
| **Platform Engineer** | System operations, recovery | Phone + Slack | Full system access |
| **Communications Lead** | Stakeholder updates | Email + Phone | No system access |

### Escalation Chain

```
Level 1: On-call Engineer
    ↓ (15 min for P1, 1h for P2)
Level 2: Security Team Lead
    ↓ (30 min for P1, 2h for P2)
Level 3: Engineering Manager
    ↓ (1h for P1, 4h for P2)
Level 4: CISO / CTO
```

## P1 Critical Incidents

### Data Exfiltration Detected

**Indicators:**
- Large data transfers in audit logs
- Sensitive data in agent responses
- External network connections to suspicious IPs
- Unusual file access patterns

**Immediate Response (0-15 minutes):**

```bash
# 1. IMMEDIATE: Activate emergency kill switch
curl -X POST https://localhost:8443/admin/kill-switch \
  -H "Authorization: Bearer $(cat /run/secrets/admin-token)" \
  -d '{"mode": "panic", "reason": "data_exfiltration_detected"}'

# 2. Isolate the system
# Block all network traffic except essential management
iptables -A OUTPUT -d 10.0.0.0/8 -j ACCEPT     # Allow internal
iptables -A OUTPUT -d 192.168.0.0/16 -j ACCEPT # Allow private
iptables -A OUTPUT -j DROP                      # Block all else

# 3. Capture immediate evidence
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".output evidence_$(date +%Y%m%d_%H%M%S).sql" \
  ".dump audit_entries"

# 4. Preserve container state
docker commit secureclaw_secureclaw_1 evidence:$(date +%Y%m%d_%H%M%S)

# 5. Start incident log
echo "$(date): P1 INCIDENT - Data exfiltration detected" >> incident.log
echo "$(date): Kill switch activated in PANIC mode" >> incident.log
echo "$(date): System isolated, evidence preserved" >> incident.log
```

**Investigation Phase (15-60 minutes):**

```bash
# 1. Identify affected agents
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT DISTINCT agent_id, COUNT(*) as suspicious_actions
   FROM audit_entries 
   WHERE timestamp > datetime('now', '-2 hours')
     AND (threat_level = 'HIGH' OR threat_level = 'CRITICAL')
   GROUP BY agent_id 
   ORDER BY suspicious_actions DESC;"

# 2. Analyze data movement patterns
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT timestamp, agent_id, direction, 
          LENGTH(content) as data_size, 
          SUBSTR(content, 1, 100) as preview
   FROM audit_entries 
   WHERE direction = 'OUTBOUND' 
     AND LENGTH(content) > 10000
     AND timestamp > datetime('now', '-4 hours')
   ORDER BY timestamp DESC;"

# 3. Check for privilege escalation
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT agent_id, level, last_promoted, violations
   FROM agent_trust 
   WHERE last_promoted > datetime('now', '-24 hours')
     OR violations = 0;"

# 4. Network traffic analysis
tcpdump -i any -w incident_traffic_$(date +%Y%m%d_%H%M%S).pcap &
TCPDUMP_PID=$!
sleep 60
kill $TCPDUMP_PID
```

**Containment Actions:**

```bash
# 1. Revoke compromised agent credentials
# (Agent-specific - depends on authentication method)

# 2. Block suspicious IP addresses
iptables -A INPUT -s SUSPICIOUS_IP -j DROP
iptables -A OUTPUT -d SUSPICIOUS_IP -j DROP

# 3. Quarantine affected containers
docker container stop $(docker ps -q --filter ancestor=suspicious_image)

# 4. Enable maximum audit logging
curl -X PUT https://localhost:8443/admin/config \
  -H "Authorization: Bearer $(cat /run/secrets/admin-token)" \
  -d '{
    "audit": {
      "log_levels": {
        "requests": "DEBUG",
        "responses": "DEBUG",
        "blocks": "DEBUG",
        "violations": "DEBUG"
      }
    }
  }'
```

### Container Escape Attempt

**Indicators:**
- Unusual system calls in container logs
- Attempts to access host filesystem
- Privilege escalation attempts
- Process injection attempts

**Immediate Response:**

```bash
# 1. IMMEDIATE: Full system isolation
curl -X POST https://localhost:8443/admin/kill-switch \
  -H "Authorization: Bearer $(cat /run/secrets/admin-token)" \
  -d '{"mode": "panic", "reason": "container_escape_attempt"}'

# 2. Stop all containers immediately
docker stop $(docker ps -q)

# 3. Preserve evidence
docker container commit SUSPECT_CONTAINER forensic_image:$(date +%Y%m%d_%H%M%S)
docker container export SUSPECT_CONTAINER > suspect_container_$(date +%Y%m%d_%H%M%S).tar

# 4. Check host system integrity
rkhunter --check --sk
chkrootkit

# 5. Monitor for continued activity
ps aux | grep -v grep | grep -E "(docker|container)" > running_processes.txt
netstat -tulpn > network_connections.txt
```

**Forensic Analysis:**

```bash
# 1. Analyze container logs
docker logs SUSPECT_CONTAINER > container_logs.txt 2>&1

# 2. Check for capability abuse
docker inspect SUSPECT_CONTAINER | jq '.HostConfig.CapAdd'
docker inspect SUSPECT_CONTAINER | jq '.HostConfig.Privileged'

# 3. Examine file system changes
docker diff SUSPECT_CONTAINER > filesystem_changes.txt

# 4. Network analysis
docker inspect SUSPECT_CONTAINER | jq '.NetworkSettings'

# 5. Mount point analysis
docker inspect SUSPECT_CONTAINER | jq '.Mounts'
```

### Audit Chain Tampering

**Indicators:**
- Audit chain integrity check failures
- Missing or modified audit entries
- Hash mismatches in audit chain
- Database corruption errors

**Immediate Response:**

```bash
# 1. IMMEDIATE: Preserve current audit state
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".backup /backup/emergency_audit_$(date +%Y%m%d_%H%M%S).db"

# 2. Activate kill switch
curl -X POST https://localhost:8443/admin/kill-switch \
  -H "Authorization: Bearer $(cat /run/secrets/admin-token)" \
  -d '{"mode": "hard_kill", "reason": "audit_integrity_compromised"}'

# 3. Calculate integrity hash of current database
sha256sum /data/agentshroud.db > audit_db_hash_$(date +%Y%m%d_%H%M%S).txt

# 4. Check for recent database modifications
stat /data/agentshroud.db
lsof /data/agentshroud.db
```

**Integrity Investigation:**

```bash
# 1. Run comprehensive integrity check
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "PRAGMA integrity_check;"

# 2. Verify audit chain manually
docker compose exec agentshroud python3 << 'EOF'
import sqlite3
import hashlib

conn = sqlite3.connect('/data/agentshroud.db')
cursor = conn.cursor()

# Get all entries ordered by timestamp
cursor.execute("SELECT id, content_hash, previous_hash, chain_hash FROM audit_entries ORDER BY timestamp")
entries = cursor.fetchall()

print(f"Total entries: {len(entries)}")

# Verify chain
prev_hash = None
broken_links = []

for i, (entry_id, content_hash, previous_hash, chain_hash) in enumerate(entries):
    if i == 0:
        if previous_hash is not None:
            print(f"ERROR: First entry has non-null previous_hash")
            broken_links.append(entry_id)
    else:
        if previous_hash != prev_hash:
            print(f"ERROR: Chain break at entry {entry_id}")
            broken_links.append(entry_id)
    
    # Verify chain hash
    expected_chain = hashlib.sha256(f"{previous_hash}{content_hash}".encode()).hexdigest()
    if chain_hash != expected_chain:
        print(f"ERROR: Invalid chain hash at entry {entry_id}")
        broken_links.append(entry_id)
    
    prev_hash = chain_hash

print(f"Chain integrity check complete. Broken links: {len(broken_links)}")
if broken_links:
    print(f"Compromised entries: {broken_links[:10]}...")  # Show first 10
EOF
```

## P2 High Priority Incidents

### Prompt Injection Detected

**Response Procedure:**

```bash
# 1. Identify the injection attempt
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?threat_level=HIGH&category=injection&limit=10" \
  | jq '.[] | {id, timestamp, agent_id, content_preview: .content[:200]}'

# 2. Block the agent temporarily
AGENT_ID="suspicious_agent_id"
curl -X POST https://localhost:8443/admin/agents/$AGENT_ID/block \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -d '{"reason": "prompt_injection_detected", "duration": 3600}'

# 3. Analyze injection patterns
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT content, COUNT(*) as frequency
   FROM audit_entries 
   WHERE agent_id = '$AGENT_ID' 
     AND threat_level IN ('HIGH', 'CRITICAL')
     AND timestamp > datetime('now', '-24 hours')
   GROUP BY content
   ORDER BY frequency DESC
   LIMIT 10;"

# 4. Update security rules if new pattern detected
# Review and update PII sanitizer patterns
# Consider adding new injection detection rules
```

### PII Leak Incident

**Response Procedure:**

```bash
# 1. Identify PII leak extent
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT agent_id, COUNT(*) as pii_incidents,
          MIN(timestamp) as first_incident,
          MAX(timestamp) as last_incident
   FROM audit_entries 
   WHERE pii_redacted = 1
     AND timestamp > datetime('now', '-7 days')
   GROUP BY agent_id
   ORDER BY pii_incidents DESC;"

# 2. Check if PII made it to external systems
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT id, timestamp, direction, agent_id
   FROM audit_entries 
   WHERE direction = 'OUTBOUND'
     AND pii_redacted = 1
     AND timestamp > datetime('now', '-24 hours')
   ORDER BY timestamp DESC;"

# 3. Notify data protection team
echo "PII leak detected at $(date)" >> data_incidents.log
# Send notification to DPO/privacy team

# 4. Enhance PII detection rules
# Review sanitizer effectiveness
# Add additional PII patterns if needed
```

### Kill Switch Triggered

**Response Procedure:**

```bash
# 1. Check kill switch status and reason
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/kill-switch | jq '.'

# 2. Review triggering events
docker compose logs agentshroud | grep -A 10 -B 10 "kill.*switch"

# 3. Analyze threat level
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/audit?threat_level=CRITICAL&since=1h" | jq '.'

# 4. If false positive, prepare deactivation
# Thorough investigation first!
# curl -X POST https://localhost:8443/admin/kill-switch \
#   -H "Authorization: Bearer $ADMIN_TOKEN" \
#   -d '{"mode": "deactivate", "reason": "false_positive_confirmed"}'

# 5. Document decision reasoning
echo "$(date): Kill switch investigation complete" >> incident.log
echo "$(date): Decision: [DEACTIVATE/MAINTAIN] - Reason: [detailed reason]" >> incident.log
```

## P3 Medium Priority Incidents

### Unauthorized SSH Access Attempt

**Response Procedure:**

```bash
# 1. Review SSH audit logs
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT ae.timestamp, mcp.agent_id, mcp.parameters, mcp.blocked, mcp.block_reason
   FROM audit_entries ae
   JOIN mcp_audit_entries mcp ON ae.id = mcp.id
   WHERE mcp.server_name = 'ssh'
     AND (mcp.blocked = 1 OR ae.threat_level = 'HIGH')
     AND ae.timestamp > datetime('now', '-24 hours')
   ORDER BY ae.timestamp DESC;"

# 2. Check for pattern of attempts
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT agent_id, COUNT(*) as attempt_count,
          MIN(timestamp) as first_attempt,
          MAX(timestamp) as last_attempt
   FROM audit_entries ae
   JOIN mcp_audit_entries mcp ON ae.id = mcp.id
   WHERE mcp.server_name = 'ssh'
     AND mcp.blocked = 1
   GROUP BY agent_id
   HAVING attempt_count > 5
   ORDER BY attempt_count DESC;"

# 3. Review agent trust levels
curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  "https://localhost:8443/admin/trust-levels?agent_ids=suspicious_agent_1,suspicious_agent_2" \
  | jq '.'

# 4. Consider trust level adjustment
# Manual review required for trust level demotion
```

### Trust Level Anomaly

**Response Procedure:**

```bash
# 1. Identify anomalous trust changes
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  "SELECT agent_id, level, last_promoted, total_actions, violations,
          ROUND(CAST(violations AS FLOAT) / total_actions * 100, 2) as violation_rate
   FROM agent_trust
   WHERE last_promoted > datetime('now', '-7 days')
      OR violation_rate > 10.0
   ORDER BY last_promoted DESC;"

# 2. Review recent actions by affected agents
# (Use agent IDs from previous query)
for agent in suspicious_agent_list; do
    echo "=== Agent: $agent ==="
    docker compose exec agentshroud sqlite3 /data/agentshroud.db \
      "SELECT timestamp, threat_level, direction, SUBSTR(content, 1, 100)
       FROM audit_entries
       WHERE agent_id = '$agent'
         AND timestamp > datetime('now', '-7 days')
       ORDER BY timestamp DESC
       LIMIT 20;"
done

# 3. Check for gaming/manipulation
# Look for patterns that might indicate attempts to game the trust system

# 4. Document findings
echo "$(date): Trust anomaly investigation for agents: $suspicious_agents" >> trust_incidents.log
```

## P4 Low Priority Incidents

### Configuration Drift

**Response Procedure:**

```bash
# 1. Compare current vs expected configuration
diff -u config/agentshroud.yaml.golden config/agentshroud.yaml

# 2. Check configuration history
git log --oneline -10 config/

# 3. Validate current configuration
docker compose exec agentshroud python -c "
import yaml
with open('/config/agentshroud.yaml') as f:
    config = yaml.safe_load(f)
    print('Configuration syntax: OK')
    print(f'Operational mode: {config.get(\"gateway\", {}).get(\"operational_mode\")}')
    print(f'Kill switch enabled: {config.get(\"security\", {}).get(\"kill_switch\", {}).get(\"enabled\")}')
"

# 4. Schedule configuration remediation
echo "$(date): Configuration drift detected - scheduling remediation" >> maintenance.log
```

## Post-Incident Activities

### Post-Incident Review Template

```markdown
# Post-Incident Review - [Incident ID]

## Incident Summary
- **Date/Time**: 
- **Duration**: 
- **Severity**: P1/P2/P3/P4
- **Root Cause**: 
- **Services Affected**: 

## Timeline
| Time | Action | Owner |
|------|--------|-------|
| HH:MM | Incident detected | |
| HH:MM | Response team notified | |
| HH:MM | Initial containment | |
| HH:MM | Root cause identified | |
| HH:MM | Resolution implemented | |
| HH:MM | Service restored | |

## What Went Well
- 
- 
- 

## What Could Be Improved
- 
- 
- 

## Action Items
- [ ] Action 1 (Owner: XXX, Due: DATE)
- [ ] Action 2 (Owner: XXX, Due: DATE)
- [ ] Action 3 (Owner: XXX, Due: DATE)

## Prevention Measures
- 
- 
- 

## Monitoring/Alerting Improvements
- 
- 
- 
```

### Lessons Learned Integration

**After each incident:**

1. **Update detection rules** based on new attack patterns
2. **Enhance monitoring** to catch similar incidents faster  
3. **Improve automation** to reduce manual response time
4. **Update documentation** with new procedures learned
5. **Conduct training** if skills gaps identified
6. **Review and update** incident response procedures

### Evidence Preservation

```bash
# Create incident evidence package
INCIDENT_ID="INC-$(date +%Y%m%d)-001"
mkdir -p /evidence/$INCIDENT_ID

# Database snapshot
docker compose exec agentshroud sqlite3 /data/agentshroud.db \
  ".backup /evidence/$INCIDENT_ID/audit_snapshot.db"

# Configuration snapshot
cp -r config/ /evidence/$INCIDENT_ID/config/

# Logs snapshot
docker compose logs --since="2h" > /evidence/$INCIDENT_ID/container_logs.txt

# System state
docker ps -a > /evidence/$INCIDENT_ID/container_state.txt
docker images > /evidence/$INCIDENT_ID/image_inventory.txt

# Network state
netstat -tulpn > /evidence/$INCIDENT_ID/network_connections.txt
iptables -L -n > /evidence/$INCIDENT_ID/firewall_rules.txt

# Create tamper-evident archive
tar czf /evidence/$INCIDENT_ID.tar.gz /evidence/$INCIDENT_ID/
sha256sum /evidence/$INCIDENT_ID.tar.gz > /evidence/$INCIDENT_ID.tar.gz.sha256

# Secure storage
chmod 444 /evidence/$INCIDENT_ID.tar.gz*
```

## Contact Information

### Emergency Contacts

| Role | Primary | Secondary | Escalation |
|------|---------|-----------|------------|
| **On-Call Engineer** | +1-XXX-XXX-XXXX | +1-XXX-XXX-XXXX | Slack: @oncall |
| **Security Team** | security@company.com | +1-XXX-XXX-XXXX | Slack: @security-team |
| **Engineering Manager** | +1-XXX-XXX-XXXX | manager@company.com | Slack: @eng-mgr |
| **CISO** | +1-XXX-XXX-XXXX | ciso@company.com | Slack: @ciso |

### External Contacts

| Service | Contact | Use Case |
|---------|---------|----------|
| **Legal** | legal@company.com | Data breach, regulatory |
| **PR** | pr@company.com | Public incident response |
| **Insurance** | +1-XXX-XXX-XXXX | Cyber insurance claims |
| **Law Enforcement** | Local FBI field office | Criminal activity |

This incident response plan should be reviewed quarterly and updated based on lessons learned from actual incidents and changes in the threat landscape.