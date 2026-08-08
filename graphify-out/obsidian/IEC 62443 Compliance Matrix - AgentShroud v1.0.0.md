---
source_file: "docs/compliance/iec-62443-matrix.md"
type: "document"
community: "docs/compliance"
location: "line 1"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/compliance
---

# IEC 62443 Compliance Matrix - AgentShroud v1.0.0

## Connections
- [[AgentShroud IEC 62443 Overall Rating SL 2 (with SL 3 in FR 2, FR 3, FR 4, FR 6)]] - `concludes` [EXTRACTED]
- [[FR 1 Identification and Authentication Control - SL 2 (gap native MFA)]] - `contains` [EXTRACTED]
- [[FR 2 Use Control - SL 3 (approval queue, tool ACL, session lock, subagent monitor)]] - `contains` [EXTRACTED]
- [[FR 3 System Integrity - SL 3 (Cosign, Trivy, Falco, Semgrep, ConfigIntegrityMonitor)]] - `contains` [EXTRACTED]
- [[FR 4 Data Confidentiality - SL 3 (PIISanitizer @ 0.9 confidence, OutboundFilter, LogSanitizer)]] - `contains` [EXTRACTED]
- [[FR 5 Restricted Data Flow - SL 2 (EgressFilter + EgressApproval, WebContentScanner, gap no DMZ)]] - `contains` [EXTRACTED]
- [[FR 6 Timely Response to Events - SL 3 (AuditStore SHA-256 hash chain, Falco, Wazuh, AlertDispatcher)]] - `contains` [EXTRACTED]
- [[FR 7 Resource Availability - SL 2 (ProgressiveLockdown, Docker resource limits, backup scripts)]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/compliance