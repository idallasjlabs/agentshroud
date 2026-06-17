---
type: community
cohesion: 0.29
members: 7
---

# Module Group 453

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[Falco rule Container Shell Spawned (WARNING — allowed for startup scripts only)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/falco-rules.md
- [[Falco rule Crypto Mining Detection (CRITICAL — known miners or stratum protocol)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/falco-rules.md
- [[Falco rule Privilege Escalation Attempt (CRITICAL — sudosusetuidchmod+s)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/falco-rules.md
- [[Falco rule Unexpected Outbound Connection (ERROR — non-RFC1918 from bot container)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/falco-rules.md
- [[Wazuh File Integrity Monitoring (agentshroud.yaml, secrets dir)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/wazuh-ossec.md
- [[falco-rules.yaml (runtime security rules — shell spawn, outbound, privilege escalation)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/falco-rules.md
- [[wazuh-ossec.conf (SIEMHIDS — gateway logs, FIM on agentshroud.yaml and secrets)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/wazuh-ossec.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_453
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Module Group 344]]
- 1 edge to [[_COMMUNITY_Module Group 326]]

## Top bridge nodes
- [[falco-rules.yaml (runtime security rules — shell spawn, outbound, privilege escalation)]] - degree 6, connects to 1 community
- [[Wazuh File Integrity Monitoring (agentshroud.yaml, secrets dir)]] - degree 2, connects to 1 community