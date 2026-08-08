---
source_file: "docs/vault/03 - Configuration/falco-rules.md"
type: "document"
community: "docs/vault"
location: "docker/falco/rules.yaml"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/vault
---

# falco-rules.yaml (runtime security rules — shell spawn, outbound, privilege escalation)

## Connections
- [[Falco rule Container Shell Spawned (WARNING — allowed for startup scripts only)]] - `defines` [EXTRACTED]
- [[Falco rule Crypto Mining Detection (CRITICAL — known miners or stratum protocol)]] - `defines` [EXTRACTED]
- [[Falco rule Privilege Escalation Attempt (CRITICAL — sudosusetuidchmod+s)]] - `defines` [EXTRACTED]
- [[Falco rule Unexpected Outbound Connection (ERROR — non-RFC1918 from bot container)]] - `defines` [EXTRACTED]
- [[agentshroud-bot service (docker-compose port 18789, 4GB memory, isolated network)]] - `monitors` [EXTRACTED]
- [[wazuh-ossec.conf (SIEMHIDS — gateway logs, FIM on agentshroud.yaml and secrets)]] - `complements` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/vault