---
type: community
cohesion: 0.29
members: 8
---

# Community 1017

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[Built-in pre-commit hooks (private key, AWS creds, large files)]] - code - .llm_settings/templates/.pre-commit-config.yaml
- [[CI gitleaks secret-scanning job]] - code - .github/workflows/ci.yml
- [[Fleet-wide pre-commit secret-blocking hook]] - concept - .llm_settings/git-hooks/README.md
- [[Pre-commit hook strategy (framework vs manual)]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[Repository security audit script]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[Secret-in-history remediation (BFG  git-filter-repo)]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[detect-secrets pre-commit hook (baseline-driven)]] - code - .llm_settings/templates/.pre-commit-config.yaml
- [[gitleaks pre-commit hook (template)]] - code - .llm_settings/templates/.pre-commit-config.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1017
SORT file.name ASC
```
