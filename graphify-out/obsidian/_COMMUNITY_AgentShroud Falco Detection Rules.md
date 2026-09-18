---
type: community
cohesion: 0.20
members: 16
---

# AgentShroud Falco Detection Rules

**Cohesion:** 0.20 - loosely connected
**Members:** 16 nodes

## Members
- [[AgentShroud Falco Detection Rules]] - document - docker/falco/rules.yaml
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Falco Rule Unexpected Outbound Connection from AgentShroud]] - concept - docker/falco/rules.yaml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Falco_Detection_Rules
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]
- 1 edge to [[_COMMUNITY_bot-access-audit.sh]]
- 1 edge to [[_COMMUNITY_Marvin Dev Overlay (port and subnet offsets from]]
- 1 edge to [[_COMMUNITY_security-entrypoint.sh]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]

## Top bridge nodes
- [[Rule Container Shell Spawned]] - degree 5, connects to 2 communities
- [[container macro (always-true placeholder inside the gateway)]] - degree 7, connects to 1 community
- [[Rule Secret File Access]] - degree 5, connects to 1 community
- [[Falco Rule Unexpected Outbound Connection from AgentShroud]] - degree 2, connects to 1 community