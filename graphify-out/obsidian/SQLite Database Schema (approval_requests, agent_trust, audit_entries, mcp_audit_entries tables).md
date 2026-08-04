---
source_file: "docs/data/schema-documentation.md"
type: "concept"
community: "Module Group 346"
location: "line 9"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/Module_Group_346
---

# SQLite Database Schema (approval_requests, agent_trust, audit_entries, mcp_audit_entries tables)

## Connections
- [[AgentShroud Schema Documentation]] - `defines` [EXTRACTED]
- [[ApprovalRequest Entity (id, agent_id, action, status PENDINGAPPROVEDDENIEDEXPIRED, expiry timeouts by priority)]] - `implements` [INFERRED]
- [[AuditEntry Data Entity (id, timestamp, direction, content_hash, chain_hash, agent_id, threat_level)]] - `implements` [INFERRED]
- [[TrustLevel Entity (agent_id, level 0-4, violations, violation_rate, promotion_eligible)]] - `implements` [INFERRED]

#graphify/concept #graphify/INFERRED #community/Module_Group_346
