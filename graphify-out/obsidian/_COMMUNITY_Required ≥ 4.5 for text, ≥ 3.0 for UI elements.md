---
type: community
cohesion: 0.14
members: 15
---

# Required: ≥ 4.5 for text, ≥ 3.0 for UI elements

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[Autonomous remote dev workflows (hdev, odev)]] - concept - .llm_settings/docs/SKILLS_REFERENCE.md
- [[Credential isolation — keys live only in the gateway]] - rationale - docker-compose.secure.yml
- [[Gateway DNS filter endpoint (port 53)]] - concept - docker-compose.secure.yml
- [[MCP servers confined to the internal network]] - rationale - docker-compose.secure.yml
- [[PostgreSQL ~.pgpass password management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[agentshroud-external network]] - code - docker-compose.secure.yml
- [[agentshroud-gateway service (proxy mode)]] - code - docker-compose.secure.yml
- [[agentshroud-internal network (no external access)]] - code - docker-compose.secure.yml
- [[direnv-based environment variable management]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[external network (gateway host-facing bridge)]] - code - docker-compose.secure.yml
- [[internal network (isolated, internaltrue)]] - code - docker-compose.secure.yml
- [[openclaw service (internal network only)]] - code - docker-compose.secure.yml
- [[openclaw service (proxy mode, internal-only network)]] - code - docker-compose.secure.yml
- [[wazuh service (proxy-mode HIDS sidecar)]] - code - docker-compose.secure.yml
- [[wazuh-agent sidecar (pinned 4.14.7)]] - code - docker-compose.secure.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Required__45_for_text__30_for_UI_elements
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Proxy mode — full network isolation + egress control]]
- 1 edge to [[_COMMUNITY_Skill Test-Driven Development (TDD)]]

## Top bridge nodes
- [[agentshroud-gateway service (proxy mode)]] - degree 6, connects to 1 community
- [[Autonomous remote dev workflows (hdev, odev)]] - degree 2, connects to 1 community
