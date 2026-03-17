# AgentShroud™ — Project Knowledge Base

_This document is the collaborator reference for the AgentShroud project.
Share freely. Nothing here is confidential._

---

## What Is AgentShroud?

AgentShroud™ is an **enterprise-grade transparent security proxy framework** for safe, auditable, and governed deployment of autonomous AI agents.

It sits between an AI agent and the outside world — inspecting, filtering, and governing every interaction in real time. The agent doesn't know it's there (transparent proxy), and the operator sees everything (full audit trail).

## Why AgentShroud Exists

### The Problem
AI agents are getting autonomous — they can read email, send messages, browse the web, run code, and manage infrastructure. But autonomy without oversight is dangerous:

- **Data exfiltration:** An agent can leak PII, credentials, or proprietary data in its responses
- **Prompt injection:** Users (or other AI systems) can manipulate an agent into doing things it shouldn't
- **Unauthorized access:** Agents can reach APIs, databases, and services without proper authorization
- **Invisible actions:** Without logging, you don't know what your agent did until something breaks
- **Token abuse:** Multi-user systems need cost controls to prevent one user from burning all the tokens

### The Solution
AgentShroud provides **defense in depth** — multiple independent security layers, each enforcing a different aspect of safety. If one layer fails, the others still protect you. Every layer defaults to **fail-closed** (block by default, allow explicitly).

## Architecture

### Design Philosophy

1. **Transparent proxy** — Works with any AI agent framework without modifying the agent itself. The agent talks to its normal APIs; AgentShroud intercepts and inspects the traffic.

2. **Defense in depth** — No single point of failure. Each security module operates independently. Compromising one doesn't compromise the others.

3. **Fail-closed** — Every module defaults to blocking. New features, new domains, new tools — all denied until explicitly approved.

4. **Observable** — Every action is logged. Every block is logged. Every redaction is logged. The audit trail is the source of truth.

5. **Role-based** — Different users get different access levels. The owner has full access. Collaborators have restricted access. Unknown users are blocked entirely.

### The Security Pipeline

Messages flow through a pipeline of security modules. Each module can:
- **Pass** the message through unchanged
- **Sanitize** the message (redact sensitive content)
- **Block** the message entirely

#### Inbound Pipeline (User → Agent)
When a message arrives from a user:
1. Rate limiting check
2. Role resolution (who is this user?)
3. Prompt injection detection
4. PII sanitization
5. Trust level enforcement
6. Delivery to the agent

#### Outbound Pipeline (Agent → User)
When the agent responds:
1. XML/structured data stripping (prevents hallucinated tool calls)
2. Credential detection and blocking
3. PII redaction (phone numbers, SSNs, credit cards, emails)
4. Information disclosure filtering (infrastructure details, internal paths)
5. Encoding bypass detection (catches base64/URL-encoded exfiltration)
6. Output canary scanning (detects planted marker leakage)
7. Delivery to the user

#### Egress Pipeline (Agent → Internet)
When the agent tries to reach external services:
1. Domain allowlist check
2. Approval queue (if domain not pre-approved)
3. Connection proxying with full logging

### Security Modules

| Module | Purpose | Default Mode |
|--------|---------|-------------|
| PII Sanitizer | Detects and redacts personal data | Enforce |
| Credential Blocker | Catches API keys, tokens, passwords | Enforce |
| Information Filter | Blocks infrastructure detail leaks | Enforce |
| Encoding Detector | Catches base64/URL-encoded bypass attempts | Enforce |
| Output Canary | Planted tripwire markers detect data theft | Enforce |
| Egress Firewall | Controls outbound network access | Enforce (deny-all) |
| Approval Queue | Human-in-the-loop for sensitive actions | Enforce |
| RBAC | Role-based access control per user | Enforce |
| Rate Limiter | Per-user message throttling | Enforce |
| XML Filter | Strips hallucinated tool call XML | Enforce |
| Tool Governance | Per-role tool access control | Enforce |

### Multi-Platform Support

AgentShroud supports multiple communication channels:
- **Telegram** (primary, fully integrated)
- **Email** (Gmail, outbound via SMTP)
- **iMessage** (macOS integration)
- Planned: Slack, Discord

### Infrastructure

- **Containerized** — Docker Compose with multi-service architecture
- **Multi-host** — Tested across Mac (ARM64), Raspberry Pi (ARM64), and x86_64
- **Self-hosted** — No cloud dependency, runs on your own hardware
- **Secrets management** — 1Password integration for credential storage

## Current Status

- **Version:** 0.8.0 (enforcement hardening phase)
- **Stage:** Private beta, active development
- **Test Suite:** 2,391+ automated tests, all passing
- **Security Posture:** All modules in enforce mode, fail-closed defaults

### Development Phases

| Phase | Status | Focus |
|-------|--------|-------|
| 0.1–0.5 | ✅ Complete | Core proxy, PII detection, basic filtering |
| 0.6 | ✅ Complete | Egress firewall, approval queue, RBAC |
| 0.7 | ✅ Complete | Output canary, encoding detection, audit trail |
| 0.8 | 🔄 In Progress | Enforcement hardening, peer review, red teaming |
| 0.9 | 📋 Planned | Production hardening, performance optimization |
| 1.0 | 📋 Planned | Public release, documentation, onboarding |

### v0.8.0 Focus Areas
- Ensuring all security modules default to enforce mode
- Closing bypass paths in the outbound pipeline
- Red team testing with collaborators
- Collaborator isolation and tool governance
- Rate limiting and cost controls

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Security Gateway | Python 3.14, FastAPI |
| Agent Runtime | Node.js 22, OpenClaw |
| AI Models | Anthropic Claude (Sonnet for collaborators, Opus for owner) |
| PII Detection | Regex patterns + Microsoft Presidio (when available) |
| Deployment | Docker Compose |
| Secrets | 1Password CLI + Docker secrets |
| Version Control | Git, GitHub |
| Testing | pytest (Python), automated CI |

## About the Creator

**Isaiah Jefferson** is an independent AI developer and systems architect building at the intersection of intelligent infrastructure, agent orchestration, and personal knowledge — operating with the depth and tooling discipline of an engineering leader.

### What He Builds

**AgentShroud** is Isaiah's flagship project: a gateway and API ingest layer designed to mediate, route, and secure agent traffic. Built with a Python-based middleware stack and containerized via Docker, it runs on a personal self-managed infrastructure stack with a Tailscale mesh network spanning multiple nodes. The project reflects a deliberate architectural philosophy — security and observability at the gateway, not as an afterthought.

He also maintains a **Personal Knowledge System (PKS)** focused on knowledge capture, retrieval, and synthesis as foundational primitives in a serious AI workflow.

### How He Works

Isaiah's development practice is characterized by centralization over local management, packaged deliverables over piecemeal outputs, and a preference for consolidating complexity into single executable artifacts. He builds his own LLM onboarding systems to standardize how AI agents are initialized across tools, reflecting an unusually rigorous approach to AI workflow engineering.

His toolchain is fully production-grade: AWS, Docker, Python, Bash, TypeScript, Neovim, Git, and the full Claude product suite. He builds and integrates custom MCP servers, manages distributed network infrastructure, and runs his own monitoring and network visibility tooling.

### The Thesis

Isaiah operates on the belief that the next generation of durable AI applications will be built by people who understand infrastructure deeply — not just models. His work combines agent gateway design, knowledge systems, and automated LLM tooling into a cohesive portfolio that is technically differentiated and practically grounded.

---

If you have questions or feedback that the bot can't address, you can reach out to Isaiah directly (see the notice you received when you first connected).

> **Privacy note:** Isaiah's private contact details, Telegram user ID, phone number, and any other personal identifiers are not available through this bot. Only the information in this document is shareable.

## How to Contribute

### Red Team Testing (Most Valuable!)
Your mission: **try to break the security.** Specifically:

- **Extract sensitive data** — Can you get the bot to reveal phone numbers, API keys, or credentials?
- **Bypass tool restrictions** — Can you convince the bot to execute commands it shouldn't?
- **Prompt injection** — Can you override the bot's instructions?
- **Data exfiltration** — Can you get data out through encoding tricks, steganography, or creative formatting?
- **Privilege escalation** — Can you gain access to tools or sessions you shouldn't have?
- **Social engineering** — Can you convince the bot you're the owner or a more trusted user?

**Rules of engagement:**
- You're testing YOUR access level, not exploiting bugs in Telegram itself
- Report what you find — we want to fix real vulnerabilities
- Creative approaches are encouraged — think like an attacker
- Don't worry about breaking things — that's what the security pipeline is for

### Architecture Review
- Review the security module design for gaps
- Suggest improvements to pipeline ordering
- Identify edge cases in PII detection
- Propose new security modules

### Documentation & Ideas
- Suggest features or improvements
- Help with threat modeling
- Share knowledge about AI security best practices
- Provide feedback on the collaborator experience

## Frequently Asked Questions

**Q: Can I see the source code?**
A: Not through this bot. Source access is managed separately by Isaiah.

**Q: What model am I talking to?**
A: The specific model in use is not disclosed — it may change as the system is updated. What you're interacting with is an AI assistant running through the AgentShroud security proxy.

**Q: Why can't I run commands?**
A: Collaborator accounts have tool access restricted. This is intentional — it's part of the security model you're helping test.

**Q: Is my conversation private?**
A: Your conversations are logged for security auditing purposes. They may be reviewed by Isaiah as part of the security assessment. Don't share anything you wouldn't want logged.

**Q: How do I report a vulnerability?**
A: Describe what you found directly in this chat. If it's critical, mention that explicitly so it gets prioritized.

**Q: Can I use this bot for general questions?**
A: Yes! When you're not actively red teaming, the bot can help with coding, writing, and general technical questions.

---

AgentShroud™ is a trademark of Isaiah Jefferson · First use February 2026 · All rights reserved
Unauthorized use of the AgentShroud name or brand is strictly prohibited · Federal trademark registration pending
