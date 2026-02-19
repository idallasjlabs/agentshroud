```
   ___              ____  _                
  / _ \ _ __   ___ / ___|| | __ ___      __
 | | | | '_ \ / _ \ |    | |/ _` \ \ /\ / /
 | |_| | | | |  __/ |___ | | (_| |\ V  V / 
  \___/|_| |_|\___|\____||_|\__,_| \_/\_/  
                                            
  S E C U R E C L A W   G A T E W A Y
```

# OneClaw — Enterprise Security Proxy for OpenClaw AI Agents

[![Tests](https://github.com/idallasj/oneclaw/actions/workflows/ci.yml/badge.svg)](https://github.com/idallasj/oneclaw/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen)](https://github.com/idallasj/oneclaw)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> *"One Claw Tied Behind Your Back"* — You decide what the agent sees, not the agent.

OneClaw (AgentShroud) is a security proxy that sits between your real digital life and an OpenClaw AI agent. It provides **12 security modules**, a **human approval queue**, **full audit logging**, and a **real-time dashboard** — ensuring your AI assistant never sees data you haven't explicitly approved.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      YOUR DEVICES                           │
│  iOS Shortcuts · Browser Extension · API · SSH Terminal     │
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
│  Multi-Agent Router · Auth (HMAC/JWT) · WebSocket Events   │
└──────────────────────────┬──────────────────────────────────┘
                           │ Filtered & Approved
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              OPENCLAW AGENT (Containerized)                  │
│  Read-only rootfs · Seccomp · Memory limits · No network*   │
└─────────────────────────────────────────────────────────────┘
                    * Internet-only, no LAN access
```

---

## Security Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | **PII Sanitizer** | Microsoft Presidio-powered detection & redaction of SSN, credit cards, emails, phone numbers, addresses |
| 2 | **Approval Queue** | Human-in-the-loop approval for sensitive actions (email, file deletion, API calls, SSH commands) |
| 3 | **Audit Ledger** | SQLite-backed immutable log of all data flows and agent actions |
| 4 | **Prompt Guard** | Detects and blocks prompt injection, jailbreak attempts, and payload smuggling |
| 5 | **Egress Filter** | Network-level control of outbound connections; blocks LAN, allows only approved endpoints |
| 6 | **Trust Manager** | Cryptographic verification of agent identity and configuration integrity |
| 7 | **Drift Detector** | Monitors container filesystem and configuration for unauthorized changes |
| 8 | **Encrypted Store** | At-rest encryption for sensitive configuration and credentials |
| 9 | **SSH Proxy** | Secure SSH access through approval workflow with command allowlists and audit trail |
| 10 | **Kill Switch** | Emergency shutdown with credential revocation — freeze, shutdown, or disconnect modes |
| 11 | **Agent Isolation** | Seccomp profiles, read-only rootfs, memory/PID limits, rootless container execution |
| 12 | **Live Dashboard** | Real-time WebSocket activity feed, approval management, and system health monitoring |

---

## Quickstart

Get OneClaw running in 5 minutes:

### 1. Clone & Configure

```bash
git clone https://github.com/idallasj/oneclaw.git
cd oneclaw

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
  -d '{"content": "Hello from OneClaw!", "source": "api", "content_type": "text"}'
```

That's it! The gateway is now filtering all data between you and your OpenClaw agent.

---

## OneClaw vs Plain OpenClaw

| Feature | Plain OpenClaw | OneClaw |
|---------|---------------|---------|
| PII detection & redaction | ❌ | ✅ Presidio-powered |
| Human approval queue | ❌ | ✅ Telegram/API/Dashboard |
| Audit trail | Basic logs | ✅ Immutable SQLite ledger |
| Prompt injection defense | ❌ | ✅ PromptGuard module |
| Network egress control | ❌ | ✅ LAN blocked, allowlist |
| Container hardening | Basic | ✅ Seccomp + read-only + rootless |
| SSH with approval | ❌ | ✅ Command allowlists + audit |
| Kill switch | ❌ | ✅ Freeze/shutdown/disconnect |
| Real-time dashboard | ❌ | ✅ WebSocket live feed |
| Drift detection | ❌ | ✅ Filesystem monitoring |
| Encrypted secrets store | ❌ | ✅ At-rest encryption |
| Version management | ❌ | ✅ Security-reviewed upgrades |

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
git clone https://github.com/idallasj/oneclaw.git
cd oneclaw

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

## License

[MIT](LICENSE) © 2026 Isaiah Jefferson

---

## Acknowledgments

Built on top of [OpenClaw](https://github.com/nicholasgasior/openclaw) — the open-source AI agent framework. OneClaw adds the security layer that makes it safe for real-world use.
