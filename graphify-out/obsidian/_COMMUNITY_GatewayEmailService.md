---
type: community
members: 36
---

# GatewayEmailService

**Members:** 36 nodes

## Members
- [[dot-__enter__()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-__exit__()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-__init__()_65]] - code - gateway/ingest_api/email_service.py
- [[dot-__init__()_66]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-build_message()]] - code - gateway/ingest_api/email_service.py
- [[dot-login()]] - code - gateway/ingest_api/email_service.py
- [[dot-login()_1]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-send()]] - code - gateway/ingest_api/email_service.py
- [[dot-sender()]] - code - gateway/ingest_api/email_service.py
- [[dot-sendmail()]] - code - gateway/ingest_api/email_service.py
- [[dot-sendmail()_1]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_html_message_has_plain_fallback_then_html()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_plain_message_has_single_plain_part()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_html_uses_html_payload()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_logs_in_and_sendmails_over_injected_transport()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_propagates_auth_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_propagates_generic_smtp_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[Build the MIME message string (multipartalternative). For HTML mail the plain…]] - rationale - gateway/ingest_api/email_service.py
- [[Gateway owner-comms email service (SCRUM-77). Consolidates the SMTP transport…]] - rationale - gateway/ingest_api/email_service.py
- [[GatewayEmailService]] - code - gateway/ingest_api/email_service.py
- [[Protocol]] - code
- [[Records loginsendmail; usable as a context manager like SMTP_SSL.]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Send one email synchronously. Blocking — call in an executor. Raises the…]] - rationale - gateway/ingest_api/email_service.py
- [[Sends owner-comms email over an injectable SMTP transport.]] - rationale - gateway/ingest_api/email_service.py
- [[SmtpLike]] - code - gateway/ingest_api/email_service.py
- [[TestBuildMessage]] - code - gateway/tests/test_gateway_email_service.py
- [[TestSend]] - code - gateway/tests/test_gateway_email_service.py
- [[Tests for GatewayEmailService (SCRUM-77). The transport is injected, so no test…]] - rationale - gateway/tests/test_gateway_email_service.py
- [[The subset of ``smtplib.SMTP_SSL`` the service uses.]] - rationale - gateway/ingest_api/email_service.py
- [[TransportFactory]] - code
- [[_FakeSmtp]] - code - gateway/tests/test_gateway_email_service.py
- [[_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[email_service.py]] - code - gateway/ingest_api/email_service.py
- [[test_gateway_email_service.py]] - code - gateway/tests/test_gateway_email_service.py
- [[test_sender_property()]] - code - gateway/tests/test_gateway_email_service.py
- [[upstream_to_client()]] - code - gateway/proxy/canvas_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GatewayEmailService
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_app]]
- 2 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_dot-test_default_transport_is_smtp_ssl]]
- 1 edge to [[_COMMUNITY_canvas_proxy.py]]

## Top bridge nodes
- [[GatewayEmailService]] - degree 11, connects to 1 community
- [[test_gateway_email_service.py]] - degree 10, connects to 1 community
- [[TestSend]] - degree 7, connects to 1 community
- [[email_service.py]] - degree 5, connects to 1 community
- [[upstream_to_client()]] - degree 2, connects to 1 community
