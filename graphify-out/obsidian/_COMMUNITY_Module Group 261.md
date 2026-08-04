---
type: community
cohesion: 0.13
members: 17
---

# Module Group 261

**Cohesion:** 0.13 - loosely connected
**Members:** 17 nodes

## Members
- [[34 Security Modules Matrix (v0.8.0 pii_sanitizer, approval_queue, security_pipeline, prompt_guard, trust_manager, egress_filter, etc.)]] - concept - docs/claude-security-audit-prompt.md
- [[7-Layer Security Pipeline (76 modules L1 Core, L2 Middleware, L3 Output, L4 Tool, L5 Network, L6 File, L7 Infra)]] - concept - docs/architecture/agentic-os.md
- [[ADR-008 Progressive Trust Levels for Agents]] - rationale - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[ADR-009 supersedes ADR-002 (Default-Allow Security Philosophy)]] - rationale - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[ADR-009 Enforce-by-Default Security Philosophy]] - rationale - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[AgentShroud Schema Documentation]] - document - docs/data/schema-documentation.md
- [[AgentShroud v0.8.0 Security & Functionality Audit Prompt]] - document - docs/claude-security-audit-prompt.md
- [[Collaborator Isolation Architecture (no exec, no owner memory, no credentials, mandatory disclosure)]] - concept - docs/claude-security-audit-prompt.md
- [[Egress Configuration Schema (DNS filtering, URL analysis, SSRF protection, MCP access control, network policy)]] - concept - docs/data/schema-documentation.md
- [[Enforce-by-Default Policy (all modules mode enforce, v0.8.0+)]] - concept - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[MCP Configuration Schema (filesystem, web, ssh servers; tool-specific rate limits and trust requirements)]] - concept - docs/data/schema-documentation.md
- [[Open Security Findings (C3-C5 Bot token in debug, root metrics no-auth, H4-H7 network isolation, ws-token, path traversal, error disclosure)]] - document - docs/claude-security-audit-prompt.md
- [[Progressive Trust Level System (Levels 0-4)]] - concept - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[Steve Hay STPA-Sec Assessment (Feb 2026) - 0% enforcement against vanilla OpenClaw]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[TokenBucket Rate Limiter Implementation (max_tokens, refill_rate, blocked_until)]] - code - docs/data/schema-documentation.md
- [[Trust Score Calculation (base + behavioral + compliance - violations - anomaly)]] - concept - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[agentshroud.yaml Main Configuration Schema (gateway, security, audit, approval, rate_limiting, proxy, monitoring)]] - concept - docs/data/schema-documentation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_261
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 346]]
- 1 edge to [[_COMMUNITY_Module Group 415]]
- 1 edge to [[_COMMUNITY_Module Group 262]]

## Top bridge nodes
- [[Progressive Trust Level System (Levels 0-4)]] - degree 5, connects to 2 communities
- [[AgentShroud Schema Documentation]] - degree 5, connects to 1 community
- [[7-Layer Security Pipeline (76 modules L1 Core, L2 Middleware, L3 Output, L4 Tool, L5 Network, L6 File, L7 Infra)]] - degree 3, connects to 1 community
