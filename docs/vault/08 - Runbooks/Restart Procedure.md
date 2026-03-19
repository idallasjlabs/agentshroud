---
title: Restart Procedure
type: runbook
tags: [operations, restart, runbook]
related: [Startup Sequence, Shutdown & Recovery, Quick Reference]
status: documented
---

# Restart Procedure

## When to Restart

| Situation | Restart Scope |
|-----------|--------------|
| Config change in `agentshroud.yaml` | Gateway only |
| Bot behavior issue | Bot only |
| Secret file rotated | Both containers |
| Image rebuild completed | Both containers |
| System-wide issue | Full stack |

---

## Full Stack Restart

```bash
cd agentshroud

# Graceful stop (15s grace period per container)
docker compose -f docker/docker-compose.yml stop

# Start (bot waits for gateway to be healthy)
docker compose -f docker/docker-compose.yml start

# Or combined
docker compose -f docker/docker-compose.yml restart
```

**Expected time:** ~60-90 seconds for both containers to be healthy.

---

## Gateway Only Restart

```bash
# Safe to restart gateway without stopping bot
# Bot will queue requests and retry when gateway comes back
docker compose -f docker/docker-compose.yml restart agentshroud-gateway

# Watch gateway come back online
docker logs -f agentshroud-gateway
# Wait for: "Application startup complete."
```

**Impact:** During gateway restart (~15-30s), the bot's requests will fail with connection errors. The bot's retry logic handles this.

---

## Bot Only Restart

```bash
docker compose -f docker/docker-compose.yml restart agentshroud-bot

# Bot will re-run start-agentshroud.sh:
# - Re-read gateway password secret
# - Re-fetch 1Password secrets (with retry logic)
# - Re-apply OpenClaw config patches
# - Re-start OpenClaw agent
```

**Expected time:** ~60s for bot to be healthy (includes 1Password secret loading with retries).

---

## After Config Change

```bash
# 1. Edit config
vim agentshroud.yaml

# 2. Validate YAML
python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))" && echo "YAML OK"

# 3. Restart gateway only (config is read at startup)
docker compose -f docker/docker-compose.yml restart agentshroud-gateway

# 4. Verify config loaded
docker logs agentshroud-gateway | grep "Configuration loaded"
```

---

## After Secret Rotation

```bash
# 1. Update secret file
echo "new-token-value" > docker/secrets/gateway_password.txt

# 2. Restart BOTH containers (both need the new token)
docker compose -f docker/docker-compose.yml restart
```

---

## Zero-Downtime Restart (Advanced)

For minimum disruption, restart containers sequentially:

```bash
# 1. Restart gateway (bot continues queuing)
docker compose -f docker/docker-compose.yml restart agentshroud-gateway

# 2. Wait for gateway to be healthy
until curl -sf http://localhost:8080/status > /dev/null; do
    echo "Waiting for gateway..."
    sleep 5
done
echo "Gateway healthy"

# 3. Restart bot (gateway is ready)
docker compose -f docker/docker-compose.yml restart agentshroud-bot
```

---

## Restart Verification

After any restart:

```bash
# 1. Container status
docker compose -f docker/docker-compose.yml ps

# 2. Gateway health
curl -s http://localhost:8080/status | jq .status

# 3. Check bot reconnected to gateway
docker logs --tail=20 agentshroud-bot | grep "\[startup\]"

# 4. Check Telegram notification (if bot restarted)
# Look for: "🛡️ AgentShroud online"
```

---

## Related Notes

- [[Startup Sequence]] — What happens during startup
- [[Shutdown & Recovery]] — Shutdown procedures
- [[Runbooks/Crash Recovery]] — When a restart isn't enough
- [[Quick Reference]] — Quick commands
