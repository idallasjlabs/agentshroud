---
type: community
cohesion: 0.08
members: 25
---

# AgentShroud™ Security Policy

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[7-Layer Security Architecture]] - concept - SECURITY.md
- [[AgentShroud™ Security Policy]] - document - SECURITY.md
- [[CI Security Scanning Toolchain]] - concept - SECURITY.md
- [[Compliance Alignment]] - document - SECURITY.md
- [[Daily CVE Sync + Page Update Workflow]] - document - .github/workflows/update-cve-page.yml
- [[Emergency Response]] - document - SECURITY.md
- [[Kill Switch Operations]] - concept - CHEATSHEET.md
- [[Layer 1 — Core Pipeline (P0)]] - document - SECURITY.md
- [[Layer 2 — Middleware (P1)]] - document - SECURITY.md
- [[Layer 3 — Output Protection]] - document - SECURITY.md
- [[Layer 4 — Tool & Agent Control]] - document - SECURITY.md
- [[Layer 5 — Network & Egress]] - document - SECURITY.md
- [[Layer 6 — File & Memory Integrity]] - document - SECURITY.md
- [[Layer 7 — Infrastructure & Supply Chain]] - document - SECURITY.md
- [[Monitor Mode Warning]] - document - SECURITY.md
- [[Pinned Vendor Versions Single Source of Truth (dockerversions.env)]] - rationale - .github/workflows/update-cve-page.yml
- [[Reporting a Vulnerability]] - document - SECURITY.md
- [[Response Timeline]] - document - SECURITY.md
- [[SECURITY]] - document - SECURITY.md
- [[Security Architecture_4]] - document - SECURITY.md
- [[Security Scan Workflow]] - document - .github/workflows/security-scan.yml
- [[Security Scanning]] - document - SECURITY.md
- [[Supported Versions]] - document - SECURITY.md
- [[Trademark_1]] - document - BRAND.md
- [[Upstream Agent CVE Tracking]] - document - SECURITY.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Policy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AgentShroud™ Brand Guidelines]]
- 2 edges to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_75 Security Modules]]
- 1 edge to [[_COMMUNITY_AgentShroud Operations Cheat Sheet]]

## Top bridge nodes
- [[Trademark_1]] - degree 4, connects to 2 communities
- [[AgentShroud™ Security Policy]] - degree 14, connects to 1 community
- [[Kill Switch Operations]] - degree 2, connects to 1 community
- [[Security Scan Workflow]] - degree 2, connects to 1 community
- [[SECURITY]] - degree 2, connects to 1 community