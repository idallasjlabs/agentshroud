---
type: community
cohesion: 0.21
members: 16
---

# Module Group 274

**Cohesion:** 0.21 - loosely connected
**Members:** 16 nodes

## Members
- [[58 Security Modules (Inbound 6, Outbound 6, PII 3, Access Control 7, NetworkEgress 6, MCPTool 6, Supply ChainBrowser 2, Audit 4, Infra 8, Encryption 3, External 4, Orchestration 3)]] - concept - docs/security/security-inventory.md
- [[ApprovalQueue (approval_queue.py) — Human-in-the-loop approval workflow]] - code - docs/security/access-control-matrix.md
- [[AuditStore (audit_store.py) — SHA-256 tamper-evident hash chain]] - code - docs/security/audit-specification.md
- [[CVE-2026-22708 (CVSS 9.8) AI Agent Container Escape via Prompt Injection — Fully Mitigated]] - concept - docs/security/cve-mitigation-matrix.md
- [[DNSFilter (dns_filter.py) — Shannon entropy, base64hex detection, rate limiting 120qmin]] - code - docs/security/cve-mitigation-matrix.md
- [[EgressFilter (egress_filter.py) — Outbound domain allowlistdenylist, default-deny]] - code - docs/security/security-inventory.md
- [[Fully Implemented Domains (D4 Capability Security, D5 Tool-Call Governance, D6 Egress, D9 Multi-Agent, D10 Approval, D13 Sandboxing, D15 Secret Mgmt)]] - concept - docs/security/security-assessment-v0.8.0-25-domain.md
- [[Gateway Security Value (Approval Queue, PII Sanitizer, Audit Ledger)]] - concept - docs/security/SECURITY_VALUE_PROPOSITION.md
- [[Key Security Modules PromptGuard, SecurityPipeline, EgressFilter, RBACConfig, TrustManager, AuditStore, KillswitchMonitor]] - concept - docs/security/security-inventory.md
- [[OWASP Agentic AI (ASI) Coverage (ASI-01 through ASI-10)]] - concept - docs/security/cve-mitigation-matrix.md
- [[PII Sanitizer (Presidio + regex, 0.9 confidence minimum)]] - code - docs/security/security-architecture.md
- [[PromptGuard (prompt_guard.py) — 49 regex patterns, 35+ languages, weighted scoring]] - code - docs/security/security-inventory.md
- [[Security Domain Gaps (D2 instructiondata separation HIGH, D3 taint tracking HIGH, D14 OCR scanning HIGH)]] - concept - docs/security/security-assessment-v0.8.0-25-domain.md
- [[SecurityPipeline (proxypipeline.py) — Central inboundoutbound security orchestration]] - code - docs/security/security-inventory.md
- [[security-assessment-v0.8.0-25-domain.md (25-Domain Prompt Injection Defense Assessment)]] - document - docs/security/security-assessment-v0.8.0-25-domain.md
- [[security-inventory.md (v0.8.0 58 modules, 9 configs, 24 docs, 38 test files, 22332233 passing)]] - document - docs/security/security-inventory.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_274
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 404]]
- 2 edges to [[_COMMUNITY_Module Group 391]]
- 2 edges to [[_COMMUNITY_Module Group 454]]
- 1 edge to [[_COMMUNITY_Module Group 538]]
- 1 edge to [[_COMMUNITY_Module Group 298]]

## Top bridge nodes
- [[58 Security Modules (Inbound 6, Outbound 6, PII 3, Access Control 7, NetworkEgress 6, MCPTool 6, Supply ChainBrowser 2, Audit 4, Infra 8, Encryption 3, External 4, Orchestration 3)]] - degree 11, connects to 3 communities
- [[CVE-2026-22708 (CVSS 9.8) AI Agent Container Escape via Prompt Injection — Fully Mitigated]] - degree 4, connects to 2 communities
- [[PromptGuard (prompt_guard.py) — 49 regex patterns, 35+ languages, weighted scoring]] - degree 5, connects to 1 community
- [[OWASP Agentic AI (ASI) Coverage (ASI-01 through ASI-10)]] - degree 4, connects to 1 community
- [[AuditStore (audit_store.py) — SHA-256 tamper-evident hash chain]] - degree 4, connects to 1 community