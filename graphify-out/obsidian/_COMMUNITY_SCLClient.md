---
type: community
members: 21
---

# SCLClient

**Members:** 21 nodes

## Members
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/forward.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_6]] - code - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SCLClient
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY__make_proxy()]]
- 7 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 2 edges to [[_COMMUNITY_TestPatternDetection]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (2)_1]]
- 1 edge to [[_COMMUNITY_AgentShroud Access Control Matrix]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[email_send()]] - degree 13, connects to 5 communities
- [[_process_inbound()]] - degree 12, connects to 4 communities
- [[forward_content()]] - degree 9, connects to 4 communities
- [[forward_content_stream()]] - degree 8, connects to 3 communities
- [[OwnerEmailRequest]] - degree 4, connects to 3 communities
