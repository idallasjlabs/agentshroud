
---
title: AgentShroud — Home
type: index
tags: [#type/index, #status/critical]
related: ["[[System Overview]]", "[[Architecture Overview]]", "[[Quick Reference]]"]
status: active
last_reviewed: 2026-03-09
---

# AgentShroud Gateway — Knowledge Vault

AgentShroud is a **security proxy gateway** that wraps autonomous AI agents (currently OpenClaw/Claude) — intercepting every message in both directions, scanning for prompt injection, PII, credential leaks, and unauthorized egress, and routing all traffic through an inspected, logged pipeline.

> [!WARNING] Check Container Health First
> Before diving in, verify the stack is running:
> ```bash
> docker compose -f docker/docker-compose.yml ps
> curl http://localhost:8080/status
> ```
> If `agentshroud-gateway` is not healthy, see [[Gateway Startup Failure]].

---

## Vault Table of Contents

### 00 - Start Here
- [[System Overview]] — what it is, who depends on it, what breaks
- [[Quick Reference]] — commands, health checks, top 5 emergency fixes

### 01 - Architecture
- [[Architecture Overview]] — component map, network topology, Mermaid diagram
- [[Startup Sequence]] — cold boot to fully operational, step by step
- [[Shutdown & Recovery]] — graceful stop, crash recovery, data integrity
- [[Data Flow]] — how a message travels from Telegram to the bot and back

### 02 - Modules
- [[main]] — FastAPI app entry point, route wiring
- [[lifespan]] — startup/shutdown orchestration, all component initialization
- [[pipeline]] — the central security processing chain
- [[telegram_proxy]] — Telegram Bot API reverse proxy, inbound/outbound inspection
- [[llm_proxy]] — Anthropic API proxy, streaming filter
- [[config]] — YAML config loader, all Pydantic models
- [[bot_config]] — per-bot protocol and container specification
- [[egress_filter]] — outbound domain allowlist enforcement
- [[prompt_guard]] — prompt injection detection and scoring
- [[prompt_protection]] — system prompt / architecture disclosure prevention
- [[sanitizer]] — PII redaction via Microsoft Presidio
- [[middleware]] — tool result scanning, log sanitization, context guard
- [[router]] — multi-agent message routing
- [[webhook_receiver]] — inbound Telegram webhook processing

### 03 - Configuration
- [[agentshroud.yaml]] — master configuration file (security posture, bots, proxy)
- [[docker-compose.yml]] — container topology, networks, volumes, secrets
- [[patch-telegram-sdk.sh]] — patches OpenClaw dist to route Telegram file downloads through gateway
- [[apply-patches.js]] — OpenClaw runtime config patches (model, tools, workspace)

### 04 - Environment Variables
- [[All Environment Variables]] — master index
- [[TELEGRAM_API_BASE_URL]] — routes Telegram API calls to gateway
- [[ANTHROPIC_BASE_URL]] — routes LLM calls to gateway
- [[HTTP_PROXY]] / [[HTTPS_PROXY]] — egress proxy for bot
- [[GATEWAY_AUTH_TOKEN_FILE]] — gateway shared secret path
- [[AGENTSHROUD_MODE]] — global enforce/monitor override
- [[PROXY_ALLOWED_NETWORKS]] — IP CIDRs allowed to use the CONNECT proxy

### 05 - Dependencies
- [[All Dependencies]] — master dependency index
- [[fastapi]] — async web framework
- [[presidio]] — Microsoft PII detection engine
- [[httpx]] — async HTTP client
- [[pydantic]] — configuration validation

### 06 - Containers & Services
- [[agentshroud-gateway]] — Python/FastAPI security proxy container
- [[agentshroud-bot]] — Node.js OpenClaw agent container

### 07 - Errors & Troubleshooting
- [[Error Index]] — master error catalog
- [[Photo Download Failure]] — "Failed to download media" on photo uploads
- [[Gateway Startup Failure]] — gateway fails to start or exits immediately
- [[Bot Isolation Error]] — bot can reach internet directly (egress breach)
- [[Troubleshooting Matrix]] — symptom → cause → fix quick reference

### 08 - Runbooks
- [[First Time Setup]] — fresh machine to running stack
- [[Restart Procedure]] — safe restart, rolling vs full
- [[Crash Recovery]] — dirty crash → verified recovery
- [[Health Checks]] — all health check commands

### 09 - Diagrams
- [[Full System Flowchart]] — complete Mermaid diagram of all components
- [[Startup Flow Diagram]] — startup sequence with failure paths

---

![[Quick Reference]]
