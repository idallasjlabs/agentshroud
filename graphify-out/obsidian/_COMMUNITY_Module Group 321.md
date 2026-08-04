---
type: community
cohesion: 0.15
members: 13
---

# Module Group 321

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_empty_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_non_json_body_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_passthrough_status_without_pipeline()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_requires_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_response_has_status_field()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_valid_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[Empty payload is handled gracefully (skipped, not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Malformed body is handled defensively (empty dict fallback).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Response always includes a 'status' field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Standard Telegram message payload is accepted.]] - rationale - gateway/tests/test_channel_ownership.py
- [[TestTelegramWebhook]] - code - gateway/tests/test_channel_ownership.py
- [[Without a pipeline configured, status is passthrough (not error).]] - rationale - gateway/tests/test_channel_ownership.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_321
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Module Group 195]]

## Top bridge nodes
- [[TestTelegramWebhook]] - degree 7, connects to 1 community
