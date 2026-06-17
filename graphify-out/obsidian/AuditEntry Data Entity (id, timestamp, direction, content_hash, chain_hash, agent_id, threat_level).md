---
source_file: "docs/data/data-dictionary.md"
type: "concept"
community: "Module Group 346"
location: "line 7"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Module_Group_346
---

# AuditEntry Data Entity (id, timestamp, direction, content_hash, chain_hash, agent_id, threat_level)

## Connections
- [[AgentShroud Data Dictionary]] - `defines` [EXTRACTED]
- [[MCPAuditEntry (extends AuditEntry with server_name, tool_name, parameters, duration_ms, blocked)]] - `extends` [EXTRACTED]
- [[SQLite Database Schema (approval_requests, agent_trust, audit_entries, mcp_audit_entries tables)]] - `implements` [INFERRED]

#graphify/concept #graphify/EXTRACTED #community/Module_Group_346