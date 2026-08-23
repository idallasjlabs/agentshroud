---
type: community
cohesion: 0.06
members: 33
---

# Channel Ownership

**Cohesion:** 0.06 - loosely connected
**Members:** 33 nodes

## Members
- [[.test_allowed_recipient_response_has_sanitized_body()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_allowed_recipient_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_empty_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_missing_required_fields_returns_422()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_missing_to_returns_422()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_non_json_body_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_owner_body_not_redacted()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_passthrough_status_without_pipeline()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_pii_redacted_for_unknown_recipient()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_requires_auth()_1]] - code - gateway/tests/test_channel_ownership.py
- [[.test_requires_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_response_has_status_field()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_response_has_timestamp()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_unknown_recipient_no_queue_returns_403()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_unknown_recipient_queued_for_approval()]] - code - gateway/tests/test_channel_ownership.py
- [[.test_valid_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[All responses include an ISO 8601 timestamp.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Allowed (owner) recipient receives the body verbatim — PII scan is skipped.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Approved response includes sanitized_body field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Email to an allowed recipient returns 200 with status=approved.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Empty payload is handled gracefully (skipped, not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Malformed body is handled defensively (empty dict fallback).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Missing 'subject' or 'body' returns 422.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Missing 'to' field returns 422.]] - rationale - gateway/tests/test_channel_ownership.py
- [[PII in email body IS redacted before queuing for unknown recipients.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Response always includes a 'status' field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Standard Telegram message payload is accepted.]] - rationale - gateway/tests/test_channel_ownership.py
- [[TestEmailSend]] - code - gateway/tests/test_channel_ownership.py
- [[TestTelegramWebhook]] - code - gateway/tests/test_channel_ownership.py
- [[Unknown recipient triggers approval queue and returns 202.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Unknown recipient with no approval queue configured returns 403.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Without a pipeline configured, status is passthrough (not error).]] - rationale - gateway/tests/test_channel_ownership.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Channel_Ownership
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Slack Proxy Coverage]]
- 2 edges to [[_COMMUNITY_Forward (routes)]]

## Top bridge nodes
- [[TestEmailSend]] - degree 11, connects to 1 community
- [[TestTelegramWebhook]] - degree 7, connects to 1 community
- [[.test_owner_body_not_redacted()]] - degree 3, connects to 1 community
- [[.test_pii_redacted_for_unknown_recipient()]] - degree 3, connects to 1 community
- [[.test_unknown_recipient_queued_for_approval()]] - degree 3, connects to 1 community