---
type: community
cohesion: 0.24
members: 11
---

# Module Group 346

**Cohesion:** 0.24 - loosely connected
**Members:** 11 nodes

## Members
- [[AgentShroud Data Dictionary]] - document - docs/data/data-dictionary.md
- [[ApprovalRequest Entity (id, agent_id, action, status PENDINGAPPROVEDDENIEDEXPIRED, expiry timeouts by priority)]] - concept - docs/data/data-dictionary.md
- [[AuditEntry Data Entity (id, timestamp, direction, content_hash, chain_hash, agent_id, threat_level)]] - concept - docs/data/data-dictionary.md
- [[DNSQuery Entity (id, domain, allowed, flagged, resolved_ip, response_time_ms)]] - concept - docs/data/data-dictionary.md
- [[Data Retention Policies (AuditEntry 7yr, ApprovalRequest 3yr, TrustLevel indefinite, DNSQuery 1yr, Session 30 days)]] - concept - docs/data/data-dictionary.md
- [[MCPAuditEntry (extends AuditEntry with server_name, tool_name, parameters, duration_ms, blocked)]] - concept - docs/data/data-dictionary.md
- [[SQLite Database Schema (approval_requests, agent_trust, audit_entries, mcp_audit_entries tables)]] - concept - docs/data/schema-documentation.md
- [[SecurityFinding Entity (threat_level, category, confidence 0-100, matched_pattern)]] - concept - docs/data/data-dictionary.md
- [[Trust Promotion Rules (L0→L1 immediate; L1→L2 100 actions, 0 violations, 7 days; L2→L3 1000 actions, 5% violations; L3→L4 manual only)]] - concept - docs/data/data-dictionary.md
- [[TrustLevel Entity (agent_id, level 0-4, violations, violation_rate, promotion_eligible)]] - concept - docs/data/data-dictionary.md
- [[URLAnalysisResult Entity (verdict SAFESUSPICIOUSMALICIOUSBLOCKED, is_ssrf, reputation_score 0-100)]] - concept - docs/data/data-dictionary.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_346
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 261]]

## Top bridge nodes
- [[SQLite Database Schema (approval_requests, agent_trust, audit_entries, mcp_audit_entries tables)]] - degree 4, connects to 1 community
- [[Trust Promotion Rules (L0→L1 immediate; L1→L2 100 actions, 0 violations, 7 days; L2→L3 1000 actions, 5% violations; L3→L4 manual only)]] - degree 2, connects to 1 community