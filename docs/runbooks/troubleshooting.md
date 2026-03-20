# Troubleshooting Runbook — AgentShroud

> Last updated: 2026-03-20

## Common Issues

### Bot Not Responding to Telegram Messages

**Symptoms:** Messages sent to bot get no reply.

**Check:**
```bash
# 1. Is the gateway running?
docker compose ps

# 2. Check gateway logs for errors
docker logs --tail 50 agentshroud-gateway

# 3. Is the Telegram webhook active?
curl -s "https://api.telegram.org/bot<TOKEN>/getWebhookInfo" | python3 -m json.tool

# 4. Network connectivity
curl -s https://api.telegram.org/bot<TOKEN>/getMe
```

**Fixes:**
- Container down → `docker compose up -d`
- Webhook misconfigured → Re-register webhook
- Token invalid → Rotate via BotFather, update Docker Secret
- Network issue → Check Tailscale, DNS resolution

---

### Tailscale Serve Not Working

**Symptoms:** HTTPS URLs return connection refused.

**Check:**
```bash
# Is Tailscale running?
tailscale status

# Are serves configured?
tailscale serve status

# Are local ports listening?
ss -tlnp | grep -E '(8080|18790|8050)'
```

**Fixes:**
- Serves not configured → `sudo ./scripts/tailscale-serve.sh start`
- Local port not listening → Restart the relevant container
- Tailscale down → `sudo tailscale up`
- Certificate issue → Tailscale auto-manages certs; wait 1–2 minutes

---

### PII Sanitizer Blocking Legitimate Content

**Symptoms:** Bot strips parts of messages that aren't actually PII.

**Check:**
```bash
# Review recent sanitization events in audit ledger
grep '"event_type": "pii_sanitized"' data/audit_ledger.jsonl | tail -10
```

**Fixes:**
- False positive on specific pattern → Review and adjust regex patterns in sanitizer config
- Too aggressive → Check sanitizer sensitivity settings
- Test with: run sanitizer unit tests to verify behavior

---

### Kill Switch Won't Deactivate

**Symptoms:** Bot stuck in frozen/shutdown state after kill switch.

**Check:**
```bash
# Check kill switch state
grep '"event_type": "kill_switch"' data/audit_ledger.jsonl | tail -5
```

**Fixes:**
- Freeze mode → Send `/kill unfreeze` via Telegram
- Shutdown mode → `docker compose up -d`
- Disconnect mode → Restore network, rotate credentials, `docker compose up -d`
- State file corrupted → Check/remove kill switch state file, restart

---

### Container Keeps Restarting

**Symptoms:** `docker compose ps` shows container restarting.

**Check:**
```bash
# Check exit code
docker inspect agentshroud-gateway --format='{{.State.ExitCode}}'

# Check last logs before crash
docker logs --tail 100 agentshroud-gateway

# Check resource usage
docker stats --no-stream
```

**Fixes:**
- Exit code 137 (OOM) → Increase memory limit in docker-compose.yml
- Exit code 1 (app error) → Check logs, fix code, redeploy
- Missing secret → Verify Docker Secrets are mounted
- Port conflict → Check if another process uses the port

---

### Tests Failing

**Symptoms:** `pytest` shows failures after changes.

**Check:**
```bash
# Run with verbose output
~/miniforge3/envs/agentshroud/bin/python -m pytest gateway/tests/ -v --tb=long

# Run specific failing test
~/miniforge3/envs/agentshroud/bin/python -m pytest gateway/tests/test_specific.py::test_name -v
```

**Fixes:**
- Import error → Check conda env is activated, deps installed
- Test data changed → Update test fixtures
- Config change → Update test config to match
- **Never deploy with failing tests**

---

### Dashboard Not Loading

**Symptoms:** Dashboard URL returns error or blank page.

**Check:**
```bash
# Is dashboard container running?
docker compose ps

# Can you reach it locally?
curl -s http://localhost:8050/

# Check dashboard logs
docker logs agentshroud-dashboard --tail 50
```

**Fixes:**
- Container down → `docker compose up -d`
- Port not exposed → Check docker-compose.yml port mapping
- Static files missing → Rebuild container

---

### SSH Command Approval Stuck

**Symptoms:** SSH commands submitted but never approved/denied.

**Check:**
```bash
# Check approval queue
grep '"event_type": "approval"' data/audit_ledger.jsonl | tail -10
```

**Fixes:**
- Approver not online → Commands timeout after configured period
- Notification not sent → Check Telegram delivery in logs
- Queue full → Review and clear stale requests

---

## Diagnostic Commands

```bash
# Full system status
docker compose ps
./scripts/tailscale-check.sh
df -h
free -m

# Recent security events
tail -20 data/audit_ledger.jsonl | python3 -m json.tool

# Network connectivity
tailscale ping raspberrypi
curl -s http://localhost:8080/health

# Process check
ps aux | grep -E '(python|docker|tailscale)'
```

---

## Known Log Messages

This section documents log lines that appear during normal operation and are safe to
ignore, along with messages that indicate real problems requiring action. Use this as
a reference before escalating any log output.

---

### `[WARN] socket-mode:SlackWebSocket:N A pong wasn't received from the server before the timeout of 5000ms!`

**Container:** `agentshroud-bot`
**Severity:** Warning — no action required
**Frequency:** Occasional bursts, especially after VPN reconnects

**What it means:**

Slack's Socket Mode connection uses WebSocket keep-alive frames. Every ~30 seconds Slack
sends a `ping` frame and expects a `pong` back within 5 000 ms. When the network is briefly
interrupted (e.g., VPN route flap, DNS hiccup, brief packet loss) the pong doesn't arrive
in time and the `@slack/socket-mode` SDK logs this warning.

The SDK automatically closes the stale connection and opens a new one. The connection
number in the log (`SlackWebSocket:42`, `SlackWebSocket:43`, …) increments with each
reconnect — this is expected. Consecutive warnings at ~1.6 s intervals on the same
connection number indicate the SDK firing rapid-retry pings during the reconnect
handshake; once the new WebSocket is established they stop.

**How to confirm it's harmless:**
- Look for `sendMessage ok` entries in the surrounding log context — if messages are
  flowing then the integration is healthy.
- Confirm the connection number eventually stabilizes or increments (reconnect succeeded).
- Check `docker logs agentshroud-bot | grep "sendMessage ok"` — should have recent entries.

**When it IS a problem:**
- If the warnings never stop and the connection number keeps climbing rapidly without
  stabilizing, the bot cannot reach Slack's WebSocket endpoint at all.
- Check outbound internet access from the bot container:
  ```bash
  docker exec agentshroud-bot curl -s https://slack.com/api/api.test
  ```
- If that fails, check the `agentshroud-external` Docker network and the gateway's egress
  allowlist — `slack.com` must be in the permanent egress allowlist.

---

## Getting Help

1. Check this runbook first
2. Review gateway logs: `docker logs agentshroud-gateway`
3. Review audit ledger: `tail data/audit_ledger.jsonl`
4. Check GitHub issues: `gh issue list`
5. Run test suite to verify system integrity
