---
title: Error Index
type: index
tags: [#type/index, #type/error]
related: ["[[Troubleshooting Matrix]]", "[[Photo Download Failure]]", "[[Gateway Startup Failure]]", "[[Bot Isolation Error]]"]
status: active
last_reviewed: 2026-03-09
---

# Error Index

## Startup Errors

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| `FileNotFoundError: No agentshroud.yaml found` | Fatal | Config file missing or wrong mount | [[config]] | Check volume mount in docker-compose.yml | [[Gateway Startup Failure]] |
| `Failed to initialize PII sanitizer` | Fatal | spaCy model not downloaded | [[sanitizer]] | Rebuild image | [[Gateway Startup Failure]] |
| `Failed to initialize data ledger` | Fatal | gateway-data volume not mounted | [[lifespan]] | Check `docker volume inspect agentshroud_gateway-data` | [[Gateway Startup Failure]] |
| `Failed to initialize approval queue` | Fatal | SQLite error or token missing | [[lifespan]] | Check TELEGRAM_BOT_TOKEN secret | [[Gateway Startup Failure]] |
| `Failed to load configuration: ValueError` | Fatal | YAML malformed or bad URL in RouterConfig | [[config]] | Validate YAML syntax | [[Gateway Startup Failure]] |
| `WARNING: grammY SDK not found` | Warning | OpenClaw version changed SDK path | [[patch-telegram-sdk.sh]] | Rebuild bot image | — |
| `ENOENT mkdir collaborator-workspace` | Error | Old apply-patches.js workspace path | [[apply-patches.js]] | Rebuild bot image | [[agentshroud-bot]] |

## Runtime Errors

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| "Failed to download media" | High | File download URL not patched through gateway | [[patch-telegram-sdk.sh]] | Rebuild bot image | [[Photo Download Failure]] |
| `403 Forbidden` on `/v1/` | High | Bot IP not in PROXY_ALLOWED_NETWORKS | [[main]] | Check `PROXY_ALLOWED_NETWORKS` env var | — |
| `401 Unauthorized` on all calls | High | Wrong or missing gateway password | [[agentshroud-gateway]] | Check `docker/secrets/gateway_password.txt` | — |
| `AuditChain integrity failure` | Critical | Hash chain tampered | [[pipeline]] | Check audit DB, investigate manually | — |
| `CRITICAL: AuditChain integrity failure detected` | Critical | Tampered audit log | [[pipeline]] | Immediate investigation required | — |

## Connection / Network Errors

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| `Error: The operation was aborted due to timeout` (Node.js fetch) | High | Bot trying to reach internet directly | [[agentshroud-bot]] | Verify `HTTP_PROXY` set; check patch applied | [[Bot Isolation Error]] |
| `getUpdates` returns error | High | Telegram token invalid | [[telegram_proxy]] | Check token file | — |
| Gateway healthcheck fails | Medium | Port 8080 not responding | [[agentshroud-gateway]] | `docker logs agentshroud-gateway --tail 50` | [[Gateway Startup Failure]] |

## Auth / Permission Errors

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| `op://` reference rejected | High | Reference not in `_ALLOWED_OP_PATHS` | [[main]] | Check allowed paths | — |
| Collaborator blocked command | Low | Expected behavior | [[telegram_proxy]] | Not an error — collaborators can't use `/exec` etc. | — |

## Data / Validation Errors

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| Presidio language warnings | Low | es/it/pl recognizers skipped | [[sanitizer]] | Benign — English only configured | — |
| PII over-redaction | Medium | `pii_min_confidence` too low | [[sanitizer]] | Raise `pii_min_confidence` in agentshroud.yaml | — |
| Prompt injection false positive | Medium | Pattern too aggressive | [[prompt_guard]] | Temporarily set `AGENTSHROUD_MODE=monitor` to debug | — |

## Resource Exhaustion

| Error | Severity | Cause | Module | First Step | Detail |
|-------|----------|-------|--------|-----------|--------|
| Bot OOM killed | High | 4GB mem_limit exceeded | [[agentshroud-bot]] | `docker stats agentshroud-bot`, reduce Playwright concurrency | — |
| Gateway OOM killed | Critical | 1280MB mem_limit exceeded | [[agentshroud-gateway]] | `docker stats agentshroud-gateway`, check PII scan memory | — |
| PID limit exceeded | High | Too many processes (512 bot / 100 gateway) | Both | Investigate process leak | — |
