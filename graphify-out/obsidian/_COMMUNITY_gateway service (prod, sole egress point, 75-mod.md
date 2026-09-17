---
type: community
cohesion: 0.06
members: 41
---

# gateway service (prod, sole egress point, 75-mod

**Cohesion:** 0.06 - loosely connected
**Members:** 41 nodes

## Members
- [[75 Active Security Modules — no stubs, fully wired]] - rationale - CLAUDE.md
- [[Autonomous remote dev workflows (hdev, odev)]] - concept - .llm_settings/docs/SKILLS_REFERENCE.md
- [[CI DAST scan job (Nuclei, self-hosted)]] - code - .github/workflows/ci.yml
- [[CI job dast (Nuclei scan, workflow_dispatch only)]] - code - .github/workflows/ci.yml
- [[Credential isolation — keys live only in the gateway]] - rationale - docker-compose.secure.yml
- [[Docker sidecar integrity — falcoclamavfluent-bit in-process, wazuh-agent standalone sidecar]] - rationale - CLAUDE.md
- [[Gateway DNS filter endpoint (port 53)]] - concept - docker-compose.secure.yml
- [[MCP servers confined to the internal network]] - rationale - docker-compose.secure.yml
- [[OpenClaw cron AI Security Standards Watch (OWASPNISTISOMAESTROATLAS)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily CVE Triage & Remediation Scan (cites agent_cve_registry.py)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[PostgreSQL ~.pgpass password management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[Proxy mode — full network isolation + egress control]] - concept - docker-compose.secure.yml
- [[Sidecar mode — optional security scanning]] - concept - docker-compose.sidecar.yml
- [[agentshroud-external network]] - code - docker-compose.secure.yml
- [[agentshroud-gateway service (proxy mode)]] - code - docker-compose.secure.yml
- [[agentshroud-gateway service (sidecar mode)]] - code - docker-compose.sidecar.yml
- [[agentshroud-gateway service (sidecar mode, optional scan)]] - code - docker-compose.sidecar.yml
- [[agentshroud-internal network (EDGE tier, internet-facing)]] - code - docker/docker-compose.yml
- [[agentshroud-internal network (no external access)]] - code - docker-compose.secure.yml
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - code - docker/docker-compose.yml
- [[deepseek-r1-0528-qwen3-8b 404 — alias mismatched oMLX real catalog ID]] - rationale - CHANGELOG.md
- [[direnv-based environment variable management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[docker-socket-proxy service (scoped, no image-pull, digest-pinned)]] - code - docker/docker-compose.yml
- [[external network (gateway host-facing bridge)]] - code - docker-compose.secure.yml
- [[gateway override (marvin dev host, port 9080)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - code - docker/docker-compose.yml
- [[hermes override (marvin dev host, dashboard port 9119)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - code - docker/docker-compose.yml
- [[internal network (isolated, internaltrue)]] - code - docker-compose.secure.yml
- [[openclaw override (marvin dev host, port 18790)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[openclaw service (exposed, sidecar mode)]] - code - docker-compose.sidecar.yml
- [[openclaw service (internal network only)]] - code - docker-compose.secure.yml
- [[openclaw service (prod, isolated network only)]] - code - docker/docker-compose.yml
- [[openclaw service (proxy mode, internal-only network)]] - code - docker-compose.secure.yml
- [[openclaw service (sidecar mode, exposed normally)]] - code - docker-compose.sidecar.yml
- [[shared network (sidecar mode bridge)]] - code - docker-compose.sidecar.yml
- [[voice-gateway override (port 8766 — avoids prod SSH-forwarder port race)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge)]] - code - docker/docker-compose.yml
- [[wazuh service (proxy-mode HIDS sidecar)]] - code - docker-compose.secure.yml
- [[wazuh-agent service (standalone sidecar, split from gateway 2026-09-06)]] - code - docker/docker-compose.yml
- [[wazuh-agent sidecar (pinned 4.14.7)]] - code - docker-compose.secure.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway_service_prod_sole_egress_point_75-mod
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_Claude Code skill catalog (59 skills)]]
- 1 edge to [[_COMMUNITY_run-standalone.sh]]

## Top bridge nodes
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - degree 6, connects to 2 communities
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - degree 13, connects to 1 community
- [[Autonomous remote dev workflows (hdev, odev)]] - degree 2, connects to 1 community