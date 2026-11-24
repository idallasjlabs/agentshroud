---
type: community
members: 12
---

# TestSupplyChain

**Members:** 12 nodes

## Members
- [[dot-test_all_modules_have_copyright()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_all_security_modules_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dockerfile_exists()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_no_eval_or_exec_in_security()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_no_hardcoded_secrets_in_source()]] - code - gateway/tests/test_security_audit.py
- [[All security modules should have copyright header.]] - rationale - gateway/tests/test_security_audit.py
- [[Dockerfile should be present for reproducible builds.]] - rationale - gateway/tests/test_security_audit.py
- [[Every security module should import without error.]] - rationale - gateway/tests/test_security_audit.py
- [[No hardcoded secrets in Python source files.]] - rationale - gateway/tests/test_security_audit.py
- [[Security modules should not call eval() or exec(). Uses AST analysis so the…]] - rationale - gateway/tests/test_security_audit.py
- [[Test supply chain security measures.]] - rationale - gateway/tests/test_security_audit.py
- [[TestSupplyChain]] - code - gateway/tests/test_security_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSupplyChain
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[TestSupplyChain]] - degree 7, connects to 1 community
