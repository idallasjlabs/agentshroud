---
title: "Error: Gateway Startup Failure"
type: error
tags: [#type/error, #status/critical]
severity: fatal
related: ["[[lifespan]]", "[[config]]", "[[sanitizer]]", "[[agentshroud-gateway]]", "[[Startup Sequence]]"]
status: active
last_reviewed: 2026-03-09
---

# Error: Gateway Startup Failure

## Symptoms

- `docker compose ps` shows `agentshroud-gateway` exiting or restarting
- `agentshroud-bot` never starts (depends_on: gateway healthy)
- `curl http://localhost:8080/status` → connection refused

## Diagnostic Flow

```bash
# Always start here
docker logs agentshroud-gateway --tail 100
```

Match the log output to the cause below.

---

## Cause 1: Configuration File Missing

```
FileNotFoundError: No agentshroud.yaml found. Searched: ./agentshroud.yaml, ...
```

**Fix:**
```bash
# Verify the volume mount
docker inspect agentshroud-gateway --format '{{json .Mounts}}' | python3 -m json.tool | grep agentshroud.yaml

# Verify the file exists on host
ls -la agentshroud.yaml

# Verify YAML is valid
python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))" && echo OK
```

---

## Cause 2: YAML Malformed or Invalid RouterConfig

```
ValueError: default_url host must be localhost, 127.0.0.1, or a Docker service name
```

**Fix:** Check `agentshroud.yaml` `bots:` section. Bot `hostname` must be a single-label Docker service name (no dots). If `bots:` section references an external hostname, RouterConfig validation rejects it.

---

## Cause 3: PII Sanitizer Init Failure (spaCy)

```
CRITICAL: Failed to initialize PII sanitizer: ...
```

Usually means the spaCy English model is missing.

**Fix:** Rebuild the gateway image:
```bash
docker compose -f docker/docker-compose.yml build gateway --no-cache
```

---

## Cause 4: Data Ledger Init Failure

```
CRITICAL: Failed to initialize data ledger: ...
```

**Fix:**
```bash
# Check volume exists
docker volume inspect agentshroud_gateway-data

# Create if missing
docker volume create agentshroud_gateway-data

# Check permissions
docker run --rm -v agentshroud_gateway-data:/data python:3.13-slim ls -la /data
```

---

## Cause 5: Approval Queue Init Failure

```
CRITICAL: Failed to initialize approval queue: ...
```

Often: missing or invalid Telegram bot token.

**Fix:**
```bash
# Check token file
cat docker/secrets/telegram_bot_token_production.txt

# Validate token format (should be: numbers:string)
# Test token with Telegram API
curl "https://api.telegram.org/bot$(cat docker/secrets/telegram_bot_token_production.txt)/getMe"
```

---

## Cause 6: Port 8080 Already In Use

```
OSError: [Errno 98] Address already in use
```

**Fix:**
```bash
# Find what's using 8080
lsof -i :8080
# Kill it or change the port mapping in docker-compose.yml
```

---

## Cause 7: Read-only Filesystem Error

```
PermissionError: [Errno 30] Read-only file system: '/app/...'
```

The gateway tries to write to a path not covered by a writable volume or tmpfs.

**Fix:** Check the path in the error. Add a tmpfs or volume mount for that path in docker-compose.yml.

---

## After Fixing

```bash
docker compose -f docker/docker-compose.yml up -d
curl http://localhost:8080/status
docker logs agentshroud-gateway | grep "Gateway ready"
```
