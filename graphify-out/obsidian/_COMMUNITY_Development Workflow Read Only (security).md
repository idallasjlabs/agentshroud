---
type: community
cohesion: 0.15
members: 16
---

# Development Workflow Read Only (security)

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Members
- [[Approval Queue Control]] - rationale - docs/security/SECURITY_ARCHITECTURE.md
- [[Approval Queue — Core Security Value]] - rationale - docs/security/SECURITY_VALUE_PROPOSITION.md
- [[DEVELOPMENT_WORKFLOW_READ_ONLY]] - document - docs/security/DEVELOPMENT_WORKFLOW_READ_ONLY.md
- [[DEVICE_PAIRING]] - document - docs/setup/DEVICE_PAIRING.md
- [[Four-Layer Access Security Model (Password  Pairing  Allowlist  Approval)]] - rationale - docs/setup/DEVICE_PAIRING.md
- [[IEC 62443 Compliance Matrix]] - concept - docs/security/SECURITY_VALUE_PROPOSITION_REVISED.md
- [[MVP Recommendation (Option A)]] - rationale - docs/security/SECURITY_VALUE_PROPOSITION.md
- [[Multi-UserMulti-Tenant Threat Model (Reversal Driver)]] - rationale - docs/security/SECURITY_VALUE_PROPOSITION_REVISED.md
- [[Phase A Development Mode (Current)]] - document - docs/security/DEVELOPMENT_WORKFLOW_READ_ONLY.md
- [[Phase B Compatibility Testing]] - document - docs/security/DEVELOPMENT_WORKFLOW_READ_ONLY.md
- [[Phase C Production Lockdown]] - document - docs/security/DEVELOPMENT_WORKFLOW_READ_ONLY.md
- [[Read-Only Filesystem (Planned)]] - concept - docs/security/container-policy.md
- [[SECURITY-POLICY-FINAL]] - document - docs/security/SECURITY-POLICY-FINAL.md
- [[SECURITY_VALUE_PROPOSITION]] - document - docs/security/SECURITY_VALUE_PROPOSITION.md
- [[Three-Phase Approach]] - document - docs/security/DEVELOPMENT_WORKFLOW_READ_ONLY.md
- [[Ultra-Conservative Credential Display Policy]] - rationale - docs/security/SECURITY-POLICY-FINAL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Development_Workflow_Read_Only_security
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Development Workflow Read Only (security)]]
- 2 edges to [[_COMMUNITY_Security Scripts Reference (security)]]
- 1 edge to [[_COMMUNITY_Credential Protection Implemented (security)]]
- 1 edge to [[_COMMUNITY_Credential Security Policy (security)]]
- 1 edge to [[_COMMUNITY_Security Policy Final (security)]]
- 1 edge to [[_COMMUNITY_Security Architecture (security)]]
- 1 edge to [[_COMMUNITY_Security Value Proposition (security)]]
- 1 edge to [[_COMMUNITY_Security Value Proposition Revised (security)]]
- 1 edge to [[_COMMUNITY_Secrets Usage And Collaborator (security)]]
- 1 edge to [[_COMMUNITY_Device Pairing (setup)]]

## Top bridge nodes
- [[SECURITY_VALUE_PROPOSITION]] - degree 10, connects to 3 communities
- [[SECURITY-POLICY-FINAL]] - degree 4, connects to 3 communities
- [[Three-Phase Approach]] - degree 5, connects to 1 community
- [[DEVELOPMENT_WORKFLOW_READ_ONLY]] - degree 4, connects to 1 community
- [[Approval Queue Control]] - degree 4, connects to 1 community