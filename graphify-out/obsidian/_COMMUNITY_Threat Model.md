---
type: community
members: 10
---

# Threat Model

**Members:** 10 nodes

## Members
- [[1. Command Injection]] - document - docs/ssh-security-review.md
- [[2. Host Spoofing  Man-in-the-Middle]] - document - docs/ssh-security-review.md
- [[3. Credential Theft]] - document - docs/ssh-security-review.md
- [[4. Privilege Escalation]] - document - docs/ssh-security-review.md
- [[5. Denial of Service]] - document - docs/ssh-security-review.md
- [[6. Audit Log Tampering  PII Leakage]] - document - docs/ssh-security-review.md
- [[D - Denial of Service]] - document - docs/security/threat-model.md
- [[Threat Model_29]] - document - docs/ssh-security-review.md
- [[Threat Context Window Stuffing]] - document - docs/security/threat-model.md
- [[Threat Resource Exhaustion]] - document - docs/security/threat-model.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Threat_Model
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Recommendations for Production Deployment]]
- 1 edge to [[_COMMUNITY_STRIDE Threat Analysis]]

## Top bridge nodes
- [[Threat Model_29]] - degree 8, connects to 1 community
- [[D - Denial of Service]] - degree 4, connects to 1 community
