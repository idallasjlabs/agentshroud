---
type: community
cohesion: 0.10
members: 26
---

# TestOutboundClassifierHelpers

**Cohesion:** 0.10 - loosely connected
**Members:** 26 nodes

## Members
- [[AGENTSHROUD_GATEWAY_CONTAINER Override (renamed container breaks CVE scan)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[AgentShroud Daily Check-in (disabled — bot-identity-locked to dev)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[AgentShroud Falco Detection Rules]] - document - docker/falco/rules.yaml
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Falco Rule Unexpected Outbound Connection from AgentShroud]] - concept - docker/falco/rules.yaml
- [[Gateway Service]] - code - docker/docker-compose.yml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Marvin Dev Overlay (port and subnet offsets from prod)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[Wazuh Agent Service]] - code - docker/docker-compose.yml
- [[bot-access-audit.sh]] - code - docker/scripts/bot-access-audit.sh
- [[bot-access-audit.sh script]] - code - docker/scripts/bot-access-audit.sh
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md
- [[run_op()]] - code - docker/scripts/bot-access-audit.sh
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundClassifierHelpers
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_Discovery Strategy]]
- 1 edge to [[_COMMUNITY_What You Must Do When Invoked]]

## Top bridge nodes
- [[Rule Container Shell Spawned]] - degree 5, connects to 2 communities
- [[Falco Rule Unexpected Outbound Connection from AgentShroud]] - degree 2, connects to 1 community