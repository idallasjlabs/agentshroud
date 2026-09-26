---
type: community
cohesion: 0.22
members: 10
---

# Collaborator Setup Checklist

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[Dockerfile.gateway vault note]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Gateway pre-installed security tools (ClamAV, Trivy, OpenSCAP, 1Password CLI, spaCy)]] - concept - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[OpenSCAP & IEC 62443 compliance validation]] - rationale - docs/security/SECURITY_VALUE_PROPOSITION_REVISED.md
- [[OpenSCAP dependency note]] - document - docs/vault/05 - Dependencies/openscap.md
- [[OpenSCAP relationship to TrivyClamAVFalco]] - concept - docs/vault/05 - Dependencies/openscap.md
- [[Security Hardening_2]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[cryptography=50.0.1 pin (CVE-2026-692476924869249, GHSA-537c-gmf6-5ccf)]] - rationale - gateway/requirements.txt
- [[gatewayrequirements.txt Python dependency manifest]] - code - gateway/requirements.txt
- [[pip-audit gap — gateway Python deps not scanned]] - rationale - reports/upgrade-2026-09-17.md
- [[setuptools=83.0.0 pin (PYSEC-2026-3447)]] - rationale - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Collaborator_Setup_Checklist
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Skills by Category]]
- 1 edge to [[_COMMUNITY_Pre-Deployment Checklist]]
- 1 edge to [[_COMMUNITY_Plan AgentShroud Security Hardening — Real Agen]]
- 1 edge to [[_COMMUNITY_auth.py]]

## Top bridge nodes
- [[Dockerfile.gateway vault note]] - degree 5, connects to 1 community
- [[OpenSCAP dependency note]] - degree 5, connects to 1 community
- [[gatewayrequirements.txt Python dependency manifest]] - degree 5, connects to 1 community
- [[Security Hardening_2]] - degree 2, connects to 1 community
- [[pip-audit gap — gateway Python deps not scanned]] - degree 2, connects to 1 community