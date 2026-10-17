---
type: community
members: 20
---

# docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)

**Members:** 20 nodes

## Members
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - code - docker/docker-compose.yml
- [[Dev Hermes polled prod's Hermes Telegram bot token all night]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - concept - docker/docker-compose.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - rationale - docker/docker-compose.yml
- [[agentshroud-secrets.sh script]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[dockerbotshermesagentshroud-secrets.sh (s6 cont-init secret injection)]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - code - docker/docker-compose.yml
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[inject()]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - code - docker/docker-compose.yml
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - code - docker/scripts/start-agentshroud.sh
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - code - docker/docker-compose.yml
- [[wazuh-manager service (4.14.8, isolated-network only, open enrollment)]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes) (2)]]
- 2 edges to [[_COMMUNITY_LLMProxy (2)]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh (2)]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 1 edge to [[_COMMUNITY_dashboard_bridge.py]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill (2) (2)]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions (2)]]

## Top bridge nodes
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - degree 11, connects to 3 communities
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - degree 6, connects to 3 communities
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - degree 8, connects to 2 communities
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - degree 8, connects to 2 communities
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - degree 4, connects to 1 community
