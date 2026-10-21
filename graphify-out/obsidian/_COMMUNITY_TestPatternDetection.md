---
type: community
members: 48
---

# TestPatternDetection

**Members:** 48 nodes

## Members
- [[dot-test_allowed_recipient_response_has_sanitized_body()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_allowed_recipient_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_empty_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_missing_required_fields_returns_422()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_missing_to_returns_422()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_non_json_body_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_owner_body_not_redacted()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_passthrough_status_without_pipeline()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_pii_redacted_for_unknown_recipient()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_requires_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_requires_auth()_1]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_response_has_status_field()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_response_has_timestamp()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_unknown_recipient_no_queue_returns_403()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_unknown_recipient_queued_for_approval()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_valid_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[All responses include an ISO 8601 timestamp.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Allowed (owner) recipient receives the body verbatim — PII scan is skipped.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Approved response includes sanitized_body field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/forward.py
- [[Email to an allowed recipient returns 200 with status=approved.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Empty payload is handled gracefully (skipped, not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Malformed body is handled defensively (empty dict fallback).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Missing 'subject' or 'body' returns 422.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Missing 'to' field returns 422.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[PII in email body IS redacted before queuing for unknown recipients.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Response always includes a 'status' field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Standard Telegram message payload is accepted.]] - rationale - gateway/tests/test_channel_ownership.py
- [[TestEmailSend]] - code - gateway/tests/test_channel_ownership.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestTelegramWebhook]] - code - gateway/tests/test_channel_ownership.py
- [[Unknown recipient triggers approval queue and returns 202.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Unknown recipient with no approval queue configured returns 403.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Without a pipeline configured, status is passthrough (not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_3]] - code - gateway/tests/test_channel_ownership.py
- [[client()_4]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPatternDetection
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_api.py (2)]]
- 2 edges to [[_COMMUNITY_WebContentScanner]]
- 2 edges to [[_COMMUNITY_SCLClient]]
- 2 edges to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_lifespan()]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[auth_dep()_4]] - degree 7, connects to 4 communities
- [[test_email_owner_bypasses_pii.py]] - degree 7, connects to 3 communities
- [[test_channel_ownership.py]] - degree 7, connects to 2 communities
- [[dot-test_owner_body_not_redacted()]] - degree 3, connects to 1 community
- [[dot-test_pii_redacted_for_unknown_recipient()]] - degree 3, connects to 1 community
