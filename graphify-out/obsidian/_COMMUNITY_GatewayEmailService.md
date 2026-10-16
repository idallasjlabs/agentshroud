---
type: community
cohesion: 0.11
members: 28
---

# GatewayEmailService

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-__enter__()_3]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-__exit__()_3]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-__init__()_120]] - code - gateway/ingest_api/email_service.py
- [[dot-__init__()_121]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-login()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-sender()]] - code - gateway/ingest_api/email_service.py
- [[dot-sendmail()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_default_transport_is_smtp_ssl()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_email_send_routes_through_injectable_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_html_message_has_plain_fallback_then_html()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_plain_message_has_single_plain_part()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_html_uses_html_payload()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_logs_in_and_sendmails_over_injected_transport()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_propagates_auth_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_send_propagates_generic_smtp_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[GatewayEmailService]] - code - gateway/tests/test_gateway_email_service.py
- [[GatewayEmailService_1]] - code - gateway/ingest_api/email_service.py
- [[POST emailsend to the owner sends via forward._email_service — proving]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Records loginsendmail; usable as a context manager like SMTP_SSL.]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Sends owner-comms email over an injectable SMTP transport.]] - rationale - gateway/ingest_api/email_service.py
- [[TestBuildMessage]] - code - gateway/tests/test_gateway_email_service.py
- [[TestEndpointUsesService]] - code - gateway/tests/test_gateway_email_service.py
- [[TestSend]] - code - gateway/tests/test_gateway_email_service.py
- [[TransportFactory]] - code - gateway/ingest_api/email_service.py
- [[_FakeSmtp]] - code - gateway/tests/test_gateway_email_service.py
- [[_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[test_gateway_email_service.py]] - code - gateway/tests/test_gateway_email_service.py
- [[test_sender_property()]] - code - gateway/tests/test_gateway_email_service.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GatewayEmailService
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_GatewayEmailService_1]]
- 2 edges to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py_1]]

## Top bridge nodes
- [[GatewayEmailService_1]] - degree 16, connects to 2 communities
- [[test_gateway_email_service.py]] - degree 8, connects to 1 community
