---
type: community
cohesion: 0.22
members: 10
---

# .send()

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[.build_message()]] - code - gateway/ingest_api/email_service.py
- [[.login()]] - code - gateway/ingest_api/email_service.py
- [[.send()]] - code - gateway/ingest_api/email_service.py
- [[.sendmail()]] - code - gateway/ingest_api/email_service.py
- [[Build the MIME message string (multipartalternative).          For HTML mail th]] - rationale - gateway/ingest_api/email_service.py
- [[Protocol]] - code
- [[Send one email synchronously.  Blocking — call in an executor.          Raises t]] - rationale - gateway/ingest_api/email_service.py
- [[SmtpLike]] - code - gateway/ingest_api/email_service.py
- [[The subset of ``smtplib.SMTP_SSL`` the service uses.]] - rationale - gateway/ingest_api/email_service.py
- [[email_service.py]] - code - gateway/ingest_api/email_service.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/send
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_GatewayEmailService]]
- 1 edge to [[_COMMUNITY_forward.py]]

## Top bridge nodes
- [[email_service.py]] - degree 3, connects to 2 communities
- [[.send()]] - degree 5, connects to 1 community
- [[.build_message()]] - degree 3, connects to 1 community