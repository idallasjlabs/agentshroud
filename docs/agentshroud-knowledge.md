AgentShroud™ — Knowledge Reference
Upload this file to the GPT's Knowledge section

The 25-Domain Prompt Injection Defense Framework
AgentShroud defends across 25 domains including: direct and indirect injection (documents, emails, web, OCR, audio transcription), cross-agent laundering, multi-agent chain abuse, memory poisoning, retrieval poisoning, authority confusion, role hijacking, goal hijacking, long-horizon multi-step attacks, data exfiltration via hidden channels, and evaluation evasion.

Maturity model: 10 layers — Policy / Context / Reasoning / Action / Execution / Egress / Memory+RAG / Observability / Approval / Recovery.

SOC Command Center — Five Pillars Detail
Pillar 1 — Security Operations Real-time threat and alert feed, injection detection events, block and rate-limit logs with reason codes, suspicious activity flagging, egress approval workflows (approve / deny / quarantine), policy enforcement status, security event history. Operators can detect and respond to a compromised agent without relying on the agent's self-reporting.

Pillar 2 — Platform Operations Start, stop, restart, rebuild, upgrade, and recover gateways, bots, containers, and supporting services. Full lifecycle management from one interface.

Pillar 3 — Contributor Management Manage contributors and collaborators, process contribution requests, approve new tools, govern operational workflows, track contributor activity against policy.

Pillar 4 — Observability Logs, health metrics, alarms, version tracking, runtime status, dependency visibility, direct console access. Full audit trail of every proxied action.

Pillar 5 — Multi-Interface Control Web for visibility and governance, CLI for power users and automation, Telegram for conversational operations. All three have full feature parity.

Collaborator System — Full Detail
Originally built to gather feedback from trusted friends. The architecture it produced is a multi-user agentic workspace: multiple humans sharing a single autonomous agent through governed channels. Each collaborator is scoped to specific capabilities, separately attributed, and auditable. Project owners retain full governance visibility. Contribution requests flow through approval before becoming active. The Telegram bot is the primary conversational entry point. This turns a feedback mechanism into a lightweight team collaboration layer with built-in security controls.

Agents AgentShroud Targets
OpenClaw — dominant autonomous agent framework (~287K GitHub stars). Primary integration target.
PicoClaw — Go-based, runs on minimal hardware
NanoClaw — containerized by default, Anthropic Agents SDK, multi-platform
NanoBot — ultra-lightweight (~4,000 lines), from HKU
memU — agentic memory framework for 24/7 proactive agents
CrocBot — Telegram-first, hardened OpenClaw fork
Competitive Positioning
AgentShroud is a security tool for agents — not an agent itself.

Direct competitors: Lakera Guard, Prompt Security (SentinelOne), CalypsoAI, Lasso Security, Cequence AI Gateway — all operate at the content layer, not the proxy layer.

Adjacent: Arcade.dev, Okta AI Identity, CyberArk (identity/auth focus). Gravitee, Maxim AI Bifrost (framework-level).

AgentShroud's differentiator: Proxy-layer inversion. No competitor enforces security at the proxy layer with assumed model compromise as the foundational threat model. Competitors trust the model to behave. AgentShroud does not. Benchmark: 26/26 vs. 0–4/26 for competitors.

Roadmap
v0.9.5 — Foundation Hardening

Taint tracking and data lineage, per-task credential scoping, tool-call argument normalization and replay protection, RAG quarantine pipeline, context overflow detection, system prompt re-anchoring, formal blue-team assessment.

v0.9.8 — Defense Depth

Cross-agent communication governance, memory and session integrity, scratchpad isolation, multi-tenant isolation, homoglyph/Unicode library expansion, scope-baseline anomaly detection, expanded red-team coverage.

v1.0.0 — Operational Maturity

SOC Command Center GA (all three interfaces), enterprise integrations (GitHub, Atlassian, AWS), policy-as-code, approval workflow completion, documentation reflecting actual code state, public open-source release.

Post-v1.0.0 (planned, subject to update after v1.0.0 access is finalized)

External versioned API, plugin marketplace with security review, Apple Container Framework integration, Nix flakes for reproducible builds, multi-agent trust and delegation model, enterprise SSO and RBAC, automated threat intelligence feeds, community contributor program using AgentShroud's own proxy as the trust boundary.

Infrastructure and Dev Tools
Host: macOS / Apple Silicon (marvin), Raspberry Pi (raspberrypi) via Tailscale
Containers: Colima (VZ driver), Docker, Debian-based images
Secrets: 1Password CLI
Scripting: Bash, Python (Telethon for Telegram)
Observability: tmux dashboard, cwatch (container monitor), logrotate
Deployment: llm-init.sh (multi-host init script)
Integrations: Telegram Bot API, MCP servers, GitHub, Atlassian, AWS
AgentShroud™ is a trademark of its creator. All rights reserved.
