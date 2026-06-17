---
type: community
cohesion: 0.25
members: 8
---

# Module Group 440

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_aws_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[.test_clean_content_passes()]] - code - gateway/tests/test_credential_injector.py
- [[.test_github_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[.test_jwt_detected()]] - code - gateway/tests/test_credential_injector.py
- [[.test_leak_detection_disabled()]] - code - gateway/tests/test_credential_injector.py
- [[.test_openai_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[.test_slack_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[TestLeakDetection]] - code - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_440
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Module Group 409]]
- 1 edge to [[_COMMUNITY_Module Group 288]]

## Top bridge nodes
- [[TestLeakDetection]] - degree 8, connects to 1 community
- [[.test_leak_detection_disabled()]] - degree 2, connects to 1 community