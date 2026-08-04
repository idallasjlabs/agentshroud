---
type: community
cohesion: 0.22
members: 9
---

# Module Group 398

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[AgentShroud IEC 62443 Overall Rating SL 2 (with SL 3 in FR 2, FR 3, FR 4, FR 6)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 1 Identification and Authentication Control - SL 2 (gap native MFA)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 2 Use Control - SL 3 (approval queue, tool ACL, session lock, subagent monitor)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 3 System Integrity - SL 3 (Cosign, Trivy, Falco, Semgrep, ConfigIntegrityMonitor)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 4 Data Confidentiality - SL 3 (PIISanitizer @ 0.9 confidence, OutboundFilter, LogSanitizer)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 5 Restricted Data Flow - SL 2 (EgressFilter + EgressApproval, WebContentScanner, gap no DMZ)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 6 Timely Response to Events - SL 3 (AuditStore SHA-256 hash chain, Falco, Wazuh, AlertDispatcher)]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR 7 Resource Availability - SL 2 (ProgressiveLockdown, Docker resource limits, backup scripts)]] - concept - docs/compliance/iec-62443-matrix.md
- [[IEC 62443 Compliance Matrix - AgentShroud v1.0.0]] - document - docs/compliance/iec-62443-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_398
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 238]]
- 2 edges to [[_COMMUNITY_Module Group 262]]

## Top bridge nodes
- [[IEC 62443 Compliance Matrix - AgentShroud v1.0.0]] - degree 9, connects to 1 community
- [[FR 2 Use Control - SL 3 (approval queue, tool ACL, session lock, subagent monitor)]] - degree 2, connects to 1 community
- [[FR 3 System Integrity - SL 3 (Cosign, Trivy, Falco, Semgrep, ConfigIntegrityMonitor)]] - degree 2, connects to 1 community
- [[FR 4 Data Confidentiality - SL 3 (PIISanitizer @ 0.9 confidence, OutboundFilter, LogSanitizer)]] - degree 2, connects to 1 community
- [[FR 6 Timely Response to Events - SL 3 (AuditStore SHA-256 hash chain, Falco, Wazuh, AlertDispatcher)]] - degree 2, connects to 1 community
