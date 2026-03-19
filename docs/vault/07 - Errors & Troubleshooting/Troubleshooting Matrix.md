---
title: Troubleshooting Matrix
type: reference
tags: [troubleshooting, operations, debugging]
related: [Errors & Troubleshooting/Error Index, Runbooks/Crash Recovery, Quick Reference]
status: documented
---

# Troubleshooting Matrix

## Quick Diagnosis Flow

```
Something is wrong →
  1. Check container status: docker compose ps
  2. Check logs: docker logs --tail=100 agentshroud-gateway
  3. Check health: curl -s http://localhost:8080/health | jq .
  4. Find symptom below → follow fix
```

---

## Connectivity Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Bot can't reach gateway (502/connection refused) | Gateway container not running | `docker compose up -d agentshroud-gateway` |
| Bot getting 401 | Token mismatch between containers | Verify `docker/secrets/gateway_password.txt` is identical for both |
| LLM calls failing | `ANTHROPIC_BASE_URL` not set or wrong | Check env: `docker compose config \| grep ANTHROPIC_BASE_URL` |
| Telegram messages not delivering | `TELEGRAM_API_BASE_URL` wrong or bot token wrong | Check secrets and env vars |
| iOS Shortcuts can't reach gateway | Tailscale not connected or `shortcuts.endpoint` not set | Set `shortcuts.endpoint` in `agentshroud.yaml` |

---

## PII / Sanitization Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Legitimate content being redacted | `pii_min_confidence` too low | Raise to 0.95 in `agentshroud.yaml` |
| PII getting through | `pii_min_confidence` too high OR wrong entity type | Lower confidence or add entity type to `redaction_rules` |
| 500 error on first request | spaCy model not loaded yet | Wait 10-30s after startup; check logs for "spaCy model loaded" |
| `AGENTSHROUD_MODE=monitor` but PII still getting blocked | Per-module config overriding | Verify env var is set in the running container |

---

## Egress / Network Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "Egress blocked" for legitimate domain | Domain not in allowlist | Add to `proxy.allowed_domains` in `agentshroud.yaml` and restart |
| Wildcard domains not matching | Missing `*` prefix or wrong format | Use `"*.domain.com"` format (with quotes in YAML) |
| RFC1918 blocked | Trying to reach private network | Design intent — use approved host paths |
| MCP server unreachable | MCP server URL not allowed | Add MCP server's domain to `proxy.allowed_domains` |

---

## Approval Queue Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Actions stuck as "pending" | Dashboard not being monitored | Access dashboard at `:18790` and approve/deny |
| Approval queue full / backlog | High-volume operations | Increase `timeout_seconds` or add bulk approval |
| Approval not persisting after restart | Queue store not flushing | Check `approval_queue/store.py` logs |
| Approval queue empty but bot blocked | Wrong action type in config | Verify `require_approval_for` list in `agentshroud.yaml` |

---

## Prompt Injection Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Legitimate prompts blocked as injections | Pattern too aggressive | Check `prompt_guard.py` threshold; switch to `monitor` mode temporarily to identify false positives |
| Prompt injections getting through | Pattern DB out of date | Check gateway version; update image |
| Tool results being blocked | Tool result contains suspicious patterns | Review specific patterns in logs; may be legitimate content |

---

## Container Stability Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Gateway OOM killed (exit 137) | Memory limit too low | Increase `mem_limit` in `docker-compose.yml` (try 2560m) |
| Bot OOM killed | High memory workload (Playwright, large files) | Increase bot `mem_limit` (already 4GB); reduce concurrency |
| Container restarts in loop | Config error or dependency missing | Check logs for error before exit; `docker logs agentshroud-gateway \| head -50` |
| `read-only file system` errors | Code writing to non-tmpfs/non-volume path | Mount a volume or tmpfs at that path |
| PID limit exceeded | Too many subprocess spawns | Increase `pids_limit` or investigate subprocess leak |

---

## Startup Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Gateway exits immediately | Missing `agentshroud.yaml` or YAML parse error | Mount config; validate YAML with `python3 -c "import yaml; yaml.safe_load(open('agentshroud.yaml'))"` |
| Bot starts before gateway is healthy | Depends_on not respected | Ensure using `condition: service_healthy` (already set) |
| spaCy download fails at startup | Model not in image (using slim image?) | Re-run `python3 -m spacy download en_core_web_sm` or rebuild image |
| "Generated new token" warning | No auth token configured | Set token in `gateway_password.txt` secret |
| 1Password secrets not loading | Service account invalid or op-proxy unreachable | Check `OP_SERVICE_ACCOUNT_TOKEN_FILE` and gateway connectivity |

---

## Security Module Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Module in monitor mode unexpectedly | `AGENTSHROUD_MODE=monitor` set | `unset AGENTSHROUD_MODE` and restart |
| All modules in monitor mode | Global monitor override active | Check env var in container: `docker exec agentshroud-gateway env \| grep AGENTSHROUD_MODE` |
| Kill switch triggered unintentionally | Kill switch endpoint hit by accident | Restart via `docker compose start` |

---

## Debugging Commands

```bash
# Check container health status
docker compose -f docker/docker-compose.yml ps

# Stream logs with timestamps
docker logs -f --timestamps agentshroud-gateway

# Inspect gateway environment
docker exec agentshroud-gateway env | sort

# Test gateway auth manually
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/status | jq .

# Check PII sanitizer status
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/health | jq .components.pii_sanitizer

# Check approval queue
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  http://localhost:8080/admin/approvals | jq .

# Check ledger count
curl -s -H "Authorization: Bearer $(cat docker/secrets/gateway_password.txt)" \
  "http://localhost:8080/ledger?limit=5" | jq .total
```

---

## Related Notes

- [[Errors & Troubleshooting/Error Index]] — Error code reference
- [[Errors & Troubleshooting/Startup Errors]] — Startup-specific diagnosis
- [[Runbooks/Crash Recovery]] — When the gateway crashes
- [[Runbooks/Health Checks]] — Systematic health verification
- [[Quick Reference]] — Quick fix commands
