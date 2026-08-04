---
type: community
cohesion: 0.18
members: 11
---

# Module Group 345

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[CI Workflows (GitHub Actions — test, lint, security scan, image build)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/ci-workflows.md
- [[ClamAV (malware scanning — pre-installed in gateway image)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Docker Security Hardening (non-root, no setuid, seccomp, read-only rootfs)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Dockerfile.gateway]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[OpenSCAP (compliance scanning — pre-installed in gateway image)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Python 3.13 Runtime (multi-stage Docker build)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Trivy (container vulnerability scanning — pre-installed in gateway image)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[gitleaks.toml (secret detection in git history — API keys, tokens, credentials)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/gitleaks.toml.md
- [[presidio-analyzer + presidio-anonymizer (≥2.2.0 — NER-based PII detection and redaction)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/05 - Dependencies/All Dependencies.md
- [[pytest.ini (test configuration — cache_dir tmppytest_cache)]] - document - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/pytest.ini.md
- [[spaCy NLP (en_core_web_sm — pre-installed for PII detection)]] - concept - /Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_345
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 370]]
- 1 edge to [[_COMMUNITY_Module Group 326]]

## Top bridge nodes
- [[Dockerfile.gateway]] - degree 8, connects to 2 communities
- [[pytest.ini (test configuration — cache_dir tmppytest_cache)]] - degree 2, connects to 1 community
- [[presidio-analyzer + presidio-anonymizer (≥2.2.0 — NER-based PII detection and redaction)]] - degree 2, connects to 1 community
