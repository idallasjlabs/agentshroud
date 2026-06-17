---
type: community
cohesion: 0.18
members: 11
---

# Module Group 341

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[ADR-001 (docsadr) Proxy-Layer Inversion Model]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/adr/ADR-001-proxy-layer-inversion.md
- [[ADR-001 Decision Transparent Proxy — zero modification for existing OpenClaw, separation of concerns, auditable]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-001 Transparent Proxy vs Agent Modification]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-003 Two-Network Container Isolation]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-003-two-network-container-isolation.md
- [[ADR-004 API Keys Never in Agent Container]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[ADR-007 Zero-Config Security (docker-compose up = fully secured)]] - rationale - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-007-zero-config-security.md
- [[AgentShroud Governance Proxy Transparent proxy between AI agents and external systems]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/USPTO_PROVISIONAL_PATENT_APPLICATION.md
- [[Interception Mechanisms HTTPHTTPS Proxy, API Endpoint Rewriting, SDK-Level Patching, SSH Proxy, WebSocket Relay]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/USPTO_PROVISIONAL_PATENT_APPLICATION.md
- [[Proxy-Side API Key Management Keys in AgentShroud only, injected into requests per destination pattern]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[Two-Network Architecture agentshroud_external (172.20.0.024) + agentshroud_internal (172.21.0.024); Gateway dual-homed]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-003-two-network-container-isolation.md
- [[Zero-Config Hierarchy Hardcoded Defaults → Environment Detection → Env Vars → Config Files]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/architecture/adr/ADR-007-zero-config-security.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_341
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 342]]

## Top bridge nodes
- [[AgentShroud Governance Proxy Transparent proxy between AI agents and external systems]] - degree 5, connects to 1 community
- [[Interception Mechanisms HTTPHTTPS Proxy, API Endpoint Rewriting, SDK-Level Patching, SSH Proxy, WebSocket Relay]] - degree 2, connects to 1 community