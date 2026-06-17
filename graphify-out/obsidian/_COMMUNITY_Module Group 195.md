---
type: community
cohesion: 0.12
members: 24
---

# Module Group 195

**Cohesion:** 0.12 - loosely connected
**Members:** 24 nodes

## Members
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/forward.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_3]] - code - gateway/ingest_api/routes/forward.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()]] - code - gateway/tests/test_channel_ownership.py
- [[client()_5]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_195
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 2 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 2 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 2 edges to [[_COMMUNITY_Webhook Receiver]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Session Manager & Webhook]]
- 1 edge to [[_COMMUNITY_Module Group 196]]
- 1 edge to [[_COMMUNITY_Module Group 221]]
- 1 edge to [[_COMMUNITY_Module Group 321]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[forward.py]] - degree 25, connects to 8 communities
- [[email_send()]] - degree 10, connects to 3 communities
- [[test_channel_ownership.py]] - degree 6, connects to 3 communities
- [[forward_content()]] - degree 7, connects to 2 communities
- [[test_email_owner_bypasses_pii.py]] - degree 5, connects to 2 communities