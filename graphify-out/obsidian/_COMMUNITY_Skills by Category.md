---
type: community
cohesion: 0.09
members: 29
---

# Skills by Category

**Cohesion:** 0.09 - loosely connected
**Members:** 29 nodes

## Members
- [[75 Active Security Modules — no stubs, fully wired]] - rationale - CLAUDE.md
- [[CI job dast (Nuclei scan, workflow_dispatch only)]] - code - .github/workflows/ci.yml
- [[Docker sidecar integrity — falcoclamavfluent-bit in-process, wazuh-agent standalone sidecar]] - rationale - CLAUDE.md
- [[Floating-tag containers found (github-mcp-serverlatest, home-assistantstable)]] - concept - reports/upgrade-2026-09-20.md
- [[OpenClaw cron AI Security Standards Watch (OWASPNISTISOMAESTROATLAS)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily CVE Triage & Remediation Scan (cites agent_cve_registry.py)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[agentshroud-gateway service (sidecar mode, optional scan)]] - code - docker-compose.sidecar.yml
- [[agentshroud-internal network (EDGE tier, internet-facing)]] - code - docker/docker-compose.yml
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - code - docker/docker-compose.yml
- [[deepseek-r1-0528-qwen3-8b 404 — alias mismatched oMLX real catalog ID]] - rationale - CHANGELOG.md
- [[docker-socket-proxy service (scoped, no image-pull, digest-pinned)]] - code - docker/docker-compose.yml
- [[gateway override (marvin dev host, port 9080)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - code - docker/docker-compose.yml
- [[gateway service override (dev)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[hermes override (marvin dev host, dashboard port 9119)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - code - docker/docker-compose.yml
- [[internal network (isolated, internaltrue)]] - code - docker-compose.secure.yml
- [[openclaw override (marvin dev host, port 18790)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[openclaw service (prod, isolated network only)]] - code - docker/docker-compose.yml
- [[openclaw service (proxy mode, internal-only network)]] - code - docker-compose.secure.yml
- [[openclaw service (sidecar mode, exposed normally)]] - code - docker-compose.sidecar.yml
- [[openclaw service override (dev)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[shared network (sidecar mode bridge)]] - code - docker-compose.sidecar.yml
- [[voice-gateway override (port 8766 — avoids prod SSH-forwarder port race)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge)]] - code - docker/docker-compose.yml
- [[voice-gateway service override (dev)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[wazuh service (proxy-mode HIDS sidecar)]] - code - docker-compose.secure.yml
- [[wazuh-agent service (standalone sidecar, split from gateway 2026-09-06)]] - code - docker/docker-compose.yml
- [[wazuh-manager service]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skills_by_Category
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Collaborator Setup Checklist]]
- 3 edges to [[_COMMUNITY_TestEgressTargetExtraction]]
- 2 edges to [[_COMMUNITY_AgentShroud Docker Configuration]]
- 2 edges to [[_COMMUNITY_TestCVE2026_9367TerminalToolDenied]]
- 2 edges to [[_COMMUNITY_Plan AgentShroud Security Hardening — Real Agen]]
- 1 edge to [[_COMMUNITY_ssh-configuration]]
- 1 edge to [[_COMMUNITY_Function Details]]
- 1 edge to [[_COMMUNITY_Skill UX Expert (UX)]]
- 1 edge to [[_COMMUNITY_CICD Pipeline Advisor (README)]]

## Top bridge nodes
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - degree 21, connects to 5 communities
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - degree 8, connects to 4 communities
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge)]] - degree 5, connects to 1 community
- [[internal network (isolated, internaltrue)]] - degree 3, connects to 1 community
- [[wazuh-manager service]] - degree 2, connects to 1 community