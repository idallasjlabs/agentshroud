---
title: Troubleshooting Matrix
type: index
tags: [#type/index, #type/error]
related: ["[[Error Index]]", "[[Photo Download Failure]]", "[[Gateway Startup Failure]]", "[[Health Checks]]"]
status: active
last_reviewed: 2026-03-09
---

# Troubleshooting Matrix

> [!BUG] Symptom: "Failed to download media" when sending photos to bot
> **Likely cause:** OpenClaw dist file download URL not patched to go through gateway
> **Check:** `docker exec agentshroud-bot grep -c "TELEGRAM_API_BASE_URL" /usr/local/lib/node_modules/openclaw/dist/pi-embedded-CtM2Mrrj.js` — should be > 0
> **Diagnostic:** `docker logs agentshroud-bot --since 5m | grep -i timeout`
> **Fix:** `docker compose -f docker/docker-compose.yml build bot --no-cache && docker compose up -d bot`
> **Detail:** [[Photo Download Failure]]

> [!BUG] Symptom: Bot container never starts (waiting on gateway health)
> **Likely cause:** Gateway startup failure
> **Check:** `docker compose -f docker/docker-compose.yml ps`
> **Diagnostic:** `docker logs agentshroud-gateway --tail 100`
> **Fix:** See [[Gateway Startup Failure]] for cause-specific remediation

> [!BUG] Symptom: Gateway starts but Telegram long-poll not working
> **Likely cause:** Invalid bot token or Telegram API unreachable
> **Check:** `docker logs agentshroud-gateway | grep -i telegram | tail -10`
> **Diagnostic:** `curl "https://api.telegram.org/bot$(cat docker/secrets/telegram_bot_token_production.txt)/getMe"`
> **Fix:** Replace token in `docker/secrets/telegram_bot_token_production.txt`, restart gateway

> [!BUG] Symptom: 401 Unauthorized on all bot → gateway calls
> **Likely cause:** Gateway password mismatch
> **Check:** `cat docker/secrets/gateway_password.txt` — must be same on both containers
> **Fix:** Regenerate password, update secret file, restart both containers

> [!BUG] Symptom: Messages blocked that shouldn't be (false positive injection detection)
> **Likely cause:** PromptGuard pattern too aggressive, or legitimate text scoring high
> **Diagnostic:** `docker logs agentshroud-gateway | grep -i "blocked\|injection\|prompt"  | tail -20`
> **Quick test:** Set `AGENTSHROUD_MODE=monitor` in gateway env → restart → retry message
> **Fix:** Review and tune patterns in [[prompt_guard]], or adjust thresholds in config

> [!BUG] Symptom: Collaborator can't use the bot at all
> **Likely cause:** Rate limit hit (200 msg/hr) or not in collaborator list
> **Check:** `docker logs agentshroud-gateway | grep -i "rate limit\|collaborator" | tail -20`
> **Fix:** Check `RBACConfig` collaborator_user_ids; rate limit resets hourly

> [!BUG] Symptom: LLM responses appear truncated or missing content
> **Likely cause:** OutboundInfoFilter or PromptProtection is redacting/blocking
> **Check:** `docker logs agentshroud-gateway | grep -i "outbound\|block\|redact" | tail -20`
> **Fix:** Enable monitor mode temporarily to diagnose; review [[pipeline]] outbound step config

> [!BUG] Symptom: Gateway OOM killed (exit code 137)
> **Likely cause:** 1280MB memory limit exceeded, usually during PII scan of large documents
> **Check:** `docker inspect agentshroud-gateway --format '{{.State.OOMKilled}}'`
> **Fix:** Increase `mem_limit` in docker-compose.yml gateway service (or split large documents)

> [!BUG] Symptom: SSH proxy calls fail ("host not found")
> **Likely cause:** `extra_hosts` IP is stale (home lab IP changed)
> **Check:** `docker exec agentshroud-gateway ping marvin`
> **Fix:** Update IP in `docker-compose.yml extra_hosts` + `agentshroud.yaml ssh.hosts[*].host`

> [!BUG] Symptom: `AuditChain integrity failure detected` in logs
> **Likelihood:** Extremely rare; indicates potential tampering
> **Severity:** CRITICAL — investigate immediately
> **Check:** `docker exec agentshroud-gateway sqlite3 /app/data/audit.db "SELECT count(*) FROM audit_entries;"`
> **Action:** Stop gateway, preserve audit DB snapshot, investigate all BLOCK events since last known-good state

> [!BUG] Symptom: Colima container starts but no internet from gateway
> **Likely cause:** VPN (Cisco AnyConnect) blocking col0 vmnet route
> **Check:** `colima ssh -- ip route show | grep col0`
> **Fix:** `colima ssh -- sudo ip route change 192.168.64.0/24 dev col0 metric 100`
> **Detail:** See [[Architecture Overview]] Colima VPN networking section
