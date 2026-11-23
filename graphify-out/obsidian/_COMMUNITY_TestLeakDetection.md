---
type: community
members: 8
---

# TestLeakDetection

**Members:** 8 nodes

## Members
- [[dot-test_aws_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_clean_content_passes()_1]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_github_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_jwt_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_leak_detection_disabled()_1]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_openai_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_slack_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[TestLeakDetection]] - code - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestLeakDetection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_CredentialInjectorConfig]]
- 1 edge to [[_COMMUNITY_test_credential_injector.py]]
- 1 edge to [[_COMMUNITY_CredentialInjector]]

## Top bridge nodes
- [[TestLeakDetection]] - degree 10, connects to 3 communities
- [[dot-test_leak_detection_disabled()_1]] - degree 2, connects to 1 community
