---
type: community
cohesion: 0.07
members: 34
---

# Module Group 138

**Cohesion:** 0.07 - loosely connected
**Members:** 34 nodes

## Members
- [[AgentShroud Architecture Diagram (Gateway to Bot Layer)]] - document - README.md
- [[AgentShroud Gateway (Core Security Proxy)]] - concept - README.md
- [[AgentShroud Product Overview Enterprise Governance Proxy]] - document - README.md
- [[AgentShroud Quickstart (Prerequisites, Clone, Secrets, Start)]] - document - README.md
- [[AgentShroud Security Hardening Plan]] - document - docs/SECURITY_PLAN.md
- [[Apple Platform Integration (Roadmap — WidgetKit, APNs, WatchOS)]] - concept - docs/ROADMAP-POST-v1.0.md
- [[Collaborator Isolation (read-only advisory access)]] - concept - docker/bots/openclaw/config/workspace/PUBLIC-INFO.md
- [[Credential Isolation (gateway as sole credential holder via op-proxy)]] - concept - docs/SECURITY_PLAN.md
- [[Docker Network Isolation (agentshroud-internal 172.20.016, agentshroud-isolated 172.21.016)]] - concept - docker/README.md
- [[Docker Scripts README]] - document - docker/scripts/README.md
- [[Docker VPN Networking Fix (Cisco AnyConnect + vpnkit-userspace)]] - document - docker/DOCKER-VPN-NETWORKING.md
- [[Documentation Index (docsREADME.md)]] - document - docs/README.md
- [[Dual Network Topology external + internal (isolated)]] - rationale - docker-compose.secure.yml
- [[Falco Configuration (falco.yaml)]] - code - docker/falco/falco.yaml
- [[Falco Rule Container Shell Spawned]] - concept - docker/falco/rules.yaml
- [[Falco Rule Privilege Escalation Attempt]] - concept - docker/falco/rules.yaml
- [[Falco Rule Secret File Access]] - concept - docker/falco/rules.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Falco Runtime Security (eBPF kernel monitoring)]] - concept - docker/falco/falco.yaml
- [[Falco Security Rules (rules.yaml)]] - code - docker/falco/rules.yaml
- [[OpenClaw Bot (Node.js AI Agent under Governance)]] - concept - README.md
- [[OpenClaw Config Workspace PUBLIC-INFO]] - document - docker/bots/openclaw/config/workspace/PUBLIC-INFO.md
- [[OpenClaw Container Isolation No Port Mapping, DNS via Gateway]] - code - docker-compose.secure.yml
- [[OpenClaw Memory Context]] - document - docker/config/openclaw/workspace/memory/context.md
- [[OpenClaw Open-source AI Agent Framework Acknowledgment]] - document - README.md
- [[Post-v1.0.0 Roadmap]] - document - docs/ROADMAP-POST-v1.0.md
- [[Prompt Injection Defense (PromptGuard + MCPInspector)]] - concept - docs/SECURITY_PLAN.md
- [[Security Hardening Phases P0–FINAL]] - concept - docs/SECURITY_PLAN.md
- [[Sidecar Mode Warning Does Not Guarantee All Traffic Scanned]] - rationale - docker-compose.sidecar.yml
- [[Tailscale Secure Remote Access (All Control Surfaces)]] - concept - CLAUDE.md
- [[VPNKit Userspace Networking Mode (Docker Desktop fix)]] - concept - docker/DOCKER-VPN-NETWORKING.md
- [[Web Control Center 7-Page Dashboard]] - document - README.md
- [[docker-compose.secure.yml Full Network Isolation Proxy Mode]] - code - docker-compose.secure.yml
- [[docker-compose.sidecar.yml Optional Sidecar Scanning Mode]] - code - docker-compose.sidecar.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_138
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Module Group 105]]
- 8 edges to [[_COMMUNITY_Module Group 174]]
- 4 edges to [[_COMMUNITY_Module Group 192]]
- 1 edge to [[_COMMUNITY_Module Group 191]]
- 1 edge to [[_COMMUNITY_Module Group 500]]

## Top bridge nodes
- [[AgentShroud Gateway (Core Security Proxy)]] - degree 22, connects to 3 communities
- [[OpenClaw Bot (Node.js AI Agent under Governance)]] - degree 9, connects to 2 communities
- [[Docker Network Isolation (agentshroud-internal 172.20.016, agentshroud-isolated 172.21.016)]] - degree 6, connects to 2 communities
- [[AgentShroud Product Overview Enterprise Governance Proxy]] - degree 6, connects to 2 communities
- [[AgentShroud Security Hardening Plan]] - degree 9, connects to 1 community
