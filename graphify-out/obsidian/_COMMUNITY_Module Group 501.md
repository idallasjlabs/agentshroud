---
type: community
cohesion: 0.40
members: 5
---

# Module Group 501

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[IEC 62443 FR3SL3 (cosign, Trivy, Falco, Semgrep alignment)]] - concept - .github/workflows/security-scan.yml
- [[Image Signing & Provenance Job (cosign, keyless OIDC, IEC 62443 FR3SL3)]] - code - .github/workflows/security-scan.yml
- [[Python Dependency Audit Job (pip-audit)]] - code - .github/workflows/security-scan.yml
- [[Security Scan Workflow]] - code - .github/workflows/security-scan.yml
- [[Trivy Filesystem Scan Job (CRITICALHIGH CVEs)]] - code - .github/workflows/security-scan.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_501
SORT file.name ASC
```
