---
source_file: "docs/data/data-dictionary.md"
type: "document"
community: "Module Group 346"
location: "line 1"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_346
---

# AgentShroud Data Dictionary

## Connections
- [[ApprovalRequest Entity (id, agent_id, action, status PENDINGAPPROVEDDENIEDEXPIRED, expiry timeouts by priority)]] - `defines` [EXTRACTED]
- [[AuditEntry Data Entity (id, timestamp, direction, content_hash, chain_hash, agent_id, threat_level)]] - `defines` [EXTRACTED]
- [[DNSQuery Entity (id, domain, allowed, flagged, resolved_ip, response_time_ms)]] - `defines` [EXTRACTED]
- [[Data Retention Policies (AuditEntry 7yr, ApprovalRequest 3yr, TrustLevel indefinite, DNSQuery 1yr, Session 30 days)]] - `specifies` [EXTRACTED]
- [[MCPAuditEntry (extends AuditEntry with server_name, tool_name, parameters, duration_ms, blocked)]] - `defines` [EXTRACTED]
- [[SecurityFinding Entity (threat_level, category, confidence 0-100, matched_pattern)]] - `defines` [EXTRACTED]
- [[TrustLevel Entity (agent_id, level 0-4, violations, violation_rate, promotion_eligible)]] - `defines` [EXTRACTED]
- [[URLAnalysisResult Entity (verdict SAFESUSPICIOUSMALICIOUSBLOCKED, is_ssrf, reputation_score 0-100)]] - `defines` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_346