---
type: community
cohesion: 0.18
members: 11
---

# Module Group 344

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[AGENTSHROUD_CONFIG (env var — explicit path to agentshroud.yaml)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[AGENTSHROUD_MODE (env var — enforcemonitor global security module override)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[HTTP_PROXY  HTTPS_PROXY (env var — network-layer egress via gateway port 8181, currently disabled)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/HTTP_PROXY.md
- [[SSH client config (bot container — pimarvin hosts, key-only auth, StrictHostKeyChecking)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/ssh-config.md
- [[agentshroud.yaml (master gateway configuration file)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[agentshroud.yaml mcp_proxy section (per-servertool MCP permissions)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[agentshroud.yaml proxy section (egress allowlist, port 8181)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[agentshroud.yaml security section (PII, approval queue, network isolation)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[agentshroud.yaml security_modules section (per-module enforcemonitor mode)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[agentshroud.yaml ssh section (SSH host allowlist, denied commands)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/agentshroud.yaml.md
- [[pyyaml (≥6.0.0 — parse agentshroud.yaml config file)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/05 - Dependencies/All Dependencies.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_344
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 326]]
- 1 edge to [[_COMMUNITY_Module Group 453]]
- 1 edge to [[_COMMUNITY_Module Group 370]]

## Top bridge nodes
- [[agentshroud.yaml (master gateway configuration file)]] - degree 10, connects to 2 communities
- [[SSH client config (bot container — pimarvin hosts, key-only auth, StrictHostKeyChecking)]] - degree 2, connects to 1 community
- [[pyyaml (≥6.0.0 — parse agentshroud.yaml config file)]] - degree 2, connects to 1 community