---
type: community
members: 8
---

# Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)

**Members:** 8 nodes

## Members
- [[CI security-scan job (pip-audit dry-run)]] - code - .github/workflows/ci.yml
- [[Python dependency audit job (pip-audit, fails on any vuln)]] - code - .github/workflows/security-scan.yml
- [[Streaming direct voice path (_call_llm_stream)]] - concept - CHANGELOG.md
- [[Transitive-dependency security floors (cryptography, setuptools, multidict, urllib3, anyio, idna, starlette)]] - rationale - gateway/requirements.txt
- [[Trivy action immutable SHA pin (CI supply chain)]] - rationale - CHANGELOG.md
- [[Upstream-advisory watch cron jobs (8 toolchain components)]] - concept - CHANGELOG.md
- [[v1.5.1 — A2A Governance patch release]] - document - CHANGELOG.md
- [[v1.6.0 — voice terminal release]] - document - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Upgrade_Report_2026-09-27_dev_PARTIAL_Hermes_creds
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]

## Top bridge nodes
- [[Transitive-dependency security floors (cryptography, setuptools, multidict, urllib3, anyio, idna, starlette)]] - degree 2, connects to 1 community
