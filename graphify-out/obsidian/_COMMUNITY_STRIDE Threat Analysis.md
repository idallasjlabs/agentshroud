---
type: community
cohesion: 0.22
members: 9
---

# STRIDE Threat Analysis

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[R - Repudiation]] - document - docs/security/threat-model.md
- [[S - Spoofing Identity]] - document - docs/security/threat-model.md
- [[STRIDE Threat Analysis]] - document - docs/security/threat-model.md
- [[T - Tampering with Data]] - document - docs/security/threat-model.md
- [[Threat API Key Impersonation]] - document - docs/security/threat-model.md
- [[Threat Agent Identity Spoofing]] - document - docs/security/threat-model.md
- [[Threat Audit Log Tampering]] - document - docs/security/threat-model.md
- [[Threat Configuration Drift]] - document - docs/security/threat-model.md
- [[Threat Non-Repudiation Bypass]] - document - docs/security/threat-model.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/STRIDE_Threat_Analysis
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_I - Information Disclosure]]
- 1 edge to [[_COMMUNITY_E - Elevation of Privilege]]
- 1 edge to [[_COMMUNITY_AgentShroud Threat Model (STRIDE Analysis)]]
- 1 edge to [[_COMMUNITY_Threat Model]]

## Top bridge nodes
- [[STRIDE Threat Analysis]] - degree 7, connects to 4 communities