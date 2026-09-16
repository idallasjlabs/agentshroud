---
type: community
cohesion: 0.29
members: 7
---

# Community 1109

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1109
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Slack Proxy & Main Endpoint Tests]]
- 1 edge to [[_COMMUNITY_Approval Routing & Event Bus]]

## Top bridge nodes
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
- [[dot-test_owner_recipient_body_preserved()]] - degree 3, connects to 1 community
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - degree 3, connects to 1 community
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - degree 3, connects to 1 community