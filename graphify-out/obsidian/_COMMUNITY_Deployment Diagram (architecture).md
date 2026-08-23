---
type: community
cohesion: 0.07
members: 31
---

# Deployment Diagram (architecture)

**Cohesion:** 0.07 - loosely connected
**Members:** 31 nodes

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
- [[Deployment Modes]] - document - docs/architecture/deployment-diagram.md
- [[Deployment Validation]] - document - docs/architecture/deployment-diagram.md
- [[Docker Runtime]] - document - docs/architecture/deployment-diagram.md
- [[Docker Secrets]] - document - docs/architecture/deployment-diagram.md
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[HashiCorp Vault Integration]] - document - docs/architecture/deployment-diagram.md
- [[Multi-Instance Support]] - document - docs/architecture/deployment-diagram.md
- [[Multi-Runtime Support_1]] - document - docs/architecture/deployment-diagram.md
- [[Network Topology]] - document - docs/architecture/deployment-diagram.md
- [[Overview_6]] - document - docs/architecture/deployment-diagram.md
- [[PII Sanitizer (Presidio + Regex)]] - concept - docs/architecture/system-architecture.md
- [[Persistent Storage Architecture]] - document - docs/architecture/deployment-diagram.md
- [[Podman Support]] - document - docs/architecture/deployment-diagram.md
- [[Port Mappings and Auto-Detection]] - document - docs/architecture/deployment-diagram.md
- [[Proxy Mode (Recommended)]] - document - docs/architecture/deployment-diagram.md
- [[Secrets Management Integration]] - document - docs/architecture/deployment-diagram.md
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[Three-Network Architecture]] - document - docs/architecture/deployment-diagram.md
- [[Volume Mounts and Secrets Management]] - document - docs/architecture/deployment-diagram.md
- [[Zero-Configuration Deployment]] - document - docs/architecture/deployment-diagram.md
- [[deployment-diagram]] - document - docs/architecture/deployment-diagram.md
- [[sanitizer.py (PII redaction, Presidioregex)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Deployment_Diagram_architecture
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Diagram 01 C4 Context (images)]]
- 1 edge to [[_COMMUNITY_Diagram 07 Data Flow (images)]]

## Top bridge nodes
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[PII Sanitizer (Presidio + Regex)]] - degree 3, connects to 1 community