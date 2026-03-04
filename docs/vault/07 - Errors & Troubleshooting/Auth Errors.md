---
title: Auth Errors
type: troubleshooting
tags: [auth, errors, security]
related: [Gateway Core/auth.py, Errors & Troubleshooting/Error Index, Environment Variables/GATEWAY_AUTH_TOKEN]
status: documented
---

# Auth Errors

## HTTP 401 — Unauthorized

All 401 errors mean the `Authorization: Bearer <token>` header is missing or the token doesn't match the gateway's configured auth token.

### Diagnosis

```bash
# Test auth manually
curl -s -H "Authorization: Bearer <your-token>" http://localhost:8080/status
curl -s http://localhost:8080/status   # Should return 401
```

### Common Causes

| Cause | Symptom | Fix |
|-------|---------|-----|
| Token mismatch between bot and gateway | Bot gets 401 on every request | Regenerate; ensure same token in `docker/secrets/gateway_password.txt` |
| Missing `Authorization` header | `Authorization header missing` error | Check MCP proxy wrapper or client code |
| Wrong format | `Token format invalid` | Must be `Bearer <token>`, not just `<token>` |
| Gateway auto-generated a new token | Bot has old token | Restart both containers with same secret file |
| Secret file empty | Gateway generates random token | Echo token to file; don't leave it empty |

### Token Verification

```bash
# Check what token gateway loaded (from logs)
docker logs agentshroud-gateway | grep "auth_token\|Generated new token"

# If gateway generated a random token, it logs it:
# "No auth_token found. Generated new token: <token>"
# → copy this and save to docker/secrets/gateway_password.txt
```

### Token Reset

```bash
# 1. Generate new token
NEW_TOKEN=$(python3 -c "import secrets; print(secrets.token_hex(32))")
echo $NEW_TOKEN

# 2. Save to secret file
echo "$NEW_TOKEN" > docker/secrets/gateway_password.txt

# 3. Restart both containers
docker compose -f docker/docker-compose.yml restart
```

---

## 1Password Auth Failures

### `op read` Failing

**Symptom in logs:**
```
[startup] ✗ Claude OAuth token: all 6 attempts failed after 2 minutes
```

**Causes and fixes:**

| Cause | Fix |
|-------|-----|
| Service account token expired or revoked | Generate new token in 1Password; update `docker/secrets/1password_service_account` |
| Service account doesn't have vault access | Grant read access to `Agent Shroud Bot Credentials` vault |
| Wrong op:// path pattern | Path must match `op://Agent Shroud Bot Credentials/*/*` |
| Gateway not yet ready when bot starts | Normal — retry logic handles this (waits up to 2 minutes) |

---

## Related Notes

- [[Gateway Core/auth.py|auth.py]] — Authentication implementation
- [[Environment Variables/GATEWAY_AUTH_TOKEN]] — Auth token env var
- [[Environment Variables/OP_SERVICE_ACCOUNT_TOKEN]] — 1Password service account
- [[Errors & Troubleshooting/Error Index]] — Full error index
