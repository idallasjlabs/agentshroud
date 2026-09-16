---
type: community
cohesion: 0.13
members: 16
---

# Community 575

**Cohesion:** 0.13 - loosely connected
**Members:** 16 nodes

## Members
- [[Autonomous remote dev workflows (hdev, odev)]] - concept - .llm_settings/docs/SKILLS_REFERENCE.md
- [[CI DAST scan job (Nuclei, self-hosted)]] - code - .github/workflows/ci.yml
- [[Credential isolation — keys live only in the gateway]] - rationale - docker-compose.secure.yml
- [[Gateway DNS filter endpoint (port 53)]] - concept - docker-compose.secure.yml
- [[MCP servers confined to the internal network]] - rationale - docker-compose.secure.yml
- [[PostgreSQL ~.pgpass password management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[Proxy mode — full network isolation + egress control]] - concept - docker-compose.secure.yml
- [[Sidecar mode — optional security scanning]] - concept - docker-compose.sidecar.yml
- [[agentshroud-external network]] - code - docker-compose.secure.yml
- [[agentshroud-gateway service (proxy mode)]] - code - docker-compose.secure.yml
- [[agentshroud-gateway service (sidecar mode)]] - code - docker-compose.sidecar.yml
- [[agentshroud-internal network (no external access)]] - code - docker-compose.secure.yml
- [[direnv-based environment variable management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[openclaw service (exposed, sidecar mode)]] - code - docker-compose.sidecar.yml
- [[openclaw service (internal network only)]] - code - docker-compose.secure.yml
- [[wazuh-agent sidecar (pinned 4.14.7)]] - code - docker-compose.secure.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_575
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 721]]

## Top bridge nodes
- [[Autonomous remote dev workflows (hdev, odev)]] - degree 2, connects to 1 community