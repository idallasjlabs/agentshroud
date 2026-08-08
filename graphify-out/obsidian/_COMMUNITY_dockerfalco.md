---
type: community
cohesion: 0.12
members: 17
---

# docker/falco

**Cohesion:** 0.12 - loosely connected
**Members:** 17 nodes

## Members
- [[Container Port Reference Table]] - rationale - docker/README.md
- [[Container Stack Architecture (gateway + openclaw + hermes + hci)]] - concept - docker/README.md
- [[Credential Isolation (gateway as sole credential holder via op-proxy)]] - concept - docs/SECURITY_PLAN.md
- [[Docker Compose --profile full (activates Hermes + HCI)]] - concept - docker/README.md
- [[Docker Configuration README]] - document - docker/README.md
- [[Docker Network Isolation (agentshroud-internal 172.20.016, agentshroud-isolated 172.21.016)]] - concept - docker/README.md
- [[Docker Quickstart Guide]] - document - docker/QUICKSTART.md
- [[Docker VPN Networking Fix (Cisco AnyConnect + vpnkit-userspace)]] - document - docker/DOCKER-VPN-NETWORKING.md
- [[Falco Configuration (falco.yaml)]] - code - docker/falco/falco.yaml
- [[Falco Rule Container Shell Spawned]] - concept - docker/falco/rules.yaml
- [[Falco Rule Privilege Escalation Attempt]] - concept - docker/falco/rules.yaml
- [[Falco Rule Secret File Access]] - concept - docker/falco/rules.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Falco Runtime Security (eBPF kernel monitoring)]] - concept - docker/falco/falco.yaml
- [[Falco Security Rules (rules.yaml)]] - code - docker/falco/rules.yaml
- [[Security Hardening Phases P0–FINAL]] - concept - docs/SECURITY_PLAN.md
- [[VPNKit Userspace Networking Mode (Docker Desktop fix)]] - concept - docker/DOCKER-VPN-NETWORKING.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/falco
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_docsvault]]

## Top bridge nodes
- [[Security Hardening Phases P0–FINAL]] - degree 3, connects to 1 community