---
type: community
cohesion: 0.22
members: 9
---

# Ssh Security Review (docs)

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[1. Command Injection]] - document - docs/ssh-security-review.md
- [[2. Host Spoofing  Man-in-the-Middle]] - document - docs/ssh-security-review.md
- [[3. Credential Theft]] - document - docs/ssh-security-review.md
- [[4. Privilege Escalation]] - document - docs/ssh-security-review.md
- [[6. Audit Log Tampering  PII Leakage]] - document - docs/ssh-security-review.md
- [[D - Denial of Service]] - document - docs/security/threat-model.md
- [[Threat Model_1]] - document - docs/ssh-security-review.md
- [[Threat Context Window Stuffing]] - document - docs/security/threat-model.md
- [[Threat Resource Exhaustion]] - document - docs/security/threat-model.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ssh_Security_Review_docs
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Threat Model (security)]]
- 1 edge to [[_COMMUNITY_Ssh Security Review (docs)]]

## Top bridge nodes
- [[Threat Model_1]] - degree 7, connects to 1 community
- [[D - Denial of Service]] - degree 4, connects to 1 community