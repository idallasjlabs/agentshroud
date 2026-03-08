# AgentShroud™ — Public Information

_This document contains publicly shareable information about the AgentShroud project.
Collaborators may reference this content freely. Nothing in this file is confidential._

---

## What Is AgentShroud?

AgentShroud™ is an **enterprise-grade transparent security proxy framework** for safe, auditable, and governed deployment of autonomous AI agents.

Think of it as a security gateway that sits between an AI agent (like Claude, GPT, etc.) and the outside world — inspecting, filtering, and governing every interaction.

## The Problem AgentShroud Solves

Autonomous AI agents are powerful but dangerous without oversight:
- They can leak sensitive data (PII, credentials, API keys)
- They can be manipulated via prompt injection attacks
- They can access systems and APIs without proper authorization
- Their actions are often invisible to operators until something goes wrong

AgentShroud provides **transparent, real-time security enforcement** — the agent operates normally while every inbound and outbound message passes through a security pipeline.

## Architecture Overview

AgentShroud operates as a **proxy layer** with multiple security modules:

### Inbound Pipeline (User → Agent)
- **Prompt Injection Defense** — Detects and blocks injection attempts
- **PII Sanitization** — Redacts sensitive data before it reaches the agent
- **Role-Based Access Control (RBAC)** — Enforces per-user permissions
- **Rate Limiting** — Prevents abuse and token exhaustion

### Outbound Pipeline (Agent → User)
- **PII Redaction** — Catches leaked phone numbers, SSNs, credit cards, emails
- **Credential Blocking** — Prevents API keys, tokens, and secrets from leaking
- **Information Disclosure Filter** — Blocks internal infrastructure details
- **Encoding Bypass Detection** — Catches base64/URL-encoded exfiltration attempts
- **Output Canary (Tripwire)** — Detects if planted markers leak, proving data theft
- **XML Injection Filter** — Strips hallucinated tool calls from output

### Governance Layer
- **Egress Firewall** — Controls which external domains/APIs the agent can access
- **Approval Queue** — Requires human approval for sensitive outbound actions
- **MCP Tool Proxy** — Inspects and governs Model Context Protocol tool calls
- **Audit Trail** — Every action logged for compliance and forensics

## Key Differentiators

1. **Transparent Proxy** — Works with any AI agent framework (OpenClaw, LangChain, etc.) without modifying the agent
2. **Defense in Depth** — Multiple independent security layers, each fail-closed
3. **Multi-Platform** — Supports Telegram, email, iMessage, Slack, Discord
4. **Self-Hosted** — Runs on your infrastructure (Docker), no cloud dependency
5. **Open Architecture** — Modular security modules, each independently testable

## Current Status

- **Version:** 0.8.0 (enforcement hardening phase)
- **Stage:** Private beta / Active development
- **Test Suite:** 2,391 automated tests, all passing
- **Platforms Supported:** Telegram (primary), email (Gmail), iMessage
- **Infrastructure:** Runs on Docker across ARM64 (Raspberry Pi, Mac) and x86_64

## Technology Stack

- **Gateway:** Python (FastAPI) — security proxy, PII detection, pipeline orchestration
- **Agent Runtime:** Node.js (OpenClaw) — AI agent hosting and tool management
- **Deployment:** Docker Compose with multi-host support
- **AI Models:** Anthropic Claude (Opus, Sonnet) via API
- **Identity:** 1Password for secrets management

## How to Contribute

AgentShroud welcomes collaborator input in these areas:

### Red Team Testing
- Test the security pipeline by attempting to extract sensitive data
- Try prompt injection attacks and report findings
- Attempt to bypass rate limits, tool restrictions, or isolation

### Architecture Review
- Review the security module design for gaps
- Suggest improvements to the pipeline ordering
- Identify edge cases in PII detection or encoding bypass

### Documentation
- Help improve public-facing documentation
- Write guides for deployment or configuration
- Create threat models and attack trees

### Code Review
- Review Python gateway code for security issues
- Suggest test coverage improvements
- Identify performance bottlenecks

## What Collaborators Cannot Access

For security reasons, collaborators do not have access to:
- Internal files, source code, or configuration
- Shell commands or system tools
- Other users' session data or message history
- Credentials, API keys, or secrets
- Infrastructure details (hostnames, IPs, ports)

## Contact

- **Project Owner:** Isaiah Jefferson
- **Project Email:** agentshroud.ai@gmail.com
- **Communication:** Via this Telegram bot

---

AgentShroud™ is a trademark of Isaiah Jefferson · First use February 2026 · All rights reserved
Unauthorized use of the AgentShroud name or brand is strictly prohibited · Federal trademark registration pending
