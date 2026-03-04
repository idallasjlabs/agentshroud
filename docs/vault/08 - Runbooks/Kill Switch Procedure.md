---
title: Kill Switch Procedure
type: runbook
tags: [emergency, kill-switch, security, runbook]
related: [Security Modules/killswitch_monitor.py, Shutdown & Recovery, Quick Reference]
status: documented
---

# Kill Switch Procedure

## When to Use

| Situation | Action |
|-----------|--------|
| Agent is performing unauthorized actions | Freeze (pause agent) |
| Security incident detected (intrusion, data exfiltration attempt) | Shutdown |
| Agent won't stop spamming/sending messages | Disconnect |
| Suspected prompt injection taking control | Freeze then investigate |
| Emergency requiring immediate stop | Shutdown |

---

## Kill Switch Actions

| Action | Effect | Recoverable? |
|--------|--------|-------------|
| `freeze` | Pause all agent actions; containers stay running | Yes — unfreeze via dashboard |
| `shutdown` | Stop all containers immediately | Yes — `docker compose start` |
| `disconnect` | Drop network connections; processes continue | Yes — restart containers |

**Default action** (configured in `agentshroud.yaml`):
```yaml
dashboard:
  kill_switch_action: "freeze"
```

---

## Method 1: Dashboard (Recommended)

1. Navigate to `http://localhost:18790`
2. Locate the "Kill Switch" button in the header/control panel
3. Click → confirm the action
4. System performs the configured action and logs the event

---

## Method 2: API

```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)

# Freeze (pause agent)
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8080/admin/kill-switch \
  -d '{"action": "freeze"}'

# Shutdown
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8080/admin/kill-switch \
  -d '{"action": "shutdown"}'

# Disconnect
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8080/admin/kill-switch \
  -d '{"action": "disconnect"}'
```

---

## Method 3: Script

```bash
./docker/scripts/killswitch.sh
```

Performs the default kill switch action (as configured in `agentshroud.yaml`).

---

## Method 4: Docker Direct (Last Resort)

If gateway API is unreachable:

```bash
# Kill both containers immediately (SIGKILL)
docker compose -f docker/docker-compose.yml kill

# Or stop gracefully
docker compose -f docker/docker-compose.yml stop
```

---

## Post-Kill Switch Procedure

### After Freeze

1. Review dashboard for the action that triggered the freeze
2. Check approval queue for pending items
3. Review recent ledger entries
4. If safe to resume: use dashboard "Unfreeze" button

### After Shutdown

1. Investigate logs:
   ```bash
   docker logs --tail=500 agentshroud-gateway | grep -E "error|alert|suspicious"
   ```
2. Check security events in ledger
3. Identify root cause of incident
4. If safe to restart: `docker compose start`

### After Disconnect

1. Review logs for the connection that was dropped
2. Check what traffic was in-flight
3. Restart containers to restore connectivity

---

## Kill Switch Monitoring

`killswitch_monitor.py` polls the kill switch state every 5 seconds. If the kill switch is triggered from any source (API, dashboard, script), all agent processing stops within 5 seconds.

Monitor the kill switch state:
```bash
TOKEN=$(cat docker/secrets/gateway_password.txt)
curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/admin/kill-switch/status | jq .
```

---

## Related Notes

- [[Security Modules/killswitch_monitor.py|killswitch_monitor.py (TODO)]] — Kill switch implementation
- [[Shutdown & Recovery]] — Normal shutdown procedures
- [[Quick Reference]] — Kill switch quick commands
- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Post-incident investigation
