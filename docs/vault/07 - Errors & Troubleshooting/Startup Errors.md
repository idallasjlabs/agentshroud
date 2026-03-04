---
title: Startup Errors
type: troubleshooting
tags: [startup, errors, troubleshooting]
related: [Errors & Troubleshooting/Error Index, Startup Sequence, Runbooks/First Time Setup]
status: documented
---

# Startup Errors

## Gateway Container Startup Failures

### `FileNotFoundError: No agentshroud.yaml found`

**When:** Gateway exits immediately after starting

**Diagnosis:**
```bash
docker logs agentshroud-gateway | head -20
```

**Causes and fixes:**

| Cause | Fix |
|-------|-----|
| Volume mount missing in docker-compose.yml | Verify `../agentshroud.yaml:/app/agentshroud.yaml:ro` is in volumes |
| Running from wrong directory | Run `docker compose` from the `docker/` directory |
| Config file doesn't exist | Create `agentshroud.yaml` from template |
| `$AGENTSHROUD_CONFIG` points to non-existent file | Fix the path |

---

### `ValueError: Invalid YAML structure`

**When:** Gateway exits during config load

**Diagnosis:**
```bash
python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))"
```

**Causes:** YAML syntax error in `agentshroud.yaml`. Common mistakes:
- Unquoted strings with special characters
- Inconsistent indentation
- Missing colon after key
- Tabs instead of spaces

---

### Gateway Health Check Never Passes

**When:** Bot container stays unhealthy; gateway container shows "unhealthy"

**Diagnosis:**
```bash
# Check if gateway is listening
curl -v http://localhost:8080/status

# Check container logs for errors
docker logs agentshroud-gateway 2>&1 | grep -i "error\|exception\|traceback"
```

**Common causes:**

| Symptom in logs | Fix |
|----------------|-----|
| `spaCy model download failed` | Rebuild image with internet access |
| `Address already in use :8080` | Kill existing process on port 8080 |
| `ModuleNotFoundError` | Python package missing; rebuild gateway image |
| `Pydantic ValidationError` | Invalid value in `agentshroud.yaml` — fix the invalid field |

---

### `No auth_token found in secret file`

**When:** Gateway generates a random token (logs a warning with the token)

**Impact:** Gateway works, but the random token is different from what the bot expects.

**Fix:**
```bash
# Create the secret file
echo "$(python3 -c "import secrets; print(secrets.token_hex(32))")" > docker/secrets/gateway_password.txt

# Restart both containers
docker compose restart
```

---

### spaCy Model Not Loading

**When:** First request fails with `PII engine not initialized`

**Diagnosis:**
```bash
docker logs agentshroud-gateway | grep -i spacy
```

**Causes:**
1. Model not downloaded at build time → uses regex fallback (still works)
2. Model file corrupted → rebuild image

**Fix for corrupted model:**
```bash
docker compose build --no-cache agentshroud-gateway
docker compose up -d
```

---

## Bot Container Startup Failures

### Bot Exits Before Gateway Is Healthy

**Symptom:** Bot logs show it exiting; `depends_on: condition: service_healthy` should prevent this

**Fix:** Verify the `depends_on` section in `docker-compose.yml` is correct:
```yaml
depends_on:
  gateway:
    condition: service_healthy
```

---

### `[startup] Warning: Gateway password file not found`

**Cause:** `/run/secrets/gateway_password` doesn't exist in the bot container

**Fix:** Verify the `gateway_password` secret is defined and the file exists:
```bash
ls docker/secrets/gateway_password.txt
```

---

### `Could not load Claude OAuth token after retries`

**Cause:** Gateway op-proxy unreachable, or 1Password service account token invalid

**Impact:** Claude OAuth token not loaded; LLM calls may fail

**Fix:**
1. Check gateway is healthy: `curl http://localhost:8080/status`
2. Verify `docker/secrets/1password_service_account` has a valid token
3. Check gateway logs for 1Password errors

---

### OpenClaw Not Starting

**Symptoms:** `docker logs agentshroud-bot` shows OpenClaw errors

**Common causes:**
- `agentshroud-config` volume is corrupt → stop containers, remove volume, restart
- Node.js exception → check logs for stack trace

---

## Related Notes

- [[Startup Sequence]] — Normal startup flow
- [[Errors & Troubleshooting/Container Errors]] — Container-level errors
- [[Runbooks/First Time Setup]] — Initial setup requirements
- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Full diagnostic matrix
