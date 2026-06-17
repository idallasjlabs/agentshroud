---
source_file: "gateway/security/agent_isolation.py"
type: "rationale"
community: "Agent Isolation & Container Config"
location: "L123"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_Isolation__Container_Config
---

# Verify that each agent has its own volume (no shared filesystems).

## Connections
- [[.verify_volume_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_Isolation__Container_Config