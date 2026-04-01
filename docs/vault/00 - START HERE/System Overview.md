---
type: overview
created: 2026-03-03
tags: [architecture, overview, security]
related: [Architecture Overview, Data Flow, Quick Reference]
---

# AgentShroud — System Overview

## What It Is

AgentShroud is a **security gateway proxy** that sits between an autonomous AI agent (OpenClaw) and the external world. Every outbound request — LLM API calls, MCP tool invocations, Telegram messages, HTTP fetches, SSH sessions — passes through the gateway's security pipeline before reaching its destination.

**Version:** 1.0.0 "Fortress"
**License:** Proprietary — Copyright © 2026 Isaiah Dallas Jefferson, Jr.
**Stack:** Python 3.13 / FastAPI (gateway) + Node.js 22 (OpenClaw bot container)

---

## Why It Exists

Autonomous AI agents operate with broad tool access: they can read files, run commands, send messages, fetch URLs, and call external APIs. Without a security boundary, a compromised agent could:

- Exfiltrate PII via API calls
- Accept prompt injection from untrusted tool results
- Escalate to sensitive credential stores
- Send messages to unauthorized recipients
- Consume unbounded compute/network resources

AgentShroud enforces a **security perimeter** around the agent. All of these risks are addressed by discrete, auditable security modules.

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Fail-closed by default** | Unrecognized traffic is blocked, not passed through |
| **Enforce mode by default** | All 4 core modules (`pii_sanitizer`, `prompt_guard`, `egress_filter`, `mcp_proxy`) start in `enforce`, not `monitor` |
| **PII redacted before forwarding** | Presidio + spaCy scan every request; PII is replaced with `<REDACTED>` tokens |
| **Human-in-the-loop approval queue** | Risky actions (email, file deletion, external API calls) require explicit operator approval via WebSocket dashboard |
| **Least privilege MCP permissions** | Each MCP tool has an explicit `read`/`write` permission level and rate limit |
| **1Password credential isolation** | The agent never sees raw credentials — the gateway proxies 1Password lookups using a service account |
| **Audit ledger** | Every forwarded message is stored in SQLite with hash-verifiable chain |

---

## Components

```
┌─────────────────────────────────────────────────────────────────┐
│  OpenClaw Bot Container (Node.js 22)                            │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  MCP Proxy Wrapper (mcp-proxy-wrapper.js)                  │ │
│  │  stdio ↔ HTTP — intercepts all MCP tool calls              │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────────┘
                          │ HTTP (port 8080)
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│  AgentShroud Gateway Container (Python 3.13 / FastAPI)         │
│                                                                  │
│  ┌──────────────┐  ┌────────────────┐  ┌─────────────────────┐ │
│  │  Ingest API  │  │  Security      │  │  Proxy Layer        │ │
│  │  (main.py)   │  │  Pipeline      │  │  mcp_proxy          │ │
│  │  auth        │  │  prompt_guard  │  │  telegram_proxy     │ │
│  │  middleware  │  │  pii_sanitizer │  │  llm_proxy          │ │
│  │  ledger      │  │  egress_filter │  │  http_proxy         │ │
│  │  router      │  │  trust_manager │  │  web_proxy          │ │
│  └──────────────┘  └────────────────┘  └─────────────────────┘ │
│                                                                  │
│  ┌──────────────┐  ┌────────────────┐  ┌─────────────────────┐ │
│  │  Approval    │  │  Web Mgmt API  │  │  Runtime Engines    │ │
│  │  Queue       │  │  (api.py)      │  │  docker/podman      │ │
│  │  WebSocket   │  │  Dashboard     │  │  compose generator  │ │
│  └──────────────┘  └────────────────┘  └─────────────────────┘ │
└──────────────────────────────┬──────────────────────────────────┘
                               │
          ┌────────────────────┼─────────────────────┐
          ▼                    ▼                     ▼
  api.anthropic.com    api.telegram.org        MCP Servers
  api.openai.com       oauth2.googleapis.com   (allowlisted)
```

---

## Security Layers (in order)

1. **Authentication** — Shared-secret `Authorization: Bearer <token>` on every request
2. **Middleware** — Rate limiting, request logging, header validation
3. **Input Normalization** — Base64 detection, encoding normalization
4. **PII Sanitization** — Presidio/spaCy detect and redact SSN, credit cards, emails, phone numbers, addresses
5. **Prompt Injection Defense** — Pattern matching + threat scoring; blocks injections in tool results
6. **Egress Filtering** — Domain and IP allowlist; RFC1918 private networks are blocked by default
7. **MCP Permission Enforcement** — Per-tool `read`/`write` level + rate limits from `agentshroud.yaml`
8. **Credential Isolation** — Only `op://Agent Shroud Bot Credentials/*/*` paths allowed through op-proxy
9. **Approval Queue** — `email_sending`, `file_deletion`, `external_api_calls`, `skill_installation` require human approval
10. **Audit Ledger** — Every request logged to SQLite with SHA-256 hash chain

---

## Who Depends On It

| Consumer | Usage |
|----------|-------|
| OpenClaw agent | All outbound traffic routed through gateway |
| macOS Shortcuts / iOS | REST API via Tailscale for voice/screenshot tasks |
| Browser extension | Sends web content for PII scanning |
| Operator dashboard | WebSocket real-time monitoring and approval queue |
| SIEM (Falco, Wazuh) | Security event forwarding |

---

## Related Notes

- [[Architecture Overview]] — Component map with full Mermaid diagram
- [[Data Flow]] — Step-by-step request trace
- [[Quick Reference]] — Operational cheat sheet
- [[Configuration/agentshroud.yaml]] — Config file breakdown
- [[Runbooks/First Time Setup]] — Deployment guide
