---
type: community
members: 6
---

# _verify_bearer

**Members:** 6 nodes

## Members
- [[dot-test_empty_token_or_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_match()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_mismatch()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Constant-time comparison against the gateway shared secret.]] - rationale - gateway/soc/auth.py
- [[TestVerifyBearer]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_verify_bearer()]] - code - gateway/soc/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_verify_bearer
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[_verify_bearer()]] - degree 7, connects to 2 communities
- [[TestVerifyBearer]] - degree 4, connects to 1 community
