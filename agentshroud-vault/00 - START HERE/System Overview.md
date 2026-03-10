---
title: System Overview
type: index
tags: [#type/index, #status/critical]
related: ["[[Architecture Overview]]", "[[Startup Sequence]]", "[[Data Flow]]", "[[agentshroud-gateway]]", "[[agentshroud-bot]]"]
status: active
last_reviewed: 2026-03-09
---

# System Overview

## What AgentShroud Is

AgentShroud is a **security isolation layer for autonomous AI agents**. It wraps a bot (currently OpenClaw, a Node.js Claude-powered agent) inside a hardened Docker network topology and intercepts every message in both directions. No LLM call, Telegram message, file download, or outbound HTTP request leaves the bot without being inspected, logged, and potentially blocked.

## Why It Exists

Autonomous agents have two fundamental security problems:
1. **Inbound attacks** — prompt injection, jailbreaks, attempts to override instructions via user messages
2. **Outbound leakage** — the bot exfiltrating PII, credentials, system architecture details, or contacting unauthorized endpoints

AgentShroud solves both by acting as an enforcing proxy at every boundary.

## Who Depends On It

| Consumer | Dependency |
|----------|-----------|
| **Owner (Isaiah)** | Sends tasks to bot via Telegram; receives responses through gateway |
| **Collaborators** | Limited access via Telegram; rate-limited and command-restricted |
| **OpenClaw bot** | All API calls (Anthropic, Telegram, iMessage MCP, web) route through gateway |
| **Home lab hosts** (marvin, trillian, raspberrypi) | Reachable via gateway SSH proxy |

## What Breaks Downstream If AgentShroud Goes Down

| Component | Impact |
|-----------|--------|
| Telegram bot | Unreachable — no getUpdates polling |
| LLM API calls | Blocked — `ANTHROPIC_BASE_URL` points to gateway |
| Outbound HTTP from bot | Blocked — `HTTP_PROXY` points to gateway |
| File downloads (photos) | Blocked — `TELEGRAM_API_BASE_URL` points to gateway |
| iMessage MCP tools | Blocked — MCP proxy is in gateway |
| SSH to home lab | Blocked — SSH proxy is in gateway |

## Architecture Summary (Plain English)

1. **Two containers**: `agentshroud-gateway` (Python/FastAPI) and `agentshroud-bot` (Node.js/OpenClaw)
2. **Two Docker networks**: `agentshroud-internal` (has internet) and `agentshroud-isolated` (no internet). Gateway is on both; bot is on `isolated` only.
3. **Three proxy layers** inside the gateway:
   - **Telegram API proxy** (`/telegram-api/`) — intercepts all Telegram Bot API calls
   - **LLM proxy** (`/v1/`) — intercepts all Anthropic API calls, scans streaming output
   - **HTTP CONNECT proxy** (port 8181) — intercepts all other outbound HTTP from bot
4. **Security pipeline** — every message passes through: prompt injection → PII → trust → canary → encoding → egress → audit
5. **Approval queue** — dangerous actions (exec, cron, external APIs) are held for human approval
6. **DNS forwarder** (port 5353) — in-process blocklist filtering, replaces Pi-hole

## Key Facts

| Property | Value |
|----------|-------|
| Gateway port | `8080` (host-bound to `127.0.0.1`) |
| Bot port | `18789` (internal) / `18790` (host) |
| HTTP CONNECT proxy port | `8181` (internal only) |
| DNS forwarder port | `5353` (internal) |
| Auth method | Shared secret (`gateway_password` Docker secret) |
| Config file | `agentshroud.yaml` (mounted read-only into gateway) |
| All security modules | Default: `enforce` mode |

## Links

- [[Architecture Overview]] — Mermaid component map
- [[Startup Sequence]] — how it all starts up
- [[Data Flow]] — how a Telegram message becomes a bot response
- [[agentshroud-gateway]] — gateway container detail
- [[agentshroud-bot]] — bot container detail
