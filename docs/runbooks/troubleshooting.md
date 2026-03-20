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

### Gateway: duplicate access log lines for every request

**Container:** `agentshroud-gateway`
**Severity:** Cosmetic — no action required

Every inbound request produces two log lines: one from our structured logger
(`2026-... | INFO | agentshroud.gateway.main | GET /status -> 200`) and one from
uvicorn's built-in access log (`INFO: 10.254.110.x:... - "GET /status HTTP/1.1" 200`).
Both represent the same request. This is expected — uvicorn's `--access-log` is on and
our middleware logs the same event. The duplication is harmless.

---

### `POST /api/alerts -> 404 (Nms)` *(resolved in v0.9.0)*

**Container:** `agentshroud-gateway`
**Severity:** Pre-fix: 404 noise. Post-fix: INFO log, no more 404.

The security scripts (`security-scan.sh`, `security-report.sh`, `security-entrypoint.sh`)
POST structured JSON payloads to `$GATEWAY_URL/api/alerts` after each scan run. Prior to
v0.9.0 this endpoint did not exist, producing silent 404s. The endpoint was added in v0.9.0
and now logs the alert and publishes it to the event bus.

**Normal post-fix output in gateway logs:**
```
[security-alert] type=security_alert severity=CRITICAL tool=clamav message=...
```

If you still see `POST /api/alerts -> 404` after upgrading, the gateway container image
has not been rebuilt. Run `docker compose build gateway && docker compose up -d gateway`.

---

### `[gateway] ⚠️ Gateway is binding to a non-loopback address`

**Container:** `agentshroud-bot`
**Severity:** Warning — no action required

This warning is emitted once at startup by OpenClaw when it binds its WebSocket server to
`0.0.0.0:18789` instead of `127.0.0.1`. OpenClaw is designed to be accessed remotely
(by the gateway container, SOC UI, etc.) so binding to all interfaces is intentional.
The gateway's Docker network restricts which containers can reach port 18789; it is not
exposed to the host network directly.

---

### `[WARN] bolt-app http request failed getaddrinfo ENOTFOUND gateway`

**Container:** `agentshroud-bot`
**Severity:** Warning — transient, self-resolving

**What it means:** The bot's Slack Bolt HTTP client tried to resolve the hostname `gateway`
(used as `SLACK_API_BASE_URL=http://gateway:8080/slack-api`) and Docker's embedded DNS
hadn't registered the gateway container yet. This typically appears within the first 5–10
seconds of a cold start before the Docker bridge network fully propagates hostname entries.

**Self-resolves:** Yes — the Bolt app retries and succeeds once DNS is available.

**When it IS a problem:** If the error persists beyond 30 seconds of bot runtime, the
gateway container may be down or on a different Docker network. Check:
```bash
docker exec agentshroud-bot nslookup gateway
docker compose ps
```

---

### `[WARN] bolt-app http request failed connect ECONNREFUSED 10.254.110.2:8181`

**Container:** `agentshroud-bot`
**Severity:** Warning — transient, self-resolving

**What it means:** The bot container's `HTTP_PROXY=http://gateway:8181` environment
variable points to the gateway's HTTP CONNECT proxy server (port 8181, separate from the
main API on port 8080). When the Slack Socket Mode client needs to reconnect and make an
outbound HTTPS call through the proxy, it briefly hits this error if the proxy server is
still initializing or momentarily unavailable.

The HTTP CONNECT proxy is an asyncio TCP server started during gateway lifespan startup.
It can be briefly unavailable during container restarts, causing the bot to get
ECONNREFUSED for a few retry cycles before connecting successfully.

**Self-resolves:** Yes — the Slack health monitor triggers a provider restart and the
connection succeeds once the proxy is ready. Look for `[slack] socket mode connected`
shortly after.

**When it IS a problem:** If ECONNREFUSED appears continuously (more than ~60 seconds
with no `socket mode connected` recovery):
```bash
# Verify HTTP CONNECT proxy is listening inside the gateway
docker exec agentshroud-gateway ss -tlnp | grep 8181
# If nothing: gateway failed to start the proxy — check gateway logs for startup errors
```

---

### `[ERROR] socket-mode:SocketModeClient:N Failed to retrieve a new WSS URL`

**Container:** `agentshroud-bot`
**Severity:** Error — transient, self-resolving

**What it means:** The Slack Socket Mode SDK called `apps.connections.open` to obtain
a new WebSocket URL but the request failed (typically because of the proxy being
temporarily unavailable — see ECONNREFUSED entry above). This error always appears
alongside the ECONNREFUSED warning.

**Self-resolves:** Yes — marked `Non-fatal unhandled rejection` by OpenClaw; the health
monitor restarts the Slack provider automatically. Look for `[slack] socket mode connected`.

---

### `[openclaw] Non-fatal unhandled rejection (continuing): Error: A request error occurred`

**Container:** `agentshroud-bot`
**Severity:** Error — non-fatal, logged by OpenClaw's global handler

OpenClaw wraps all unhandled promise rejections and re-emits them with this prefix when
they are classified as non-fatal. The full error (ECONNREFUSED or ENOTFOUND) is included.
No action required; the system continues operating.

---

### `[health-monitor] [slack:default] health-monitor: restarting (reason: stale-socket)`

**Container:** `agentshroud-bot`
**Severity:** Info — normal auto-recovery

**What it means:** OpenClaw's health monitor runs every 300 seconds and checks that the
Slack Socket Mode WebSocket is still alive. If the socket went stale (too many pong
timeouts without recovery), the monitor restarts the entire Slack provider. This is the
intended recovery path — it always ends with `[slack] socket mode connected`.

**Pattern in logs (normal):**
```
[health-monitor] [slack:default] health-monitor: restarting (reason: stale-socket)
[slack] [default] starting provider
[slack] socket mode connected
```

---

### `[telegram] autoSelectFamily=false (config)` / `fetch fallback: forcing autoSelectFamily=false + dnsResultOrder=ipv4first`

**Container:** `agentshroud-bot`
**Severity:** Info — intentional configuration

**What it means:** Node.js 22's default is to try IPv6 first (`autoSelectFamily=true`).
The bot is explicitly configured to prefer IPv4 (`dnsResultOrder=ipv4first`) because
Telegram's API and the Docker bridge network are IPv4. The `fetch fallback` line appears
once when the bot re-applies this setting after detecting a DNS policy change (typically
after a network reconnect event).

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

### `[agent/embedded] embedded run agent end: isError=true error=Ollama API stream ended without a final response`

**Container:** `agentshroud-bot`
**Severity:** Error — non-fatal, agent request failed

**What it means:** The local Ollama model (e.g. `qwen3:14b`) started streaming a response
but the stream terminated before producing a complete final message. This typically occurs
when the model runs out of context window, the host machine is under heavy memory pressure,
or Ollama's process was briefly interrupted.

The bot catches this error, logs it, and returns an error response to the user. The bot
itself remains operational; subsequent messages will be processed normally.

**Diagnosis:**
```bash
# Check Ollama host for errors
# (Ollama runs on the host, not in Docker)
journalctl -u ollama --since "5 minutes ago"

# Check host memory
free -h
```

**Fixes:**
- Memory pressure → reduce `--memory` in Colima / close other applications
- Model too large for context → switch to a smaller model via `/switch_model`
- Persistent → restart Ollama service on the host

---

### ClamAV: `WARNING: Can't query current.cvd.clamav.net` / `ERROR: Database update process failed`

**Container:** `agentshroud-clamav`
**Severity:** Warning/Error — startup-only, non-fatal

**What it means:** On startup, `freshclam` (ClamAV's virus database updater) immediately
attempts to download the latest signature database from `database.clamav.net`. The VPN
(Cisco AnyConnect) or the container network isn't ready for external DNS/HTTP at that
exact moment. After a few retries freshclam gives up and logs:
```
ERROR: Update failed for database: daily
ERROR: Database update process failed: HTTP GET failed
```

**This is harmless** — `clamd` starts regardless and uses whatever virus signatures were
bundled in the container image (or previously downloaded). `freshclam` will retry its
scheduled update later (every 12 hours by default).

**Confirm ClamAV is healthy despite the startup errors:**
```bash
docker exec agentshroud-clamav clamdscan --version
docker logs agentshroud-clamav | grep "socket found, clamd started"
```

**When it IS a problem:** If `clamd` never starts (no `socket found, clamd started` line
after retry counter reaches ~74), or `docker inspect agentshroud-clamav` shows unhealthy.

---

### ClamAV: `Socket for clamd not found yet, retrying (N/1800)...`

**Container:** `agentshroud-clamav`
**Severity:** Info — normal startup sequencing

**What it means:** The ClamAV entrypoint script starts `freshclam` and `clamd` in
parallel, then waits for `clamd`'s UNIX socket to appear before declaring itself ready.
The retry counter increments once per second. ClamAV typically takes 60–90 seconds to
load its full signature database. Retries up to ~100 are completely normal.

**Only investigate if** the counter reaches 200+ with no `socket found, clamd started`
line. In that case check `docker logs agentshroud-clamav` for `clamd` startup errors.

---

### ClamAV: `SelfCheck: Database status OK.`

**Container:** `agentshroud-clamav`
**Severity:** Info — periodic health confirmation

`clamd` runs a self-check every 600 seconds (10 minutes) and logs this line when its
in-memory signature database is intact. This line appearing every 10 minutes confirms
ClamAV is healthy and actively scanning. No action required.

---

### Gateway: `CONNECT tunnel established: wss-primary.slack.com:443`

**Container:** `agentshroud-gateway`
**Severity:** Info — normal operation

The gateway's HTTP CONNECT proxy (port 8181) approved an outbound WebSocket tunnel from
the bot to Slack's WebSocket endpoint. This line appears each time the Slack Socket Mode
connection is established or re-established. It confirms the proxy allowlist is correctly
permitting `wss-primary.slack.com`.

---

### Gateway: `GET /status -> 200 (0.000s)` every 30 seconds

**Container:** `agentshroud-gateway`
**Severity:** Info — Docker healthcheck

Docker's `HEALTHCHECK` directive polls `GET /status` every 30 seconds from inside the
container (`127.0.0.1`). These are expected and confirm the gateway is alive.

---

### Gateway: `POST /telegram-api/bot***/getUpdates -> 200 (30–32s)`

**Container:** `agentshroud-gateway`
**Severity:** Info — normal Telegram long-polling

The bot uses Telegram's long-poll method: it sends a `getUpdates` request that the
gateway holds open for up to 30 seconds, returning immediately when a message arrives or
timing out at ~30 s. The `***/` in the log replaces the bot token for security. Response
times of 30–32 s with no incoming messages are normal. Sub-second response times mean
a message arrived.

---

## Getting Help

1. Check this runbook first
2. Review gateway logs: `docker logs agentshroud-gateway`
3. Review audit ledger: `tail data/audit_ledger.jsonl`
4. Check GitHub issues: `gh issue list`
5. Run test suite to verify system integrity
