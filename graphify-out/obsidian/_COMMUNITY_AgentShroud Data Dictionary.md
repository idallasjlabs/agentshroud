---
type: community
members: 21
---

# AgentShroud Data Dictionary

**Members:** 21 nodes

## Members
- [[AgentShroud Data Dictionary]] - document - docs/data/data-dictionary.md
- [[Approval Decision Criteria]] - document - skills/custom/securebrowser/references/security-policies.md
- [[Approval Workflows]] - document - skills/custom/securebrowser/references/security-policies.md
- [[ApprovalRequest_2]] - document - docs/data/data-dictionary.md
- [[AuditEntry]] - document - docs/data/data-dictionary.md
- [[Configuration Entities]] - document - docs/data/data-dictionary.md
- [[Configuration Setup]] - document - skills/openclaw/himalaya/SKILL.md
- [[Core Audit Entities]] - document - docs/data/data-dictionary.md
- [[DNSQuery]] - document - docs/data/data-dictionary.md
- [[Data Classification]] - document - docs/data/data-dictionary.md
- [[Data Retention Policies]] - document - docs/data/data-dictionary.md
- [[InspectionResult_1]] - document - docs/data/data-dictionary.md
- [[Network Security Entities]] - document - docs/data/data-dictionary.md
- [[RateLimitBucket]] - document - docs/data/data-dictionary.md
- [[Relationship Diagram]] - document - docs/data/data-dictionary.md
- [[Runtime State Entities]] - document - docs/data/data-dictionary.md
- [[Security Management Entities]] - document - docs/data/data-dictionary.md
- [[SessionState]] - document - docs/data/data-dictionary.md
- [[TrustLevel]] - document - docs/data/data-dictionary.md
- [[URLAnalysisResult]] - document - docs/data/data-dictionary.md
- [[data-dictionary]] - document - docs/data/data-dictionary.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Data_Dictionary
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_SecurityFinding]]
- 1 edge to [[_COMMUNITY_Common Operations]]
- 1 edge to [[_COMMUNITY_SecureBrowser Security Policies]]

## Top bridge nodes
- [[Network Security Entities]] - degree 5, connects to 1 community
- [[Approval Workflows]] - degree 3, connects to 1 community
- [[Configuration Setup]] - degree 2, connects to 1 community
