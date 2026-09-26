---
type: community
cohesion: 0.20
members: 19
---

# RuntimeConfig

**Cohesion:** 0.20 - loosely connected
**Members:** 19 nodes

## Members
- [[Pre-commit Hooks Configuration]] - document - .pre-commit-config.yaml
- [[Security scanner endpoints (managescan)]] - code - gateway/ingest_api/main.py
- [[alert_if_critical()]] - code - docker/scripts/security-scan.sh
- [[black (Python formatter)]] - concept - .pre-commit-config.yaml
- [[detect-secrets (Yelp secret scanner)]] - concept - .pre-commit-config.yaml
- [[gitleaks (secret scanner)]] - concept - .pre-commit-config.yaml
- [[install.sh (llm_settings git-hooks)]] - code - .llm_settings/git-hooks/install.sh
- [[log()_4]] - code - docker/scripts/security-scan.sh
- [[pre-commit-hook.sh]] - code - scripts/pre-commit-hook.sh
- [[pre-commit-hook.sh script]] - code - scripts/pre-commit-hook.sh
- [[ruff (Python linter)]] - concept - .pre-commit-config.yaml
- [[run_clamav()]] - code - docker/scripts/security-scan.sh
- [[run_oscap()]] - code - docker/scripts/security-scan.sh
- [[run_sbom()]] - code - docker/scripts/security-scan.sh
- [[run_trivy()]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh_2]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh script]] - code - docker/scripts/security-scan.sh
- [[security-scan.yml (CI)]] - code - .github/workflows/security-scan.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RuntimeConfig
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_graphify reference extra exports and benchmark]]
- 1 edge to [[_COMMUNITY_Discovery Strategy]]
- 1 edge to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[Pre-commit Hooks Configuration]] - degree 9, connects to 2 communities
- [[security-scan.sh_2]] - degree 9, connects to 2 communities
- [[pre-commit-hook.sh]] - degree 5, connects to 1 community
- [[install.sh (llm_settings git-hooks)]] - degree 3, connects to 1 community
- [[Security scanner endpoints (managescan)]] - degree 2, connects to 1 community