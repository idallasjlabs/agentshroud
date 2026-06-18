<div align="center">

<!-- AgentShroud™ Brand Header -->
<img src="branding/logos/png/logo-transparent.png" alt="AgentShroud™ Logo" width="120" height="120" />

<h1>AgentShroud™</h1>


<p><strong>Enterprise Governance Proxy for Autonomous AI Agents</strong></p>

> *"One Shroud Over Every Wire"* — You decide what the agent sees, not the agent.


<p>
  <a href="https://github.com/idallasjlabs/agentshroud/actions/workflows/ci.yml">
    <img src="https://github.com/idallasjlabs/agentshroud/actions/workflows/ci.yml/badge.svg" alt="Tests" />
  </a>
  <a href="https://github.com/idallasjlabs/agentshroud">
    <img src="https://img.shields.io/badge/coverage-85%25-brightgreen" alt="Coverage" />
  </a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue.svg" alt="Python 3.9+" />
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/trademark-AgentShroud™-1583f0" alt="AgentShroud™ Trademark" />
  <img src="https://img.shields.io/badge/modules-76-blueviolet" alt="76 Security Modules" />
</p>

<p><em>Built by a system architect, for system architects. Powered by agents. Governed by design.</em></p>

<hr />

</div>

**AgentShroud** is an open-source, enterprise-grade transparent proxy framework designed to enable the safe, auditable, and governed deployment of autonomous AI agents in real-world production environments.

It bridges the gap between the transformative potential of autonomous AI agents and the security, compliance, and governance requirements of modern enterprises — proving that speed and safety are not mutually exclusive.

AgentShroud sits as an intermediary layer between AI agents — Claude Code, Gemini CLI, OpenAI Codex, OpenClaw, and others — and the systems they interact with. Every API call, file write, cloud resource change, and tool invocation is intercepted, inspected, logged, and policy-enforced without disrupting the agent's native workflow.

Think of it as a **security mesh for autonomous agents**: invisible to the agent, indispensable to the enterprise.

AgentShroud is simultaneously a **production-grade tool**, a **learning laboratory**, and a **living proof of concept** — built in the open, by a system architect, using the very technologies it governs. It is itself built almost entirely by AI agents under human architectural direction, making it a real working demonstration of the methodology it enables.

---

## What's New — v1.1.1 "Hermes" (June 2026)

The v1.1.x line introduces **multi-bot governance**: AgentShroud now secures two autonomous AI agents simultaneously — **OpenClaw** (Node.js, the original) and **Hermes** (Python, `nousresearch/hermes-agent`) — through the same 76-module security pipeline.

- **v1.1.0 "Hermes"** (2026-05-29): Hermes bot first-class peer to OpenClaw, Tailscale serve integration, per-bot Telegram tokens, ClamAV OOM fix, branding refresh
- **v1.1.1** (2026-06-10): Two dormant guards (ContextIntegrityScorer, EnvelopeSigner) wired live, Gemini quota-failover translator, container log hygiene

### v1.0.0 "Fortress" foundations (March 2026)

The original release wired all **76 security modules** into the live pipeline and delivered two complete control center interfaces — Web (7-page responsive dashboard) and Terminal (TUI + chat console). Every module is active in the pipeline — no stubs, no dead code, no planned-but-unbuilt features.

- **P0 — Core Pipeline**: PromptGuard, TrustManager, EgressFilter, PII fix, gateway binding
- **P1 — Middleware**: 12 modules wired (7 original + SessionManager, TokenValidator, ConsentFramework, SubagentMonitor, AgentRegistry) + MCP fail-closed enforcement
- **P2 — Network**: 5 modules active in web proxy into the request flow
- **P3 — Infrastructure**: 10 modules loaded (AlertDispatcher, DriftDetector, EncryptedStore, KeyVault, Canary, ClamAV, Trivy, Falco, Wazuh, HealthReport)

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
│                  AGENTSHROUD GATEWAY  :8080                  │
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
│  │   SSH    │  │   Kill   │  │  Agent   │  │  Context  │  │
│  │  Proxy   │  │  Switch  │  │Isolation │  │   Guard   │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │   HTTP   │  │   MCP    │  │  Web     │  │Credential │  │
│  │  CONNECT │  │  Proxy   │  │  Proxy   │  │Isolation  │  │
│  │  Proxy   │  │          │  │          │  │(op-proxy) │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │ Browser  │  │   Git    │  │ Key Leak │  │  DNS      │  │
│  │ Security │  │  Guard   │  │ Detector │  │  Filter   │  │
│  │  Guard   │  │          │  │          │  │           │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │Subagent  │  │ Sidecar  │  │ Metadata │  │Environment│  │
│  │ Monitor  │  │ Scanner  │  │  Guard   │  │  Guard    │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
│                                                             │
│  Multi-Agent Router · Auth (HMAC/JWT) · WebSocket Events   │
│  Web Control Center · Terminal Control Center (TUI)        │
└───────────────┬──────────────────────────┬─────────────────┘
                │ Filtered & Approved       │ Filtered & Approved
                ▼                           ▼
┌───────────────────────────┐  ┌───────────────────────────────┐
│  OpenClaw  (agentshroud-  │  │  Hermes Agent (agentshroud-   │
│  bot)  :18789             │  │  hermes)  :8642 API           │
│  Node.js · Telegram bot   │  │  :9119 dashboard · :9121 HCI  │
│  @agentshroud_bot         │  │  Python · @agentshroud_       │
│                           │  │  hermes_bot                   │
└───────────────────────────┘  └───────────────────────────────┘
```

**Multi-bot**: v1.1.0 introduces a second bot — Hermes — running alongside OpenClaw behind the same 76-module gateway. Start the full stack (gateway + OpenClaw + Hermes + HCI) with `--profile full`; omit `--profile full` for gateway + OpenClaw only.

**MCP-native**: Any MCP-compatible agent (Claude Code, Gemini CLI, Codex) can plug in without modification. AgentShroud extends MCP with an enterprise governance layer.

---

## 76 Security Modules

AgentShroud implements a defense-in-depth strategy with 76 security modules operating across 7 distinct layers, from network isolation to application-level content filtering.

### Core Security Pipeline

| # | Module | Description |
|---|--------|-------------|
| 1 | **PII Sanitizer** | Microsoft Presidio-powered detection & redaction of SSN, credit cards, emails, phone numbers, addresses |
| 2 | **PII Scanner** | Deep content scanning for PII patterns across all data flows |
| 3 | **Prompt Guard** | Detects and blocks prompt injection, jailbreak attempts, and payload smuggling (11+ pattern detectors) |
| 4 | **Egress Filter** | Network-level control of outbound connections; blocks LAN, SSRF, and DNS tunneling; domain allowlist |
| 5 | **Egress Monitor** | Real-time monitoring and alerting on outbound traffic patterns and anomalies |
| 6 | **Trust Manager** | Cryptographic verification of agent identity and configuration integrity; progressive trust levels |
| 7 | **Drift Detector** | Monitors container filesystem and configuration for unauthorized changes |
| 8 | **Encrypted Store** | AES-256-GCM at-rest encryption for sensitive configuration and credentials |

### Proxy & Network Layer

| # | Module | Description |
|---|--------|-------------|
| 9 | **SSH Proxy** | Secure SSH access through approval workflow with command allowlists and audit trail |
| 10 | **HTTP CONNECT Proxy** | All bot outbound traffic routed through gateway; allowlist enforcement; traffic statistics |
| 11 | **MCP Inspector** | Deep inspection of MCP tool calls for injection, PII, encoding, and sensitive operations |
| 12 | **MCP Permission Manager** | Per-tool permission policies, rate limiting, and scope enforcement for MCP tools |
| 13 | **MCP Proxy** | Full MCP JSON-RPC proxy with fail-closed enforcement — uninspected calls are blocked |
| 14 | **Web Proxy** | HTTP/HTTPS content proxy with domain filtering and content inspection |
| 15 | **Web Content Scanner** | Scans proxied web content for injection payloads, malicious scripts, and data exfiltration attempts |
| 16 | **DNS Filter** | DNS-level domain filtering and tunneling detection |

### Agent Containment

| # | Module | Description |
|---|--------|-------------|
| 17 | **Kill Switch** | Emergency shutdown with credential revocation — freeze, shutdown, or disconnect modes |
| 18 | **Isolation Verifier** | Validates container security posture: seccomp, read-only rootfs, capability drops, rootless execution |
| 19 | **Credential Isolation** | `op://` references proxied via gateway; 1Password service account token never in the bot container |
| 20 | **Resource Guard** | Per-agent CPU, memory, disk, and request rate limits with cumulative tracking |

### Content & Context Guards

| # | Module | Description |
|---|--------|-------------|
| 21 | **Context Guard** | Validates conversation context integrity and detects context manipulation attacks |
| 22 | **Environment Guard** | Monitors and enforces environment variable security policies |
| 23 | **Metadata Guard** | Inspects and sanitizes metadata in requests and responses to prevent information leakage |
| 24 | **Browser Security Guard** | Security controls for browser automation: URL filtering, script injection prevention, download policies |
| 25 | **Git Guard** | Monitors git operations for force pushes, sensitive file commits, and unauthorized branch operations |
| 26 | **Key Leak Detector** | Scans all content for exposed API keys, tokens, private keys, and other credentials |
| 27 | **Log Sanitizer** | Ensures sensitive data is redacted from all log output before persistence |

### Infrastructure & Monitoring

| # | Module | Description |
|---|--------|-------------|
| 28 | **Subagent Monitor** | Tracks and controls spawned sub-agents; enforces depth limits and resource boundaries |
| 29 | **Sidecar Scanner** | Inspects sidecar containers and services for security compliance |
| 30 | **Audit Ledger** | SQLite-backed immutable log with SHA-256 hash chain of all data flows and agent actions |

### Supporting Infrastructure

| Component | Description |
|-----------|-------------|
| **Approval Queue** | Human-in-the-loop approval for sensitive actions (email, file deletion, API calls, SSH commands) |
| **Session Manager** | Manages agent sessions, authentication state, and session-scoped permissions |
| **Port Manager** | Controls and audits network port allocations and bindings |
| **Proxy Dashboard** | Real-time WebSocket activity feed, approval management, and system health monitoring |
| **SecurityPipelineIntegrator** | Orchestrates all 33 modules into a unified processing pipeline |

---

## Control Centers

### Web Control Center

A 7-page responsive web dashboard providing full management capabilities:

- **Dashboard** — Real-time activity feed, system health, active alerts
- **Security Modules** — Status and configuration for all 33 modules
- **Approval Queue** — Review and action pending approval requests
- **Audit Trail** — Browse and search the immutable audit ledger
- **Agent Management** — Monitor connected agents, trust levels, resource usage
- **Settings** — Gateway configuration, allowlists, notification preferences
- **Kill Switch** — Emergency controls with one-click freeze/shutdown/disconnect

### Terminal Control Center

A full TUI (Text User Interface) + chat console designed for terminal-first workflows, optimized for Blink Shell and mobile SSH access:

- Module status overview and health monitoring
- Interactive approval queue management
- Live activity feed in terminal
- Chat console for direct agent interaction
- Keyboard-driven navigation for efficiency

---

## Quickstart

### Prerequisites

- **Git**
- **Docker Engine** — [Colima](https://github.com/abiosoft/colima) on macOS, Docker CE on Linux
- **Claude OAuth token** — `sk-ant-oat01-...` (required)
- **Telegram bot token** — create one via [@BotFather](https://t.me/BotFather) (required)
- **1Password account** — email, master password, and secret key (required)
- **Python 3** — for gateway key generation

### 1. Clone

```bash
git clone https://github.com/idallasjlabs/agentshroud.git
cd agentshroud
```

### 2. Store credentials

```bash
./docker/setup-secrets.sh store
```

This prompts for each credential interactively. The backend is auto-detected:

| Backend | Platform | Requires |
|---------|----------|---------|
| 1Password CLI | Any | `op` CLI installed and signed in |
| macOS Keychain | macOS | Interactive TTY (auto-unlocks; prompts for login password over SSH) |
| secret-tool | Linux | `libsecret` / `secret-tool` in PATH |
| `~/.agentshroud/secrets/` | Any | SSH sessions, service accounts |

Secrets required: Claude OAuth token, Telegram bot token, 1Password email/master password/secret key.
Optional: OpenAI API key, Google API key, Slack tokens.

### 3. Start the stack

```bash
# Gateway + OpenClaw only (default)
scripts/asb up

# Full stack — adds Hermes agent and HCI control interface
docker-compose -f docker/docker-compose.yml -p agentshroud --profile full up -d
```

Secrets are extracted into a temp directory for the duration of `docker compose up` and cleaned up automatically on exit — nothing persists on disk.

### 4. Verify

```bash
scripts/asb status   # container health
scripts/asb logs     # tail all logs
```

### `asb` reference

| Command | Action |
|---------|--------|
| `asb up` | Start the stack |
| `asb down` | Stop the stack |
| `asb rebuild` | Rebuild images and restart |
| `asb clean-rebuild` | Full teardown, prune, rebuild, restart |
| `asb status` | Show container health |
| `asb logs [service]` | Tail logs |
| `asb test` | Run test suite inside gateway container |
| `asb pull` | `git pull --rebase` |

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
| PII detection & redaction | ❌ | ✅ Presidio-powered + deep scanning |
| Human approval queue | ❌ | ✅ Telegram/API/Web/TUI Dashboard |
| Audit trail | Basic logs | ✅ Immutable SHA-256 hash-chain ledger |
| Prompt injection defense | ❌ | ✅ 11+ pattern detectors + context guard |
| Outbound traffic control | ❌ | ✅ HTTP CONNECT proxy + domain allowlist + DNS filter |
| Credential isolation | ❌ | ✅ op-proxy — token never in bot |
| Container hardening | Minimal | ✅ Seccomp + read-only rootfs + rootless + isolation verifier |
| SSH with approval | ❌ | ✅ Command allowlists + audit |
| Kill switch | ❌ | ✅ Freeze/shutdown/disconnect |
| Real-time dashboard | ❌ | ✅ Web Control Center (7 pages) + Terminal TUI |
| Drift detection | ❌ | ✅ Filesystem monitoring |
| MCP tool governance | ❌ | ✅ Per-tool permissions + rate limits + fail-closed |
| Multi-agent support | Per-platform | ✅ Claude Code, Gemini, Codex, OpenClaw |
| Git operation security | ❌ | ✅ Force push detection, secret scanning |
| Key/credential leak detection | ❌ | ✅ Real-time scanning across all content |
| Browser automation security | ❌ | ✅ URL filtering, script injection prevention |
| Sub-agent control | ❌ | ✅ Depth limits, resource boundaries |
| Web content scanning | ❌ | ✅ Injection and exfiltration detection |
| Environment hardening | ❌ | ✅ Environment variable policy enforcement |
| Log sanitization | ❌ | ✅ Sensitive data redacted before persistence |

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
git clone https://github.com/idallasjlabs/agentshroud.git
cd agentshroud

# Create virtual environment
python3 -m venv .venv
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

## Media

- 🎙️ **[Introduction to AgentShroud](https://overcast.fm/+ABV5l7XfkRk)** — Podcast episode covering the motivation, architecture, and real-world use cases for AgentShroud.

---

## Acknowledgments

The bot layer is built on [OpenClaw](https://github.com/openclaw/openclaw) — the open-source AI agent framework. AgentShroud wraps it with an enterprise security and governance layer without modifying the underlying platform.

Special thanks to the collaborators who stress-tested AgentShroud in production,
broke things in creative ways, and helped harden it into what it is today:
**Ana, Brett, Chris, Gabe, German, Michael, Praveen, Steve, and TJ.**

---

<div align="center">

<img src="branding/logos/png/logo-transparent.png" alt="AgentShroud™" width="48" height="48" />

**AgentShroud™** · Enterprise AI Governance Gateway

[MIT License](LICENSE) · © 2026 Isaiah Dallas Jefferson, Jr. · All rights reserved

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)*
*Patent Pending — U.S. Provisional Application No. 64/018,744*
*Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.*

[agentshroud.ai@gmail.com](mailto:agentshroud.ai@gmail.com) · [github.com/idallasjlabs/agentshroud](https://github.com/idallasjlabs/agentshroud)

</div>
