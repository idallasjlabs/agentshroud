---
type: community
members: 6
---

# _score_secure_development

**Members:** 6 nodes

## Members
- [[dot-test_at_least_one()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_semgrep_and_precommit_present()]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 11 Secure Development (0-5). 1=Trivy in build, 2=semgrep config,…]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreSecureDevelopment]] - code - gateway/tests/test_scanner_integration.py
- [[_score_secure_development()]] - code - gateway/security/scanner_integration.py
- [[path_factory()]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_score_secure_development
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[_score_secure_development()]] - degree 6, connects to 2 communities
- [[TestScoreSecureDevelopment]] - degree 3, connects to 1 community
