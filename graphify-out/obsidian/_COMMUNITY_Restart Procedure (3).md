---
type: community
members: 8
---

# Restart Procedure (3)

**Members:** 8 nodes

## Members
- [[dot-test_aws_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_clean_content_passes()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_github_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_jwt_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_leak_detection_disabled()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_openai_key_detected()]] - code - gateway/tests/test_credential_injector.py
- [[dot-test_slack_token_detected()]] - code - gateway/tests/test_credential_injector.py
- [[TestLeakDetection]] - code - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Restart_Procedure_3
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_voice_latency_guard.py (2)]]
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]

## Top bridge nodes
- [[TestLeakDetection]] - degree 8, connects to 1 community
- [[dot-test_leak_detection_disabled()]] - degree 2, connects to 1 community
