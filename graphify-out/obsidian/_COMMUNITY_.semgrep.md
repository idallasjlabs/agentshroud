---
type: community
cohesion: 0.13
members: 15
---

# .semgrep

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[AgentShroud Semgrep SAST Configuration]] - document - .semgrep.yml
- [[Pre-commit Hooks Configuration]] - document - .pre-commit-config.yaml
- [[Rule agentshroud-assert-security-check]] - concept - .semgrep.yml
- [[Rule agentshroud-hardcoded-password]] - concept - .semgrep.yml
- [[Rule agentshroud-log-sensitive-key]] - concept - .semgrep.yml
- [[Rule agentshroud-pickle-load]] - concept - .semgrep.yml
- [[Rule agentshroud-sql-injection]] - concept - .semgrep.yml
- [[Rule agentshroud-ssrf-httpx]] - concept - .semgrep.yml
- [[Rule agentshroud-ssrf-requests]] - concept - .semgrep.yml
- [[Rule agentshroud-subprocess-shell-true]] - concept - .semgrep.yml
- [[Rule agentshroud-subprocess-unvalidated-input]] - concept - .semgrep.yml
- [[black (Python formatter)]] - concept - .pre-commit-config.yaml
- [[detect-secrets (Yelp secret scanner)]] - concept - .pre-commit-config.yaml
- [[gitleaks (secret scanner)]] - concept - .pre-commit-config.yaml
- [[ruff (Python linter)]] - concept - .pre-commit-config.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/semgrep
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Key Rotation]]
- 1 edge to [[_COMMUNITY_Pull Request Template (.github)]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Privilege Separation & File Sandbox]]

## Top bridge nodes
- [[AgentShroud Semgrep SAST Configuration]] - degree 13, connects to 3 communities
- [[Rule agentshroud-ssrf-httpx]] - degree 2, connects to 1 community
- [[Rule agentshroud-ssrf-requests]] - degree 2, connects to 1 community
- [[Rule agentshroud-subprocess-shell-true]] - degree 2, connects to 1 community