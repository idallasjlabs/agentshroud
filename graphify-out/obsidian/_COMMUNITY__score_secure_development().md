---
type: community
cohesion: 0.50
members: 5
---

# _score_secure_development()

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_at_least_one()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_semgrep_and_precommit_present()]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 11 Secure Development (0-5).      1=Trivy in build, 2=semgrep conf]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreSecureDevelopment]] - code - gateway/tests/test_scanner_integration.py
- [[_score_secure_development()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_score_secure_development
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_compute_scorecard()]]

## Top bridge nodes
- [[_score_secure_development()]] - degree 7, connects to 3 communities
- [[TestScoreSecureDevelopment]] - degree 3, connects to 1 community