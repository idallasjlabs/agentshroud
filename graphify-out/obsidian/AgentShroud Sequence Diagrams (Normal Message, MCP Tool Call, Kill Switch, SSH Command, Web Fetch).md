---
source_file: "docs/flows/sequence-diagrams.md"
type: "document"
community: "Module Group 238"
location: "line 1"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_238
---

# AgentShroud Sequence Diagrams (Normal Message, MCP Tool Call, Kill Switch, SSH Command, Web Fetch)

## Connections
- [[Kill Switch Activation Flow (Admin → Dashboard → KillSw → Gateway → all proxies stop → audit → notify)]] - `contains` [EXTRACTED]
- [[SSH Command Flow (Agent → SSHProxy → Injection Check → Approval Queue → Execute → Audit)]] - `contains` [EXTRACTED]
- [[Web Fetch Flow (Agent → WebProxy → URL Analyzer → DNS Check → WebFetch → ContentScan → Agent)]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_238
