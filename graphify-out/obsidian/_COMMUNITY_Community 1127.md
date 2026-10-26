---
type: community
members: 7
---

# Community 1127

**Members:** 7 nodes

## Members
- [[.test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1127
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 37]]
- 1 edge to [[_COMMUNITY_Community 2154]]

## Top bridge nodes
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
- [[.test_owner_recipient_body_preserved()]] - degree 3, connects to 1 community
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - degree 3, connects to 1 community
- [[.test_unknown_recipient_body_still_scrubbed()]] - degree 3, connects to 1 community