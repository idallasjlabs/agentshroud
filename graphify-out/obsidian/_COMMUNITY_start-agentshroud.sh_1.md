---
type: community
cohesion: 0.15
members: 17
---

# start-agentshroud.sh

**Cohesion:** 0.15 - loosely connected
**Members:** 17 nodes

## Members
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[bot-access-audit.sh]] - code - docker/scripts/bot-access-audit.sh
- [[bot-access-audit.sh script]] - code - docker/scripts/bot-access-audit.sh
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md
- [[run_op()]] - code - docker/scripts/bot-access-audit.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh_2]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]

## Top bridge nodes
- [[Rule Container Shell Spawned]] - degree 4, connects to 2 communities
- [[container macro (always-true placeholder inside the gateway)]] - degree 7, connects to 1 community
- [[Falco Rule Unexpected Outbound Connection]] - degree 2, connects to 1 community
