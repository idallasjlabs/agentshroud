---
source_file: "gateway/security/agent_isolation.py"
type: "rationale"
community: "AgentRegistry"
location: "L123"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentRegistry
---

# Verify that each agent has its own volume (no shared filesystems).

## Connections
- [[.verify_volume_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentRegistry