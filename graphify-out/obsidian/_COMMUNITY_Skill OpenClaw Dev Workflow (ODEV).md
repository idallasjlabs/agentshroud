---
type: community
cohesion: 0.25
members: 8
---

# Skill: OpenClaw Dev Workflow (ODEV)

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
TABLE source_file, type FROM #community/Skill_OpenClaw_Dev_Workflow_ODEV
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ssh_proxy.py]]
- 1 edge to [[_COMMUNITY_Features]]

## Top bridge nodes
- [[TestLeakDetection]] - degree 8, connects to 1 community
- [[.test_leak_detection_disabled()]] - degree 2, connects to 1 community