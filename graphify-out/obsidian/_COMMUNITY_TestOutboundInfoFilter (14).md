---
type: community
cohesion: 0.50
members: 5
---

# TestOutboundInfoFilter (14)

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Members
- [[Built-in pre-commit hooks (private key, AWS creds, large files)]] - code - .llm_settings/templates/.pre-commit-config.yaml
- [[Fleet-wide pre-commit secret-blocking hook]] - concept - .llm_settings/git-hooks/README.md
- [[Pre-commit hook strategy (framework vs manual)]] - concept - .llm_settings/docs/SECURITY_GUIDE.md
- [[detect-secrets pre-commit hook (baseline-driven)]] - code - .llm_settings/templates/.pre-commit-config.yaml
- [[gitleaks pre-commit hook (template)]] - code - .llm_settings/templates/.pre-commit-config.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundInfoFilter_14
SORT file.name ASC
```
