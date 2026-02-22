<div align="center">

<!-- AgentShroud™ Brand Header -->
<img src="branding/logos/png/logo-transparent.png" alt="AgentShroud™ Logo" width="120" height="120" />

<h1>AgentShroud™</h1>

<p><strong>Enterprise Governance Proxy for Autonomous AI Agents</strong></p>

<p>
  <a href="https://github.com/idallasj/agentshroud/actions/workflows/ci.yml">
    <img src="https://github.com/idallasj/agentshroud/actions/workflows/ci.yml/badge.svg" alt="Tests" />
  </a>
  <a href="https://github.com/idallasj/agentshroud">
    <img src="https://img.shields.io/badge/coverage-92%25-brightgreen" alt="Coverage" />
  </a>
  <img src="https://img.shields.io/badge/python-3.11-blue.svg" alt="Python 3.11" />
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/trademark-AgentShroud™-1583f0" alt="AgentShroud™ Trademark" />
</p>

<p><em>Built by a system architect, for system architects. Powered by agents. Governed by design.</em></p>

<hr />

</div>

**AgentShroud** is an open-source, enterprise-grade transparent proxy framework designed to enable the safe, auditable, and governed deployment of autonomous AI agents in real-world production environments.

It bridges the gap between the transformative potential of autonomous AI agents and the security, compliance, and governance requirements of modern enterprises — proving that speed and safety are not mutually exclusive.

AgentShroud sits as an intermediary layer between AI agents — Claude Code, Gemini CLI, OpenAI Codex, OpenClaw, and others — and the systems they interact with. Every API call, file write, cloud resource change, and tool invocation is intercepted, inspected, logged, and policy-enforced without disrupting the agent's native workflow.

Think of it as a **security mesh for autonomous agents**: invisible to the agent, indispensable to the enterprise.

AgentShroud is simultaneously a **production-grade tool**, a **learning laboratory**, and a **living proof of concept** — built in the open, by a system architect, using the very technologies it governs. It is itself built almost entirely by AI agents under human architectural direction, making it a real working demonstration of the methodology it enables. It is not a whitepaper. It is not a pilot. It is a production-grade reference implementation that enterprise leaders can examine, fork, and deploy.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      YOUR DEVICES                           │
│  Telegram · iOS Shortcuts · Browser Extension · SSH · API  │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTPS (Tailscale)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  AGENTSHROUD GATEWAY                         │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │   PII    │  │ Approval │  │  Audit   │  │  Prompt   │  │
│  │Sanitizer │→ │  Queue   │→ │  Ledger  │  │  Guard    │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │  Egress  │  │  Trust   │  │  Drift   │  │ Encrypted │  │
│  │  Filter  │  │ Manager  │  │ Detector │  │   Store   │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │   SSH    │  │   Kill   │  │  Agent   │  │ Dashboard │  │
│  │  Proxy   │  │  Switch  │  │Isolation │  │ (WebSocket│  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │   HTTP   │  │   MCP    │  │  Web     │  │Credential │  │
│  │  CONNECT │  │  Proxy   │  │  Proxy   │  │Isolation  │  │
│  │  Proxy   │  │          │  │          │  │(op-proxy) │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  Multi-Agent Router · Auth (HMAC/JWT) · WebSocket Events   │
└──────────────────────────┬──────────────────────────────────┘
                           │ Filtered & Approved
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              AI AGENT CONTAINER (OpenClaw)                   │
│  Read-only rootfs · Seccomp · Memory limits · Internet-only │
│  1Password via op-proxy (token stays on gateway)            │
└─────────────────────────────────────────────────────────────┘
```

**MCP-native**: Any MCP-compatible agent (Claude Code, Gemini CLI, Codex) can plug in without modification. AgentShroud extends MCP with an enterprise governance layer.

---

## Security Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | **PII Sanitizer** | Microsoft Presidio-powered detection & redaction of SSN, credit cards, emails, phone numbers, addresses |
| 2 | **Approval Queue** | Human-in-the-loop approval for sensitive actions (email, file deletion, API calls, SSH commands) |
| 3 | **Audit Ledger** | SQLite-backed immutable log with SHA-256 hash chain of all data flows and agent actions |
| 4 | **Prompt Guard** | Detects and blocks prompt injection, jailbreak attempts, and payload smuggling (11+ pattern detectors) |
| 5 | **Egress Filter** | Network-level control of outbound connections; blocks LAN, SSRF, and DNS tunneling; domain allowlist |
| 6 | **Trust Manager** | Cryptographic verification of agent identity and configuration integrity; progressive trust levels |
| 7 | **Drift Detector** | Monitors container filesystem and configuration for unauthorized changes |
| 8 | **Encrypted Store** | AES-256-GCM at-rest encryption for sensitive configuration and credentials |
| 9 | **SSH Proxy** | Secure SSH access through approval workflow with command allowlists and audit trail |
| 10 | **Kill Switch** | Emergency shutdown with credential revocation — freeze, shutdown, or disconnect modes |
| 11 | **Agent Isolation** | Seccomp profiles, read-only rootfs, memory/PID limits, rootless container execution |
| 12 | **Live Dashboard** | Real-time WebSocket activity feed, approval management, and system health monitoring |
| 13 | **HTTP CONNECT Proxy** | All bot outbound traffic routed through gateway; allowlist enforcement; traffic statistics |
| 14 | **Credential Isolation** | `op://` references proxied via gateway; 1Password service account token never in the bot container |

---

## Quickstart

Get AgentShroud running in 5 minutes:

### 1. Clone & Configure

```bash
git clone https://github.com/idallasj/agentshroud.git
cd agentshroud

# Copy example config
cp examples/minimal.env .env

# Generate auth token
python3 -c "import secrets; print(f'GATEWAY_AUTH_TOKEN={secrets.token_hex(32)}')" >> .env
```

### 2. Start with Docker Compose

```bash
docker compose -f examples/docker-compose.minimal.yml up -d
```

### 3. Verify

```bash
# Health check
curl -s http://localhost:8080/health | python3 -m json.tool

# Dashboard
open http://localhost:3000
```

### 4. Forward Your First Data

```bash
curl -X POST http://localhost:8080/api/v1/forward \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello from AgentShroud!", "source": "api", "content_type": "text"}'
```

That's it! The gateway is now filtering all data between you and your OpenClaw agent.

---

## Why AgentShroud

Most enterprises are not moving slowly because they lack interest in AI — they are moving slowly because they lack a safe on-ramp. The risks are real: agents with unconstrained access can exfiltrate data, rack up cloud costs, corrupt repositories, or expose internal systems to collaborators who shouldn't have that visibility.

AgentShroud answers the question every CIO, CISO, and innovation leader is quietly asking: *"How do we actually let AI agents do real work without creating unacceptable risk?"*

### Core Objectives

**Personal Mastery Through Real Building** — AgentShroud is an intentional learning vehicle. The project exists in part to develop hands-on fluency with the current generation of autonomous agent frameworks and developer tools — including Claude Code, OpenAI Codex, Google Gemini CLI, MCP, multi-agent coordination, GitHub, Atlassian Jira/Confluence, and AWS. The goal is not theoretical familiarity — it is working knowledge, earned by shipping something real.

**Observability Without Obstruction** — Every action taken by an AI agent is captured, attributed, and made auditable. Nothing happens in the dark.

**Policy Enforcement at the Agent Layer** — Configurable guardrails prevent agents from taking destructive, unauthorized, or out-of-scope actions. Scope-limited permissions, rate limiting, blast radius controls, and dry-run modes.

**Secure Multi-Agent Orchestration** — Controlled environment for multiple agents and external collaborators without exposing sensitive systems or credentials.

**MCP-Native Architecture** — Built around the Model Context Protocol. Any MCP-compatible agent can plug in without modification. AgentShroud extends MCP with an enterprise governance layer.

### AgentShroud vs Unprotected Agent

| Feature | Unprotected Agent | AgentShroud |
|---------|-------------------|-------------|
| PII detection & redaction | ❌ | ✅ Presidio-powered |
| Human approval queue | ❌ | ✅ Telegram/API/Dashboard |
| Audit trail | Basic logs | ✅ Immutable SHA-256 ledger |
| Prompt injection defense | ❌ | ✅ 11+ pattern detectors |
| Outbound traffic control | ❌ | ✅ HTTP CONNECT proxy + domain allowlist |
| Credential isolation | ❌ | ✅ op-proxy — token never in bot |
| Container hardening | Minimal | ✅ Seccomp + read-only rootfs + rootless |
| SSH with approval | ❌ | ✅ Command allowlists + audit |
| Kill switch | ❌ | ✅ Freeze/shutdown/disconnect |
| Real-time dashboard | ❌ | ✅ WebSocket live feed |
| Drift detection | ❌ | ✅ Filesystem monitoring |
| MCP tool governance | ❌ | ✅ Per-tool permissions + rate limits |
| Multi-agent support | Per-platform | ✅ Claude Code, Gemini, Codex, OpenClaw |

---

## Dashboard

The live dashboard provides real-time visibility into agent activity:

```
┌─────────────────────────────────────────────────────────┐
│  AgentShroud Dashboard          [Kill Switch] [Settings] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Activity Feed (Live)              Approval Queue (3)   │
│  ─────────────────                 ──────────────────   │
│  10:21 Forward text → general      🔴 Send email to     │
│  10:20 PII: 2 items redacted          boss@corp.com    │
│  10:19 SSH: git status (auto)         [Approve] [Deny] │
│  10:18 Auth: token verified                             │
│  10:15 Agent: response sent        🟡 Delete /tmp/data  │
│                                       [Approve] [Deny] │
│  System Health                                          │
│  ─────────────                     🟡 Install package   │
│  Gateway: ● Online                    requests==2.31    │
│  Agent: ● Online                      [Approve] [Deny] │
│  Ledger: 1,247 entries                                  │
│  Uptime: 4d 12h 33m                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Documentation

### Quick Start
| Document | Description |
|----------|-------------|
| [Setup Guide](docs/setup/OPENCLAW_SETUP.md) | Full installation walkthrough |
| [User Guide](docs/user-guide.md) | Day-to-day usage |
| [Security](SECURITY.md) | Vulnerability reporting & security overview |
| [Contributing](CONTRIBUTING.md) | How to contribute |

### Technical Documentation
| Category | Directory | Description |
|----------|-----------|-------------|
| **Architecture** | [docs/architecture/](docs/architecture/) | System design, ADRs, deployment, network topology |
| **Flows** | [docs/flows/](docs/flows/) | State diagrams, DFDs, sequence diagrams, activity diagrams |
| **Data** | [docs/data/](docs/data/) | ERDs, data dictionary, schema documentation |
| **API** | [docs/api/](docs/api/) | OpenAPI spec, API reference, integration guides |
| **Security** | [docs/security/](docs/security/) | Threat model, security architecture, access control |
| **Operations** | [docs/operations/](docs/operations/) | Runbooks, SOPs, incident response, deployment procedures |
| **Requirements** | [docs/requirements/](docs/requirements/) | SRS, FRD, NFR, use cases |
| **Testing** | [docs/testing/](docs/testing/) | Test plans, coverage reports, benchmarks |
| **Project** | [docs/project/](docs/project/) | RACI, glossary, release notes |
| **Integrations** | [docs/integrations/](docs/integrations/) | ICDs, integration architecture, message schemas |
| **Reference** | [docs/reference/](docs/reference/) | Quick references and guides |
| **Setup** | [docs/setup/](docs/setup/) | Installation and configuration guides |
| **Compliance** | [docs/compliance/](docs/compliance/) | IEC 62443 alignment and compliance documentation |

### Development Resources
| Resource | Location | Description |
|----------|----------|-------------|
| [Examples](examples/) | Configuration examples and templates |
| [Scripts](scripts/) | Utility scripts and automation tools |
| [Gateway Source](gateway/) | Core proxy implementation |
| [Changelog](CHANGELOG.md) | Version history and changes |

---
## Example Configurations

See the [`examples/`](examples/) directory:

- **`minimal.env`** — Bare minimum to get running
- **`recommended.env`** — Recommended production settings
- **`paranoid.env`** — Maximum security (all modules, strict egress, read-only fs)
- **`docker-compose.minimal.yml`** — Quick start compose file
- **`docker-compose.production.yml`** — Hardened production deployment

---

## Development

```bash
# Clone
git clone https://github.com/idallasj/agentshroud.git
cd agentshroud

# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r gateway/requirements.txt

# Run tests
pytest gateway/tests/ -v --tb=short

# Run with coverage
pytest gateway/tests/ -v --cov=gateway --cov-report=term-missing
```

---

## Who It's For

AgentShroud is designed for technically-minded enterprise leaders — architects, engineers, and innovation executives — who want to move beyond theoretical AI adoption and demonstrate to their organizations what responsible, high-velocity AI-augmented work actually looks like in practice.

It is equally a resource for individuals who learn best by building: professionals who want to develop real fluency with agentic AI not through courses, but through the discipline of shipping production software with these tools.

If you are a system architect who wants to use LLMs to build real software, bring in outside collaborators securely, or show corporate stakeholders that speed and safety are not mutually exclusive — this is for you.

---

## Acknowledgments

The bot layer is built on [OpenClaw](https://github.com/openclaw/openclaw) — the open-source AI agent framework. AgentShroud wraps it with an enterprise security and governance layer without modifying the underlying platform.

---

<div align="center">

<img src="branding/logos/png/logo-transparent.png" alt="AgentShroud™" width="48" height="48" />

**AgentShroud™** · Enterprise AI Governance Gateway

[MIT License](LICENSE) · © 2026 Isaiah Dallas Jefferson, Jr. · All rights reserved

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.*
*Protected by common law trademark rights. Federal trademark registration pending.*
*Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.*

[agentshroud.ai@gmail.com](mailto:agentshroud.ai@gmail.com) · [github.com/idallasj/agentshroud](https://github.com/idallasj/agentshroud)

</div>
