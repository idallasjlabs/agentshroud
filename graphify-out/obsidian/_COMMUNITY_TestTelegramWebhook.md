---
type: community
cohesion: 0.14
members: 14
---

# TestTelegramWebhook

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_empty_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_non_json_body_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_passthrough_status_without_pipeline()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_requires_auth()_1]] - code - gateway/tests/test_channel_ownership.py
- [[.test_requires_auth()_2]] - code - gateway/tests/test_channel_ownership.py
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
TABLE source_file, type FROM #community/TestTelegramWebhook
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_TestEmailSend]]

## Top bridge nodes
- [[TestTelegramWebhook]] - degree 7, connects to 1 community
- [[.test_requires_auth()_1]] - degree 2, connects to 1 community