---
type: community
cohesion: 0.07
members: 29
---

# AgentShroud Deployment Architecture

**Cohesion:** 0.07 - loosely connected
**Members:** 29 nodes

## Members
- [[ADR-001 Transparent Proxy Decision]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[ADR-007 Zero-Config Security]] - concept - docs/architecture/adr/ADR-007-zero-config-security.md
- [[Agent Modification Approach (rejected alternative)]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[AgentShroud Deployment Architecture]] - document - docs/architecture/deployment-diagram.md
- [[Apple Containers (macOS)]] - document - docs/architecture/deployment-diagram.md
- [[Cloud Provider Secrets]] - document - docs/architecture/deployment-diagram.md
- [[DNS Routing Configuration]] - document - docs/architecture/deployment-diagram.md
- [[Default Port Allocation]] - document - docs/architecture/deployment-diagram.md
- [[Deployment Modes_1]] - document - docs/architecture/deployment-diagram.md
- [[Deployment Validation]] - document - docs/architecture/deployment-diagram.md
- [[Docker Runtime]] - document - docs/architecture/deployment-diagram.md
- [[Docker Secrets]] - document - docs/architecture/deployment-diagram.md
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[HashiCorp Vault Integration]] - document - docs/architecture/deployment-diagram.md
- [[Multi-Instance Support]] - document - docs/architecture/deployment-diagram.md
- [[Multi-Runtime Support_1]] - document - docs/architecture/deployment-diagram.md
- [[Network Topology]] - document - docs/architecture/deployment-diagram.md
- [[Overview_9]] - document - docs/architecture/deployment-diagram.md
- [[Persistent Storage Architecture]] - document - docs/architecture/deployment-diagram.md
- [[Podman Support]] - document - docs/architecture/deployment-diagram.md
- [[Port Mappings and Auto-Detection]] - document - docs/architecture/deployment-diagram.md
- [[Proxy Mode (Recommended)_1]] - document - docs/architecture/deployment-diagram.md
- [[Secrets Management Integration]] - document - docs/architecture/deployment-diagram.md
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[Three-Network Architecture]] - document - docs/architecture/deployment-diagram.md
- [[Volume Mounts and Secrets Management]] - document - docs/architecture/deployment-diagram.md
- [[Zero-Configuration Deployment]] - document - docs/architecture/deployment-diagram.md
- [[deployment-diagram]] - document - docs/architecture/deployment-diagram.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Deployment_Architecture
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]

## Top bridge nodes
- [[Gateway (FastAPI)]] - degree 4, connects to 2 communities
